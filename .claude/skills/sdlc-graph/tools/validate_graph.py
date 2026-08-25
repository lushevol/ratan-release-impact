#!/usr/bin/env python3
"""Validate the compact schema-v2 SDLC graph and its source evidence."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


TOP_FIELDS = {"schema_version", "generated_at", "generator", "repositories", "nodes", "edges", "evidence", "diagnostics"}
NODE_FIELDS = {"id", "type", "name", "repository", "dimensions", "component_kind", "functional_role", "business_meaning", "source_paths", "evidence", "assertion_status", "properties"}
EDGE_FIELDS = {"id", "source", "target", "relationship", "dimension", "evidence", "assertion_status", "resolution_status", "properties"}
EVIDENCE_FIELDS = {"id", "repository", "path", "line", "declaration", "extractor", "directness"}


def load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("graph root must be an object")
    return value


def wildcard_parent(workspace: Path, value: str) -> Path:
    concrete = value.split("*", 1)[0].rstrip("/")
    return workspace / concrete


def validate(graph: dict[str, Any], workspace: Path) -> list[str]:
    errors: list[str] = []
    if set(graph) != TOP_FIELDS:
        errors.append(f"top-level fields must be exactly {sorted(TOP_FIELDS)}")
    if graph.get("schema_version") != "2.0.0":
        errors.append("schema_version must be 2.0.0")
    collections = {name: graph.get(name) for name in ("repositories", "nodes", "edges", "evidence", "diagnostics")}
    for name, values in collections.items():
        if not isinstance(values, list):
            errors.append(f"{name} must be an array")
    if errors:
        return errors

    ids: dict[str, set[str]] = {}
    for name in ("repositories", "nodes", "edges", "evidence", "diagnostics"):
        values = collections[name]
        item_ids = [item.get("id") for item in values if isinstance(item, dict)]
        ids[name] = {item_id for item_id in item_ids if isinstance(item_id, str)}
        if len(item_ids) != len(ids[name]):
            errors.append(f"{name} has a missing or duplicate ID")
        if item_ids != sorted(item_ids):
            errors.append(f"{name} is not sorted by ID")

    repositories = {item["id"]: item for item in graph["repositories"]}
    nodes = {item["id"]: item for item in graph["nodes"]}
    evidence = {item["id"]: item for item in graph["evidence"]}
    hidden = {item["id"] for item in graph["repositories"] if not item.get("visible")}

    for index, node in enumerate(graph["nodes"]):
        prefix = f"nodes[{index}]"
        unknown = set(node) - NODE_FIELDS
        if unknown:
            errors.append(f"{prefix} has unsupported fields {sorted(unknown)}")
        required = NODE_FIELDS - {"component_kind", "properties"}
        missing = required - set(node)
        if missing:
            errors.append(f"{prefix} misses {sorted(missing)}")
        repository = node.get("repository")
        if repository is not None and repository not in repositories:
            errors.append(f"{prefix} references missing repository {repository}")
        if repository in hidden:
            errors.append(f"{prefix} belongs to excluded foundation repository {repository}")
        if not set(node.get("dimensions", [])) <= {"RUNTIME", "BUSINESS"} or not node.get("dimensions"):
            errors.append(f"{prefix} has invalid dimensions")
        for ref in node.get("evidence", []):
            if ref not in evidence:
                errors.append(f"{prefix} references missing evidence {ref}")
        for path in node.get("source_paths", []):
            if not isinstance(path, str) or path.startswith("/") or ".." in Path(path).parts:
                errors.append(f"{prefix} has unsafe source path {path!r}")
            elif not wildcard_parent(workspace, path).exists():
                errors.append(f"{prefix} source path does not exist: {path}")
        if node.get("type") == "TABLE":
            if not any(evidence.get(ref, {}).get("extractor") == "java-database-client" for ref in node.get("evidence", [])):
                errors.append(f"{prefix} table lacks database-client evidence")
        if node.get("id") == "data-platform:dqsl":
            if node.get("properties", {}).get("platform_kind") != "EXTERNAL_DATA_LAKE":
                errors.append("DQSL must be classified as EXTERNAL_DATA_LAKE")

    for index, edge in enumerate(graph["edges"]):
        prefix = f"edges[{index}]"
        unknown = set(edge) - EDGE_FIELDS
        if unknown:
            errors.append(f"{prefix} has unsupported fields {sorted(unknown)}")
        required = EDGE_FIELDS - {"resolution_status", "properties"}
        missing = required - set(edge)
        if missing:
            errors.append(f"{prefix} misses {sorted(missing)}")
        if edge.get("source") not in nodes or edge.get("target") not in nodes:
            errors.append(f"{prefix} has a dangling endpoint")
        if edge.get("dimension") not in {"RUNTIME", "BUSINESS"}:
            errors.append(f"{prefix} has invalid dimension")
        for ref in edge.get("evidence", []):
            if ref not in evidence:
                errors.append(f"{prefix} references missing evidence {ref}")

    for index, item in enumerate(graph["evidence"]):
        prefix = f"evidence[{index}]"
        unknown = set(item) - EVIDENCE_FIELDS
        if unknown:
            errors.append(f"{prefix} has unsupported fields {sorted(unknown)}")
        if set(item) != EVIDENCE_FIELDS:
            errors.append(f"{prefix} must contain exactly {sorted(EVIDENCE_FIELDS)}")
        repository = item.get("repository")
        if repository is not None and repository not in repositories:
            errors.append(f"{prefix} references missing repository {repository}")
        path = item.get("path")
        if not isinstance(path, str) or not wildcard_parent(workspace, path).exists():
            errors.append(f"{prefix} path does not exist: {path}")

    for repository in graph["repositories"]:
        if not repository.get("visible"):
            continue
        owned = [node for node in graph["nodes"] if node.get("repository") == repository["id"]]
        if not any("RUNTIME" in node.get("dimensions", []) for node in owned):
            errors.append(f"{repository['id']} has no runtime projection")
        if not any("BUSINESS" in node.get("dimensions", []) for node in owned):
            errors.append(f"{repository['id']} has no business projection")
    return errors


def validate_dependencies(data: dict[str, Any], graph: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    expected = {repo["id"] for repo in graph["repositories"] if repo["visible"]}
    repositories = data.get("repositories", {})
    if data.get("schema_version") != "2.0.0" or set(repositories) != expected:
        errors.append("dependency catalog version or repository set does not match graph")
        return errors
    for repository, groups in repositories.items():
        for category in ("tables", "kafka_topics", "remote_applications", "data_platforms", "service_calls"):
            rows = groups.get(category)
            if not isinstance(rows, list):
                errors.append(f"{repository}.{category} must be an array")
                continue
            names = [row.get("name") for row in rows]
            if len(names) != len(set(names)):
                errors.append(f"{repository}.{category} contains duplicate dependencies")
            for row in rows:
                if not row.get("source_paths") or not row.get("relationships"):
                    errors.append(f"{repository}.{category}.{row.get('name')} lacks paths or relationships")
                if category == "tables" and (not row.get("access") or not row.get("clients")):
                    errors.append(f"{repository}.tables.{row.get('name')} lacks access or database-client evidence")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("graph", type=Path)
    parser.add_argument("--workspace", type=Path, default=Path(__file__).resolve().parents[4])
    parser.add_argument("--dependencies", type=Path)
    args = parser.parse_args()
    graph = load(args.graph)
    errors = validate(graph, args.workspace.resolve())
    if args.dependencies:
        errors.extend(validate_dependencies(load(args.dependencies), graph))
    if errors:
        print(json.dumps({"valid": False, "errors": errors}, indent=2))
        return 1
    print(json.dumps({"valid": True, "graph": str(args.graph.resolve())}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Analyze SDLC graph impact from a requirement or changed source paths."""

from __future__ import annotations

import argparse
import fnmatch
import json
import re
import subprocess
from collections import defaultdict, deque
from pathlib import Path
from typing import Any


STOP_WORDS = {"a", "allow", "an", "and", "as", "be", "by", "data", "for", "from", "in", "is", "of", "on", "operator", "operators", "or", "support", "the", "to", "with"}


def tokens(value: str) -> set[str]:
    return {item for item in re.findall(r"[a-z0-9]+", value.lower()) if len(item) > 2 and item not in STOP_WORDS}


def path_matches(pattern: str, changed: str) -> bool:
    if "*" in pattern:
        return fnmatch.fnmatch(changed, pattern)
    return changed == pattern or changed.startswith(pattern.rstrip("/") + "/")


def changed_from_git(workspace: Path, base_ref: str) -> list[str]:
    result = subprocess.check_output(["git", "diff", "--name-only", base_ref, "--"], cwd=workspace, text=True)
    return sorted({line.strip() for line in result.splitlines() if line.strip()})


def seed_requirement(nodes: list[dict[str, Any]], requirement: str) -> list[tuple[str, float, str]]:
    requested = tokens(requirement)
    ranked = []
    for node in nodes:
        if node["type"] not in {"BUSINESS_CAPABILITY", "PAGE", "COMPONENT", "SERVICE", "APPLICATION"}:
            continue
        searchable = " ".join((node["name"], node.get("functional_role", ""), node.get("business_meaning", "")))
        overlap = requested & tokens(searchable)
        if overlap:
            score = len(overlap) / max(len(requested), 1)
            ranked.append((node["id"], score, f"matched terms: {', '.join(sorted(overlap))}"))
    ranked.sort(key=lambda item: (-item[1], item[0]))
    return ranked[:12]


def seed_changes(nodes: list[dict[str, Any]], changed: list[str]) -> list[tuple[str, float, str]]:
    seeds = []
    for node in nodes:
        matches = sorted({path for path in changed for pattern in node.get("source_paths", []) if path_matches(pattern, path)})
        if matches:
            seeds.append((node["id"], 1.0, f"source path match: {', '.join(matches[:5])}"))
    return seeds


def traverse(graph: dict[str, Any], seeds: list[tuple[str, float, str]], depth: int) -> dict[str, Any]:
    nodes = {node["id"]: node for node in graph["nodes"]}
    adjacency: dict[str, list[tuple[str, dict[str, Any]]]] = defaultdict(list)
    for edge in graph["edges"]:
        adjacency[edge["source"]].append((edge["target"], edge))
        adjacency[edge["target"]].append((edge["source"], edge))
    queue = deque((node_id, 0, [node_id], [], score, reason) for node_id, score, reason in seeds)
    best: dict[str, dict[str, Any]] = {}
    while queue:
        node_id, distance, path, relationships, score, reason = queue.popleft()
        previous = best.get(node_id)
        if previous and previous["distance"] <= distance:
            continue
        best[node_id] = {"node": node_id, "distance": distance, "path": path, "relationships": relationships,
                         "score": round(score, 3), "reason": reason}
        if distance >= depth:
            continue
        if distance > 0 and nodes.get(node_id, {}).get("type") in {"APPLICATION", "SERVICE"}:
            continue
        for neighbor, edge in adjacency.get(node_id, []):
            if neighbor in path:
                continue
            queue.append((neighbor, distance + 1, path + [neighbor], relationships + [edge["relationship"]], score * 0.82, reason))
    rows = []
    for item in best.values():
        node = nodes.get(item["node"], {})
        rows.append(item | {"name": node.get("name"), "type": node.get("type"), "repository": node.get("repository"),
                            "dimensions": node.get("dimensions", []), "source_paths": node.get("source_paths", [])})
    rows.sort(key=lambda item: (item["distance"], -item["score"], item["node"]))
    business = [item for item in rows if "BUSINESS" in item["dimensions"]]
    runtime = [item for item in rows if "RUNTIME" in item["dimensions"]]
    return {"seeds": [item[0] for item in seeds], "business_impact": business, "runtime_impact": runtime,
            "affected_repositories": sorted({item["repository"] for item in rows if item.get("repository")}),
            "unresolved_frontiers": [item for item in rows if item["type"] in {"EXTERNAL_SYSTEM", "REMOTE_APPLICATION", "DATA_PLATFORM"}]}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--graph", type=Path, default=Path("system-graph/graph.json"))
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--requirement")
    group.add_argument("--changed-file", action="append", dest="changed_files")
    group.add_argument("--base-ref")
    parser.add_argument("--depth", type=int, default=4)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    graph = json.loads(args.graph.read_text(encoding="utf-8"))
    if args.requirement:
        mode, input_value = "REQUIREMENT", args.requirement
        seeds = seed_requirement(graph["nodes"], args.requirement)
    else:
        changed = args.changed_files or changed_from_git(args.graph.resolve().parents[1], args.base_ref)
        mode, input_value = "CODE_CHANGE", changed
        seeds = seed_changes(graph["nodes"], changed)
    result = {"schema_version": graph["schema_version"], "mode": mode, "input": input_value,
              **traverse(graph, seeds, args.depth)}
    payload = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")
    return 0 if seeds else 3


if __name__ == "__main__":
    raise SystemExit(main())

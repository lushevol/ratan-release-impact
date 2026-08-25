#!/usr/bin/env python3
"""Reusable, dependency-free query helpers for the canonical SDLC graph."""

from __future__ import annotations

import fnmatch
import re
from collections import Counter, defaultdict, deque
from typing import Any, Iterable


STOP_WORDS = {
    "a", "allow", "an", "and", "as", "be", "by", "data", "for", "from",
    "in", "is", "of", "on", "operator", "operators", "or", "support", "the",
    "to", "with",
}


def tokens(value: str) -> set[str]:
    return {
        item for item in re.findall(r"[a-z0-9]+", value.lower())
        if len(item) > 2 and item not in STOP_WORDS
    }


def path_matches(pattern: str, changed: str) -> bool:
    return fnmatch.fnmatch(changed, pattern) if "*" in pattern else (
        changed == pattern or changed.startswith(pattern.rstrip("/") + "/")
    )


def compact_node(node: dict[str, Any]) -> dict[str, Any]:
    """Keep the useful public fields while avoiding evidence-id noise."""
    fields = (
        "id", "type", "name", "repository", "dimensions", "functional_role",
        "business_meaning", "source_paths", "assertion_status", "component_kind",
        "properties",
    )
    return {field: node[field] for field in fields if field in node}


def seed_requirement(nodes: list[dict[str, Any]], requirement: str, limit: int = 12) -> list[tuple[str, float, str]]:
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
    return ranked[:limit]


def seed_changes(nodes: list[dict[str, Any]], changed: list[str]) -> list[tuple[str, float, str]]:
    seeds = []
    for node in nodes:
        matches = sorted({
            path for path in changed for pattern in node.get("source_paths", [])
            if path_matches(pattern, path)
        })
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
        best[node_id] = {
            "node": node_id, "distance": distance, "path": path,
            "relationships": relationships, "score": round(score, 3), "reason": reason,
        }
        if distance >= depth:
            continue
        if distance > 0 and nodes.get(node_id, {}).get("type") in {"APPLICATION", "SERVICE"}:
            continue
        for neighbor, edge in adjacency.get(node_id, []):
            if neighbor not in path:
                queue.append((
                    neighbor, distance + 1, path + [neighbor],
                    relationships + [edge["relationship"]], score * 0.82, reason,
                ))
    rows = []
    for item in best.values():
        node = nodes.get(item["node"], {})
        rows.append(item | {
            "name": node.get("name"), "type": node.get("type"),
            "repository": node.get("repository"), "dimensions": node.get("dimensions", []),
            "source_paths": node.get("source_paths", []),
        })
    rows.sort(key=lambda item: (item["distance"], -item["score"], item["node"]))
    return {
        "seeds": [item[0] for item in seeds],
        "business_impact": [item for item in rows if "BUSINESS" in item["dimensions"]],
        "runtime_impact": [item for item in rows if "RUNTIME" in item["dimensions"]],
        "affected_repositories": sorted({item["repository"] for item in rows if item.get("repository")}),
        "unresolved_frontiers": [
            item for item in rows
            if item["type"] in {"EXTERNAL_SYSTEM", "REMOTE_APPLICATION", "DATA_PLATFORM"}
        ],
    }


def search_graph(
    graph: dict[str, Any], query: str, repository: str | None = None,
    dimension: str | None = None, node_types: Iterable[str] | None = None, limit: int = 25,
) -> list[dict[str, Any]]:
    requested = tokens(query)
    allowed_types = set(node_types or [])
    repository_id = None if not repository else (repository if repository.startswith("repo:") else f"repo:{repository}")
    ranked = []
    for node in graph["nodes"]:
        if repository_id and node.get("repository") != repository_id:
            continue
        if dimension and dimension.upper() not in node.get("dimensions", []):
            continue
        if allowed_types and node["type"] not in allowed_types:
            continue
        searchable = " ".join([
            node["name"], node.get("functional_role", ""), node.get("business_meaning", ""),
            " ".join(node.get("source_paths", [])), " ".join(str(value) for value in node.get("properties", {}).values()),
        ])
        overlap = requested & tokens(searchable)
        phrase = query.lower() in searchable.lower()
        if not overlap and not phrase:
            continue
        score = (2.0 if phrase else 0.0) + len(overlap) / max(len(requested), 1)
        ranked.append((score, node["id"], compact_node(node)))
    ranked.sort(key=lambda item: (-item[0], item[1]))
    return [{"score": round(score, 3), **node} for score, _, node in ranked[:max(1, min(limit, 100))]]


def service_catalog(graph: dict[str, Any], dependencies: dict[str, Any]) -> dict[str, Any]:
    """Build the compact system picture used by AI clients and the MCP server."""
    nodes_by_repo: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for node in graph["nodes"]:
        if node.get("repository"):
            nodes_by_repo[node["repository"]].append(node)
    nodes = {node["id"]: node for node in graph["nodes"]}
    services = []
    for repo in graph["repositories"]:
        if not repo["visible"]:
            continue
        owned = nodes_by_repo.get(repo["id"], [])
        roots = [node for node in owned if node["type"] in {"APPLICATION", "SERVICE"}]
        capabilities = [compact_node(node) for node in owned if node["type"] == "BUSINESS_CAPABILITY"]
        pages = [compact_node(node) for node in owned if node["type"] == "PAGE"]
        components = [node for node in owned if node["type"] == "COMPONENT"]
        operations = {}
        for edge in graph["edges"]:
            source = nodes[edge["source"]]
            target = nodes[edge["target"]]
            if source.get("repository") != repo["id"] or target["type"] != "API_OPERATION":
                continue
            key = (target["id"], edge["relationship"])
            row = operations.setdefault(key, {
                "id": target["id"], "name": target["name"], "relationship": edge["relationship"],
                "protocol": target.get("properties", {}).get("protocol"),
                "path": target.get("properties", {}).get("path"), "source_paths": set(),
            })
            row["source_paths"].update(source.get("source_paths", []))
        api_operations = [
            {key: sorted(value) if isinstance(value, set) else value for key, value in row.items() if value is not None}
            for row in operations.values()
        ]
        api_operations.sort(key=lambda row: (row.get("protocol", ""), row["name"], row["relationship"]))
        databases = [compact_node(node) for node in owned if node["type"] == "DATABASE"]
        services.append({
            "id": repo["id"], "name": repo["name"], "kind": repo["kind"], "path": repo["path"],
            "root": compact_node(roots[0]) if roots else None,
            "business": {
                "capabilities": capabilities,
                "pages": pages,
                "component_count": len(components),
                "component_kinds": dict(sorted(Counter(node.get("component_kind", "UNCLASSIFIED") for node in components).items())),
            },
            "runtime": {
                "api_operations": api_operations,
                "databases": databases,
                **dependencies.get("repositories", {}).get(repo["id"], {}),
            },
        })
    return {
        "schema_version": graph["schema_version"],
        "purpose": "AI-ready service picture and entry point for requirement and code impact analysis",
        "counts": {
            "services": sum(service["kind"] == "SPRING" for service in services),
            "web_applications": sum(service["kind"] == "WEB" for service in services),
            "nodes": len(graph["nodes"]), "edges": len(graph["edges"]),
        },
        "services": services,
    }

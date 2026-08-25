#!/usr/bin/env python3
"""Reusable, dependency-free query helpers for the canonical SDLC graph."""

from __future__ import annotations

import fnmatch
import json
import re
from collections import Counter, defaultdict, deque
from typing import Any, Iterable


STOP_WORDS = {
    "a", "allow", "an", "and", "as", "be", "by", "data", "for", "from",
    "in", "is", "of", "on", "operator", "operators", "or", "support", "the",
    "to", "with",
}

# Requirement prose contains routing words that are useful for a human but too
# broad to identify an architecture node. Keep them out of seed selection;
# they remain searchable through search_graph().
DEFAULT_REQUIREMENT_GENERIC_TOKENS = {
    "business", "behavior", "cashflow", "change", "current", "exception", "future", "impact", "logic",
    "match", "matching", "requirement", "runtime", "same", "service", "services",
    "source", "status", "system", "within",
}

DEFAULT_DISTINCTIVE_SEED_TOKENS = {
    "amendment", "cashflowduplicatecheck", "duplicate", "lineage", "rebook",
    "settlement", "stella",
}

DEFAULT_REQUIREMENT_SYNONYMS = {
    # The graph models the owning capability as Duplicate Check while the
    # business requirement commonly calls the outcome a Rebook exception.
    "rebook": {"duplicate"},
    "duplicate": {"rebook"},
}

DEFAULT_SEED_CONFIG = {
    "generic_tokens": DEFAULT_REQUIREMENT_GENERIC_TOKENS,
    "distinctive_tokens": DEFAULT_DISTINCTIVE_SEED_TOKENS,
    "synonyms": DEFAULT_REQUIREMENT_SYNONYMS,
    "minimum_overlap": 2,
    "component_minimum_name_overlap": 2,
    "name_weight": 1.0,
    "description_weight": 0.25,
    "exact_name_bonus": 0.5,
    "confirmed_bonus": 0.1,
    "max_seeds": 12,
    "allow_weak_component_seeds": False,
}


def load_seed_config(path: str | None = None) -> dict[str, Any]:
    """Load requirement-seeding policy; absent config uses stable defaults."""
    config = dict(DEFAULT_SEED_CONFIG)
    if not path:
        return config
    with open(path, encoding="utf-8") as handle:
        payload = json.load(handle)
    section = payload.get("requirement_seeding", payload)
    if not isinstance(section, dict):
        raise ValueError("requirement_seeding config must be an object")
    for key, default in DEFAULT_SEED_CONFIG.items():
        if key in section:
            value = section[key]
            if isinstance(default, set):
                if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
                    raise ValueError(f"{key} must be an array of strings")
                config[key] = set(value)
            elif key == "synonyms":
                if not isinstance(value, dict) or not all(isinstance(k, str) and isinstance(v, list) and all(isinstance(item, str) for item in v) for k, v in value.items()):
                    raise ValueError("synonyms must map strings to arrays of strings")
                config[key] = {k: set(v) for k, v in value.items()}
            else:
                config[key] = value
    for key in ("minimum_overlap", "component_minimum_name_overlap", "max_seeds"):
        if not isinstance(config[key], int) or isinstance(config[key], bool):
            raise ValueError(f"{key} must be an integer")
    for key in ("name_weight", "description_weight", "exact_name_bonus", "confirmed_bonus"):
        if not isinstance(config[key], (int, float)) or isinstance(config[key], bool):
            raise ValueError(f"{key} must be numeric")
    if not isinstance(config["allow_weak_component_seeds"], bool):
        raise ValueError("allow_weak_component_seeds must be boolean")
    if config["minimum_overlap"] < 1 or config["component_minimum_name_overlap"] < 1 or config["max_seeds"] < 1:
        raise ValueError("minimum_overlap, component_minimum_name_overlap, and max_seeds must be positive")
    return config


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


def seed_requirement(nodes: list[dict[str, Any]], requirement: str, limit: int | None = None, config: dict[str, Any] | None = None) -> list[tuple[str, float, str]]:
    policy = config or DEFAULT_SEED_CONFIG
    requested = tokens(requirement) - policy["generic_tokens"]
    expanded_requested = set(requested)
    for term, aliases in policy["synonyms"].items():
        if term in requested:
            expanded_requested.update(aliases)
    ranked = []
    for node in nodes:
        if node["type"] not in {"BUSINESS_CAPABILITY", "PAGE", "COMPONENT", "SERVICE", "APPLICATION"}:
            continue
        searchable = " ".join((node["name"], node.get("functional_role", ""), node.get("business_meaning", "")))
        node_tokens = tokens(searchable)
        overlap = expanded_requested & node_tokens
        if not overlap:
            continue

        name_tokens = tokens(node["name"])
        name_overlap = overlap & name_tokens
        name_match = len(name_tokens) >= 2 and name_tokens <= expanded_requested
        distinctive = overlap & policy["distinctive_tokens"]
        if node["type"] in {"COMPONENT", "PAGE"} and len(name_overlap) < policy["component_minimum_name_overlap"] and not name_match and not distinctive and not policy["allow_weak_component_seeds"]:
            continue
        # A single generic match is not evidence of requirement ownership.
        # Preserve one-token seeds only for distinctive domain terms or an
        # exact named capability/component match.
        if len(overlap) < policy["minimum_overlap"] and not distinctive and not name_match:
            continue

        # Weight evidence in the node name much more than incidental prose
        # overlap. This prevents a long requirement from diluting the owning
        # capability below unrelated one-token matches.
        score = (policy["name_weight"] * len(name_overlap) / max(len(name_tokens), 1)) + (
            policy["description_weight"] * len(overlap) / max(len(expanded_requested), 1)
        )
        if name_match:
            score += policy["exact_name_bonus"]
        if node.get("assertion_status") == "CONFIRMED":
            score += policy["confirmed_bonus"]
        reason = f"matched terms: {', '.join(sorted(overlap))}"
        if name_match:
            reason += "; exact node-name coverage"
        ranked.append((node["id"], score, reason))
    ranked.sort(key=lambda item: (-item[1], item[0]))
    return ranked[:limit or policy["max_seeds"]]


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

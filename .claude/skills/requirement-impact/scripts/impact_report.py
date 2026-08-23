#!/usr/bin/env python3
"""Generate a deterministic candidate impact report from an SDLC graph."""
from __future__ import annotations

import argparse
import json
import re
from collections import deque
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from wiki_mcp import DEFAULT_COMMAND, search as wiki_search


STOP = {"the", "and", "for", "with", "from", "this", "that", "support", "new", "change"}
EDGE_TYPES = {"IMPLEMENTS", "PROVIDES", "CALLS", "DEPENDS_ON", "PUBLISHES", "SUBSCRIBES_TO", "READS_FROM", "WRITES_TO", "CONTAINS"}
TYPE_PRIORITY = {"Feature": 0, "Service": 1, "Endpoint": 2, "MessageQueue": 3, "Table": 4, "Database": 5, "ExternalDependency": 6, "Library": 7}


def local_wiki_search(root: Path, query_terms: set[str], limit: int = 8) -> list[dict]:
    """Use checked-in Wiki pages as an explicit offline fallback."""
    hits = []
    for path in sorted(root.rglob("*.md")) if root.exists() else []:
        content = path.read_text(errors="replace")
        overlap = sorted(query_terms & terms(content))
        if overlap:
            hits.append((len(overlap), path, overlap, content))
    hits.sort(key=lambda item: (-item[0], str(item[1])))
    return [{"path": str(path), "snippet": content[:500], "terms": overlap, "kind": "wiki-local-fallback"} for _, path, overlap, content in hits[:limit]]


def parse_wiki_text(text: str, limit: int = 8) -> list[dict]:
    """Extract auditable page references from the Wiki MCP Markdown response."""
    results = []
    blocks = re.split(r"\n(?=##?\s|---\s*$)", text)
    for block in blocks:
        path_match = re.search(r"^Path:\s*(.+)$", block, re.MULTILINE)
        if path_match:
            results.append({"path": path_match.group(1).strip(), "snippet": block[:700], "kind": "wiki"})
    return results[:limit]


def terms(text: str) -> set[str]:
    return {word for word in re.findall(r"[a-z0-9][a-z0-9_-]{2,}", text.lower()) if word not in STOP}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--graph", type=Path, default=Path("graph/graph.json"))
    parser.add_argument("--requirement", required=True)
    parser.add_argument("--out", type=Path, default=Path("impact.json"))
    parser.add_argument("--max-depth", type=int, default=3)
    parser.add_argument("--limit", type=int, default=120, help="Maximum affected nodes retained in the candidate report")
    parser.add_argument("--wiki-command", default=DEFAULT_COMMAND, help="Path to the Wiki MCP entrypoint")
    parser.add_argument("--wiki-project", default="current")
    parser.add_argument("--no-wiki", action="store_true", help="Skip the Wiki MCP query")
    parser.add_argument("--wiki-local", type=Path, default=Path("knowledge-base/wiki"), help="Offline Wiki fallback directory")
    args = parser.parse_args()
    graph = json.loads(args.graph.read_text())
    req_terms = terms(args.requirement)
    wiki_results = []
    wiki_error = None
    if not args.no_wiki:
        try:
            wiki_results = wiki_search(" ".join(sorted(req_terms)), args.wiki_command, args.wiki_project)
            if not isinstance(wiki_results, list):
                wiki_results = wiki_results.get("results", wiki_results.get("items", [])) if isinstance(wiki_results, dict) else parse_wiki_text(wiki_results)
        except Exception as exc:  # MCP is an optional evidence layer; static analysis remains useful.
            wiki_error = str(exc)
            wiki_results = local_wiki_search(args.wiki_local, req_terms)
    nodes = {node["id"]: node for node in graph.get("nodes", [])}
    features = [node for node in nodes.values() if node.get("type") == "Feature"]
    matched = []
    for node in features:
        haystack = terms(node.get("name", "")) | terms(node.get("id", ""))
        overlap = sorted(req_terms & haystack)
        if len(overlap) >= 2:
            matched.append((len(overlap), node, overlap))
    matched.sort(key=lambda item: (-item[0], item[1]["id"]))

    adjacency: dict[str, list[tuple[str, dict]]] = {}
    for edge in graph.get("edges", []):
        if edge.get("type") not in EDGE_TYPES:
            continue
        adjacency.setdefault(edge["source"], []).append((edge["target"], edge))
        adjacency.setdefault(edge["target"], []).append((edge["source"], edge))

    affected = {}
    queue = deque((node["id"], 0, [node["id"]]) for _, node, _ in matched)
    seen = set()
    while queue:
        current, distance, path = queue.popleft()
        if (current, distance) in seen or distance > args.max_depth:
            continue
        seen.add((current, distance))
        if current in nodes:
            impact = "direct" if distance == 0 else "indirect"
            affected.setdefault(current, {"id": current, "name": nodes[current].get("name"), "type": nodes[current].get("type"), "attributes": nodes[current].get("attributes", {}), "impact": impact, "distance": distance, "confidence": 0.82 if distance == 0 else max(0.4, 0.82 - distance * 0.14), "path": path})
        for target, edge in adjacency.get(current, []):
            if target not in path:
                queue.append((target, distance + 1, path + [target]))

    ranked = sorted(affected.values(), key=lambda item: (item["distance"], TYPE_PRIORITY.get(item["type"], 99), item["id"]))
    omitted = max(0, len(ranked) - args.limit)
    retained = ranked[:args.limit]
    repo_names = sorted({node.get("attributes", {}).get("repository", "").split("/")[-1] for node in retained if node.get("attributes", {}).get("repository")})
    report = {
        "schemaVersion": "1.0",
        "requirement": {"text": args.requirement, "terms": sorted(req_terms)},
        "matchedFeatures": [{"id": node["id"], "name": node["name"], "overlap": overlap, "confidence": min(0.95, 0.65 + 0.1 * count)} for count, node, overlap in matched],
        "affectedRepositories": repo_names,
        "affectedNodes": retained,
        "affectedFlows": [],
        "predictedChanges": [{"operation": "inspect", "target": item["id"], "reason": "reachable from matched feature"} for item in retained if item["type"] in {"Service", "Endpoint", "Table", "MessageQueue", "Library"}],
        "risks": [{"level": "high" if len(affected) > 40 else "medium" if len(affected) > 8 else "low", "reason": f"{len(affected)} graph nodes reachable within depth {args.max_depth}"}],
        "testScope": [],
        "unknowns": ["GitNexus symbol-level mappings and live Wiki freshness require a full MCP-enabled analysis pass."] + ([f"{omitted} lower-ranked graph nodes were omitted; expand with --limit or targeted GitNexus queries."] if omitted else []),
        "clarificationQuestions": [] if matched else ["Which business feature or domain process does this requirement change?"],
        "evidence": [{"kind": "graph", "source": str(args.graph), "detail": "Deterministic feature-term match and typed graph traversal"}] + [{"kind": item.get("kind", "wiki"), "source": item.get("path") or item.get("source") or item.get("title", "llm-wiki"), "detail": item.get("snippet") or item.get("content", "")[:500]} for item in wiki_results if isinstance(item, dict)],
    }
    if wiki_error:
        report["unknowns"].append(f"Wiki MCP query failed: {wiki_error}")
    args.out.write_text(json.dumps(report, indent=2, ensure_ascii=True) + "\n")
    print(json.dumps({"matchedFeatures": len(matched), "affectedNodes": len(affected), "out": str(args.out)}, ensure_ascii=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

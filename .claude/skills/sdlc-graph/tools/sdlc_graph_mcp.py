#!/usr/bin/env python3
"""Expose the generated SDLC graph as a dependency-free stdio MCP server."""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict, deque
from pathlib import Path
from typing import Any

from graph_query import compact_node, load_seed_config, search_graph, seed_changes, seed_requirement, traverse
from langfuse_trace import impact_trace


SERVER = {"name": "sdlc-graph", "version": "1.0.0"}


class GraphStore:
    def __init__(self, data_dir: Path, config_path: Path | None = None):
        self.data_dir = data_dir.resolve()
        self.graph = self._load("graph.json")
        self.services = self._load("services.json")
        self.dependencies = self._load("dependencies.json")
        self.manifest = self._load("manifest.json")
        self.seed_config = load_seed_config(str(config_path)) if config_path and config_path.is_file() else load_seed_config()
        self.nodes = {node["id"]: node for node in self.graph["nodes"]}

    def overview(self) -> dict[str, Any]:
        services = []
        for item in self.services["services"]:
            runtime = item["runtime"]
            services.append({
                "name": item["name"], "kind": item["kind"], "path": item["path"],
                "business": {
                    "capabilities": [node["name"] for node in item["business"]["capabilities"]],
                    "pages": [{"name": node["name"], "route": node.get("properties", {}).get("route")} for node in item["business"]["pages"]],
                    "component_kinds": item["business"]["component_kinds"],
                },
                "runtime": {
                    "api_operations": len(runtime["api_operations"]),
                    "databases": [node["name"] for node in runtime["databases"]],
                    "tables": [node["name"] for node in runtime["tables"]],
                    "kafka_topics": [node["name"] for node in runtime["kafka_topics"]],
                    "remote_applications": [node["name"] for node in runtime["remote_applications"]],
                    "data_platforms": [node["name"] for node in runtime["data_platforms"]],
                    "service_calls": [node["name"] for node in runtime["service_calls"]],
                },
            })
        return {"schema_version": self.services["schema_version"], "counts": self.services["counts"], "services": services}

    def _load(self, name: str) -> dict[str, Any]:
        path = self.data_dir / name
        if not path.is_file():
            raise FileNotFoundError(f"Missing generated artifact: {path}")
        return json.loads(path.read_text(encoding="utf-8"))

    def service(self, repository: str, include_components: bool = False) -> dict[str, Any]:
        name = repository.removeprefix("repo:")
        service = next((item for item in self.services["services"] if item["name"] == name), None)
        if not service:
            raise ValueError(f"Unknown repository: {repository}")
        result = dict(service)
        if include_components:
            repo_id = service["id"]
            result["business"] = dict(result["business"])
            result["business"]["components"] = [
                compact_node(node) for node in self.graph["nodes"]
                if node.get("repository") == repo_id and node["type"] == "COMPONENT"
            ]
        return result

    def impact(self, seeds: list[tuple[str, float, str]], depth: int, limit: int) -> dict[str, Any]:
        result = traverse(self.graph, seeds, max(1, min(depth, 8)))
        for key in ("business_impact", "runtime_impact", "unresolved_frontiers"):
            rows = result[key]
            result[f"{key}_total"] = len(rows)
            result[key] = rows[:max(1, min(limit, 200))]
        return result

    def neighborhood(self, node_id: str, depth: int) -> dict[str, Any]:
        if node_id not in self.nodes:
            raise ValueError(f"Unknown node: {node_id}")
        adjacency: dict[str, list[tuple[str, dict[str, Any]]]] = defaultdict(list)
        for edge in self.graph["edges"]:
            adjacency[edge["source"]].append((edge["target"], edge))
            adjacency[edge["target"]].append((edge["source"], edge))
        seen = {node_id}
        queue = deque([(node_id, 0)])
        edges = {}
        while queue:
            current, distance = queue.popleft()
            if distance >= max(1, min(depth, 4)):
                continue
            for neighbor, edge in adjacency[current]:
                edges[(edge["source"], edge["target"], edge["relationship"])] = edge
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append((neighbor, distance + 1))
        return {
            "center": compact_node(self.nodes[node_id]),
            "nodes": [compact_node(self.nodes[item]) for item in sorted(seen)],
            "edges": [edges[key] for key in sorted(edges)],
        }


TOOLS = [
    {
        "name": "get_system_overview",
        "description": "Get the compact full picture of all web applications, Spring services, business areas, and runtime dependency counts.",
        "inputSchema": {"type": "object", "properties": {}, "additionalProperties": False},
    },
    {
        "name": "list_services",
        "description": "List every visible repository with its kind, path, and architecture counts.",
        "inputSchema": {"type": "object", "properties": {}, "additionalProperties": False},
    },
    {
        "name": "get_service_picture",
        "description": "Get one repository's business capabilities, pages, component structure, APIs, tables, Kafka topics, remotes, and service calls.",
        "inputSchema": {
            "type": "object", "required": ["repository"], "additionalProperties": False,
            "properties": {
                "repository": {"type": "string", "description": "Repository name or repo:<name> id"},
                "include_components": {"type": "boolean", "default": False},
            },
        },
    },
    {
        "name": "search_architecture",
        "description": "Search business meaning, functional roles, protocols, names, and source paths across the architecture.",
        "inputSchema": {
            "type": "object", "required": ["query"], "additionalProperties": False,
            "properties": {
                "query": {"type": "string"}, "repository": {"type": "string"},
                "dimension": {"type": "string", "enum": ["BUSINESS", "RUNTIME"]},
                "node_types": {"type": "array", "items": {"type": "string"}},
                "limit": {"type": "integer", "minimum": 1, "maximum": 100, "default": 25},
            },
        },
    },
    {
        "name": "analyze_requirement_impact",
        "description": "Map a natural-language requirement to candidate business and runtime impact, affected repositories, files, and unresolved external frontiers.",
        "inputSchema": {
            "type": "object", "required": ["requirement"], "additionalProperties": False,
            "properties": {
                "requirement": {"type": "string"},
                "depth": {"type": "integer", "minimum": 1, "maximum": 8, "default": 4},
                "limit": {"type": "integer", "minimum": 1, "maximum": 200, "default": 60},
            },
        },
    },
    {
        "name": "analyze_code_impact",
        "description": "Map changed workspace-relative files to affected business workflows, runtime dependencies, and repositories.",
        "inputSchema": {
            "type": "object", "required": ["changed_files"], "additionalProperties": False,
            "properties": {
                "changed_files": {"type": "array", "minItems": 1, "items": {"type": "string"}},
                "depth": {"type": "integer", "minimum": 1, "maximum": 8, "default": 4},
                "limit": {"type": "integer", "minimum": 1, "maximum": 200, "default": 60},
            },
        },
    },
    {
        "name": "get_dependencies",
        "description": "Get database tables, Kafka topics, remote MFEs, data platforms, and downstream service calls for a repository.",
        "inputSchema": {
            "type": "object", "required": ["repository"], "additionalProperties": False,
            "properties": {"repository": {"type": "string"}},
        },
    },
    {
        "name": "get_node_neighborhood",
        "description": "Inspect one architecture node and its directly related business/runtime nodes and edges.",
        "inputSchema": {
            "type": "object", "required": ["node_id"], "additionalProperties": False,
            "properties": {
                "node_id": {"type": "string"},
                "depth": {"type": "integer", "minimum": 1, "maximum": 4, "default": 1},
            },
        },
    },
]


def call_tool(store: GraphStore, name: str, arguments: dict[str, Any]) -> Any:
    if name == "get_system_overview":
        return store.overview()
    if name == "list_services":
        return [{
            "id": item["id"], "name": item["name"], "kind": item["kind"], "path": item["path"],
            "business": {
                "capabilities": len(item["business"]["capabilities"]),
                "pages": len(item["business"]["pages"]),
                "components": item["business"]["component_count"],
            },
            "runtime": {
                "api_operations": len(item["runtime"]["api_operations"]),
                "tables": len(item["runtime"]["tables"]),
                "kafka_topics": len(item["runtime"]["kafka_topics"]),
                "service_calls": len(item["runtime"]["service_calls"]),
            },
        } for item in store.services["services"]]
    if name == "get_service_picture":
        return store.service(arguments["repository"], arguments.get("include_components", False))
    if name == "search_architecture":
        return search_graph(
            store.graph, arguments["query"], arguments.get("repository"), arguments.get("dimension"),
            arguments.get("node_types"), arguments.get("limit", 25),
        )
    if name == "analyze_requirement_impact":
        seeds = seed_requirement(store.graph["nodes"], arguments["requirement"], config=store.seed_config)
        return {"mode": "REQUIREMENT", "input": arguments["requirement"], **store.impact(
            seeds, arguments.get("depth", 4), arguments.get("limit", 60),
        )}
    if name == "analyze_code_impact":
        changed = arguments["changed_files"]
        return {"mode": "CODE_CHANGE", "input": changed, **store.impact(
            seed_changes(store.graph["nodes"], changed), arguments.get("depth", 4), arguments.get("limit", 60),
        )}
    if name == "get_dependencies":
        repo_id = arguments["repository"]
        repo_id = repo_id if repo_id.startswith("repo:") else f"repo:{repo_id}"
        result = store.dependencies["repositories"].get(repo_id)
        if result is None:
            raise ValueError(f"Unknown repository: {arguments['repository']}")
        return {"repository": repo_id, **result}
    if name == "get_node_neighborhood":
        return store.neighborhood(arguments["node_id"], arguments.get("depth", 1))
    raise ValueError(f"Unknown tool: {name}")


def resource(store: GraphStore, uri: str) -> Any:
    if uri == "sdlc-graph://overview":
        return store.overview()
    if uri == "sdlc-graph://manifest":
        return store.manifest
    if uri == "sdlc-graph://dependencies":
        return store.dependencies
    if uri.startswith("sdlc-graph://repository/"):
        return store.service(uri.removeprefix("sdlc-graph://repository/"))
    if uri.startswith("sdlc-graph://node/"):
        node_id = uri.removeprefix("sdlc-graph://node/")
        if node_id not in store.nodes:
            raise ValueError(f"Unknown node: {node_id}")
        return compact_node(store.nodes[node_id])
    raise ValueError(f"Unknown resource: {uri}")


def result_text(value: Any) -> dict[str, Any]:
    return {"content": [{"type": "text", "text": json.dumps(value, indent=2, ensure_ascii=False)}]}


def handle(store: GraphStore, request: dict[str, Any]) -> dict[str, Any] | None:
    method = request.get("method")
    params = request.get("params", {})
    request_id = request.get("id")
    if request_id is None:
        return None
    if method == "initialize":
        result = {
            "protocolVersion": params.get("protocolVersion", "2025-06-18"),
            "capabilities": {"tools": {}, "resources": {}, "prompts": {}},
            "serverInfo": SERVER,
        }
    elif method == "ping":
        result = {}
    elif method == "tools/list":
        result = {"tools": TOOLS}
    elif method == "tools/call":
        try:
            tool_name = params.get("name", "")
            arguments = params.get("arguments", {})
            with impact_trace(f"sdlc-mcp.{tool_name}", arguments, {"tool": tool_name, "observation_type": "tool"}) as trace:
                value = call_tool(store, tool_name, arguments)
                if trace.trace_id and isinstance(value, dict):
                    value = {**value, "trace_id": trace.trace_id}
                trace.update({"result_type": type(value).__name__, "result_keys": sorted(value) if isinstance(value, dict) else []},
                             output={"result_type": type(value).__name__, "result_keys": sorted(value) if isinstance(value, dict) else []})
                result = result_text(value)
        except (KeyError, TypeError, ValueError) as error:
            result = {"content": [{"type": "text", "text": str(error)}], "isError": True}
    elif method == "resources/list":
        result = {"resources": [
            {"uri": "sdlc-graph://overview", "name": "System service catalog", "mimeType": "application/json"},
            {"uri": "sdlc-graph://manifest", "name": "Generated artifact manifest", "mimeType": "application/json"},
            {"uri": "sdlc-graph://dependencies", "name": "Runtime dependency catalog", "mimeType": "application/json"},
        ]}
    elif method == "resources/templates/list":
        result = {"resourceTemplates": [
            {"uriTemplate": "sdlc-graph://repository/{repository}", "name": "Repository architecture picture", "mimeType": "application/json"},
            {"uriTemplate": "sdlc-graph://node/{node_id}", "name": "Architecture node", "mimeType": "application/json"},
        ]}
    elif method == "resources/read":
        uri = params["uri"]
        value = resource(store, uri)
        result = {"contents": [{"uri": uri, "mimeType": "application/json", "text": json.dumps(value, indent=2, ensure_ascii=False)}]}
    elif method == "prompts/list":
        result = {"prompts": [{
            "name": "analyze-requirement-impact",
            "description": "Analyze a requirement against both business and runtime dimensions.",
            "arguments": [{"name": "requirement", "description": "Requirement or user story", "required": True}],
        }]}
    elif method == "prompts/get":
        if params.get("name") != "analyze-requirement-impact":
            raise ValueError(f"Unknown prompt: {params.get('name')}")
        requirement = params.get("arguments", {}).get("requirement", "")
        result = {"description": "Evidence-backed SDLC impact analysis", "messages": [{
            "role": "user", "content": {"type": "text", "text": (
                f"Analyze this requirement: {requirement}\n"
                "Use get_system_overview, then analyze_requirement_impact. Inspect affected services and node neighborhoods. "
                "Separate business impact from runtime impact; include source paths, database tables, Kafka topics, APIs, "
                "external frontiers, confidence limits, and suggested test areas. Treat inferred descriptions as candidates."
            )},
        }]}
    else:
        return {"jsonrpc": "2.0", "id": request_id, "error": {"code": -32601, "message": f"Method not found: {method}"}}
    return {"jsonrpc": "2.0", "id": request_id, "result": result}


def read_message() -> dict[str, Any] | None:
    first = sys.stdin.buffer.readline()
    if not first:
        return None
    if first.lower().startswith(b"content-length:"):
        length = int(first.split(b":", 1)[1].strip())
        while sys.stdin.buffer.readline() not in {b"\n", b"\r\n", b""}:
            pass
        return json.loads(sys.stdin.buffer.read(length))
    return json.loads(first)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-dir", type=Path, default=Path("sdlc-graph-output"))
    parser.add_argument("--config", type=Path, default=Path("sdlc-graph-config.json"), help="Requirement seeding policy JSON")
    args = parser.parse_args()
    store = GraphStore(args.data_dir, args.config)
    while True:
        request: dict[str, Any] | None = None
        try:
            request = read_message()
            if request is None:
                break
            response = handle(store, request)
            if response is not None:
                sys.stdout.write(json.dumps(response, separators=(",", ":"), ensure_ascii=False) + "\n")
                sys.stdout.flush()
        except Exception as error:  # Keep the server alive and return a JSON-RPC error when possible.
            request_id = request.get("id") if isinstance(request, dict) else None
            response = {"jsonrpc": "2.0", "id": request_id, "error": {"code": -32603, "message": str(error)}}
            sys.stdout.write(json.dumps(response, separators=(",", ":")) + "\n")
            sys.stdout.flush()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

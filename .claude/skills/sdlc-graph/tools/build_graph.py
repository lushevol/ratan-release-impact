#!/usr/bin/env python3
"""Build the schema-v2 SDLC graph directly from local web and Spring repositories."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

from extract_java_dependencies import extract as extract_java_dependencies


SCHEMA_VERSION = "2.0.0"
GENERATOR_VERSION = "2.0.0"
FOUNDATION_REPOS = {"mfe-root-config"}
IGNORED_PARTS = {"node_modules", "generated", "coverage", "dist", "build", "test", "tests", "__tests__", "@types"}
WEB_GROUPS = {
    "components": ("UI_COMPONENT", "renders the user interactions and visual state for"),
    "hooks": ("HOOK", "coordinates reusable React behavior for"),
    "store": ("STATE", "owns client-side state and actions for"),
    "state": ("STATE", "owns client-side state and actions for"),
    "services": ("CLIENT", "integrates runtime data required by"),
    "service": ("CLIENT", "integrates runtime data required by"),
    "utils": ("UTILITY", "provides shared calculations and transformations for"),
    "common": ("UTILITY", "provides shared supporting behavior for"),
    "schema": ("SCHEMA", "defines data contracts used by"),
    "schemas": ("SCHEMA", "defines data contracts used by"),
}
WEB_DETAIL_PARENTS = {"components", "hooks", "services", "service", "utils", "workflow", "store", "state", "adapters"}
GENERIC_WEB_DIRS = {"common", "components", "hooks", "services", "service", "utils", "workflow", "store", "state", "config", "local", "production", "main", "root"}
JAVA_DETAIL_SUFFIXES = ("Controller", "Service", "Repository", "Client", "Listener", "Processor", "Handler", "Command", "Task", "Mapper", "Publisher")


def stable_id(prefix: str, *parts: object) -> str:
    raw = "|".join(str(part) for part in parts)
    return f"{prefix}:{hashlib.sha256(raw.encode()).hexdigest()[:24]}"


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-") or "unknown"


def words(value: str) -> str:
    value = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", value)
    return re.sub(r"[_-]+", " ", value).strip()


def git(repo: Path, *args: str) -> str | None:
    try:
        return subprocess.check_output(["git", "-C", str(repo), *args], text=True, stderr=subprocess.DEVNULL).strip() or None
    except (OSError, subprocess.CalledProcessError):
        return None


def read(path: Path) -> str:
    try:
        if path.stat().st_size > 2 * 1024 * 1024:
            return ""
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def source_path(workspace: Path, path: Path) -> str:
    return path.relative_to(workspace).as_posix()


class Graph:
    def __init__(self, workspace: Path) -> None:
        self.workspace = workspace
        self.repositories: list[dict[str, Any]] = []
        self.nodes: dict[str, dict[str, Any]] = {}
        self.edges: dict[tuple[str, str, str, str], dict[str, Any]] = {}
        self.evidence: dict[str, dict[str, Any]] = {}
        self.diagnostics: dict[str, dict[str, Any]] = {}
        self.repo_roots: dict[str, Path] = {}

    def add_repository(self, path: Path, kind: str, visible: bool) -> str:
        repo_id = f"repo:{path.name}"
        self.repo_roots[repo_id] = path
        self.repositories.append({
            "id": repo_id, "name": path.name, "path": source_path(self.workspace, path),
            "kind": kind, "role": "FOUNDATION" if not visible else "APPLICATION",
            "visible": visible, "ref": git(path, "branch", "--show-current"),
            "commit": git(path, "rev-parse", "HEAD"),
        })
        return repo_id

    def add_evidence(self, repository: str | None, path: str, line: int, declaration: str, extractor: str,
                     *, directness: str = "DIRECT") -> str:
        evidence_id = stable_id("evidence", repository, path, line, declaration, extractor)
        self.evidence[evidence_id] = {
            "id": evidence_id, "repository": repository, "path": path, "line": max(line, 1),
            "declaration": declaration[:500], "extractor": extractor, "directness": directness,
        }
        return evidence_id

    def add_node(self, node_id: str, node_type: str, name: str, repository: str | None, *,
                 dimensions: Iterable[str], component_kind: str | None, functional_role: str,
                 business_meaning: str, source_paths: Iterable[str], evidence: Iterable[str],
                 assertion_status: str = "CONFIRMED", properties: dict[str, Any] | None = None) -> str:
        item = self.nodes.get(node_id)
        if item:
            item["source_paths"] = sorted(set(item["source_paths"]) | set(source_paths))
            item["evidence"] = sorted(set(item["evidence"]) | set(evidence))
            item["dimensions"] = sorted(set(item["dimensions"]) | set(dimensions))
            item.get("properties", {}).update(properties or {})
            return node_id
        node = {
            "id": node_id, "type": node_type, "name": name, "repository": repository,
            "dimensions": sorted(set(dimensions)), "functional_role": functional_role,
            "business_meaning": business_meaning, "source_paths": sorted(set(source_paths)),
            "evidence": sorted(set(evidence)), "assertion_status": assertion_status,
        }
        if component_kind:
            node["component_kind"] = component_kind
        if properties:
            node["properties"] = properties
        self.nodes[node_id] = node
        return node_id

    def add_edge(self, source: str, target: str, relationship: str, dimension: str, evidence: Iterable[str], *,
                 assertion_status: str = "CONFIRMED", resolution_status: str | None = None,
                 properties: dict[str, Any] | None = None) -> str:
        key = (source, target, relationship, dimension)
        item = self.edges.get(key)
        if item:
            item["evidence"] = sorted(set(item["evidence"]) | set(evidence))
            return item["id"]
        edge = {
            "id": stable_id("edge", *key), "source": source, "target": target,
            "relationship": relationship, "dimension": dimension,
            "evidence": sorted(set(evidence)), "assertion_status": assertion_status,
        }
        if resolution_status:
            edge["resolution_status"] = resolution_status
        if properties:
            edge["properties"] = properties
        self.edges[key] = edge
        return edge["id"]

    def diagnostic(self, code: str, message: str, repository: str | None = None, path: str | None = None) -> None:
        diagnostic_id = stable_id("diagnostic", code, repository, path, message)
        self.diagnostics[diagnostic_id] = {
            "id": diagnostic_id, "severity": "WARNING", "code": code,
            "message": message, **({"repository": repository} if repository else {}),
            **({"path": path} if path else {}),
        }

    def document(self) -> dict[str, Any]:
        return {
            "schema_version": SCHEMA_VERSION,
            "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
            "generator": {"name": "sdlc-graph", "version": GENERATOR_VERSION},
            "repositories": sorted(self.repositories, key=lambda item: item["id"]),
            "nodes": sorted(self.nodes.values(), key=lambda item: item["id"]),
            "edges": sorted(self.edges.values(), key=lambda item: item["id"]),
            "evidence": sorted(self.evidence.values(), key=lambda item: item["id"]),
            "diagnostics": sorted(self.diagnostics.values(), key=lambda item: item["id"]),
        }


def code_files(root: Path, suffixes: tuple[str, ...]) -> Iterable[Path]:
    for path in sorted(root.rglob("*")):
        if path.is_file() and path.suffix in suffixes and not any(part in IGNORED_PARTS for part in path.parts):
            yield path


def line_at(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def resolve_import(source: Path, specifier: str) -> Path | None:
    if not specifier.startswith("."):
        return None
    base = (source.parent / specifier).resolve()
    for candidate in (base, *(base.with_suffix(suffix) for suffix in (".tsx", ".ts", ".jsx", ".js")),
                      *(base / f"index{suffix}" for suffix in (".tsx", ".ts", ".jsx", ".js"))):
        if candidate.is_file():
            return candidate
    return None


def web_owner_for(path: Path, page_roots: dict[Path, str], app_id: str) -> str:
    matches = [(root, node_id) for root, node_id in page_roots.items() if path == root or root in path.parents]
    return max(matches, key=lambda item: len(item[0].parts))[1] if matches else app_id


def web_detail_kind(path: Path) -> tuple[str, str, str]:
    lower_parts = {part.lower() for part in path.parts}
    name = words(path.name)
    if "quick search" in name.lower() or "quicksearch" in path.as_posix().lower():
        return "QUICK_SEARCH", f"Captures, validates, and transforms rapid search criteria for {name}", f"Lets users narrow operational data quickly without constructing an advanced query"
    if "components" in lower_parts:
        return "UI_COMPONENT", f"Renders the {name} user interface and interaction states", f"Presents the {name} portion of its owning workflow"
    if "hooks" in lower_parts:
        return "HOOK", f"Coordinates reusable React behavior for {name}", f"Keeps {name} workflow behavior consistent across screens"
    if "workflow" in lower_parts:
        return "WORKFLOW_COMPONENT", f"Coordinates the frontend steps for {name}", f"Implements the user journey for {name}"
    if lower_parts & {"services", "service", "adapters"}:
        return "CLIENT", f"Integrates data and actions required by {name}", f"Connects the {name} workflow to runtime capabilities"
    if lower_parts & {"store", "state"}:
        return "STATE", f"Owns client-side state and actions for {name}", f"Preserves the working state of the {name} workflow"
    return "UTILITY", f"Provides supporting frontend behavior for {name}", f"Supports the {name} portion of its owning business capability"


def extract_web_details(graph: Graph, repo: Path, repository: str, domain_roots: dict[str, Path],
                        page_roots: dict[Path, str]) -> None:
    src = repo / "src"
    for directory in sorted(path for path in src.rglob("*") if path.is_dir()):
        relative = directory.relative_to(src)
        if any(part in IGNORED_PARTS for part in relative.parts) or len(relative.parts) > 7:
            continue
        name_lower = directory.name.lower()
        parent_lower = directory.parent.name.lower()
        is_quick_search = "quicksearch" in directory.as_posix().lower() or "quick-search" in directory.as_posix().lower()
        if is_quick_search and any("quicksearch" in parent.name.lower() or "quick-search" in parent.name.lower() for parent in directory.parents if parent != src):
            continue
        if not is_quick_search and (parent_lower not in WEB_DETAIL_PARENTS or name_lower in GENERIC_WEB_DIRS):
            continue
        direct_files = sorted(path for path in directory.iterdir() if path.is_file() and path.suffix in {".ts", ".tsx", ".js", ".jsx", ".json"}
                              and not path.name.endswith((".test.ts", ".test.tsx", ".spec.ts", ".spec.tsx")))
        if not direct_files:
            continue
        domain_name, domain_root = next(((name, root) for name, root in domain_roots.items() if root == directory or root in directory.parents), (relative.parts[0], src / relative.parts[0]))
        capability_id = f"capability:{repo.name}:{slug(domain_name)}"
        if capability_id not in graph.nodes:
            continue
        kind, role, meaning = web_detail_kind(directory)
        path_value = source_path(graph.workspace, directory) + "/**/*"
        ev = graph.add_evidence(repository, source_path(graph.workspace, direct_files[0]), 1,
                                f"Detailed frontend component {directory.name}", "web-component-detail", directness="SEMANTIC")
        component_id = f"component:{repo.name}:web-detail:{slug(relative.as_posix())}"
        graph.add_node(component_id, "COMPONENT", f"{words(domain_name)} / {words(directory.name)}", repository,
                       dimensions=("RUNTIME", "BUSINESS"), component_kind=kind, functional_role=role,
                       business_meaning=meaning, source_paths=(path_value,), evidence=(ev,), assertion_status="INFERRED",
                       properties={"description_source": "SOURCE_INFERRED", "detail_level": "MODULE"})
        graph.add_edge(capability_id, component_id, "REALIZED_BY", "BUSINESS", (ev,), assertion_status="INFERRED")
        domain_component = f"component:{repo.name}:{slug(domain_name)}:domain"
        if domain_component in graph.nodes:
            graph.add_edge(domain_component, component_id, "CONTAINS_COMPONENT", "RUNTIME", (ev,), assertion_status="INFERRED")
        for page_root, page_id in page_roots.items():
            if domain_root == page_root or domain_root in page_root.parents or page_root in domain_root.parents:
                graph.add_edge(page_id, component_id, "USES_COMPONENT", "RUNTIME", (ev,), assertion_status="INFERRED")


def extract_web(graph: Graph, repo: Path, repository: str, visible: bool) -> None:
    app_id = f"application:{repo.name}"
    manifest = repo / "package.json"
    evidence = graph.add_evidence(repository, source_path(graph.workspace, manifest), 1, "Web application manifest", "web-manifest")
    graph.add_node(
        app_id, "APPLICATION", repo.name, repository, dimensions=("RUNTIME", "BUSINESS"),
        component_kind="MICRO_FRONTEND" if visible else "FOUNDATION", functional_role="Hosts a React micro-frontend runtime",
        business_meaning="Provides shared platform behavior" if not visible else f"Delivers the {words(repo.name)} user experience",
        source_paths=(source_path(graph.workspace, repo / "src") + "/**/*",), evidence=(evidence,),
        properties={"visible": visible},
    )
    imports: dict[Path, dict[str, Path]] = {}
    files = list(code_files(repo / "src", (".ts", ".tsx", ".js", ".jsx")))
    for path in files:
        text = read(path)
        mapping: dict[str, Path] = {}
        for match in re.finditer(r'import\s+(?:\{[^}]+\}|\*\s+as\s+)?([A-Za-z_$][\w$]*)?[^"\']*from\s*["\']([^"\']+)["\']', text):
            target = resolve_import(path, match.group(2))
            if match.group(1) and target:
                mapping[match.group(1)] = target
        imports[path] = mapping

    page_roots: dict[Path, str] = {}
    for path in files:
        text = read(path)
        for match in re.finditer(r'<Route\b[^>]*\bpath\s*=\s*(?:["\']([^"\']+)["\']|\{([^}]+)\})[^>]*\belement\s*=\s*\{\s*<([A-Za-z_$][\w$]*)', text, re.S):
            route, route_expression, component = match.groups()
            route = route or route_expression.strip()
            component_path = imports.get(path, {}).get(component, path)
            page_root = component_path.parent if component_path.name.startswith("index.") else component_path
            route_ev = graph.add_evidence(repository, source_path(graph.workspace, path), line_at(text, match.start()), match.group(0), "react-router")
            page_id = f"page:{repo.name}:{slug(route)}"
            graph.add_node(
                page_id, "PAGE", words(component), repository, dimensions=("RUNTIME", "BUSINESS"), component_kind="PAGE",
                functional_role=f"Renders the React route {route}", business_meaning=f"Supports the {words(component)} business workflow",
                source_paths=(source_path(graph.workspace, component_path),), evidence=(route_ev,),
                properties={"route": route},
            )
            graph.add_edge(app_id, page_id, "ROUTES_TO", "RUNTIME", (route_ev,))
            graph.add_edge(app_id, page_id, "DELIVERS", "BUSINESS", (route_ev,), assertion_status="INFERRED")
            page_roots[page_root] = page_id

    domain_roots: dict[str, Path] = {}
    for child in sorted((repo / "src").iterdir() if (repo / "src").exists() else []):
        if child.is_dir() and child.name not in IGNORED_PARTS | {"Root", "root", "LazyAntd"}:
            domain_roots[child.name] = child
    for name, root in domain_roots.items():
        capability_ev = graph.add_evidence(repository, source_path(graph.workspace, root), 1, f"Domain source area {name}", "web-domain-grouping", directness="SEMANTIC")
        capability_id = f"capability:{repo.name}:{slug(name)}"
        graph.add_node(
            capability_id, "BUSINESS_CAPABILITY", words(name), repository, dimensions=("BUSINESS",), component_kind=None,
            functional_role=f"Groups the frontend behavior for {words(name)}", business_meaning=f"Represents the {words(name)} business capability",
            source_paths=(source_path(graph.workspace, root) + "/**/*",), evidence=(capability_ev,), assertion_status="INFERRED",
        )
        graph.add_edge(app_id, capability_id, "IMPLEMENTS", "BUSINESS", (capability_ev,), assertion_status="INFERRED")
        domain_component_id = f"component:{repo.name}:{slug(name)}:domain"
        graph.add_node(
            domain_component_id, "COMPONENT", f"{words(name)} domain", repository,
            dimensions=("RUNTIME", "BUSINESS"), component_kind="DOMAIN_COMPONENT",
            functional_role=f"Coordinates the frontend behavior owned by {words(name)}",
            business_meaning=f"Implements the user-facing portion of the {words(name)} capability",
            source_paths=(source_path(graph.workspace, root) + "/**/*",), evidence=(capability_ev,), assertion_status="INFERRED",
        )
        graph.add_edge(capability_id, domain_component_id, "REALIZED_BY", "BUSINESS", (capability_ev,), assertion_status="INFERRED")
        related_pages = [node_id for page_root, node_id in page_roots.items() if page_root == root or root in page_root.parents]
        for page_id in related_pages:
            graph.add_edge(capability_id, page_id, "REALIZED_BY", "BUSINESS", (capability_ev,), assertion_status="INFERRED")
            graph.add_edge(page_id, domain_component_id, "USES_COMPONENT", "RUNTIME", (capability_ev,), assertion_status="INFERRED")
        for group_name, (kind, role) in WEB_GROUPS.items():
            group = root / group_name
            if not group.exists():
                continue
            component_id = f"component:{repo.name}:{slug(name)}:{kind.lower()}"
            graph.add_node(
                component_id, "COMPONENT", f"{words(name)} {words(group_name)}", repository,
                dimensions=("RUNTIME", "BUSINESS"), component_kind=kind,
                functional_role=f"{role.capitalize()} {words(name)}",
                business_meaning=f"Supports the {words(name)} workflow without defining a separate business capability",
                source_paths=(source_path(graph.workspace, group) + "/**/*",), evidence=(capability_ev,), assertion_status="INFERRED",
            )
            graph.add_edge(capability_id, component_id, "REALIZED_BY", "BUSINESS", (capability_ev,), assertion_status="INFERRED")
            for page_id in related_pages:
                graph.add_edge(page_id, component_id, "USES_COMPONENT", "RUNTIME", (capability_ev,), assertion_status="INFERRED")

    extract_web_details(graph, repo, repository, domain_roots, page_roots)

    endpoint_nodes: dict[tuple[str, str], str] = {}
    for path in files:
        if path.name.endswith((".test.ts", ".test.tsx", ".spec.ts", ".spec.tsx")) or path.name.lower().startswith("readme"):
            continue
        text = read(path)
        owner = web_owner_for(path, page_roots, app_id)
        path_value = source_path(graph.workspace, path)
        for match in re.finditer(r'System\.import\s*\(\s*["\']([^"\']+)["\']\s*\)', text):
            name = match.group(1)
            ev = graph.add_evidence(repository, path_value, line_at(text, match.start()), match.group(0), "systemjs-import")
            remote_id = f"remote:{slug(name)}"
            graph.add_node(remote_id, "REMOTE_APPLICATION", name, None, dimensions=("RUNTIME",), component_kind=None,
                           functional_role="Provides a remotely loaded micro-frontend", business_meaning="External or separately deployed user capability",
                           source_paths=(), evidence=(ev,), properties={"module": name})
            graph.add_edge(owner, remote_id, "LOADS_REMOTE", "RUNTIME", (ev,), resolution_status="UNRESOLVED")
        url_matches = list(re.finditer(r'["\'](/api/[A-Za-z0-9_./{}?=&:-]+)["\']', text))
        lower = text.lower()
        protocol = "GRAPHQL" if "graphql" in lower else "REST"
        relationship = "CALLS_GRAPHQL" if protocol == "GRAPHQL" else "CALLS_REST"
        if "websocketlink" in lower or "graphql-ws" in lower or re.search(r'\bWebSocket\s*\(', text):
            protocol, relationship = "WEBSOCKET", "SUBSCRIBES_WS"
        for match in url_matches:
            url = match.group(1).rstrip(".,;)")
            ev = graph.add_evidence(repository, path_value, line_at(text, match.start()), match.group(0), f"web-{protocol.lower()}")
            operation_id = endpoint_nodes.setdefault((protocol, url), f"operation:{protocol.lower()}:{slug(url)}")
            graph.add_node(operation_id, "API_OPERATION", url, None, dimensions=("RUNTIME",), component_kind=None,
                           functional_role=f"Provides a {protocol} runtime interface", business_meaning="Supplies data or actions required by a user workflow",
                           source_paths=(), evidence=(ev,), properties={"protocol": protocol, "path": url})
            client_id = f"component:{repo.name}:client:{stable_id('path', path_value).split(':')[1]}"
            graph.add_node(client_id, "COMPONENT", path.stem, repository, dimensions=("RUNTIME", "BUSINESS"),
                           component_kind=f"{protocol}_CLIENT", functional_role=f"Calls {protocol} operation {url}",
                           business_meaning=f"Connects {graph.nodes.get(owner, {}).get('name', repo.name)} to required runtime data",
                           source_paths=(path_value,), evidence=(ev,))
            graph.add_edge(owner, client_id, "USES_COMPONENT", "RUNTIME", (ev,))
            graph.add_edge(client_id, operation_id, relationship, "RUNTIME", (ev,), resolution_status="UNRESOLVED")
        for match in re.finditer(r'\bgql\s*`\s*(query|mutation|subscription)\s+([A-Za-z_$][\w$]*)', text, re.I):
            operation_type, operation_name = match.groups()
            protocol = "WEBSOCKET" if operation_type.lower() == "subscription" else "GRAPHQL"
            relationship = "SUBSCRIBES_WS" if protocol == "WEBSOCKET" else "CALLS_GRAPHQL"
            ev = graph.add_evidence(repository, path_value, line_at(text, match.start()), match.group(0), "web-graphql-operation")
            operation_id = f"operation:{protocol.lower()}:{slug(operation_name)}"
            graph.add_node(
                operation_id, "API_OPERATION", operation_name, None, dimensions=("RUNTIME",), component_kind=None,
                functional_role=f"Provides a {operation_type.lower()} GraphQL operation",
                business_meaning="Supplies data or actions required by a user workflow", source_paths=(), evidence=(ev,),
                properties={"protocol": protocol, "operation_type": operation_type.upper(), "operation_name": operation_name},
            )
            client_id = f"component:{repo.name}:client:{stable_id('path', path_value).split(':')[1]}"
            graph.add_node(
                client_id, "COMPONENT", path.stem, repository, dimensions=("RUNTIME", "BUSINESS"),
                component_kind=f"{protocol}_CLIENT", functional_role=f"Invokes GraphQL operation {operation_name}",
                business_meaning=f"Connects {graph.nodes.get(owner, {}).get('name', repo.name)} to required runtime data",
                source_paths=(path_value,), evidence=(ev,),
            )
            graph.add_edge(owner, client_id, "USES_COMPONENT", "RUNTIME", (ev,))
            graph.add_edge(client_id, operation_id, relationship, "RUNTIME", (ev,), resolution_status="UNRESOLVED")


def java_area(relative: Path) -> str:
    parts = relative.parts
    for marker in ("domain", "application", "service", "entrypoint", "infra", "shared"):
        if marker in parts:
            index = parts.index(marker)
            if index + 1 < len(parts) - 1:
                return parts[index + 1]
            return f"{marker}-core"
    if "controller" in parts or "web" in parts:
        stem = relative.stem.removesuffix("Controller")
        return stem or "api"
    if "feign" in parts:
        return "external-services"
    if "listener" in parts or "consumer" in parts or "event" in parts:
        return "messaging"
    if "repository" in parts or "mapper" in parts or "entity" in parts:
        return "persistence"
    if "configuration" in parts or "config" in parts:
        return "configuration"
    return "service-core"


def java_kind(path: Path, text: str) -> tuple[str, str]:
    if "@RestController" in text or "@Controller" in text:
        return "CONTROLLER", "entrypoint"
    if "@FeignClient" in text:
        return "FEIGN_CLIENT", "infrastructure"
    if "@KafkaListener" in text:
        return "KAFKA_CONSUMER", "entrypoint"
    if "KafkaTemplate" in text or "ProducerRecord" in text:
        return "KAFKA_PRODUCER", "infrastructure"
    if "Dqsl" in text or "DQSL" in text or "/dqsl/" in path.as_posix().lower():
        return "DATA_PLATFORM_CLIENT", "infrastructure"
    if any(token in text for token in ("Repository<", "JpaRepository", "CrudRepository", "BaseMapper", "JdbcTemplate")) or "repository" in path.as_posix().lower():
        return "REPOSITORY", "infrastructure"
    if "/domain/" in path.as_posix():
        return "DOMAIN_COMPONENT", "domain"
    if "Service" in path.stem or "/application/" in path.as_posix():
        return "APPLICATION_SERVICE", "application"
    return "COMPONENT", "support"


def ensure_java_component(graph: Graph, repo: Path, repository: str, service_id: str, path: Path, text: str,
                          capabilities: dict[str, str]) -> str:
    relative = path.relative_to(repo)
    area = java_area(relative)
    kind, layer = java_kind(relative, text)
    component_id = f"component:{repo.name}:{slug(area)}:{slug(layer)}"
    path_value = source_path(graph.workspace, path)
    ev = graph.add_evidence(repository, path_value, 1, f"{kind} in {area}", "spring-component-grouping", directness="SEMANTIC")
    graph.add_node(
        component_id, "COMPONENT", f"{words(area)} {words(layer)}", repository,
        dimensions=("RUNTIME", "BUSINESS"), component_kind=kind,
        functional_role=f"Implements the {layer} responsibilities for {words(area)}",
        business_meaning=f"Supports the {words(area)} business capability",
        source_paths=(source_path(graph.workspace, path.parent) + "/**/*.java",), evidence=(ev,), assertion_status="INFERRED",
        properties={"layer": layer},
    )
    capability_id = capabilities.get(area)
    if not capability_id:
        capability_id = f"capability:{repo.name}:{slug(area)}"
        capabilities[area] = capability_id
        graph.add_node(capability_id, "BUSINESS_CAPABILITY", words(area), repository, dimensions=("BUSINESS",), component_kind=None,
                       functional_role=f"Groups service behavior for {words(area)}", business_meaning=f"Represents the {words(area)} business capability",
                       source_paths=(source_path(graph.workspace, path.parent) + "/**/*.java",), evidence=(ev,), assertion_status="INFERRED")
        graph.add_edge(service_id, capability_id, "IMPLEMENTS", "BUSINESS", (ev,), assertion_status="INFERRED")
    graph.add_edge(capability_id, component_id, "REALIZED_BY", "BUSINESS", (ev,), assertion_status="INFERRED")
    return component_id


def java_detail_description(path: Path, kind: str, area: str) -> tuple[str, str]:
    name = words(path.stem)
    roles = {
        "CONTROLLER": f"Exposes inbound operations that invoke {name} behavior",
        "FEIGN_CLIENT": f"Calls a remote service required by {name}",
        "KAFKA_CONSUMER": f"Consumes Kafka messages and starts {name} processing",
        "KAFKA_PRODUCER": f"Publishes Kafka messages produced by {name}",
        "DATA_PLATFORM_CLIENT": f"Fetches selected upstream data through DQSL for {name}",
        "REPOSITORY": f"Reads and writes persistent data required by {name}",
        "DOMAIN_COMPONENT": f"Applies domain rules implemented by {name}",
        "APPLICATION_SERVICE": f"Coordinates the application use cases implemented by {name}",
        "COMPONENT": f"Provides supporting service behavior implemented by {name}",
    }
    meanings = {
        "CONTROLLER": f"Makes the {words(area)} capability available to callers",
        "FEIGN_CLIENT": f"Obtains external capabilities needed by {words(area)}",
        "KAFKA_CONSUMER": f"Responds asynchronously to events affecting {words(area)}",
        "KAFKA_PRODUCER": f"Notifies downstream consumers about {words(area)} outcomes",
        "DATA_PLATFORM_CLIENT": f"Supplies governed upstream data used by {words(area)} decisions",
        "REPOSITORY": f"Preserves the operational state of {words(area)}",
        "DOMAIN_COMPONENT": f"Enforces business behavior for {words(area)}",
        "APPLICATION_SERVICE": f"Carries out the {name} business operation within {words(area)}",
        "COMPONENT": f"Supports the {words(area)} business capability",
    }
    return roles[kind], meanings[kind]


def ensure_java_detail_component(graph: Graph, repo: Path, repository: str, path: Path, text: str,
                                 group_component: str, capabilities: dict[str, str]) -> str:
    relative = path.relative_to(repo)
    kind, layer = java_kind(relative, text)
    significant = kind in {"CONTROLLER", "FEIGN_CLIENT", "KAFKA_CONSUMER", "KAFKA_PRODUCER", "DATA_PLATFORM_CLIENT", "REPOSITORY"} or path.stem.endswith(JAVA_DETAIL_SUFFIXES)
    if not significant:
        return group_component
    area = java_area(relative)
    path_value = source_path(graph.workspace, path)
    ev = graph.add_evidence(repository, path_value, 1, f"Detailed Spring component {path.stem}", "spring-component-detail", directness="SEMANTIC")
    component_id = f"component:{repo.name}:java-detail:{stable_id('path', relative.as_posix()).split(':')[1]}"
    role, meaning = java_detail_description(path, kind, area)
    graph.add_node(component_id, "COMPONENT", path.stem, repository, dimensions=("RUNTIME", "BUSINESS"),
                   component_kind=kind, functional_role=role, business_meaning=meaning,
                   source_paths=(path_value,), evidence=(ev,), assertion_status="INFERRED",
                   properties={"description_source": "SOURCE_INFERRED", "detail_level": "CLASS", "layer": layer})
    graph.add_edge(group_component, component_id, "CONTAINS_COMPONENT", "RUNTIME", (ev,), assertion_status="INFERRED")
    capability_id = capabilities[area]
    graph.add_edge(capability_id, component_id, "REALIZED_BY", "BUSINESS", (ev,), assertion_status="INFERRED")
    return component_id


def extract_spring(graph: Graph, repo: Path, repository: str) -> None:
    service_id = f"service:{repo.name}"
    pom = repo / "pom.xml"
    manifest_ev = graph.add_evidence(repository, source_path(graph.workspace, pom), 1, "Spring service manifest", "spring-manifest")
    graph.add_node(service_id, "SERVICE", repo.name, repository, dimensions=("RUNTIME", "BUSINESS"), component_kind="SPRING_SERVICE",
                   functional_role="Runs a Spring service and its runtime adapters", business_meaning=f"Delivers the {words(repo.name)} business service",
                   source_paths=(source_path(graph.workspace, repo / "src/main") + "/**/*",), evidence=(manifest_ev,))
    java_root = repo / "src/main/java"
    files = list(code_files(java_root, (".java",)))
    capabilities: dict[str, str] = {}
    component_by_path: dict[str, str] = {}
    for path in files:
        text = read(path)
        path_value = source_path(graph.workspace, path)
        group_component = ensure_java_component(graph, repo, repository, service_id, path, text, capabilities)
        component = ensure_java_detail_component(graph, repo, repository, path, text, group_component, capabilities)
        component_by_path[path.relative_to(repo).as_posix()] = component
        for annotation in re.finditer(r'@(Get|Post|Put|Delete|Patch|Request)Mapping\s*\(([^)]*)\)', text, re.S):
            method = "ANY" if annotation.group(1) == "Request" else annotation.group(1).upper()
            values = re.findall(r'["\'](/[^"\']*)["\']', annotation.group(2))
            for url in values:
                ev = graph.add_evidence(repository, path_value, line_at(text, annotation.start()), annotation.group(0), "spring-rest")
                operation_id = f"operation:{repo.name}:{method.lower()}:{slug(url)}"
                graph.add_node(operation_id, "API_OPERATION", f"{method} {url}", repository, dimensions=("RUNTIME",), component_kind=None,
                               functional_role="Exposes a REST operation", business_meaning=f"Allows callers to invoke {words(java_area(path.relative_to(repo)))} behavior",
                               source_paths=(path_value,), evidence=(ev,), properties={"protocol": "REST", "method": method, "path": url})
                graph.add_edge(service_id, operation_id, "EXPOSES", "RUNTIME", (ev,))
                graph.add_edge(operation_id, component, "INVOKES", "RUNTIME", (ev,))
        feign = re.search(r'@FeignClient\s*\(([^)]*)\)', text, re.S)
        if feign:
            target_values = re.findall(r'["\']([^"\']+)["\']', feign.group(1))
            target = target_values[0] if target_values else "unresolved-service"
            ev = graph.add_evidence(repository, path_value, line_at(text, feign.start()), feign.group(0), "spring-feign")
            target_id = f"external-service:{slug(target)}"
            graph.add_node(target_id, "EXTERNAL_SYSTEM", target, None, dimensions=("RUNTIME",), component_kind=None,
                           functional_role="Provides a service called through Feign", business_meaning="External runtime dependency",
                           source_paths=(), evidence=(ev,), properties={"service_alias": target})
            graph.add_edge(component, target_id, "CALLS_SERVICE", "RUNTIME", (ev,), resolution_status="UNRESOLVED", properties={"client": "FEIGN"})
        if "Dqsl" in text or "DQSL" in text or "/dqsl/" in path.as_posix().lower():
            ev = graph.add_evidence(repository, path_value, 1, "DQSL data-platform client or query behavior", "dqsl-client")
            dqsl_id = "data-platform:dqsl"
            graph.add_node(dqsl_id, "DATA_PLATFORM", "DQSL", None, dimensions=("RUNTIME", "BUSINESS"), component_kind=None,
                           functional_role="Allows consumers to fetch data from selected upstream sources",
                           business_meaning="External data-lake access platform mediating governed upstream data retrieval",
                           source_paths=(), evidence=(ev,), properties={"platform_kind": "EXTERNAL_DATA_LAKE"})
            graph.add_edge(component, dqsl_id, "CALLS_DATA_PLATFORM", "RUNTIME", (ev,), resolution_status="RESOLVED")
        if re.search(r'Elasticsearch|OpenSearch|RestHighLevelClient|ElasticsearchClient', text):
            ev = graph.add_evidence(repository, path_value, 1, "Explicit search-engine client", "search-client")
            search_id = f"data-platform:{repo.name}:search"
            graph.add_node(search_id, "DATA_PLATFORM", "Search engine", None, dimensions=("RUNTIME",), component_kind=None,
                           functional_role="Provides indexed search operations", business_meaning="External indexed data dependency",
                           source_paths=(), evidence=(ev,), properties={"platform_kind": "SEARCH_ENGINE"})
            graph.add_edge(component, search_id, "QUERIES_DATA_PLATFORM", "RUNTIME", (ev,), resolution_status="UNRESOLVED")

    extracted = extract_java_dependencies(repo)
    if extracted["tables"]:
        postgres_evidence = next(
            (path for path in (repo / "pom.xml", repo / "src/main/resources/application.yml", repo / "src/main/resources/application.yaml")
             if path.exists() and re.search(r"postgres(?:ql)?", read(path), re.I)),
            None,
        )
        if postgres_evidence:
            postgres_path = source_path(graph.workspace, postgres_evidence)
            postgres_text = read(postgres_evidence)
            match = re.search(r"postgres(?:ql)?", postgres_text, re.I)
            ev = graph.add_evidence(
                repository, postgres_path, line_at(postgres_text, match.start()) if match else 1,
                "PostgreSQL runtime dependency", "postgres-client",
            )
            database_id = f"database:{repo.name}:postgresql"
            graph.add_node(
                database_id, "DATABASE", "PostgreSQL", repository, dimensions=("RUNTIME",), component_kind=None,
                functional_role="Hosts relational data accessed by the running service",
                business_meaning="Durable service-owned operational data store", source_paths=(postgres_path,), evidence=(ev,),
                properties={"engine": "POSTGRESQL"},
            )
            graph.add_edge(service_id, database_id, "CONNECTS_TO", "RUNTIME", (ev,))
    for table in extracted["tables"]:
        path_value = f"repos/{repo.name}/{table['path']}"
        ev = graph.add_evidence(repository, path_value, int(table["line"]), f"{table['client']} {table['access']} {table['name']}", "java-database-client",
                                directness="SEMANTIC" if table.get("assertion_status") == "INFERRED" else "DIRECT")
        table_id = f"table:{repo.name}:{slug(table['name'])}"
        graph.add_node(table_id, "TABLE", table["name"], repository, dimensions=("RUNTIME",), component_kind=None,
                       functional_role="Stores data accessed by the running service", business_meaning="Persists state required by service workflows",
                       source_paths=tuple(f"repos/{repo.name}/{item}" for item in table.get("related_paths", [table["path"]])), evidence=(ev,),
                       assertion_status=table.get("assertion_status", "CONFIRMED"), properties={"client": table["client"], "access": table["access"]})
        owner = component_by_path.get(table["path"], service_id)
        operations = ("READS", "WRITES") if table["access"] == "READ_WRITE" else (("READS",) if table["access"] == "READ" else ("WRITES",))
        for relationship in operations:
            graph.add_edge(owner, table_id, relationship, "RUNTIME", (ev,), assertion_status=table.get("assertion_status", "CONFIRMED"))
        database_id = f"database:{repo.name}:postgresql"
        if database_id in graph.nodes:
            graph.add_edge(database_id, table_id, "CONTAINS", "RUNTIME", (ev,))
    for topic in extracted["topics"]:
        path_value = f"repos/{repo.name}/{topic['path']}"
        ev = graph.add_evidence(repository, path_value, int(topic["line"]), f"{topic['direction']} {topic['name']}", "java-kafka-client")
        topic_id = f"message-channel:kafka:{slug(topic['name'])}"
        graph.add_node(topic_id, "MESSAGE_CHANNEL", topic["name"], None, dimensions=("RUNTIME",), component_kind=None,
                       functional_role="Carries Kafka messages between runtime components", business_meaning="Asynchronous event or command channel",
                       source_paths=(), evidence=(ev,), properties={"protocol": "KAFKA", "topic": topic["name"]})
        owner = component_by_path.get(topic["path"], service_id)
        relationship = topic["direction"] if topic["direction"] in {"PUBLISHES", "CONSUMES"} else "CONFIGURES_TOPIC"
        graph.add_edge(owner, topic_id, relationship, "RUNTIME", (ev,), assertion_status="CONFIRMED" if relationship != "CONFIGURES_TOPIC" else "INFERRED")


def resolve_cross_repository(graph: Graph) -> None:
    visible_apps = {repo["name"]: (f"application:{repo['name']}" if repo["kind"] == "WEB" else f"service:{repo['name']}")
                    for repo in graph.repositories if repo["visible"]}
    remote_aliases = {
        "@fm/ratan_cashflow_blotter": "mfe-cashflow-blotter",
        "@fm/ratan_container": "mfe-ratan-container",
        "@fm/base": "mfe-base",
    }
    service_aliases: dict[str, str] = {}
    for name, node_id in visible_apps.items():
        if node_id.startswith("service:"):
            for alias in {name, name.removesuffix("-service"), name.replace("-", "_"), name.upper()}:
                service_aliases[slug(alias)] = node_id
    additions: list[tuple[str, str, str, str, list[str], dict[str, Any]]] = []
    for edge in graph.edges.values():
        target = graph.nodes.get(edge["target"], {})
        if edge["relationship"] == "LOADS_REMOTE":
            repo_name = remote_aliases.get(str(target.get("properties", {}).get("module")))
            if repo_name in visible_apps:
                additions.append((edge["source"], visible_apps[repo_name], "LOADS_REMOTE", "RUNTIME", edge["evidence"], {"resolved_from": edge["target"]}))
                edge["resolution_status"] = "RESOLVED"
        if edge["relationship"] in {"CALLS_REST", "CALLS_GRAPHQL", "SUBSCRIBES_WS"}:
            caller_operation = target
            caller_path = str(caller_operation.get("properties", {}).get("path", ""))
            caller_name = str(caller_operation.get("properties", {}).get("operation_name", ""))
            caller_protocol = str(caller_operation.get("properties", {}).get("protocol", ""))
            candidates: list[dict[str, Any]] = []
            for provider in graph.nodes.values():
                if provider.get("type") != "API_OPERATION" or provider.get("repository") is None:
                    continue
                properties = provider.get("properties", {})
                provider_path = str(properties.get("path", ""))
                provider_name = str(properties.get("operation_name", ""))
                provider_protocol = str(properties.get("protocol", ""))
                path_match = bool(caller_path and provider_path and (caller_path.endswith(provider_path) or provider_path.endswith(caller_path)))
                name_match = bool(caller_name and provider_name and caller_name.lower() == provider_name.lower())
                protocol_match = caller_protocol == provider_protocol or {caller_protocol, provider_protocol} <= {"GRAPHQL", "WEBSOCKET"}
                if protocol_match and (path_match or name_match):
                    candidates.append(provider)
            if len(candidates) == 1:
                provider = candidates[0]
                additions.append((edge["source"], provider["id"], edge["relationship"], "RUNTIME", edge["evidence"], {"resolved_from": edge["target"]}))
                edge["resolution_status"] = "RESOLVED"
        if edge["relationship"] == "CALLS_SERVICE":
            alias = slug(str(target.get("properties", {}).get("service_alias", target.get("name", ""))))
            if alias in service_aliases:
                additions.append((edge["source"], service_aliases[alias], "CALLS_SERVICE", "RUNTIME", edge["evidence"], {"resolved_from": edge["target"]}))
                edge["resolution_status"] = "RESOLVED"
    for source, target, relationship, dimension, evidence, properties in additions:
        graph.add_edge(source, target, relationship, dimension, evidence, resolution_status="RESOLVED", properties=properties)


def apply_description_overrides(graph: Graph, path: Path) -> None:
    if not path.exists():
        return
    data = json.loads(path.read_text(encoding="utf-8"))
    for description in data.get("descriptions", []):
        node_id = description.get("node_id")
        node = graph.nodes.get(node_id)
        if not node:
            graph.diagnostic("UNKNOWN_DESCRIPTION_NODE", f"Description override references unknown node {node_id}", path=source_path(graph.workspace, path))
            continue
        evidence_ids = []
        for evidence_path in description.get("evidence_paths", []):
            candidate = graph.workspace / evidence_path.split("*", 1)[0].rstrip("/")
            if not candidate.exists():
                graph.diagnostic("INVALID_DESCRIPTION_EVIDENCE", f"Description evidence path does not exist: {evidence_path}", node.get("repository"), evidence_path)
                continue
            evidence_ids.append(graph.add_evidence(node.get("repository"), evidence_path, 1,
                                                   description.get("rationale", "AI-assisted business description"),
                                                   "business-description-override", directness="SEMANTIC"))
        for field in ("functional_role", "business_meaning"):
            value = description.get(field)
            if isinstance(value, str) and value.strip():
                node[field] = value.strip()
        node["evidence"] = sorted(set(node["evidence"]) | set(evidence_ids))
        node.setdefault("properties", {}).update({
            "description_source": description.get("source", "AI_INFERRED"),
            "description_confidence": description.get("confidence", "LOW"),
            "description_rationale": description.get("rationale", "AI inference from source context"),
        })


def dependencies(graph: Graph) -> dict[str, Any]:
    keys = ("tables", "kafka_topics", "remote_applications", "data_platforms", "service_calls")
    buckets: dict[str, dict[str, dict[str, dict[str, Any]]]] = {
        repo["id"]: {key: {} for key in keys} for repo in graph.repositories if repo["visible"]
    }
    for edge in graph.edges.values():
        source, target = graph.nodes.get(edge["source"]), graph.nodes.get(edge["target"])
        if not source or not target:
            continue
        repository = source.get("repository")
        if repository not in buckets:
            continue
        category = None
        if target["type"] == "TABLE" and edge["relationship"] in {"READS", "WRITES"}: category = "tables"
        elif target["type"] == "MESSAGE_CHANNEL": category = "kafka_topics"
        elif target["type"] == "REMOTE_APPLICATION": category = "remote_applications"
        elif target["type"] == "DATA_PLATFORM": category = "data_platforms"
        elif edge["relationship"] == "CALLS_SERVICE": category = "service_calls"
        if not category:
            continue
        row = buckets[repository][category].setdefault(target["name"], {"name": target["name"], "source_paths": set()})
        row["source_paths"].update(source.get("source_paths", []))
        row.setdefault("relationships", set()).add(edge["relationship"])
        for key, value in target.get("properties", {}).items():
            if key in {"access", "client"}:
                row.setdefault({"access": "access", "client": "clients"}[key], set()).add(value)
            else:
                row[key] = value
        if edge.get("resolution_status"):
            row.setdefault("resolution_statuses", set()).add(edge["resolution_status"])
    result: dict[str, dict[str, list[dict[str, Any]]]] = {}
    for repository, values in buckets.items():
        result[repository] = {}
        for key, rows in values.items():
            normalized = []
            for row in rows.values():
                normalized.append({name: sorted(value) if isinstance(value, set) else value for name, value in row.items()})
            result[repository][key] = sorted(normalized, key=lambda row: (row["name"], json.dumps(row, sort_keys=True)))
    return {"schema_version": SCHEMA_VERSION, "repositories": result}


def write_outputs(graph: Graph, out: Path) -> None:
    out.mkdir(parents=True, exist_ok=True)
    document = graph.document()
    (out / "graph.json").write_text(json.dumps(document, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (out / "dependencies.json").write_text(json.dumps(dependencies(graph), indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    repository_root = out / "repositories"
    for repo in document["repositories"]:
        if not repo["visible"]:
            continue
        directory = repository_root / repo["name"]
        directory.mkdir(parents=True, exist_ok=True)
        view = {"schema_version": SCHEMA_VERSION, "graph": "../../graph.json", "repository": repo["id"],
                "dimensions": {"runtime": {"repository": repo["id"], "dimension": "RUNTIME"},
                               "business": {"repository": repo["id"], "dimension": "BUSINESS"}}}
        (directory / "view.json").write_text(json.dumps(view, indent=2) + "\n", encoding="utf-8")
    counts = {collection: len(document[collection]) for collection in ("repositories", "nodes", "edges", "evidence", "diagnostics")}
    (out / "summary.json").write_text(json.dumps({"schema_version": SCHEMA_VERSION, "counts": counts}, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace", type=Path, default=Path(__file__).resolve().parents[4])
    parser.add_argument("--repos", type=Path)
    parser.add_argument("--out", type=Path)
    parser.add_argument("--descriptions", type=Path)
    args = parser.parse_args()
    workspace = args.workspace.resolve()
    repos_root = (args.repos or workspace / "repos").resolve()
    out = (args.out or workspace / "sdlc-graph-output").resolve()
    graph = Graph(workspace)
    for repo in sorted(path for path in repos_root.iterdir() if path.is_dir() and (path / ".git").is_dir()):
        if (repo / "package.json").exists():
            visible = repo.name not in FOUNDATION_REPOS
            repository = graph.add_repository(repo, "WEB", visible)
            if visible:
                extract_web(graph, repo, repository, visible)
        elif (repo / "pom.xml").exists():
            repository = graph.add_repository(repo, "SPRING", True)
            extract_spring(graph, repo, repository)
        else:
            graph.diagnostic("UNSUPPORTED_REPOSITORY", "No supported package.json or pom.xml", path=source_path(workspace, repo))
    resolve_cross_repository(graph)
    apply_description_overrides(graph, (args.descriptions or workspace / "architecture-descriptions.json").resolve())
    write_outputs(graph, out)
    print(json.dumps({"output": str(out), "repositories": len(graph.repositories), "visible_repositories": sum(bool(r["visible"]) for r in graph.repositories),
                      "nodes": len(graph.nodes), "edges": len(graph.edges), "evidence": len(graph.evidence), "diagnostics": len(graph.diagnostics)}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

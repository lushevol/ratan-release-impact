#!/usr/bin/env python3
"""Bounded, evidence-backed SDLC graph scan for the local Ratan repositories."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from xml.etree import ElementTree


ROOT = Path(__file__).resolve().parents[4]
REPOS_ROOT = ROOT / "repos"
OUT = ROOT / "graph"
EXTRACTOR_VERSION = "sdlc-graph-local/1.1.0"
MAX_FILE_BYTES = 2 * 1024 * 1024


def slug(value: str) -> str:
    value = re.sub(r"[^A-Za-z0-9._-]+", "-", value.strip().lower()).strip("-")
    return value or "unknown"


def sha256(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def git(repo: Path, *args: str) -> str:
    try:
        return subprocess.check_output(["git", "-C", str(repo), *args], text=True, stderr=subprocess.DEVNULL).strip()
    except (subprocess.CalledProcessError, OSError):
        return "unknown"


def rel(repo: Path, path: Path) -> str:
    return path.relative_to(repo).as_posix()


def read_lines(path: Path, diagnostics: list[dict], repo_id: str) -> list[str]:
    try:
        if path.stat().st_size > MAX_FILE_BYTES:
            diagnostics.append({"severity": "warning", "code": "file_skipped_size", "repository": repo_id,
                                "path": path.relative_to(ROOT).as_posix(), "detail": f"Skipped file larger than {MAX_FILE_BYTES} bytes"})
            return []
        data = path.read_bytes()
        if b"\x00" in data:
            diagnostics.append({"severity": "info", "code": "binary_skipped", "repository": repo_id,
                                "path": path.relative_to(ROOT).as_posix(), "detail": "Skipped binary file"})
            return []
        return data.decode("utf-8", errors="replace").splitlines()
    except OSError as exc:
        diagnostics.append({"severity": "warning", "code": "file_unreadable", "repository": repo_id,
                            "path": path.relative_to(ROOT).as_posix(), "detail": type(exc).__name__})
        return []


class Graph:
    def __init__(self) -> None:
        self.nodes: dict[str, dict] = {}
        self.edges: dict[tuple[str, str, str], dict] = {}
        self.diagnostics: list[dict] = []
        self.repo_meta: list[dict] = []

    def node(self, node_id: str, node_type: str, name: str, **attrs: object) -> str:
        if node_id not in self.nodes:
            self.nodes[node_id] = {"id": node_id, "type": node_type, "name": name, "lifecycle": "active", "attributes": {}}
        self.nodes[node_id]["attributes"].update({k: v for k, v in attrs.items() if v is not None})
        return node_id

    def edge(self, source: str, target: str, edge_type: str, *, repository: str, commit: str, path: str,
             start: int, end: int | None = None, kind: str, detail: str, confidence: float,
             status: str = "supported", extractor: str = "local") -> None:
        key = (source, target, edge_type)
        evidence = {"kind": kind, "repository": repository, "commit": commit, "path": path,
                    "startLine": start, "endLine": end or start, "extractor": extractor,
                    "extractorVersion": EXTRACTOR_VERSION, "detail": detail}
        if key not in self.edges:
            self.edges[key] = {"id": f"edge:{sha256('|'.join(key))[:32]}", "source": source, "target": target,
                               "type": edge_type, "status": status, "confidence": confidence,
                               "firstSeen": commit, "lastSeen": commit, "evidence": [evidence]}
        else:
            edge = self.edges[key]
            edge["confidence"] = max(edge["confidence"], confidence)
            edge["evidence"].append(evidence)
            edge["evidence"] = sorted(edge["evidence"], key=lambda e: (e["repository"], e["path"], e["startLine"], e["detail"]))


def xml_ns(root: ElementTree.Element) -> dict[str, str]:
    if root.tag.startswith("{"):
        return {"m": root.tag.split("}", 1)[0][1:]}
    return {"m": ""}


def text_of(elem: ElementTree.Element | None, ns: dict[str, str]) -> str | None:
    if elem is None:
        return None
    return (elem.text or "").strip() or None


def pom_info(repo: Path, graph: Graph, repo_id: str, commit: str) -> tuple[str, str, str, dict[str, str]] | None:
    path = repo / "pom.xml"
    lines = read_lines(path, graph.diagnostics, repo_id)
    if not lines:
        return None
    try:
        root = ElementTree.fromstring("\n".join(lines))
    except ElementTree.ParseError as exc:
        graph.diagnostics.append({"severity": "error", "code": "malformed_pom", "repository": repo_id,
                                  "path": "pom.xml", "detail": type(exc).__name__})
        return None
    ns = xml_ns(root)
    def find(path_expr: str) -> ElementTree.Element | None:
        return root.find(path_expr, ns)
    group = text_of(find("m:groupId"), ns)
    artifact = text_of(find("m:artifactId"), ns)
    version = text_of(find("m:version"), ns)
    parent = root.find("m:parent", ns)
    if parent is not None:
        group = group or text_of(parent.find("m:groupId", ns), ns)
        version = version or text_of(parent.find("m:version", ns), ns)
    if not group or not artifact or not version:
        graph.diagnostics.append({"severity": "error", "code": "pom_identity_incomplete", "repository": repo_id,
                                  "path": "pom.xml", "detail": "Could not resolve groupId, artifactId, and version"})
        return None
    dep_rows: dict[str, str] = {}
    for dep in root.findall("m:dependencies/m:dependency", ns):
        dg = text_of(dep.find("m:groupId", ns), ns)
        da = text_of(dep.find("m:artifactId", ns), ns)
        ds = text_of(dep.find("m:scope", ns), ns) or "compile"
        dv = text_of(dep.find("m:version", ns), ns)
        if dg and da:
            dep_rows[f"{dg}:{da}"] = json.dumps({"scope": ds, "version": dv})
    # Direct dependency evidence is line-based, but values are parsed structurally above.
    for coord, payload in sorted(dep_rows.items()):
        dg, da = coord.split(":", 1)
        meta = json.loads(payload)
        dep_line = next((i for i, line in enumerate(lines, 1) if f"<artifactId>{da}</artifactId>" in line), 1)
        lid = graph.node(f"library:maven/{slug(dg)}/{slug(da)}", "Library", da, groupId=dg, version=meta["version"], scope=meta["scope"], external=True)
        sid = f"service:ratan-release-impact/{repo.name}"
        graph.edge(sid, lid, "DEPENDS_ON", repository=repo_id, commit=commit, path="pom.xml", start=dep_line,
                   kind="manifest", detail=f"Direct Maven dependency {coord} (scope={meta['scope']})", confidence=0.98)
    return group, artifact, version, {k: json.loads(v).get("version") or "managed" for k, v in dep_rows.items()}


def find_lines(lines: list[str], pattern: str) -> list[tuple[int, re.Match[str]]]:
    rx = re.compile(pattern)
    return [(i, m) for i, line in enumerate(lines, 1) if (m := rx.search(line))]


def scan_delivery_metadata(repo: Path, graph: Graph, repo_id: str, commit: str, pom_version: str) -> None:
    """Inspect CI metadata for diagnostics only; never add delivery nodes or edges."""
    for path in sorted(repo.glob("*pipeline*.yml")):
        lines = read_lines(path, graph.diagnostics, repo_id)
        if not lines:
            continue
        package_version = next((m.group(1) for _, m in find_lines(lines, r"packageVersion:\s*['\"]?([^'\"\s]+)")), pom_version)
        if package_version != pom_version:
            graph.diagnostics.append({"severity": "warning", "code": "pipeline_pom_version_mismatch", "repository": repo_id,
                                      "path": rel(repo, path), "detail": f"pipeline packageVersion={package_version}, pom version={pom_version}"})
        graph.diagnostics.append({"severity": "info", "code": "delivery_metadata_excluded", "repository": repo_id,
                                  "path": rel(repo, path), "detail": "CI/CD configuration was inspected for provenance and version diagnostics; no pipeline or deployment nodes were emitted"})


def scan_configs_and_sql(repo: Path, graph: Graph, repo_id: str, commit: str, service_id: str) -> None:
    db_id = f"database:ratan-release-impact/{repo.name}/postgresql"
    config_paths = sorted(set(repo.glob("src/main/resources/application*.yml")) | set(repo.glob("src/main/resources/bootstrap*.yml")) | set(repo.glob("app.conf")))
    db_seen = False
    for path in config_paths:
        lines = read_lines(path, graph.diagnostics, repo_id)
        for i, line in enumerate(lines, 1):
            if re.search(r"\b(datasource|jdbc|PGSL_RDB_URL|SPRING_DATASOURCE_URL)\b", line, re.I):
                db_seen = True
                break
    migration_paths = sorted((repo / "src/main/resources/db/migration").rglob("*.sql")) if (repo / "src/main/resources/db/migration").exists() else []
    reported_unknown_schema: set[Path] = set()
    if db_seen or migration_paths:
        graph.node(db_id, "Database", f"{repo.name} PostgreSQL database", engine="postgresql", repository=repo_id)
    if db_seen:
        path = next((p for p in config_paths if p.exists()), repo / "app.conf")
        lines = read_lines(path, graph.diagnostics, repo_id)
        line_no = next((i for i, line in enumerate(lines, 1) if re.search(r"\b(datasource|jdbc|PGSL_RDB_URL|SPRING_DATASOURCE_URL)\b", line, re.I)), 1)
        graph.edge(service_id, db_id, "CONNECTS_TO", repository=repo_id, commit=commit, path=rel(repo, path), start=line_no,
                   kind="configuration", detail="Datasource configuration references a redacted PostgreSQL connection variable", confidence=0.90)
        graph.diagnostics.append({"severity": "info", "code": "redacted_datasource", "repository": repo_id,
                                  "path": rel(repo, path), "detail": "Datasource URL values were intentionally excluded from graph output"})
    for path in migration_paths:
        lines = read_lines(path, graph.diagnostics, repo_id)
        for i, line in enumerate(lines, 1):
            m = re.search(r"\bCREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?([A-Za-z0-9_.\"`-]+)", line, re.I)
            if not m:
                m = re.search(r"\b(?:ALTER\s+TABLE|(?:INSERT\s+INTO)|UPDATE|DELETE\s+FROM|FROM)\s+([A-Za-z0-9_.\"`-]+)", line, re.I)
            if not m:
                continue
            qualified = m.group(1).strip('"`').lower()
            parts = qualified.split(".")
            schema = parts[-2] if len(parts) > 1 else "unknown"
            table = parts[-1]
            schema_id = graph.node(f"schema:{db_id}/{slug(schema)}", "Schema", schema, database=db_id, resolved=schema != "unknown")
            graph.edge(db_id, schema_id, "CONTAINS", repository=repo_id, commit=commit, path=rel(repo, path), start=i,
                       kind="sql-migration", detail=f"Migration resolves schema {schema}", confidence=0.98 if schema != "unknown" else 0.62)
            table_id = graph.node(f"table:{schema_id}/{slug(table)}", "Table", table, database=db_id, schema=schema_id)
            graph.edge(schema_id, table_id, "CONTAINS", repository=repo_id, commit=commit, path=rel(repo, path), start=i,
                       kind="sql-migration", detail=f"Migration references table {table}", confidence=0.98)
            if schema == "unknown" and path not in reported_unknown_schema:
                reported_unknown_schema.add(path)
                graph.diagnostics.append({"severity": "info", "code": "unresolved_sql_schema", "repository": repo_id,
                                          "path": rel(repo, path), "line": i, "detail": "One or more unqualified tables were emitted under an unresolved schema"})
            upper = line.upper()
            if re.search(r"\b(?:SELECT|FROM)\b", upper):
                graph.edge(service_id, table_id, "READS_FROM", repository=repo_id, commit=commit, path=rel(repo, path), start=i,
                           kind="sql-migration", detail=f"Static SQL read of table {table}", confidence=0.94)
            if re.search(r"\b(?:INSERT|UPDATE|DELETE)\b", upper):
                graph.edge(service_id, table_id, "WRITES_TO", repository=repo_id, commit=commit, path=rel(repo, path), start=i,
                           kind="sql-migration", detail=f"Static SQL write of table {table}", confidence=0.94)


def scan_endpoints_and_feign(repo: Path, graph: Graph, repo_id: str, commit: str, service_id: str,
                             known_services: dict[str, str], endpoint_index: dict[tuple[str, str], str]) -> None:
    java_paths = sorted((repo / "src/main/java").rglob("*.java")) if (repo / "src/main/java").exists() else []
    mappings: list[tuple[str, str, int, str]] = []
    for path in java_paths:
        lines = read_lines(path, graph.diagnostics, repo_id)
        for i, line in enumerate(lines, 1):
            m = re.search(r"@(Get|Post|Put|Delete|Patch|Request)Mapping\s*(?:\([^)]*)?", line)
            if not m:
                continue
            method = "ANY" if m.group(1) == "Request" else m.group(1).upper()
            path_match = re.search(r"(?:path|value)\s*=\s*['\"]([^'\"]+)['\"]|Mapping\s*\(\s*['\"]([^'\"]+)['\"]", line)
            endpoint_path = next((x for x in path_match.groups() if x), "") if path_match else ""
            if not endpoint_path.startswith("/"):
                continue
            mappings.append((method, endpoint_path, i, rel(repo, path)))
            endpoint_id = graph.node(f"endpoint:{service_id}/{method}/{sha256(endpoint_path)[:16]}", "Endpoint", f"{method} {endpoint_path}", path=endpoint_path, method=method, service=service_id)
            endpoint_index[(service_id, f"{method} {endpoint_path}")] = endpoint_id
            graph.edge(service_id, endpoint_id, "PROVIDES", repository=repo_id, commit=commit, path=rel(repo, path), start=i,
                       kind="source", detail=f"Spring mapping {method} {endpoint_path}", confidence=0.93, extractor="spring.mapping")
        # Feign declarations are deliberately resolved by exact normalized service aliases only.
        lines = read_lines(path, graph.diagnostics, repo_id)
        for i, line in enumerate(lines, 1):
            fm = re.search(r"@FeignClient\s*\((.*)\)", line)
            if not fm:
                continue
            args = fm.group(1)
            quoted = re.findall(r"['\"]([^'\"]+)['\"]", args)
            target_name = quoted[0] if quoted else None
            if not target_name:
                graph.diagnostics.append({"severity": "warning", "code": "unresolved_feign_client", "repository": repo_id,
                                          "path": rel(repo, path), "line": i, "detail": "Feign client has no statically resolvable service name"})
                continue
            key = slug(target_name)
            target_id = known_services.get(key)
            if not target_id:
                target_id = graph.node(f"external-dependency:service-registry/{key}", "ExternalDependency", target_name,
                                       dependencyKind="service-registry", resolution="unresolved-service-registry")
                graph.diagnostics.append({"severity": "info", "code": "external_service_unresolved", "repository": repo_id,
                                          "path": rel(repo, path), "line": i, "detail": f"Feign target {target_name} is outside the scanned repository scope"})
            graph.edge(service_id, target_id, "CALLS", repository=repo_id, commit=commit, path=rel(repo, path), start=i,
                       kind="source", detail=f"Feign client targets service name {target_name}", confidence=0.88, extractor="spring.feign")
            # Add endpoint call evidence for mappings in the following interface block when resolvable.
            for j in range(i, min(i + 35, len(lines))):
                mm = re.search(r"@(Get|Post|Put|Delete|Patch|Request)Mapping\s*(?:\([^)]*)?", lines[j])
                if not mm:
                    continue
                method = "ANY" if mm.group(1) == "Request" else mm.group(1).upper()
                pm = re.search(r"(?:path|value)\s*=\s*['\"]([^'\"]+)['\"]|Mapping\s*\(\s*['\"]([^'\"]+)['\"]", lines[j])
                ep = next((x for x in pm.groups() if x), "") if pm else ""
                if target_id and ep.startswith("/"):
                    endpoint_id = endpoint_index.get((target_id, f"{method} {ep}"))
                    if endpoint_id:
                        graph.edge(service_id, endpoint_id, "CALLS", repository=repo_id, commit=commit, path=rel(repo, path), start=j + 1,
                                   kind="source", detail=f"Feign mapping calls {method} {ep}", confidence=0.84, extractor="spring.feign")
                break


def scan_topics(repo: Path, graph: Graph, repo_id: str, commit: str, service_id: str) -> None:
    java_paths = sorted((repo / "src/main/java").rglob("*.java")) if (repo / "src/main/java").exists() else []
    constants: dict[str, str] = {}
    broker_id: str | None = None
    def ensure_broker(path: Path, line_no: int) -> str:
        nonlocal broker_id
        if broker_id is None:
            broker_id = graph.node("message-broker:ratan/kafka", "MessageBroker", "Kafka", technology="kafka")
            graph.edge(service_id, broker_id, "CONNECTS_TO", repository=repo_id, commit=commit, path=rel(repo, path), start=line_no,
                       kind="configuration", detail="Kafka dependency or messaging configuration detected", confidence=0.90, extractor="kafka.detector")
        return broker_id
    pom_lines = read_lines(repo / "pom.xml", graph.diagnostics, repo_id)
    config_candidates = sorted(repo.glob("src/main/resources/application*.yml"))
    kafka_line = next(((repo / "pom.xml", i) for i, line in enumerate(pom_lines, 1) if "kafka" in line.lower()), None)
    if kafka_line is None:
        for candidate in config_candidates:
            candidate_lines = read_lines(candidate, graph.diagnostics, repo_id)
            kafka_line = next(((candidate, i) for i, line in enumerate(candidate_lines, 1) if "kafka" in line.lower()), None)
            if kafka_line:
                break
    if kafka_line:
        ensure_broker(kafka_line[0], kafka_line[1])
    for path in java_paths:
        lines = read_lines(path, graph.diagnostics, repo_id)
        for i, line in enumerate(lines, 1):
            m = re.search(r"(?:static\s+final\s+)?String\s+([A-Z][A-Z0-9_]*(?:TOPIC|EVENT)[A-Z0-9_]*)\s*=\s*['\"]([^'\"]+)['\"]", line)
            if m and "${" not in m.group(2):
                constants[m.group(1)] = m.group(2)
    for path in java_paths:
        lines = read_lines(path, graph.diagnostics, repo_id)
        for i, line in enumerate(lines, 1):
            listener = re.search(r"@KafkaListener\s*\([^)]*topics\s*=\s*([^,)]*)", line)
            if listener:
                token = listener.group(1).strip()
                topic = constants.get(token) or (token.strip('"\'{} ') if token.startswith(('"', "'")) else None)
                if topic and not topic.startswith(("$", "#")):
                    broker = ensure_broker(path, i)
                    tid = graph.node(f"message-queue:ratan/{slug(topic)}", "MessageQueue", topic, broker=broker, technology="kafka")
                    graph.edge(broker, tid, "CONTAINS", repository=repo_id, commit=commit, path=rel(repo, path), start=i,
                               kind="source", detail=f"Kafka broker contains queue/topic {topic}", confidence=0.91, extractor="spring.kafka")
                    graph.edge(service_id, tid, "SUBSCRIBES_TO", repository=repo_id, commit=commit, path=rel(repo, path), start=i,
                               kind="source", detail=f"Kafka listener subscribes to {topic}", confidence=0.91, extractor="spring.kafka")
                elif topic and topic.startswith(("$", "#")):
                    graph.diagnostics.append({"severity": "info", "code": "dynamic_topic_unresolved", "repository": repo_id,
                                              "path": rel(repo, path), "line": i, "detail": "Kafka listener topic is a runtime expression and was not materialized"})
            if re.search(r"(?:KafkaTemplate|ProducerRecord|produceMsg|publishProcessing)", line):
                tokens = re.findall(r"\b[A-Z][A-Z0-9_]*(?:TOPIC|EVENT)[A-Z0-9_]*\b", line)
                for token in tokens:
                    topic = constants.get(token)
                    if topic:
                        broker = ensure_broker(path, i)
                        tid = graph.node(f"message-queue:ratan/{slug(topic)}", "MessageQueue", topic, broker=broker, technology="kafka")
                        graph.edge(broker, tid, "CONTAINS", repository=repo_id, commit=commit, path=rel(repo, path), start=i,
                                   kind="source", detail=f"Kafka broker contains queue/topic {topic}", confidence=0.86, extractor="spring.kafka")
                        graph.edge(service_id, tid, "PUBLISHES", repository=repo_id, commit=commit, path=rel(repo, path), start=i,
                                   kind="source", detail=f"Kafka producer uses {token}={topic}", confidence=0.86, extractor="spring.kafka")
    # Configuration names are retained as unresolved topic nodes without values.
    for path in sorted(repo.glob("src/main/resources/application*.yml")):
        lines = read_lines(path, graph.diagnostics, repo_id)
        for i, line in enumerate(lines, 1):
            if re.search(r"(?:topic|topics):\s*\$\{", line, re.I):
                graph.diagnostics.append({"severity": "info", "code": "dynamic_topic_unresolved", "repository": repo_id,
                                          "path": rel(repo, path), "line": i, "detail": "Kafka topic is supplied by an environment variable and was not materialized"})


FEATURE_CATALOG = {
    "lifecycle": [
        ("Cashflow lifecycle and status transitions", "src/main/java/com/scb/ratan/cashflow/lifecycle/lifecycle"),
        ("Cashflow creation, amendment, withdrawal, reinstatement, and release", "src/main/java/com/scb/ratan/cashflow/lifecycle/lifecycle/domain/action"),
        ("Cashflow holding, replay, and message management", "src/main/java/com/scb/ratan/cashflow/lifecycle/service"),
        ("Cashflow cutoff, materialization, and payment-date calculation", "src/main/java/com/scb/ratan/cashflow/lifecycle/service/cutoff"),
        ("Duplicate checking and validation", "src/main/java/com/scb/ratan/cashflow/lifecycle/controller/CashflowDuplicateCheckController.java"),
        ("Batch and scheduler processing", "src/main/java/com/scb/ratan/cashflow/lifecycle/lifecycle/job"),
        ("Maker-checker lifecycle operations", "src/main/java/com/scb/ratan/cashflow/lifecycle/lifecycle/entrypoint/CashflowLifecycleMakerCheckerController.java"),
        ("Settlement, netting, splitting, SWIFT, SSI, and downstream event updates", "src/main/java/com/scb/ratan/cashflow/lifecycle/lifecycle/domain/action"),
        ("Counterparty and DQSL data enrichment", "src/main/java/com/scb/ratan/cashflow/lifecycle/lifecycle/infra/dqsl"),
    ],
    "netting": [
        ("Manual cashflow netting", "src/main/java/com/cn/ratan/netting/entrypoint/web/netting/NettingController.java"),
        ("Automatic netting rules, configuration, and rule refresh", "src/main/java/com/cn/ratan/netting/domain/autonetting/rule"),
        ("Automatic netting prematch, grouping, subjobs, and resultant compensation", "src/main/java/com/cn/ratan/netting/domain/autonetting"),
        ("Netting by CCIL, BIC, NDS, and IRS settlement flows", "src/main/java/com/cn/ratan/netting/application/service"),
        ("Cashflow splitting, validation, amount amendment, and unsplitting", "src/main/java/com/cn/ratan/netting/domain/splitting"),
        ("Component/resultant cashflow mapping and lifecycle updates", "src/main/java/com/cn/ratan/netting/domain/autonetting/processor/resultant"),
        ("Netting rule checks and static-data integration", "src/main/java/com/cn/ratan/netting/application/service/NettingRuleCheckService.java"),
        ("Netting request history and event processing", "src/main/java/com/cn/ratan/netting/domain/nettinghistory"),
    ],
    "orchestration": [
        ("Camunda cash-settlement workflow orchestration", "src/main/java/com/scb/ratan/orchestration/router"),
        ("Maker-checker user tasks and approvals", "src/main/java/com/scb/ratan/orchestration/web/UserTaskController.java"),
        ("Auto-DVP processing", "src/main/java/com/scb/ratan/orchestration/cashflow/consumer/AutoDVPConsumer.java"),
        ("Cashflow release jobs and lifecycle actions", "src/main/java/com/scb/ratan/orchestration/web/ReleaseJobController.java"),
        ("Exception capture, repair, fail, and replay", "src/main/java/com/scb/ratan/orchestration/service/ExceptionPlatformAdapter.java"),
        ("Kafka inbound processing and enriched-message publishing", "src/main/java/com/scb/ratan/orchestration/service/Publisher.java"),
        ("Cashflow lifecycle and SSI stamping workflow integration", "src/main/java/com/scb/ratan/orchestration/feign"),
        ("Auto-split and splitting-rule checks", "src/main/java/com/scb/ratan/orchestration/service/AutoSplitRuleCheckService.java"),
    ],
    "ssi-stamping": [
        ("Cashflow SSI stamping", "src/main/java/com/scb/ratan/stamping/entrypoint/web/CashflowStampingController.java"),
        ("Trade stamping for strategic, adhoc, and uber flows", "src/main/java/com/scb/ratan/stamping/entrypoint/web"),
        ("Nostro and vostro account matching and stamping", "src/main/java/com/scb/ratan/stamping/domain/nostro"),
        ("SSI and nostro/vostro refresh workflows", "src/main/java/com/scb/ratan/stamping/application/ssiplus"),
        ("Maker-checker stamping operations", "src/main/java/com/scb/ratan/stamping/application/makerchecker"),
        ("Exception handling, remediation, and exception-event publishing", "src/main/java/com/scb/ratan/stamping/entrypoint/web/ExceptionHandlingController.java"),
        ("Raw trade/message ingestion and SCBML transformation", "src/main/java/com/scb/ratan/stamping/domain/rawmessage"),
        ("Counterparty, account, and trade data enrichment", "src/main/java/com/scb/ratan/stamping/domain/counterparty"),
        ("GraphQL cashflow data retrieval", "src/main/java/com/scb/ratan/stamping/infra/ratan/graphql"),
    ],
}


def analyze_features(repo: Path, repo_id: str, commit: str, diagnostics: list[dict]) -> list[dict]:
    """Return curated business capabilities with repository evidence, not inferred marketing claims."""
    result = []
    for name, source in FEATURE_CATALOG.get(repo.name, []):
        path = repo / source
        if not path.exists():
            diagnostics.append({"severity": "warning", "code": "feature_evidence_missing", "repository": repo_id,
                                "path": source, "detail": f"Feature evidence path for '{name}' does not exist"})
            continue
        result.append({"name": name, "evidence": {"repository": repo_id, "commit": commit, "path": source,
                                                     "extractor": EXTRACTOR_VERSION}})
    return result


def main() -> int:
    import argparse
    parser = argparse.ArgumentParser(description="Generate the dependency-focused SDLC graph")
    parser.add_argument("--view", action="store_true", help="Generate graph/sdlc-graph.html and open it")
    parser.add_argument("--no-open", action="store_true", help="With --view, do not launch a browser")
    args = parser.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    graph = Graph()
    features_by_repo: dict[str, list[dict]] = {}
    repos = sorted(p for p in REPOS_ROOT.iterdir() if p.is_dir() and (p / ".git").is_dir())
    if not repos:
        print("No repositories found under repos/", file=sys.stderr)
        return 2
    service_info: dict[str, tuple[str, str, str, str]] = {}
    aliases: dict[str, str] = {}
    for repo in repos:
        repo_id = f"repo:ratan-release-impact/{repo.name}"
        commit = git(repo, "rev-parse", "HEAD")
        commit_date = git(repo, "show", "-s", "--format=%cI", "HEAD") or "unknown"
        graph.repo_meta.append({"id": repo_id, "path": str(repo.relative_to(ROOT)), "ref": git(repo, "branch", "--show-current") or "detached", "commit": commit, "commitDate": commit_date})
        info = pom_info(repo, graph, repo_id, commit)
        if not info:
            continue
        group, artifact, version, _ = info
        service_id = graph.node(f"service:ratan-release-impact/{repo.name}", "Service", artifact, repository=repo_id, technology="java/spring", coordinates=f"{group}:{artifact}:{version}")
        service_info[repo.name] = (repo_id, commit, service_id, artifact)
        features_by_repo[repo.name] = analyze_features(repo, repo_id, commit, graph.diagnostics)
        for feature in features_by_repo[repo.name]:
            feature_id = graph.node(f"feature:ratan-release-impact/{repo.name}/{slug(feature['name'])}", "Feature", feature["name"],
                                    repository=repo_id, service=service_id, evidencePath=feature["evidence"]["path"])
            graph.edge(service_id, feature_id, "IMPLEMENTS", repository=repo_id, commit=commit,
                       path=feature["evidence"]["path"], start=1, kind="feature-analysis",
                       detail=f"Business feature: {feature['name']}", confidence=0.82, extractor="business-feature.catalog")
        aliases[slug(repo.name)] = service_id
        aliases[slug(artifact)] = service_id
        aliases[slug(artifact.replace("-service", ""))] = service_id
    # Resolve common service-registry aliases only against the scanned repository set.
    for repo_name, (_, _, sid, artifact) in service_info.items():
        for alias in (artifact, artifact.upper(), repo_name, repo_name.upper()):
            aliases[slug(alias)] = sid
    endpoint_index: dict[tuple[str, str], str] = {}
    for repo in repos:
        if repo.name not in service_info:
            continue
        repo_id, commit, service_id, artifact = service_info[repo.name]
        scan_delivery_metadata(repo, graph, repo_id, commit, artifact_version(graph, service_id))
        scan_configs_and_sql(repo, graph, repo_id, commit, service_id)
        scan_endpoints_and_feign(repo, graph, repo_id, commit, service_id, aliases, endpoint_index)
        scan_topics(repo, graph, repo_id, commit, service_id)
    # Add a deterministic diagnostic for the external shared pipeline template used by all four repos.
    for repo_name, (repo_id, commit, _, _) in service_info.items():
        graph.diagnostics.append({"severity": "info", "code": "external_pipeline_template", "repository": repo_id,
                                  "path": "azure-pipelines-maven.yml", "detail": "Shared FMQPR/51358-ratanone-ado-templates repository is referenced but was outside scan scope"})
    commit_set = ";".join(f"{m['id']}={m['commit']}" for m in graph.repo_meta)
    scan_id = f"scan-{sha256(commit_set)[:16]}"
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    forbidden_types = {"Repository", "Pipeline", "Deployment", "RuntimeService", "Environment", "Artifact"}
    emitted_forbidden = sorted({n["type"] for n in graph.nodes.values()} & forbidden_types)
    if emitted_forbidden:
        raise RuntimeError(f"dependency graph emitted forbidden delivery nodes: {', '.join(emitted_forbidden)}")
    graph_doc = {"schemaVersion": "1.0", "scan": {"scanId": scan_id, "toolVersion": EXTRACTOR_VERSION,
                 "startedAt": now, "completedAt": now, "scope": "repos/* local Git repositories",
                 "repositories": sorted(graph.repo_meta, key=lambda x: x["id"])},
                 "nodes": sorted(graph.nodes.values(), key=lambda x: (x["id"], x["type"])),
                 "edges": sorted(graph.edges.values(), key=lambda x: (x["source"], x["type"], x["target"])),
                 "diagnostics": sorted(graph.diagnostics, key=lambda x: (x.get("repository", ""), x.get("path", ""), x.get("line", 0), x["code"])),
                 "features": {name: features_by_repo[name] for name in sorted(features_by_repo)}}
    (OUT / "graph.json").write_text(json.dumps(graph_doc, indent=2, sort_keys=False) + "\n", encoding="utf-8")
    diag_doc = {"schemaVersion": "1.0", "scanId": scan_id, "diagnostics": graph_doc["diagnostics"]}
    (OUT / "diagnostics.json").write_text(json.dumps(diag_doc, indent=2) + "\n", encoding="utf-8")
    counts = Counter(n["type"] for n in graph_doc["nodes"])
    edge_counts = Counter(e["type"] for e in graph_doc["edges"])
    report = [f"# SDLC Graph Scan {scan_id}", "", f"Scope: `{graph_doc['scan']['scope']}`", f"Generated: `{now}`", "",
              "## Repositories", "", "| Repository | Commit |", "|---|---|"]
    report += [f"| `{m['id']}` | `{m['commit']}` |" for m in graph_doc["scan"]["repositories"]]
    report += ["", "## Counts", "", f"Nodes: {len(graph_doc['nodes'])} ({', '.join(f'{k}={v}' for k, v in sorted(counts.items()))})",
               f"Edges: {len(graph_doc['edges'])} ({', '.join(f'{k}={v}' for k, v in sorted(edge_counts.items()))})",
               f"Diagnostics: {len(graph_doc['diagnostics'])}", "", "## Cross-repository relationships", ""]
    cross = [e for e in graph_doc["edges"] if e["source"].startswith("service:ratan-release-impact/") and e["target"].startswith("service:ratan-release-impact/")
             and e["source"].split("/", 1)[1] != e["target"].split("/", 1)[1]]
    if cross:
        for e in cross:
            report.append(f"- `{e['source']}` **{e['type']}** `{e['target']}` (confidence {e['confidence']:.2f})")
    else:
        report.append("- None were statically resolved within the four-repository scope.")
    report += ["", "## Business features", ""]
    for repo_name in sorted(features_by_repo):
        report.append(f"### {repo_name}")
        report.extend(f"- {feature['name']} (`{feature['evidence']['path']}`)" for feature in features_by_repo[repo_name])
        report.append("")
    report += ["## Caveats", "", "- Delivery topology (repositories, CI/CD, pipelines, deployments, artifacts, and environments) is intentionally excluded from graph nodes.",
               "- Maven transitive dependencies and runtime service discovery were not fetched.",
               "- Datasource URLs and environment values were redacted; `CONNECTS_TO` records configuration evidence only.",
               "- CI/CD metadata is retained only as diagnostics; shared pipeline templates are outside scope.",
               "- Dynamic topic names, unresolved Feign registry names, and unsupported syntax are retained as diagnostics.", ""]
    (OUT / "scan-report.md").write_text("\n".join(report), encoding="utf-8")
    if args.view:
        view_cmd = [sys.executable, str(Path(__file__).resolve().parent / "sdlc_graph_view.py"), "--graph", str(OUT / "graph.json"),
                    "--out", str(OUT / "sdlc-graph.html")]
        if args.no_open:
            view_cmd.append("--no-open")
        subprocess.run(view_cmd, check=True)
    print(json.dumps({"scanId": scan_id, "nodes": len(graph_doc["nodes"]), "edges": len(graph_doc["edges"]), "diagnostics": len(graph_doc["diagnostics"])}, sort_keys=True))
    return 0


def artifact_version(graph: Graph, service_id: str) -> str:
    coords = graph.nodes[service_id]["attributes"].get("coordinates", "")
    return coords.rsplit(":", 1)[-1] if ":" in coords else "unknown"


if __name__ == "__main__":
    raise SystemExit(main())

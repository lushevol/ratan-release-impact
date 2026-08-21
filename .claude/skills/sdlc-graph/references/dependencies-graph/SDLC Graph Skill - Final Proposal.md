# SDLC Graph Skill - Final Proposal

## 1. Purpose

Create a reusable skill that scans one or more software repositories and emits an evidence-backed relationship graph for software delivery and operational dependencies. The skill must prefer deterministic evidence, make uncertainty explicit, protect secrets, and work with partial or heterogeneous repositories.

The skill answers questions such as:

- Which applications and services depend on this repository, API, database, or library?
- Which consumers may be affected by a change?
- Why does the graph contain a relationship, and which revision produced it?
- Which dependencies are configured but unobserved, unresolved, or stale?

The skill is an analyzer and graph generator. It is not a CMDB, service catalog, approval workflow, runtime tracing system, or authoritative ownership registry.

## 2. Invocation Contract

The skill accepts either local paths or repository locators:

```yaml
repositories:
  - path: ./trade-ui
    ref: main
  - url: https://dev.azure.com/org/project/_git/trade-service
    ref: main
```

Optional configuration controls include `include`/`exclude` globs, repository-specific aliases, detector enablement, scan timeout, concurrency, confidence thresholds, output directory, and whether network access is permitted. Local scanning is the default; remote fetching and runtime connectors are explicit opt-ins.

The command must provide machine-readable output and a human summary, for example:

```text
sdlc-graph scan --config graph.yml --out graph/
sdlc-graph impact --graph graph/graph.json --node service:trade-service
sdlc-graph diff --before graph/a.json --after graph/b.json
```

Exit codes distinguish success, successful partial scan, invalid configuration, and total failure.

## 3. Scope and Non-Goals

The first release supports representative Java/Spring, TypeScript/JavaScript, SQL migrations, and common CI configuration. Extractors are plugins; unsupported languages and providers produce diagnostics and no guessed edges. Runtime evidence, Azure DevOps discovery, and graph databases are later connectors, not prerequisites.

## 4. Canonical Graph Model

### Node types

```text
Repository, Application, Service, RuntimeService, API, Endpoint,
Library, Database, Table, Pipeline, Artifact, Deployment,
Environment, ExternalSystem, Queue, Topic
```

`RuntimeService`, `Artifact`, and `Deployment` are separate from logical services and pipelines so the code-to-runtime lifecycle is representable. `Queue` and `Topic` cover asynchronous dependencies without pretending they are HTTP APIs.

Every node has:

```json
{
  "id": "service:org/project/trade-service",
  "type": "Service",
  "name": "trade-service",
  "aliases": ["TradeService"],
  "attributes": {},
  "lifecycle": "active"
}
```

IDs are stable, namespaced by source host/project/repository where applicable, and never derived from display name alone. Alias resolution is explicit and evidence-backed.

### Relationship types

Canonical edge direction is always from dependent/producer to dependency/consumer as documented below:

```text
Repository    CONTAINS       -> Application/Service/Library/Pipeline
Repository    BUILDS         -> Artifact
Pipeline      PRODUCES       -> Artifact
Pipeline      DEPLOYS        -> Artifact/Application/Service
Deployment    DEPLOYS        -> RuntimeService
RuntimeService RUNS_IN       -> Environment
Application   CALLS          -> API/Endpoint/ExternalSystem
Service       PROVIDES       -> API/Endpoint
Service       CALLS          -> API/Endpoint/Service
Service       CONNECTS_TO    -> Database
Service       READS_FROM     -> Table
Service       WRITES_TO     -> Table
Service       DEPENDS_ON     -> Library
Database      CONTAINS       -> Table
Table         REFERENCES     -> Table
Service       PUBLISHES      -> Queue/Topic
Service       SUBSCRIBES_TO  -> Queue/Topic
```

Do not emit generic edges. UI inverse labels such as “deployed by” are presentation-only aliases of the canonical direction.

## 5. Edge and Evidence Schema

The graph is a versioned JSON document. Nodes and edges are sorted deterministically by ID and type.

```json
{
  "schemaVersion": "1.0",
  "scan": {
    "scanId": "2026-08-20T01:02:03Z-...",
    "toolVersion": "1.0.0",
    "startedAt": "2026-08-20T01:02:03Z",
    "repositories": [{"id": "repo:...", "ref": "main", "commit": "abc123"}]
  },
  "nodes": [],
  "edges": [],
  "diagnostics": []
}
```

Each edge has one shape for all extractors:

```json
{
  "id": "edge:sha256(...)",
  "source": "service:org/project/trade-service",
  "target": "db:org/trade-db",
  "type": "CONNECTS_TO",
  "status": "supported",
  "confidence": 0.91,
  "firstSeen": "2026-08-20T01:02:03Z",
  "lastSeen": "2026-08-20T01:02:03Z",
  "evidence": [{
    "kind": "configuration",
    "repository": "repo:...",
    "commit": "abc123",
    "path": "application-prod.yml",
    "startLine": 42,
    "endLine": 42,
    "extractor": "spring.datasource",
    "extractorVersion": "1.0.0",
    "detail": "JDBC host resolved to trade-db"
  }]
}
```

`status` is one of `supported`, `contradicted`, `unknown`, or `stale`. Confidence has a documented scoring rubric, is not presented as a probability unless calibrated, and is aggregated from individual evidence items. Missing evidence means the edge is omitted or marked `unknown`, never silently upgraded to fact.

## 6. Identity and Resolution

The skill normalizes repository URLs, package coordinates, Maven/Gradle coordinates, service names, hostnames, database URLs, API base URLs, OpenAPI operation IDs, and queue/topic names. Resolution proceeds from exact identifiers, then configured aliases, then conservative normalized matches. Ambiguous matches create diagnostics and unresolved nodes instead of merging entities.

Repository, branch/ref, commit SHA, environment, and source host are part of provenance. A logical service may have multiple runtime deployments; those are not merged.

## 7. Extractors

All extractors implement the same interface:

```text
scan(repository snapshot) -> nodes, edges, diagnostics
```

They must be deterministic, bounded by timeout, and safe to run independently.

### Java/Spring

Use format-aware parsing where available, with conservative source matching for controllers, mappings, Feign/WebClient/RestClient/RestTemplate, configuration, ORM annotations, repository methods, MyBatis, Flyway, and Liquibase. Emit endpoint paths only when resolvable; retain unresolved templates as attributes.

### TypeScript/JavaScript/React

Parse manifests, workspaces, lockfiles, imports, generated client metadata, OpenAPI/GraphQL clients, fetch/Axios calls, and configuration references. Environment interpolation produces a reference with the variable name and redacted value, not a secret.

### SQL and migrations

Parse dialect-aware DDL for databases, schemas, tables, columns, foreign keys, and indexes. SQL statements produce `READS_FROM`/`WRITES_TO` only when table names are statically known. Datasource configuration produces `CONNECTS_TO` only.

### CI/CD

Support declared providers and document them explicitly (for example Azure Pipelines and GitHub Actions). Resolve templates/includes, variables, matrices, artifacts, deployment jobs, environments, and reusable workflows where statically possible. A configured deployment is evidence of intended deployment, not proof of execution.

### Cross-cutting

Detect OpenAPI, GraphQL, gRPC, messaging, Docker/Kubernetes, Terraform, and service-discovery metadata only through enabled plugins. Generated and vendored files are excluded by default and configurable.

## 8. Security and Privacy

Secret values, tokens, passwords, private keys, connection-string credentials, and environment values are never written to graph output, logs, caches, or evidence. URLs are normalized and credentials/query secrets redacted. The scanner refuses paths outside configured roots, does not follow unsafe symlinks, and treats repository content as untrusted input. Remote access uses least-privilege credentials, bounded downloads, and explicit user opt-in.

## 9. Diagnostics and Partial Results

Malformed files, unsupported syntax, missing repositories, permission errors, ambiguous resolution, and timeouts produce structured diagnostics containing repository, path, detector, severity, and remediation. A scan may publish a partial graph only when explicitly allowed; failed repositories cannot erase the last known snapshot by default.

## 10. Impact Analysis

Impact analysis uses a deterministic, typed traversal with configurable maximum depth and confidence threshold. It is environment-aware, cycle-safe, and excludes purely structural edges unless requested. Results include:

```text
node, severity, distance, relationship path, confidence, evidence, caveats
```

Severity is calculated from relationship type, path length, environment, and configured weights. Every result must explain the path, for example `Trade UI CALLS Trade API PROVIDED_BY Trade Service`; “high/medium/low” is not manually assigned.

## 11. Maintenance, History, and Diff

Each snapshot is identified by scan ID plus repository commit set. Output is atomically written only after validation. Removed nodes/edges are represented in graph diffs and receive lifecycle `removed` or `stale`; they are not silently retained forever. Retention, branch policy, concurrency, caching, retries, and rate limits are configurable. Snapshot history is optional and has a retention limit.

## 12. Validation and Success Criteria

The repository includes golden fixtures for each supported detector, including positive, negative, ambiguous, malformed, secret-containing, monorepo, and generated-code cases. Tests validate schema, deterministic output, redaction, diagnostics, identity resolution, and impact paths.

Metrics are measured against an annotated ground-truth corpus:

```text
precision and recall by edge type
false-positive rate
evidence coverage
unsupported/unknown rate
scan failure rate
runtime and peak memory
```

Initial targets for the fixture corpus are at least 90% precision, 80% recall for supported edge types, 100% secret redaction, 90% evidence coverage, and impact queries under five seconds for the POC graph. “Manual configuration under 10%” is measured as the percentage of repositories requiring overrides.

## 13. Deliverables

1. Versioned graph JSON Schema and canonical relationship registry.
2. Scanner CLI/library with local repository support and structured diagnostics.
3. Initial React, Spring, SQL, and CI extractors.
4. Identity resolver and configuration/alias mechanism.
5. Deterministic graph writer, snapshot validation, and graph diff command.
6. Typed impact-analysis command with path explanations.
7. Redaction/security tests and golden fixture corpus.
8. Minimal viewer that searches, filters, expands, and displays evidence and uncertainty.
9. Skill documentation describing supported detectors, limits, configuration, and examples.

## 14. Evolution

The graph schema and extractor interface are the stable core. Later add repository-provider connectors, runtime telemetry, ownership metadata, richer protocols, Neo4j or another indexed store, and AI/MCP query interfaces without changing the meaning of existing edge types. Runtime evidence strengthens or contradicts static evidence; it does not replace provenance or turn absence of traffic into proof of absence.

## 15. Design Principle

> The SDLC Graph is an automatically generated, evidence-backed dependency graph. Deterministic extractors produce conservative, reproducible facts; explicit uncertainty and diagnostics prevent guesses from becoming architecture truth; visualization and AI consume the graph rather than creating its primary relationships.

## 16. Skill Package and Execution Workflow

The skill should be packaged as a self-contained directory with a small, stable entry point:

```text
skills/dependencies-graph/
  SKILL.md
  schemas/
    graph.schema.json
    config.schema.json
  extractors/
    registry.md
    spring.md
    javascript.md
    sql.md
    ci.md
  fixtures/
  scripts/
    scan
    impact
    diff
  references/
    relationship-registry.md
    security.md
```

`SKILL.md` defines when to invoke the skill, required inputs, safety rules, commands, output artifacts, and failure behavior. The implementation must follow this sequence:

1. Validate configuration and resolve repository snapshots.
2. Apply path, secret, binary, generated-file, and symlink policies.
3. Run enabled extractors independently with bounded resources.
4. Normalize identities and reconcile evidence without guessing through ambiguity.
5. Validate the graph schema and deterministic ordering.
6. Atomically publish the graph, diagnostics, and optional diff.
7. Run impact analysis only against the validated graph and include evidence paths.

The skill must be useful without a viewer. The required artifacts are `graph.json`, `diagnostics.json`, and a concise scan report; the UI is an optional consumer.

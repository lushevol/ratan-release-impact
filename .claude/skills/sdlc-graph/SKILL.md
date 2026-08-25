---
name: sdlc-graph
description: Build, visualize, and analyze a cross-repository SDLC graph with per-repository runtime data-flow and business/functional dimensions for React micro-frontends and Spring services. Use for architecture discovery, dependency mapping, graph generation, business requirement impact, code-change impact, or tracing REST, GraphQL, WebSocket, SystemJS, Feign, PostgreSQL, Elasticsearch, Kafka, and external data-platform dependencies.
---

# SDLC Graph

Use this as the single public skill for graph generation, visualization, dependency resolution, flow tracing, incremental regeneration, and impact analysis. Read the [graph contract](references/architecture/graph-contract.md) before changing graph producers or consumers.

## Generate every graph

From the workspace root run:

```text
python3 .claude/skills/sdlc-graph/tools/generate_all_graphs.py
```

Add `--open` to open `system-graph/relationship-viewer.html`. This one command scans every supported repository, resolves cross-repository dependencies, renders both dimensions, validates source links and semantics, and atomically publishes the result. It does not create SQLite; JSON is the authoritative and default query surface.

## Repository dimensions

For every visible repository produce two projections over the same canonical facts:

- `RUNTIME`: routes and remote imports for web repositories; REST, GraphQL, WebSocket, Feign, PostgreSQL tables, Elasticsearch/OpenSearch, Kafka, service calls, and external data platforms for applicable repositories.
- `BUSINESS`: pages or service capabilities mapped to domain components, UI, hooks, state, clients, utilities, controllers, application/domain services, and infrastructure. Every component explains its functional role and business meaning and links to a file or narrow wildcard path.

Detailed extraction retains meaningful frontend modules beneath `components`, `hooks`, `workflow`, `services`, `store`, and similar ownership directories. It retains concrete Spring controllers, services, repositories, clients, listeners, processors, handlers, commands, tasks, and mappers beneath their domain/layer groups. Do not collapse a named workflow such as Quick Search into a generic UI bucket.

Treat `mfe-root-config` as scan-only MFE foundation metadata. Never expose it as a selectable application graph. DQSL is an external data lake that lets consumers fetch data from selected upstream sources; model it as `DATA_PLATFORM` with `platform_kind=EXTERNAL_DATA_LAKE`, never infer Elasticsearch from DQSL naming.

Use the detailed [React](references/architecture/react-extraction.md), [Spring](references/architecture/spring-extraction.md), and [external boundary](references/architecture/external-boundaries.md) rules when modifying extractors.

## Impact analysis

Run exactly one input mode:

```text
python3 .claude/skills/sdlc-graph/tools/analyze_impact.py --requirement "Allow operators to refresh SSI"
python3 .claude/skills/sdlc-graph/tools/analyze_impact.py --changed-file repos/example/src/main/java/example/File.java
python3 .claude/skills/sdlc-graph/tools/analyze_impact.py --base-ref main
```

Requirement mode starts from matching business capabilities, pages, and components and expands into runtime dependencies. Code-change mode starts from exact/wildcard source-path ownership and expands toward affected workflows and consumers. Report the two result sets separately and preserve unresolved external frontiers. Read [impact analysis](references/architecture/impact-analysis.md) for interpretation rules.

## AI business-description enrichment

Generation writes `system-graph/business-description-context.json`, a compact evidence packet for detailed components whose descriptions remain source-inferred. Use it to propose overrides in workspace-root `architecture-descriptions.json`; generation applies that file automatically. Keep `source=AI_INFERRED` unless an authoritative product/Wiki source confirms the meaning, include rationale and source paths, and never let a description override create or alter runtime relationships.

For higher accuracy, request the business glossary/capability map, user personas, workflow descriptions, requirements and acceptance criteria, meanings of domain fields/statuses/events, operational runbooks, and an SME/owner for ambiguous terminology. Source code can establish functional behavior; those business sources establish why the behavior exists.

## Evidence rules

- Keep all paths workspace-relative and clickable. Use the narrowest honest wildcard for multi-file components.
- Database connectivity may use datasource/build configuration, but required tables and `READS`/`WRITES` must come from runtime database-client declarations. Migration SQL never proves runtime use.
- Kafka dependencies retain exact topic or unresolved expression, direction, and calling source path.
- Cross-repository links require deterministic aliases or compatible consumer/provider operations. Keep unresolved boundaries visible.
- Never invent a relationship, deployment value, database table, topic, or upstream DQSL dataset. Emit diagnostics or inferred assertions when evidence is incomplete.
- Never store credentials, tokens, or unredacted connection strings.

## Canonical outputs

```text
system-graph/
├── graph.json
├── dependencies.json
├── business-description-context.json
├── summary.json
├── relationship-viewer.html
└── repositories/<repository>/view.json
```

`graph.json` is the sole canonical graph. The other files are reproducible projections or indexes and must not duplicate alternative graph contracts. Validate before publishing with `tools/validate_graph.py`; generation already performs this check.

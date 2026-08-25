# SDLC Graph Contract v2

`sdlc-graph-output/graph.json` is the canonical architecture and impact graph. Every viewer, repository view, catalog, and MCP response is derived from it.

## Envelope

The exact top-level fields are `schema_version`, `generated_at`, `generator`, `repositories`, `nodes`, `edges`, `evidence`, and `diagnostics`. Collections and IDs are sorted and unique. Optional fields are omitted when empty; do not store confidence labels, repeated commits, null placeholders, or separate interface/resolution copies.

Repositories declare `kind` (`WEB` or `SPRING`), `role`, and `visible`. `mfe-root-config` remains repository metadata with `role=FOUNDATION`, `visible=false`, and owns no graph nodes.

## Nodes

Every node contains:

- identity: `id`, `type`, `name`, nullable `repository`;
- projections: one or both of `RUNTIME`, `BUSINESS` in `dimensions`;
- explanations: `functional_role`, `business_meaning`;
- provenance: `source_paths`, `evidence`, `assertion_status`;
- optional non-empty `component_kind` and protocol-specific `properties`.

External nodes have `repository=null` and may have no source path. Local nodes use workspace-relative files or the narrowest honest wildcard. Wildcard labels remain intact; viewers link them to the nearest concrete parent.

## Edges

Edges contain `source`, `target`, `relationship`, one `dimension`, evidence, and assertion status. `resolution_status` appears only for a resolved, ambiguous, or unresolved boundary. Edges point from owner/caller to dependency, except provider containment such as `DATABASE CONTAINS TABLE`.

Runtime relationships include `ROUTES_TO`, `USES_COMPONENT`, `LOADS_REMOTE`, `CALLS_REST`, `CALLS_GRAPHQL`, `SUBSCRIBES_WS`, `EXPOSES`, `INVOKES`, `CALLS_SERVICE`, `CONNECTS_TO`, `READS`, `WRITES`, `CONTAINS`, `PUBLISHES`, `CONSUMES`, `CALLS_DATA_PLATFORM`, and `QUERIES_DATA_PLATFORM`.

`CONTAINS_COMPONENT` links a semantic domain/layer group to a detailed module or class without duplicating its responsibility. Description enrichment may replace `functional_role` and `business_meaning` and attach provenance properties, but it cannot add runtime facts.

Business relationships include `DELIVERS`, `IMPLEMENTS`, and `REALIZED_BY`.

## Evidence and dependency claims

Evidence records the workspace-relative `path`, line, sanitized declaration, extractor, and directness. Do not store secrets.

- PostgreSQL connection evidence may come from build or datasource configuration.
- Tables and read/write access require runtime client evidence: Spring Data/JPA, MyBatis, native query, JDBC, or equivalent. Migration SQL cannot establish a runtime dependency.
- Kafka topic nodes require a producer/consumer declaration and direction.
- DQSL is `DATA_PLATFORM` with `platform_kind=EXTERNAL_DATA_LAKE`; its datasets or upstream sources appear only when directly identified.
- Elasticsearch/OpenSearch appears only from an explicit engine client or configuration, never by interpreting DQSL.

The normative machine contract is [architecture-graph.schema.json](architecture-graph.schema.json). `tools/validate_graph.py` additionally validates source existence and domain-specific invariants.

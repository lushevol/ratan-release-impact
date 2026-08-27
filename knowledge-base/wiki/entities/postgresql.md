---
type: entity
title: PostgreSQL
created: 2026-08-24
updated: 2026-08-24
tags: ["database", "relational-data", "metadata", "cash-settlement", "sql", "query-planner", "postgresql", "query-planning", "relational-database", "pg", "fallback", "persistence"]
related: ["minio", "database-object-storage-separation", "object-reference-storage-pattern", "large-field-dual-write-migration", "cash-settlement-query-cn-cashflow-data", "jsonb-expression-indexed-query-performance", "postgresql-query-cache-warm-up-effects", "postgresql-sequential-scan-triage", "postgresql-lossy-bitmap-scan", "postgresql-jsonb-expression-index-matching", "postgresql-index-cond-vs-filter", "cashflow-data-history", "postgresql-toast-storage", "replacement-table-purge-and-swap", "opensearch", "opensearch-business-live", "double-writing", "three-way-data-reconciliation"]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Minio Solutioning.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/PostgreSQL performance/SQL performance  in different condition.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/PostgreSQL performance/SQL performance summary.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Cash Settlement Query Service - cashflow_data_history purge.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/OpenSearch Business Live Plan.md"]
---
# PostgreSQL

## Roles in the architecture

[[PostgreSQL]] is proposed as the system of record for business metadata and references to raw payloads held in [[minio]]. The proposed `trade_message` model retains the bucket, key, size, and SHA-256 checksum instead of inline `raw_message` text.

The Minio Solutioning source identifies database bloat, slow backups, connection pressure, and constrained scalability as reasons to externalise large payloads. These are general architecture arguments; that source provides no Indonesia-specific measurements.

The canonical reference schema, constraints, indexing, nullability, and migration-state fields remain unresolved. See [[object-reference-storage-pattern]] and [[large-field-dual-write-migration]].

Separately, the SQL performance summary source describes PostgreSQL as the database technology used for Cash Settlement queries against `cash_settlement_query_cn.cashflow_data`. That source focuses on planner choices, expression indexes, bitmap scans, `work_mem`, filtering, and result ordering.

## Role in the OpenSearch transition

According to the OpenSearch Business Live Plan source, PostgreSQL (PG) is the current query and persistence target for Cash Settlement data. During Day 1 of the proposed [[opensearch]] business-live rollout, PG remains a persistence target and fallback query source.

This transition role is distinct from the proposed `trade_message` metadata-and-object-reference model and from the performance and historical-payload designs described elsewhere on this page.

### Fallback behavior

The OpenSearch Business Live Plan proposes immediately switching blotter, detail, or dashboard queries back to PG if OpenSearch-backed queries encounter production issues.

The source states that this fallback is safe only if query semantics are equivalent. The design must compare filtering, sorting, pagination, field availability, freshness, authorization, and error behavior across the two query sources.

### Decommissioning ambiguity

The OpenSearch Business Live Plan describes eventual decommissioning of PG as a target while also requiring continued PG persistence during the transition. It does not define:

- How long PG writes continue.
- Which cutover gates permit stopping PG writes.
- Whether PG remains an emergency rollback store.
- How reconciliation changes after PG retirement.

## Role in historical-payload slimming

The Cash Settlement Query Service purge design describes PostgreSQL as the database platform underlying the `cash_settlement_query_cn` schema and the `cashflow_data_history` table. In that design, PostgreSQL storage and maintenance behavior determines the feasibility of slimming historical payloads.

The purge design relies on PostgreSQL features including:

- `jsonb` storage.
- `json_build_object`.
- `jsonb_extract_path_text`.
- TOAST storage for oversized attributes.
- B-tree indexes.
- `VACUUM FULL`.
- Table renaming.

These claims apply to the `cashflow_data_history` purge design and are separate from the proposed `trade_message` metadata-and-object-reference model.

## Planner and index behavior

PostgreSQL evaluates available access paths and chooses an execution plan based on statistics, estimated selectivity, available indexes, ordering requirements, and resource settings. More indexed predicates can provide additional planner options, but additional indexes are not automatically beneficial and add write and maintenance cost.

The SQL performance source distinguishes between:

- **`Index Cond`**: an index is used to constrain access.
- **`Filter`**: rows retrieved by an access path are evaluated after retrieval.
- **Bitmap scans**: index matches can be combined or processed before heap access.
- **Lossy bitmap scans**: additional heap-page rechecks are required.

The benchmark concerns PostgreSQL planner choices for JSONB expression predicates, ordering, row filtering, and repeated execution.

## Resource constraints

The SQL performance summary source identifies increasing `work_mem` as a possible mitigation for large bitmap operations and records an approximate upper limit of 30 MB for the Ratan business context. This is an environment-specific constraint, not a universal PostgreSQL recommendation. Because `work_mem` can apply per operation and across concurrent sessions, changes require workload testing.

The SQL performance source reports an environment using:

- `work_mem: 4MB`
- `shared_buffers: 15972MB`

## Storage and maintenance observations

The Cash Settlement Query Service purge design reports that updating a large `jsonb` value in place increased a one-million-row test table from 5,535 MB to 6,933 MB. After `VACUUM FULL`, the table decreased to 1,692 MB. The design interprets this as consistent with update-induced tuple versioning followed by table rewriting and space reclamation.

The same design reports that creating a replacement table containing slim JSON produced a much smaller DEV result, with near-zero reported TOAST storage.

## Replacement-table and production constraints

The purge design does not quantify production lock duration, WAL volume, replication impact, disk headroom, concurrent-write behavior, or query latency. These characteristics must be measured before a production table swap.

That source also does not provide the canonical production DDL. Therefore, `CREATE TABLE AS SELECT` must not be assumed to preserve all schema properties.

## Evidence and validation boundary

The SQL performance source references `EXPLAIN (ANALYZE, BUFFERS, VERBOSE, SETTINGS)` for plan-level validation before the results are used as production guidance.

The SQL performance summary source references `EXPLAIN ANALYZE` but does not include the execution plans, timings, index definitions, or memory settings needed to confirm the reported planner behavior.

The purge-design measurements are test and DEV observations. They do not establish production lock duration, WAL behavior, replication effects, available disk headroom, concurrent-write behavior, or production query latency.
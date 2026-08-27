---
type: entity
title: EXPLAIN
created: 2026-08-24
updated: 2026-08-24
tags: [postgresql, explain, query-planning, diagnostics]
related: [postgresql, postgresql-explain-plan-reading, postgresql-query-lifecycle, postgresql-index-bitmap-sequential-scan-selection, postgresql-sequential-scan-triage]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/PostgreSQL performance/PostgreSQL Explain.md"]
---
# EXPLAIN

`EXPLAIN` is the PostgreSQL command used to inspect the query plan selected by the planner. It exposes a hierarchical plan tree containing node types, estimated costs, estimated output rows, and properties such as `Index Cond` and `Filter`.

Plain `EXPLAIN` reports planner estimates rather than measured execution behavior. For production diagnosis, [[postgresql-explain-plan-reading]] recommends comparing estimates with actual rows, timing, and buffer activity through carefully controlled `EXPLAIN (ANALYZE, BUFFERS)` runs.

`EXPLAIN` is most useful when read together with the [[postgresql-query-lifecycle]] and the scan-selection trade-offs described in [[postgresql-index-bitmap-sequential-scan-selection]].
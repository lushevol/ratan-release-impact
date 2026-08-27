---
type: query
title: Why Is the created_at-Ordered Cashflow Query Slower at 1,200k?
created: 2026-08-24
updated: 2026-08-24
tags: [cashflow, postgresql, query-performance, created-at, indexing, execution-plan]
related: [cashflow-data-provider, cash-settlement-query-cn-cashflow-data, which-expression-indexes-support-cashflow-data-date-filters-and-sorts, cashflow-blotter-query-performance, postgresql]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Expose The Cashflow Data Design/Cashflow data provider query solution for big volume/PT for big volume query.md"]
---
# Why Is the created_at-Ordered Cashflow Query Slower at 1,200k?

The V2 Final tests report a substantial runtime difference at 1,200k rows:

- `created_at` descending with `created_at <= now()`, pool maximum 10: 3,357 seconds for three queries.
- `cashflow_Ids`, pool maximum 20: 320 seconds for three queries.
- `cashflow_Ids`, pool maximum 20: 334 seconds for five queries.

The result is a significant performance signal, but it is not a controlled comparison. Pool sizes differ, the exact SQL is not provided, and the source contains no execution plans, index inventory, cardinalities, cache-state information, or response-size measurements.

## Required Investigation

A controlled rerun should hold constant:

- Service and database environment.
- JVM and connection-pool settings.
- Query volume and concurrency.
- Exact predicates, ordering, pagination, and selected columns.
- Dataset size and data distribution.
- Cache state and client behavior.

Collect `EXPLAIN (ANALYZE, BUFFERS)`, relevant index definitions, row counts, database wait events, connection occupancy, and server/client transfer metrics. Confirm whether pagination uses deterministic ordering and whether large `OFFSET` values are involved.

Until this evidence exists, the source supports neither a conclusion that `created_at` ordering is inherently unsuitable nor a categorical claim that `cashflow_Ids` is always superior.
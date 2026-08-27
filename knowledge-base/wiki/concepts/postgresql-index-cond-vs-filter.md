---
type: concept
title: PostgreSQL Index Cond versus Filter
created: 2026-08-24
updated: 2026-08-24
tags: [postgresql, query-plan, indexes, filtering, cash-settlement]
related: [postgresql, cash-settlement-query-cn-cashflow-data, postgresql-jsonb-expression-index-matching, postgresql-sequential-scan-triage, cashflow-query-indexing-options]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/PostgreSQL performance/SQL performance summary.md"]
---
# PostgreSQL Index Cond versus Filter

## Execution-plan distinction

`Index Cond` identifies predicates used by an index access method to constrain which index entries or table locations are retrieved. These predicates generally reduce the amount of data that must be fetched.

`Filter` identifies predicates evaluated after rows have been retrieved by the chosen access path. A filter can remove many rows, but the database has already incurred retrieval work for them.

The distinction is therefore useful for diagnosing whether an index is reducing the scan or merely supporting a later filtering step.

## Cash Settlement relevance

The documented queries apply predicates to JSONB values in `cash_settlement_query_cn.cashflow_data`. A predicate may remain a `Filter` when there is no suitable index, when the expression does not match an expression index, or when the planner estimates that another access path is cheaper.

The source uses this distinction to explain why non-indexed predicates can fetch more data and then discard rows. It does not provide the actual plans needed to determine which predicates became `Index Cond` in the four examples.

## Validation

Inspect `EXPLAIN (ANALYZE, BUFFERS)` and compare:

- Predicates shown under `Index Cond`.
- Predicates shown under `Filter`.
- Rows removed by filter.
- Estimated and actual row counts.
- Heap and index block activity.
- The impact of alternate expression, composite, or generated-column indexes.

An `Index Cond` is not by itself proof of an optimal plan; selectivity, ordering, table visibility, cache state, and write-maintenance cost also matter.
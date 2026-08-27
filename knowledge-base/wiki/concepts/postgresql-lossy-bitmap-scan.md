---
type: concept
title: PostgreSQL Lossy Bitmap Scan
created: 2026-08-24
updated: 2026-08-24
tags: [postgresql, bitmap-scan, query-performance, work-mem, cash-settlement]
related: [postgresql, cash-settlement-query-cn-cashflow-data, postgresql-sequential-scan-triage, cashflow-blotter-query-performance, cashflow-query-indexing-options]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/PostgreSQL performance/SQL performance summary.md"]
---
# PostgreSQL Lossy Bitmap Scan

## Definition

A bitmap scan is a PostgreSQL access strategy that uses bitmap information derived from one or more indexes before fetching rows from the heap. When the bitmap becomes too large for the available memory, PostgreSQL may store page-level information instead of exact tuple-level information. This is a lossy bitmap.

A lossy bitmap requires PostgreSQL to recheck more tuples on the affected heap pages. The additional work can increase latency, especially when the predicates are not highly selective.

## Cash Settlement relevance

The source associates the multi-condition query on `cash_settlement_query_cn.cashflow_data` with bitmap-scan behavior. It proposes increasing `work_mem` as a possible optimization and records an approximate 30 MB limit in the Ratan business context.

This is a hypothesis rather than a confirmed diagnosis because the source does not include the execution plan or heap recheck counts.

## How to validate

Use `EXPLAIN (ANALYZE, BUFFERS)` and record:

- Whether a bitmap index scan and bitmap heap scan are selected.
- `Heap Blocks: exact` and `Heap Blocks: lossy`.
- Rows removed by index recheck.
- Estimated versus actual rows.
- Execution time and buffer reads.
- The plan and latency at each tested `work_mem` value.

A higher `work_mem` setting should be evaluated against concurrent workload, because memory may be allocated independently for multiple operations and sessions.

## Related considerations

A lossy bitmap is not automatically evidence that `work_mem` is the only solution. A composite index, more selective predicates, expression-index alignment, generated columns, or a different ordering strategy may be more appropriate depending on the plan and business requirements.
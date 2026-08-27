---
type: concept
title: PostgreSQL Index, Bitmap, and Sequential Scan Selection
created: 2026-08-24
updated: 2026-08-24
tags: [postgresql, index-scan, bitmap-scan, sequential-scan, selectivity, work-mem]
related: [postgresql, explain, postgresql-explain-plan-reading, postgresql-sequential-scan-triage, cashflow-blotter-query-performance, value-date-query-performance-guardrail, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/PostgreSQL performance/PostgreSQL Explain.md"]
---
# PostgreSQL Index, Bitmap, and Sequential Scan Selection

PostgreSQL chooses among access paths using estimated selectivity and relative planner costs. The choice is workload-dependent rather than governed by a universal percentage threshold.

## Access-path trade-offs

### Sequential scan

A sequential scan reads table pages and evaluates predicates row by row. It can be cheaper when a predicate returns a large proportion of the table because sequential I/O avoids many separate heap fetches.

A selective predicate does not automatically make a sequential scan cheap. If the predicate appears only as `Filter`, PostgreSQL may still inspect every row.

### Index scan

An index scan locates qualifying rows through an index and fetches table tuples individually. It is often suitable for very selective predicates and can provide the requested ordering when the index order matches `ORDER BY`.

### Bitmap scan

A bitmap index scan collects matching tuple locations. A bitmap heap scan then fetches the corresponding heap pages, generally in physical page order. This can reduce random I/O for moderately selective predicates, but constructing the bitmap adds startup work.

If the bitmap exceeds available memory, it can become lossy and retain page-level rather than tuple-level matches. PostgreSQL must recheck conditions for rows on those pages. `work_mem` and the number of matching rows therefore affect bitmap performance.

## Effects of predicates, ordering, and limits

A condition on an indexed column can appear as `Index Cond`, while a condition on a non-indexed column may appear as `Filter` after the same candidate rows have been retrieved. Separate indexes may be combined with bitmap `AND` or `OR`, but visiting multiple indexes is not always cheaper than using one index and filtering the remaining condition.

An index that supplies the required `ORDER BY` can eliminate an explicit sort. `LIMIT` can favor a plan with lower startup cost because execution may stop after enough rows are produced. `LIMIT` without deterministic ordering does not guarantee which rows are returned.

Composite indexes should be designed from actual workload evidence. The number of indexed columns alone is not a measure of quality; column order, equality and range predicates, ordering, index size, write overhead, and query frequency all matter.

## Ratan DEV observation

The source tested this query against `cash_settlement_query_cn.cashflow_data`:

```sql
select *
from cash_settlement_query_cn.cashflow_data
where created_at < '2024-02-27 08:35:40';
```

The test table contained 124,635 records and had a B-tree index on `created_at`. The observed plan transitions were:

| Result records | Approximate share | Observed plan |
|---:|---:|---|
| Less than 2,010 | Less than approximately 1.6% | Index scan |
| Approximately 2,006–17,161 | Approximately 1.6%–13.7% | Bitmap index scan / bitmap heap scan |
| More than 17,214 | More than approximately 13.8% | Sequential scan |

These results are a local empirical baseline for the tested table and query. They depend on data distribution, table width, PostgreSQL version, statistics, planner cost settings, memory, cache state, hardware, and concurrency. The approximately 13.8% transition must not be applied to other tables or workloads without testing.

## Operational validation

Validate scan choices with representative data and controlled plan capture. Record PostgreSQL version, statistics freshness, `seq_page_cost`, `random_page_cost`, `work_mem`, `effective_cache_size`, cache conditions, and concurrency. Compare plain `EXPLAIN` estimates with `EXPLAIN (ANALYZE, BUFFERS)` measurements.

This concept extends [[postgresql-sequential-scan-triage]] and is relevant to [[cashflow-blotter-query-performance]] and [[value-date-query-performance-guardrail]].
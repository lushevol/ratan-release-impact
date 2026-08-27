---
type: concept
title: PostgreSQL work_mem for Bitmap Scans
created: 2026-08-24
updated: 2026-08-24
tags: [postgresql, work-mem, bitmap-scan, query-tuning, memory-management]
related: [postgresql-lossy-bitmap-scans, postgresql-index-bitmap-sequential-scan-selection, postgresql-explain-plan-reading, cashflow-data, what-work-mem-setting-is-safe-for-cash-settlement-query-workloads]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/PostgreSQL performance/SQL performance when using bitmap scan.md"]
---
# PostgreSQL work_mem for Bitmap Scans

## Definition

`work_mem` is the amount of memory PostgreSQL makes available to an individual query operation before it spills or changes execution behavior. Relevant operations include sorts, hash operations, and bitmap-related work. It is not a simple per-database or per-query global memory reservation.

## Bitmap-Scan Relevance

When a bitmap used by a bitmap heap scan exceeds available memory, PostgreSQL may represent page matches in a lossy form. Exact tuple locations are replaced by page-level information, requiring additional row inspection and predicate rechecks. Increasing `work_mem` can allow a more detailed bitmap to remain in memory and reduce this overhead.

The behavior is described in [[postgresql-lossy-bitmap-scans]]. It must be confirmed from the actual plan rather than inferred solely from elapsed time.

## Cash Settlement Benchmark

Tests against [[cashflow-data]] compared 4 MB/default, 10 MB, and 30 MB:

- Query 1 decreased from approximately 15,000 ms to 400 ms.
- Query 2 decreased from approximately 1,600 ms to 400 ms.
- Query 3 decreased from approximately 30,000 ms to 600 ms.

These results are specific to the tested queries, data distribution, PostgreSQL environment, and test conditions. They do not establish 30 MB as a universal minimum or optimal value.

## Tuning Guidance

Prefer validating the setting at the narrowest appropriate scope, such as a query, transaction, endpoint, or dedicated connection pool. A global increase should be evaluated against concurrent workload and worst-case operation counts because multiple operations and sessions can consume `work_mem` simultaneously.

Use `EXPLAIN (ANALYZE, BUFFERS)` to compare settings and inspect:

- Bitmap index and bitmap heap scan nodes.
- `Heap Blocks: exact` and `Heap Blocks: lossy`.
- `Rows Removed by Index Recheck`.
- Actual and estimated row counts.
- Buffer hits and reads.
- Sort method and memory.
- Planning and execution time.

See [[what-work-mem-setting-is-safe-for-cash-settlement-query-workloads]] for the unresolved deployment scope and capacity question.

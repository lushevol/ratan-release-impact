---
type: concept
title: PostgreSQL Lossy Bitmap Scans
created: 2026-08-24
updated: 2026-08-24
tags: [postgresql, bitmap-scan, lossy-bitmap, index-recheck, query-performance]
related: [postgresql-work-mem-for-bitmap-scans, postgresql-index-bitmap-sequential-scan-selection, postgresql-explain-plan-reading, cashflow-data]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/PostgreSQL performance/SQL performance when using bitmap scan.md"]
---
# PostgreSQL Lossy Bitmap Scans

## Definition

A bitmap scan collects row locations from one or more index conditions before fetching table pages. An exact bitmap retains tuple-level locations. A lossy bitmap retains only the pages that may contain matches when the bitmap cannot retain all tuple-level detail within its memory budget.

## Performance Cost

For lossy pages, PostgreSQL must inspect rows on the page and recheck the original predicates. This can increase page access, CPU work, and execution time. The cost is particularly relevant for multi-condition queries over a large table, including JSONB-derived predicates and ordered retrieval with a row limit.

The source benchmark associates higher `work_mem` with much lower latency for queries against [[cashflow-data]]. The association is consistent with reduced lossy bitmap overhead, but the source does not transcribe the execution plans and therefore does not prove that every tested query used a bitmap heap scan at every setting.

## Diagnostic Evidence

A plan-level investigation should compare:

- The scan node type and index conditions.
- `Heap Blocks: exact`.
- `Heap Blocks: lossy`.
- `Rows Removed by Index Recheck`.
- Actual rows versus estimated rows.
- Buffer hits and reads.
- Sort behavior for `ORDER BY created_at DESC`.

The distinction between a conventional index scan and a bitmap index/heap scan is important. The source uses both descriptions, so the terminology should not be treated as verified until the screenshots are replaced or supplemented with textual `EXPLAIN (ANALYZE, BUFFERS)` output.

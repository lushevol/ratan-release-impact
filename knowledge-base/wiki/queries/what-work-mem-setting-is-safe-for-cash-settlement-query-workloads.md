---
type: query
title: What work_mem Setting Is Safe for Cash Settlement Query Workloads?
created: 2026-08-24
updated: 2026-08-24
tags: [postgresql, work-mem, cash-settlement, capacity-planning, query-performance]
related: [postgresql-work-mem-for-bitmap-scans, postgresql-lossy-bitmap-scans, cashflow-data, cashflow-blotter-query-performance]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/PostgreSQL performance/SQL performance when using bitmap scan.md"]
---
# What work_mem Setting Is Safe for Cash Settlement Query Workloads?

## Question

Should the observed 30 MB `work_mem` value be applied per query, per application connection pool, per workload, or globally for Cash Settlement PostgreSQL queries?

## Evidence So Far

The source reports materially lower runtimes for three queries against [[cashflow-data]] when `work_mem` increased from 4 MB/default or 10 MB to 30 MB. The results support further investigation of a workload-specific tuning change, but they do not establish a universal setting.

The mechanism should be validated with textual plans showing whether lossy bitmap blocks and index rechecks decrease at higher settings. Query 3's different runtime profile also indicates that one setting may not affect all query shapes identically.

## Required Investigation

1. Capture repeated `EXPLAIN (ANALYZE, BUFFERS)` output at each candidate setting.
2. Confirm scan nodes, exact and lossy heap blocks, and index rechecks.
3. Measure warm-cache and cold-cache behavior separately.
4. Record PostgreSQL version, table size, row count, indexes, hardware, and concurrency.
5. Estimate worst-case memory usage from concurrent sessions and simultaneous operations.
6. Compare results with the applicable cashflow query or blotter SLA.
7. Test a session-, transaction-, endpoint-, or pool-scoped setting before considering a global change.

## Current Position

30 MB should be treated as a candidate benchmark value for the tested workload, not as an approved production-wide configuration.

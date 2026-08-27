---
type: concept
title: PostgreSQL work_mem Sizing
created: 2026-08-24
updated: 2026-08-24
tags: [postgresql, work-mem, memory, bitmap-index-scan, performance, capacity]
related: [postgresql-sequential-scan-triage, cash-settlement-performance-and-stress-testing, query-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/PostgreSQL performance/PostgreSQL increase work_mem up to 30MB & user define pg function risk analyze.md"]
---
# PostgreSQL work_mem Sizing

## Purpose

`work_mem` is PostgreSQL memory available to an individual query operation, including operations such as sorts, hashes, and bitmap processing. Increasing it can allow a bitmap index scan to retain more exact tuple information instead of switching to a lossy representation.

## Cash Settlement change

The tested change increases the Query Service session setting from `4MB` to `30MB`. On approximately four million rows, the documented bitmap-filter query improved from `10,073.726 ms` to `534.751 ms`, approximately an 18.8× speedup.

## Planning estimate

The source estimates the incremental memory requirement as:

```text
40 connections × 6 query-service instances × (30 MB − 4 MB)
= 6.24 GB
```

The estimate assumes one additional allocation per active connection. It is not a hard maximum because a single query can use `work_mem` for multiple plan nodes, and parallel workers may create additional consumers.

## Operational controls

A production rollout should monitor:

- Active database sessions and connection-pool utilization.
- Query latency and timeout rates.
- Temporary-file creation and size.
- Bitmap scan lossiness and execution plans.
- Sort and hash memory behavior.
- PostgreSQL host memory pressure and swap activity.
- Effects on mixed workloads, writes, and background processes.

The 500-user test showed improved post-change throughput, but the `4MB` baseline was substantially affected by database connection timeouts. Therefore, the result does not by itself establish a production capacity limit.

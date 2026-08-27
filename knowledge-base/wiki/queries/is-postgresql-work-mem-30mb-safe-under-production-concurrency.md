---
type: query
title: Is PostgreSQL work_mem=30MB Safe Under Production Concurrency?
created: 2026-08-24
updated: 2026-08-24
tags: [postgresql, work-mem, production-safety, concurrency, memory]
related: [postgresql-work-mem-sizing, query-service, cash-settlement-performance-and-stress-testing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/PostgreSQL performance/PostgreSQL increase work_mem up to 30MB & user define pg function risk analyze.md"]
---
# Is PostgreSQL work_mem=30MB Safe Under Production Concurrency?

## Question

Can Query Service use `work_mem=30MB` safely under sustained production-like concurrency and mixed query plans?

## Evidence

The documented estimate is:

```text
40 connections × 6 query-service instances × (30 MB − 4 MB) = 6.24 GB
```

The source describes a 64 GB PostgreSQL machine with approximately 55% baseline memory usage and estimates approximately 64% usage after the change.

A SQL bitmap-filter test improved from `10,073.726 ms` at `4MB` to `534.751 ms` at `30MB`. In the 500-user test, throughput increased from `5.5` to `24.7` QPS, but most baseline requests were affected by database connection timeouts.

## Open validation

The estimate does not account explicitly for multiple `work_mem` consumers per query, parallel workers, other PostgreSQL memory settings, or activity beyond the assumed peak connection count.

Validation should use equal-duration, production-like tests and capture active sessions, successful-request rates, query plans, temporary files, host memory, swap, and rollback thresholds.

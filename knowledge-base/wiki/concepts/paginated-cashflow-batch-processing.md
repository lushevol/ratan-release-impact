---
type: concept
title: Paginated Cashflow Batch Processing
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, pagination, batch-processing, memory-management]
related: [ratan, cash-settlement-batch-job-performance, is-six-gb-jvm-heap-sufficient-for-ratan-auto-materialize-at-uk-volume]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/Batch Job Performance.md"]
---
# Paginated Cashflow Batch Processing

Paginated processing bounds the number of cashflows retrieved and processed at once. In the reported Cash Settlement V2 jobs, a 2,000-record page size is used, with per-page query-by-ID and lifecycle processing.

For Auto Materialize at 50k, V2 processed 25 pages and completed in 406.13 seconds, compared with 790 seconds for the non-paginated V1 result. This is evidence of a relative improvement in the tested Dev workload, not a general production guarantee.

Pagination alone does not prove bounded total memory growth. At 100k, Auto Materialize V2 reached page 48 of 50 and failed with `java.lang.OutOfMemoryError: Java heap space` at 1.99 GB under a 2 GB maximum heap. Retained objects, lifecycle state, result aggregation, caches, or unclosed resources may still accumulate across pages and require profiling.

Auto Release V2 also uses 25 pages at 50k, but its main elapsed-time cost is group-lock filtering rather than its approximately 2.7-second per-page lifecycle stage.
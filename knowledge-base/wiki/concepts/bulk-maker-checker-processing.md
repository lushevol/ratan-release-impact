---
type: concept
title: Bulk Maker-Checker Processing
created: 2026-08-24
updated: 2026-08-24
tags: [bulk-processing, maker-checker, cash-settlement, ratanone, throughput]
related: [camunda, camunda-task-completion-performance, profilelimitation-batch-validation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Multi-Exception Handling - Bulk Submit Approve Reject Tech Design/Bulk Approve performance check result/bulk maker checker Performance Analysis.md"]
---
# Bulk Maker-Checker Processing

Bulk maker-checker processing handles multiple RATANONE Cash Settlement cashflows in bounded batches rather than issuing one request per cashflow.

## Reported implementation

The analyzed test processed 1,000 cashflows in 20 batches, implying 50 cashflows per batch. Total elapsed time decreased from 210 seconds to 52 seconds, an approximate 75.2% reduction.

The source attributes the improvement to fuller use of machine resources. It does not provide enough CPU, memory, thread-pool, database-concurrency, or throughput data to validate that explanation independently.

## Associated optimizations

The batch design was accompanied by:

- `ProfileLimitation` batch validation.
- Removal of unnecessary exception-collection JSON serialization and deserialization.
- Removal of frequent per-request object serialization.
- Index optimization for `userTask` and Camunda task-table queries.

These optimizations should not be treated as evidence that every workload can safely use 50-item batches. Batch-size limits, concurrency, lock behavior, partial failure, retry, and rollback semantics remain unspecified.

## Operational questions

Performance validation should measure p50, p95, and p99 latency, throughput, database load, lock contention, queue behavior, and failure recovery across representative batch sizes and concurrency levels.

See [[camunda-task-completion-performance]] for the remaining task-completion bottleneck analysis.

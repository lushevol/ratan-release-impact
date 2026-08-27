---
type: concept
title: Bulk Exception Processing Performance
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, bulk-processing, performance, maker, checker, batch-partitioning]
related: [camunda-task-completion-bottleneck, cashflow-retrieval-concurrency-bottleneck, cashflow-based-user-task-indexing, camunda, orchestration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Multi-Exception Handling - Bulk Submit Approve Reject Tech Design/Bulk Approve performance check result.md"]
---

# Bulk Exception Processing Performance

Bulk exception processing in RATANONE Cash Settlement covers maker submission and checker approval or rejection of many cashflows. The source evaluates batches of 100 and 1,000 `cashflowId` values in `uat2`.

## Main finding

Checker processing is the dominant performance bottleneck. Cashflow retrieval is the next most significant bottleneck, while `checkLimitationsBatch` contributes comparatively little latency in the endpoint-level measurements.

The reported 1,000-cashflow results include:

- Cashflow retrieval: 34.87 seconds.
- Batch profile limitation checking: 657.41 milliseconds.
- Checker endpoint: approximately 2.2 minutes.

These values are environment-specific observations rather than production SLOs.

## Batch partitioning

Partitioning 1,000 cashflows into 20 batches of 50 reduced observed maker latency from a maximum of 90 seconds to 17–55 seconds across the reported runs. Checker results also improved in some batched scenarios, with reported maxima ranging from 52 to 90 seconds.

The results do not support treating batching as a universal solution:

- Checker latency remains materially higher than maker latency.
- Increasing the database pool from 20 to 50 did not consistently resolve checker latency.
- Several cases have incomplete or ambiguous metrics.
- Equivalent-looking runs report different values, including maker results of 17 and 21 seconds.

## Concurrency controls

The tested application thread pools used:

```text
core thread size: 20 or 50
max thread size: 50
queue capacity: 10000
```

Database pool settings included `minimumIdle: 4` and `maximumPoolSize` values of 10, 20, or 50. The application pool and database pool should be evaluated separately because increasing application concurrency can expose downstream database or workflow bottlenecks.

## Performance decomposition

Bulk checker latency should be analyzed as separate stages:

1. Cashflow retrieval through `/api/ratan/stmcn/v1/cashflows`.
2. Profile limitation validation through `/api/ratan/v1/profileLimitation/checkLimitationsBatch`.
3. User-task lookup and persistence.
4. Camunda task completion through `/api/ratan/v2/camunda/task/NSTPSSI/checker`.
5. Listener, entitlement, status-update, and related orchestration work.

This decomposition prevents the relatively inexpensive rule check from being incorrectly treated as the primary cause of checker latency.

## Evidence limitations

The source does not define a consistent benchmark protocol, repeat count, percentile method, or SLA target. The labels “two query user task” and “three query user task” are also undefined. Results should therefore guide optimization priorities but should not be used as capacity commitments without controlled reruns.

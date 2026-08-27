---
type: concept
title: Cash Settlement Lifecycle Job Batch Performance
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, lifecycle-jobs, batch-processing, performance, capacity]
related: [cash-settlement-batch-job-performance, paginated-cashflow-batch-processing, long-running-batch-job-api-execution, cash-settlement-asynchronous-batch-processing, cashflow-lifecycle-service, orchestration, swift-service, what-caused-and-resolved-the-241-auto-fail-data-loss-records, what-explains-the-auto-release-performance-difference-between-fmrp2-and-staging]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/Lifecycle Jobs Performance Test.md"]
---

# Cash Settlement Lifecycle Job Batch Performance

## Overview

Cash Settlement lifecycle jobs were tested as paginated batch operations to address resource under-utilization, `moveStatus` validation overhead, database and memory performance issues, and queries that selected unnecessary columns.

The tested jobs were Auto Materialize, Auto Fail, and Auto Release Job. The results indicate that batch processing can sustain large workloads without observed OOM conditions, but they do not establish that every batch implementation is functionally ready to replace its online counterpart.

## Observed results

| Job / round | Volume | Total time | Approximate throughput | Maximum memory | Maximum CPU | Reported success |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| Auto Materialize | 100,000 | 706.5 s | 141.5 records/s | 2.09G | 78% | 100% |
| Auto Fail | 234,945 | 5,890.5 s | 39.9 records/s | 1.76G | 90.7% | 94.93%; 241 records reported as `data lose` |
| Auto Release, Round 1 | 1,000 | 42 s | 23.8 records/s | 1.40G | 92.5% | 100% |
| Auto Release, Round 2 | 19,024 | 513 s | 37.1 records/s | 4.63G | 87.6% | 100% |
| Auto Release, Round 3 | 20,272 | 612 s | 33.1 records/s | 4.70G | 15.7% | 100% |

The throughput values are arithmetic transformations of the reported measurements. They are not normalized benchmarks because environments, datasets, deployment topologies, and downstream conditions differed.

## Pagination and resource behavior

The tests generally used 1,000-record pages:

- Auto Materialize: 100 pages for 100,000 records.
- Auto Fail: 235 pages for 234,945 records.
- Auto Release Round 1: 1 page for 1,000 records.
- Auto Release Round 2: 20 pages for 19,024 records.
- Auto Release Round 3: 21 pages for 20,272 records.

All tests used:

```text
-Xms2048m -Xmx8192m -XX:MaxMetaspaceSize=1024m
```

No OOM was observed. Auto Materialize and Auto Fail used less than 2.1G of memory, while Auto Release used approximately 4.6–4.7G at similar volumes. This indicates that memory behavior is job-specific and should not be generalized from Auto Materialize to Auto Release.

## Downstream bottlenecks

Auto Release Round 2 recorded maximum CPU usage of 87.6% in Lifecycle, 83.2% in Orchestration, and 94.4% in SWIFT. The downstream SWIFT measurement is important because end-to-end runtime may be constrained by downstream work rather than lifecycle-service CPU.

Round 3 processed a similar volume in a different environment but took longer while recording much lower CPU usage:

- Round 2: 19,024 records, 513 seconds, Lifecycle CPU 87.6%.
- Round 3: 20,272 records, 612 seconds, Lifecycle CPU 15.7%.

Possible explanations include environment differences, data composition, downstream latency, queueing, throttling, lock contention, or different concurrency and deployment configurations. The source does not provide enough evidence to identify the cause.

## Query projection and validation

The report states that `materializeJob` and `failJob` need only:

```text
cashflowId
BusinessVersion
CashflowVersion
MinorVersion
```

Selecting only these fields is a plausible query-projection optimization, but the report does not provide query plans, database timings, or an isolated before-and-after measurement. The effect of `moveStatus` validation on batch execution is also identified but not quantified.

## Interpretation

The evidence is strongest for execution continuity and observed resource stability:

- Auto Materialize completed 100,000 records with a reported 100% success rate and no OOM.
- Auto Fail completed a 234,945-record run without interruption or database query exceptions, but reported 241 records as `data lose`.
- Auto Release completed all three reported runs with a 100% success rate and no OOM.

The evidence is weaker for functional correctness and production readiness. In particular, the Auto Fail data-loss result must be explained and reconciled before treating the batch version as a safe replacement. Formal acceptance criteria for runtime, throughput, resource usage, retry behavior, and data integrity are also required.

This page extends [[cash-settlement-batch-job-performance]] with job-specific evidence and should be read alongside [[paginated-cashflow-batch-processing]] and [[long-running-batch-job-api-execution]].
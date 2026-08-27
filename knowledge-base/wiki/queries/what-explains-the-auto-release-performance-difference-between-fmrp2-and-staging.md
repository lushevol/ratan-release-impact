---
type: query
title: What Explains the Auto Release Performance Difference Between fmrp2 and staging?
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, auto-release, performance-testing, environment-comparison, downstream-bottlenecks]
related: [cash-settlement-lifecycle-job-batch-performance, cash-settlement-batch-job-performance, long-running-batch-job-api-execution, cashflow-lifecycle-service, orchestration, swift-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/Lifecycle Jobs Performance Test.md"]
---

# What Explains the Auto Release Performance Difference Between fmrp2 and staging?

## Question

Why did Auto Release Round 3 take longer than Round 2 while processing a similar number of records and showing substantially lower CPU utilization across Lifecycle, Orchestration, and SWIFT?

## Evidence

| Round | Environment | Volume | Total time | Lifecycle CPU | Orchestration CPU | SWIFT CPU | Maximum memory |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Round 2 | `fmrp2` | 19,024 | 513 s | 87.6% | 83.2% | 94.4% | 4.63G |
| Round 3 | `staging` | 20,272 | 612 s | 15.7% | 25.8% | 24.2% | 4.7G |

Both runs used the `/v2/cashflow/holding-release` endpoint, a 1k page size, and the same JVM options. Both reported a 100% success rate and no OOM.

## Possible causes

The source does not establish which of the following explains the difference:

- Different data composition or business-rule paths.
- Different service-instance counts or deployment topology.
- Queueing or throttling.
- Lock contention.
- Different concurrency or partitioning configuration.
- Downstream response latency.
- Network or infrastructure conditions.
- Differences in monitoring windows or peak measurements.

The 94.4% SWIFT CPU observed in Round 2 shows that downstream processing can be a significant contributor to end-to-end behavior. Conversely, low CPU in Round 3 may indicate waiting or an external bottleneck rather than efficient execution.

## Required investigation

A controlled comparison should capture the same workload characteristics and deployment settings in both environments, including:

1. Service-instance counts and resource limits.
2. Page concurrency and partitioning configuration.
3. Queue, lock, and throttling metrics.
4. Per-page and downstream response times.
5. Lifecycle, Orchestration, and SWIFT CPU, memory, GC, and saturation metrics.
6. Database query duration and wait events.
7. Retry, timeout, and failure counts.
8. Data composition and business-rule distributions.

Until these variables are controlled, the two rounds should not be used as a single throughput benchmark or as evidence that lower CPU implies better system performance.
---
type: source
title: Lifecycle Jobs Performance Test
authors: []
year: 2026
url: "https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/11222354"
venue: Internal performance-test report
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, lifecycle-jobs, performance-testing, batch-processing, Ratan]
related: [cash-settlement-lifecycle-job-batch-performance, paginated-cashflow-batch-processing, cash-settlement-batch-job-performance, long-running-batch-job-api-execution, cash-settlement-asynchronous-batch-processing, cashflow-lifecycle-service, orchestration, swift-service, what-caused-and-resolved-the-241-auto-fail-data-loss-records, what-explains-the-auto-release-performance-difference-between-fmrp2-and-staging]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/Lifecycle Jobs Performance Test.md"]
---

# Lifecycle Jobs Performance Test

## Summary

This internal report evaluates batch implementations of Auto Materialize, Auto Fail, and Auto Release Job in the Ratan cash-settlement platform. The tests focus on execution time, pagination, CPU and memory usage, database-query behavior, and processing success.

The report identifies four problems in the earlier implementation:

1. Distributed deployments did not fully utilize available machine resources.
2. `moveStatus` data validation affected batch execution.
3. Database and memory performance problems occurred.
4. Queries retrieved unnecessary columns. The report states that `materializeJob` and `failJob` require only the following fields:

```text
cashflowId
BusinessVersion
CashflowVersion
MinorVersion
```

The tests generally used a page size of 1k and an 8 GB maximum heap. No out-of-memory condition was observed. The results support batch processing for large-volume lifecycle jobs, but they do not by themselves establish production acceptance criteria or functional completeness.

## Reported benchmark results

| Job / round | Data volume | Environment | Endpoint | Page size | Page amount | Data-loading time | Total time | Maximum memory | Maximum CPU | Success |
| --- | ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Auto Materialize | 100,000 | `stagiorchestrationng` | `/v2/ratan/cashflow/auto/materialization` | 1,000 | 100 | 2.17 s | 706.5 s; last PT: 17 m 31.26 s | 2.09G, 26.1% of 8G | 78% | 100%; `cashflowId` starts with `PTMJ` |
| Auto Fail | 234,945 | `staging` | `/v1/cashflow/jobs/cashflows/autoFail` | 1,000 | 235 | 14.5 s | 5,890.5 s, 98m10s | 1.76G, 22% of 8G | 90.7% | 94.93%; `succ: 223028`, `data lose: 241` |
| Auto Release Job, Round 1 | 1,000 | `dev` | `/v2/cashflow/holding-release` | 1,000 | 1 | 0.04 s | 42 s | 1.40G, 17.5% of 8G | 92.5% | 100% |
| Auto Release Job, Round 2 | 19,024 | `fmrp2` | `/v2/cashflow/holding-release` | 1,000 | 20 | 5.3 s | 513 s, 8m33s | 4.63G, 57.8% of 8G | 87.6% | 100% |
| Auto Release Job, Round 3 | 20,272 | `staging` | `/v2/cashflow/holding-release` | 1,000 | 21 | 0.7 s | 612 s, 10m12s | 4.7G, 58.75% of 8G | 15.7% | 100% |

Approximate arithmetic throughput, calculated as records divided by total seconds, is shown below. These values are not normalized benchmarks because the tests used different environments, data profiles, and possibly different deployment conditions.

| Job / round | Approximate records per second |
| --- | ---: |
| Auto Materialize | 141.5 |
| Auto Fail | 39.9 |
| Auto Release Job, Round 1 | 23.8 |
| Auto Release Job, Round 2 | 37.1 |
| Auto Release Job, Round 3 | 33.1 |

## JVM configuration

All reported tests used the same JVM options:

```text
-Xms2048m -Xmx8192m -XX:MaxMetaspaceSize=1024m
```

## Auto Materialize

Auto Materialize processed 100,000 records in `stagiorchestrationng` using 100 pages of 1,000 records. The reported total time was 706.5 seconds, with a separate last-PT measurement of 17 minutes 31.26 seconds.

Maximum observed memory was 2.09G, or 26.1% of the 8 GB heap, and no OOM occurred. Maximum CPU usage was 78%. The report records a 100% success rate for records whose `cashflowId` starts with `PTMJ`.

The report states that the distributed implementation saved approximately six minutes compared with an earlier test in the dev environment and concludes that the batch version can replace the original online version. This comparison is not a controlled A/B benchmark because the environments and baseline conditions are not fully specified.

The report includes Grafana monitoring links and screenshots for CPU, memory, and GC count. The primary monitored service was `ratan-cashflow-lifecycle-service`.

## Auto Fail

Auto Fail processed 234,945 records in `staging` using 235 pages of 1,000 records. Data loading by condition took 14.5 seconds and total execution took 5,890.5 seconds, or 98 minutes 10 seconds.

Maximum memory was 1.76G, or 22% of the 8 GB heap, with no OOM. Maximum CPU usage was 90.7%. The report states that all data was processed once without interruption caused by missing data and that no database query exceptions occurred, including no exception caused by excessively long input parameters.

The reported result was:

```text
Success rate: 94.93%
succ: 223028
data lose: 241
```

The meaning and disposition of the 241 records described as `data lose` are not defined. The report does not establish whether these records were rejected, transiently failed, excluded by business rules, retried, reconciled, or actually lost. Consequently, the execution appears stable from a resource and continuity perspective, but functional completeness remains unresolved.

The report nevertheless concludes that the batch version can replace the original online version and can process large datasets smoothly and efficiently. That replacement conclusion requires validation against the unexplained data-loss result.

## Auto Release Job

### Round 1

Round 1 processed 1,000 records in `dev` using one page. Total execution time was 42 seconds, with 0.04 seconds spent loading data by condition. Maximum memory was 1.40G, or 17.5% of the 8 GB heap, and maximum CPU usage was 92.5%. The reported success rate was 100%.

This small-volume result supports successful execution but is insufficient by itself to demonstrate large-scale performance.

### Round 2

Round 2 processed 19,024 records in `fmrp2` using 20 pages. Total execution time was 513 seconds, or 8 minutes 33 seconds. Maximum memory was 4.63G, or 57.8% of the 8 GB heap, and no OOM occurred.

The observed maximum CPU values across the service path were:

| Component | Maximum CPU |
| --- | ---: |
| Lifecycle | 87.6% |
| Orchestration | 83.2% |
| SWIFT | 94.4% |

The 94.4% SWIFT CPU measurement indicates that downstream processing may be a limiting factor. Lifecycle-service CPU alone should not be treated as a complete measure of system bottleneck or end-to-end efficiency.

### Round 3

Round 3 processed 20,272 records in `staging` using 21 pages. Total execution time was 612 seconds, or 10 minutes 12 seconds. Maximum memory was 4.7G, or 58.75% of the 8 GB heap, and no OOM occurred.

The observed maximum CPU values were:

| Component | Maximum CPU |
| --- | ---: |
| Lifecycle | 15.7% |
| Orchestration | 25.8% |
| SWIFT | 24.2% |

Round 3 took longer than Round 2 despite processing a similar volume and showing substantially lower CPU utilization. The report does not identify whether the difference resulted from data composition, downstream latency, queueing, throttling, lock contention, concurrency, or deployment topology.

## Evidence and limitations

The report provides concrete measurements for volume, page size, page count, runtime, memory, CPU, and reported success. It also provides monitoring links and screenshots, although the screenshots are not independently assessable from the text alone.

The results should be interpreted with the following limitations:

- Tests ran in `stagiorchestrationng`, `staging`, `dev`, and `fmrp2`; cross-environment comparisons are not controlled.
- No formal runtime, throughput, memory, or data-integrity acceptance criteria are stated.
- The Auto Fail data-loss count is unexplained.
- The number of participating service instances and the partitioning or concurrency strategy are not documented.
- The report does not define retry, reconciliation, cancellation, or asynchronous completion semantics.
- Stable memory and the absence of OOM do not establish functional correctness.
- Lower lifecycle CPU does not necessarily indicate better performance when downstream services or waiting time dominate.

## Related wiki topics

The report provides evidence for [[cash-settlement-lifecycle-job-batch-performance]], [[paginated-cashflow-batch-processing]], [[long-running-batch-job-api-execution]], and [[cash-settlement-asynchronous-batch-processing]]. The monitored execution path includes [[cashflow-lifecycle-service]], [[orchestration]], and [[swift-service]].

The unresolved Auto Fail result is tracked in [[what-caused-and-resolved-the-241-auto-fail-data-loss-records]]. The inconsistent Auto Release results are tracked in [[what-explains-the-auto-release-performance-difference-between-fmrp2-and-staging]].
---
type: source
title: Bulk Maker-Checker Performance Analysis
authors: []
year: 2025
url: ""
venue: "Internal RATANONE Cash Settlement technical design"
created: 2026-08-24
updated: 2026-08-24
tags: [ratanone, cash-settlement, bulk-processing, maker-checker, performance-analysis]
related: [camunda, bulk-maker-checker-processing, camunda-task-completion-performance, profilelimitation-batch-validation, holding-release-precheck, orchestration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Multi-Exception Handling - Bulk Submit Approve Reject Tech Design/Bulk Approve performance check result/bulk maker checker Performance Analysis.md"]
---
# Bulk Maker-Checker Performance Analysis

## Scope

This internal analysis evaluates bulk submit, approve, and reject processing for RATANONE Cash Settlement exception workflows. The principal focus is Camunda task completion, database lookup performance, validation, serialization, holding-check execution, and event publication.

The observed examples are dated September 4–10, 2025.

## Reported optimization results

| item name | before optimization | after optimization | remark |
| --- | --- | --- | --- |
| Using batch processing | 210 s | 52 s | 1000 cashflows are divided into 20 batches，make full use of all machine resources |
| Optimize the index of userTask table | 4000 ms | 2 ms | Use the cashflowId index, and delete invalid indexes |
| Optimize the index of camunda table | 1600 ms | 1-2 ms | Camunda task table query by index |
| JSON serialization/deserialization | 600 ms | 0 ms | Removed json serialization and deserialization of parsing exception collection |
| Transform frequent serialization | 450 ms | 8 ms | Remove the object serialization operation for each request |
| ProfileLimitation changed from single verification to batch verification | 700 ms per request | 150 ms for a batch of 50 requests | Changed from 1000 requests to 20 requests |

Processing 1,000 cashflows in 20 batches corresponds to 50 cashflows per batch. The reported elapsed time decreased from 210 seconds to 52 seconds, an approximate 75.2% reduction.

## Performance conclusion

The source concludes that the remaining bottleneck is mainly Camunda's internal logic. The evidence supports a narrower conclusion: database lookup, serialization, and validation overheads were substantially reduced, while residual latency remains concentrated around workflow completion and operations invoked during completion.

The source also reports that the `holding-check` operation takes 1–6 seconds. The available trace does not establish whether this time is attributable to Camunda engine work, holding-check business logic, transaction waits, event publication, OpenSearch handling, or an interaction among those components.

## Representative timing observations

| Cashflow | Classification | Total task time |
|---|---:|---:|
| `AF7536600535` | Bad | 10,239 ms |
| `AF7536600547` | Bad | 9,797 ms |
| `AF7237600060` | Bad | 9,518 ms |
| `AF7536600983` | Common | 3,408 ms |

The three bad examples are approximately 2.8–3.0 times slower than the common example. These observations are illustrative rather than a generalized benchmark because the source provides only four cases and no percentile distribution, concurrency conditions, workload normalization, or resource metrics.

## Trace excerpt

| Step | Service | AF7536600535 Execute time | AF7536600535 time taken(ms) | AF7536600547 Execute time | AF7536600547 time taken(ms) | AF7237600060 Execute time | AF7237600060 time taken(ms) | AF7536600983 Execute time | AF7536600983 time taken(ms) |
|---|---|---|---:|---|---:|---|---:|---|---:|
| Get Lock |  | Sep 10, 2025 @ 11:29:59.478 |  | Sep 10, 2025 @ 11:30:00.397 |  | Sep 4, 2025 @ 19:34:11.257 |  | Sep 9, 2025 @ 17:10:00.799 |  |
| Query task for role （task start） |  | Sep 10, 2025 @ 11:29:59.938 | sleep 1.5s | Sep 10, 2025 @ 11:30:00.701 | sleep 1.5s | Sep 4, 2025 @ 19:34:11.407 | sleep 1.5s | Sep 9, 2025 @ 17:10:01.392 | sleep 1.5s |
| Query CashflowUserTask by processBusinessKey |  | Sep 10, 2025 @ 11:30:01.519 | 68 | Sep 10, 2025 @ 11:30:02.454 | 204 | Sep 4, 2025 @ 19:34:13.177 | 249 | Sep 9, 2025 @ 17:10:02.981 | 59 |
| CashflowQueryServiceImpl.query | lifecycle |  |  | Sep 10, 2025 @ 11:30:02.454 | 28 | Sep 4, 2025 @ 19:34:13.300 | 122 |  |  |
| Get latest SCBML message | orchestration | Sep 10, 2025 @ 11:30:01.561 | 41 | Sep 10, 2025 @ 11:30:02.455 | 31 | Sep 4, 2025 @ 19:34:13.301 | 123 | Sep 9, 2025 @ 17:10:03.105 | 124 |
| save user task done |  | Sep 10, 2025 @ 11:30:01.580 |  | Sep 10, 2025 @ 11:30:02.520 |  | Sep 4, 2025 @ 19:34:13.330 |  | Sep 9, 2025 @ 17:10:03.121 |  |
| PublishEnrichedMessageService | orchestration | Sep 10, 2025 @ 11:30:02.246 | 148 | Sep 10, 2025 @ 11:30:03.033 | 113 | Sep 4, 2025 @ 19:34:14.920 |  | Sep 9, 2025 @ 17:10:03.863 | 101 |
| Send domain event success | lifecycle | Sep 10, 2025 @ 11:30:03.590 |  | Sep 10, 2025 @ 11:30:04.211 |  | Sep 4, 2025 @ 19:34:15.795 |  |  |  |
| message-event insert successfully | message-event | Sep 10, 2025 @ 11:30:03.599 |  | Sep 10, 2025 @ 11:30:04.940 |  | Sep 4, 2025 @ 19:34:15.541 |  | Sep 9, 2025 @ 17:10:03.565 |  |
| handleDomainEventForOpenSearch done | lifecycle | Sep 10, 2025 @ 11:30:04.243 |  |  |  | Sep 4, 2025 @ 19:34:15.869 |  | Sep 9, 2025 @ 17:10:03.778 |  |
| message-event insert successfully | message-event | Sep 10, 2025 @ 11:30:05.567 |  | Sep 10, 2025 @ 11:30:05.512 |  |  |  | Sep 9, 2025 @ 17:10:03.865 |  |
| Task completed |  | Sep 10, 2025 @ 11:30:10.178 | 10239 | Sep 10, 2025 @ 11:30:10.499 | 9797 | Sep 4, 2025 @ 19:34:20.911 | 9518 | Sep 9, 2025 @ 17:10:04.801 | 3408 |
| Release lock |  | Sep 10, 2025 @ 11:30:10.228 |  | Sep 10, 2025 @ 11:30:10.507 |  | Sep 4, 2025 @ 19:34:20.926 |  | Sep 9, 2025 @ 17:10:04.808 |  |

## Limitations and follow-up

The analysis does not provide the database engine or exact index definitions, query plans, sample sizes, latency percentiles, resource utilization, connection-pool metrics, Camunda metrics, or failure and retry behavior. The `ProfileLimitation` result is also ambiguous: it is unclear whether 150 ms is the total time for a 50-request batch or a per-request measurement.

The fixed `sleep 1.5s` shown during task startup should be separately investigated rather than attributed to Camunda engine processing. Event persistence and `handleDomainEventForOpenSearch` should likewise be instrumented independently to determine whether they are synchronous parts of the user-visible critical path.

## Related topics

- [[bulk-maker-checker-processing]]
- [[camunda-task-completion-performance]]
- [[profilelimitation-batch-validation]]
- [[holding-release-precheck]]
- [[orchestration]]
- [[queries/which-service-owns-fields-validation-rules-and-profile-limitation]]
- [[queries/what-is-the-authoritative-holding-release-verification-contract]]

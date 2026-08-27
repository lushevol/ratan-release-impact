---
type: source
title: Bulk Approve Performance Check Result
authors: []
year: 2025
url: ""
venue: "RATANONE Cash Settlement Technical Design"
tags: [cash-settlement, performance-testing, bulk-approve, bulk-reject, uat2, ratanone]
related: [bulk-exception-processing-performance, camunda-task-completion-bottleneck, cashflow-retrieval-concurrency-bottleneck, cashflow-based-user-task-indexing, camunda, orchestration, rule-service, ratan-cashflow-lifecycle-service, rule-service-performance-testing, rule-engine-vs-workflow-orchestration]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Multi-Exception Handling - Bulk Submit Approve Reject Tech Design/Bulk Approve performance check result.md"]
---

# Bulk Approve Performance Check Result

## Scope

This source reports `uat2` performance testing for RATANONE Cash Settlement bulk maker and checker operations involving 100 to 1,000 `cashflowId` values. The tested paths were cashflow retrieval, profile limitation checks, and Camunda-backed checker task completion.

The source concludes that the checker interface is the primary bottleneck, followed by cashflow-information retrieval. The batch limitation-check endpoint is comparatively inexpensive.

## Tested interfaces

```text
GET /api/ratan/stmcn/v1/cashflows

POST /api/ratan/v1/profileLimitation/checkLimitationsBatch

POST /api/ratan/v2/camunda/task/NSTPSSI/checker

original single verification interface:
checkLimitation/{profile}/{currency}/{amount}
```

The source identifies the first endpoint with cashflow retrieval, the second with `rule-service`, and the third with the `foundation` checker interface.

## Thread-pool configuration

```text
core thread size: 20 (50)

max thread size: 50

queue capacity: 10000
```

Database-pool conditions reported in the tests included `minimumIdle: 4` with `maximumPoolSize` values of 10, 20, or 50. Several test descriptions refer to “4 database connections” even when the maximum pool size is higher.

## Endpoint-level results

| Test rows | Fetch cashflow information | checkLimitationsBatch | Checker |
| --- | --- | --- | --- |
| 2 | 548ms | 999ms | 7.84s |
| 100 | 3.14s | 324ms | 22.84s |
| 1000 | 22.83s | 1.64s (max, first request) | 3.5m |
| 1000, core thread size 50 | 34.87s | 657ms | 2.2m |

The results are environment-specific observations from `uat2`, not production service-level objectives. The source does not provide consistent repeat counts, percentile definitions, or controlled run metadata.

## Maker results

| Case | Cashflow ID rows | Interface | Application thread pool | Database thread pool | Batch condition | Max (second) |
| --- | ---: | --- | --- | --- | --- | ---: |
| 1000 cashflows in a single batch | 1000 | maker | core 50, max 50, queue 10000 | minimumIdle 4, maximumPoolSize 20 | — | 90 |
| Backend 20 batches | 1000 | maker | core 50, max 50, queue 10000 | minimumIdle 4, maximumPoolSize 20 | 20 batches of 50 cashflows | 55 |
| Frontend and backend 20 batches | 1000 | maker | core 50, max 50, queue 10000 | minimumIdle 4, maximumPoolSize 20 | 20 batches of 50 cashflows | 45 |
| Frontend and backend 20 batches | 1000 | maker | core 50, max 50, queue 10000 | minimumIdle 4, maximumPoolSize 50 | 20 batches of 50 cashflows | 17 |
| Frontend and backend 20 batches | 1000 | maker | core 50, max 50, queue 10000 | minimumIdle 4, maximumPoolSize 50 | 20 batches of 50 cashflows | 21 |

Partitioning the work into 20 batches reduced the observed maker maximum from 90 seconds to between 17 and 55 seconds in the reported runs. The two maximum-pool-size-50 results differ, so the data does not establish a stable capacity guarantee.

## Checker results

| Case | Cashflow ID rows | Application core threads | Database maximum pool size | Batch condition | Additional condition | Max (second) | Min (second) | Average (second) |
| --- | ---: | ---: | ---: | --- | --- | ---: | ---: | ---: |
| Single batch | 100 | 20 | — | — | — | 22.84 | — | — |
| Single batch | 1000 | 20 | — | — | — | 210 | — | — |
| Single batch | 1000 | 50 | — | — | — | 132 | — | — |
| Frontend, 2 batches | 100 | 50 | 20 | 2 batches of 50 cashflows | — | 18.68 | — | — |
| Frontend, 20 batches | 1000 | 50 | 20 | 20 batches of 50 cashflows | — | 72 | 13.18 | 41.93 |
| Frontend, 20 batches | 1000 | 50 | 20 | 20 batches of 50 cashflows | — | 72 | 17.58 | 44.73 |
| Backend, 20 batches | 1000 | 50 | 20 | 20 batches of 50 cashflows | — | 90 | — | — |
| Frontend and backend, 20 batches | 1000 | 50 | 20 | 20 batches of 50 cashflows | — | 90 | — | — |
| Frontend and backend, 20 batches | 1000 | 50 | 50 | 20 batches of 50 cashflows | — | 72 | 14.44 | — |
| Frontend and backend, 20 batches | 1000 | 50 | 50 | 20 batches of 50 cashflows | two query user task | 52 | 12.24 | — |
| Frontend and backend, 20 batches | 1000 | 50 | 50 | 20 batches of 50 cashflows | three query user task | 59 | — | — |

Increasing application core threads from 20 to 50 reduced the single-batch 1,000-cashflow maximum from 210 to 132 seconds. Batching reduced some observed maxima, but checker latency remained high and the meaning of “two query user task” and “three query user task” is not defined.

## Checker-operation breakdown

The source reports two checker operations:

- `ProfileLimitCheck`, which calls `checkLimitation/{profile}/{currency}/{amount}` and takes approximately 300 milliseconds on average.
- `checkerOperate`, which takes approximately 6.7 seconds on average.

The reported breakdown is:

| Service method | Call times | Total time taken (ms) |
| --- | ---: | ---: |
| `checkUserLimitBasedProfileAccess`, mostly `cashFlowApiClient.getCashFlows` | 1 | 829 |
| `statusUpdateService.getLatestSCBMLMessage` | 3 | 120 |
| `userTaskService.queryActiveTask` | 3 | 534 |
| `userTaskService.queryDeadTask` | 1 | Not specified |
| `taskService.complete` | 1 | 4336 |
| `commonServiceCaller.execute` | 1 | 163 |
| `userTaskService.save` | 3 | Not specified |
| `authServerClient.getUserEntitlement` | 1 | 100 |
| Total | — | 6742 |

The source identifies three main hotspots: per-cashflow profile-access checking, unindexed `queryActiveTask` access, and `taskService.complete`.

## Improvement plan

The following items are marked complete or struck through in the source:

```sql
CREATE INDEX idx_ratan_cashflow_user_task_cid_bt_bv_active
    ON ratan_cashflow_user_task (cashflow_id, business_type, business_version, active);
```

The source also describes these completed optimizations:

- Replacing direct database connections in Orchestration with `HikariDataSource`, configured with a minimum of 4 and a maximum of 10 connections.
- Avoiding repeated JSON serialization and deserialization in `parseExceptionListRequest`.
- Reusing `ObjectMapper` rather than creating `new ObjectMapper()` for each `getEntitlement` invocation.

Proposed or ongoing work includes optimizing `taskService.complete`, making Camunda completion asynchronous where appropriate, improving `/api/ratan/stmcn/v1/cashflows`, and investigating Lifecycle cashflow retrieval under increasing concurrency.

## Camunda table observations

The source reports the following `uat2` figures. The `w` and `W` units are preserved because their meaning is not defined:

| Table | Reported row count |
| --- | ---: |
| `ACT_RU_TASK` | 60.9w |
| `ACT_RU_VARIABLE` | 2471.3W |
| `ACT_RU_EXECUTION` | 907W |
| `ACT_HI_TASKINST` | 3.6W |
| `ACT_HI_VARINST` | 466.7W |
| `ACT_HI_ACTINST` | 148.9W |
| `ACT_HI_DETAIL` | 890.1W |
| `ACT_GE_BYTEARRAY` | 1762W |

These figures justify investigating retention, indexing, query plans, and runtime/history separation, but they do not independently prove that table size caused the measured latency.

## Interpretation and limitations

The evidence supports prioritizing Camunda task completion and its listener path before tuning profile limitation checks. `CompleteTaskListener` reportedly sleeps for approximately 1.5 seconds and performs `userTask`, `getLatestSCBMLMessage`, and other operations during completion.

The source does not establish:

- Whether measurements are end-to-end, server-side, or browser-observed.
- Whether the values are single runs, maxima, averages, or percentiles.
- How duplicate checker cases differ.
- Whether the struck-through changes were deployed before every benchmark.
- Whether asynchronous completion preserves approval status, retry, duplicate-submission, and failure-reporting semantics.

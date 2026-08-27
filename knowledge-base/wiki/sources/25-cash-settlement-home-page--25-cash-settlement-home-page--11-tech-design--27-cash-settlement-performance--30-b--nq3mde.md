---
type: source
title: Cash Settlement Batch Status Update API Tuning
authors: []
year: 2025
url: ""
venue: ""
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, batch-processing, performance, lifecycle, netting, transaction-atomicity]
related: [lifecycle-batch-status-update-api, cashflow-batch-transaction-atomicity, batch-distributed-locking, cash-settlement-asynchronous-batch-processing, netting-service, cashflow-lifecycle-service, cashflow-status-write-back, cashflow-release-and-netting-race-condition, hot-nstp-rule-exception-reconciliation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/Batch Status Update API Tuning.md"]
---
# Cash Settlement Batch Status Update API Tuning

## Summary

This technical design analyzes production timeout risk in the Netting API and proposes performance improvements for the Lifecycle Batch Status Update API. The design focuses on reducing Redis operations, database round trips, JVM processing time, persistence overhead, and exception-closure latency while preserving whole-batch transaction behavior.

The document notes that the existing multi-thread transaction model performs well in most cases but does not guarantee that all operations commit or roll back together in edge cases. The proposed design separates batch processing into data retrieval, in-memory calculation and status transitions, batch persistence, and post-processing.

## Batch update callers and use cases

The API is used by several synchronous and scheduled flows:

- UI → preview API → Lifecycle query API
- UI → Net API → Lifecycle Batch Status Update API
- UI → Unnet API → Lifecycle Batch Status Update API
- Netting Service job → Net/API → Lifecycle Batch Status Update API
- Workflow → Auto Unnet API → Lifecycle Batch Status Update API
- Other functions related to batch status updates

The API also supports batch status events for:

- `Cashflow Ready + Pending Ack` receiving an Ack during a Release action
- Cashflow Settle actions
- Other batch status events

Because the API is batch-oriented and has no stated user-facing volume limitation, sudden increases in request size may create timeout and resource-consumption risk.

## Proposed processing structure

The proposed redesign is:

1. Fetch all required data in one query.
2. Perform calculations and status-machine processing in application memory.
3. Persist existing cashflow changes at batch level.
4. Execute post-processing, including CQRS operations, exception closure, and Kafka-triggered STP processing.

The document proposes that the processing for individual cashflows within the core task may run in parallel. This requires a separate validation of transaction semantics because JVM-level parallelism does not by itself guarantee all-or-nothing database behavior.

## Tuning points

The source table is preserved below.

| SN. | | Benefit | Challenge | Solution | Status |
| --- | --- | --- | --- | --- | --- |
| 1 | Distributed lock could be in batch instead of 1 by 1 | Reduce time cost of redis read/write | batch lock should be in transactional | 1. Lua script execution 2. use Completable Future or Cyclic Barrier to lock in parallel, 1 fail, all release | |
| 2 | Query from DB at once | Reduce DB interaction, Reduce time cost and IO cost | 1. There is table join sql which is complicated. 2. query all data to memory to process, memory usage might be larger than before. | Spring data JPA, rely on JPQL and spring data projection | |
| 3 | Run status machine in parallel | Multi-thread processing in pure JVM, reduce time cost | - | CompletableFuture | |
| 4 | Save all for existing cashflows at once | Reduce DB interaction, Reduce time cost and IO cost | JPA saveAll() on insert/update operation is not efficient enough, need to implement manually | 1. Enabling batch operation with configuration: spring.jpa.properties.hibernate.jdbc.batch_size=100 spring.jpa.properties.hibernate.order_inserts=true 1. Use @Modifying or JdbcTemplate.batchUpdate() with native batch update sql | |
| 5 | Batch close exception instead of close 1 by 1 | reduce 2 exception close API time cost | Need code change on 1. SSI stamping service 2. NSTP service | JDBC batch update | |

The source does not populate the `Status` column. The tuning points should therefore be treated as proposals or locally tested changes rather than confirmed production capabilities.

## Reported test result

The source reports local implementation of tuning points 2 and 3 for a 2,300-cashflow netting test.

| Volume | 2300 cashflow netting | 2300 cashflow netting |
| --- | --- | --- |
| Env | DEV(after tuning) | UAT1(before tuning) |
| Stage | Time Cost | Time Cost |
| preprocess - Add lock for cashflowids | ~8.7s | first lock - Mar 12, 2025 @ 14:20:09.414 last release - Mar 12, 2025 @ 14:21:03.855 time cost: ~54.4s |
| core process - run lifecycle | ~22s | |
| post process - release lock | ~3s | |
| post process - close exceptions | close SSI exceptions: ~2s close NSTP exceptions: ~4s ~6s | close SSI exceptions: ~1s close NSTP exceptions: ~1.5s time cost: ~2.5s |
| Total Cost | ~39.7s | ~57s |
| Reference | Discover - Elastic | Discover - Elastic |

The reported elapsed time decreased from approximately 57 seconds to 39.7 seconds, or approximately 30%. The comparison is directional rather than a controlled benchmark because it compares DEV after tuning with UAT1 before tuning, omits a UAT1 core-process timing, and provides no sample size, percentile data, error rate, rollback rate, workload controls, or resource-utilization measurements.

The result supports further testing but does not establish a production performance or transaction-consistency guarantee.

## Long-term architecture

The document proposes two complementary architectural directions:

1. Move netting and lifecycle logic into the same application to reduce synchronous timeout exposure between Netting and Lifecycle.
2. Process large netting requests asynchronously, potentially through a notification center.

The staged proposal is:

- **Step 1:** Migrate net/Unnet logic from Netting Service to Lifecycle.
- **Step 2:** Restructure the Batch Status Update API around single-query retrieval, in-memory processing, batch persistence, and post-processing.
- **Step 3:** Optimize distributed locking for a list of cashflow IDs.
- **Step 4:** Consider asynchronous processing for large request bodies.

Co-location can remove one service boundary, but it does not by itself solve long-running request admission, queueing, retry, idempotency, or downstream side-effect consistency.

## Consistency and implementation risks

The design leaves several important boundaries unspecified:

- Whether “whole transaction” covers only database writes or also SSI and NSTP exception closure.
- Whether Kafka-triggered STP processing participates in the same consistency boundary.
- How partial lock acquisition is rolled back when one lock fails.
- How lock ownership, expiry, retry, and crash recovery are handled.
- Whether parallel status-machine execution is limited to calculation or includes transactional persistence.
- Whether manual JDBC batching preserves validation, auditing, optimistic locking, and entity lifecycle behavior.
- What maximum batch size, payload size, concurrency, timeout, and back-pressure limits apply.
- How asynchronous requests expose job state, failures, retries, duplicate detection, and completion.

These concerns connect the source to [[cashflow-batch-transaction-atomicity]], [[batch-distributed-locking]], [[cashflow-release-and-netting-race-condition]], and [[cash-settlement-asynchronous-batch-processing]].
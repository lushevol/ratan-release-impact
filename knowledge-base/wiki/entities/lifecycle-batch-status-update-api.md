---
type: entity
title: Lifecycle Batch Status Update API
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, api, lifecycle, batch-processing]
related: [cashflow-batch-transaction-atomicity, cashflow-status-write-back, cashflow-release-and-netting-race-condition, cashflow-lifecycle-service, netting-service, cash-settlement-asynchronous-batch-processing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/Batch Status Update API Tuning.md"]
---
# Lifecycle Batch Status Update API

The Lifecycle Batch Status Update API processes status changes for multiple cashflows in a single request. It is used by UI flows, Netting Service jobs, workflow-driven Auto Unnet actions, Release actions, Cashflow Settle actions, and other batch status events.

## Responsibilities

The proposed processing model is:

1. Retrieve all required data in one database query.
2. Run calculations and status-machine transitions in memory.
3. Persist existing cashflow changes in a database batch.
4. Perform post-processing such as CQRS actions, SSI and NSTP exception closure, and Kafka-triggered STP processing.

The source proposes parallel execution for independent cashflow processing, but the transaction boundary and failure behavior require explicit validation.

## Performance concerns

The API has no documented user-facing limitation on batch size. Large request bodies and sudden increases in cashflow volume can therefore cause:

- Long synchronous request durations.
- Netting-to-Lifecycle timeout exposure.
- Increased Redis and database load.
- Greater JVM memory consumption when all data is loaded for in-memory processing.
- Increased downstream exception-closure and event-processing latency.

A local comparison for 2,300 cashflows reported approximately 39.7 seconds after tuning versus approximately 57 seconds before tuning. The comparison used DEV and UAT1 rather than identical environments and should not be treated as a controlled benchmark.

## Architectural direction

The source proposes moving net/Unnet logic from [[netting-service]] into [[cashflow-lifecycle-service]] to reduce cross-service timeout risk. It also recommends considering asynchronous batch processing through a notification-center pattern for large requests.

The API should be evaluated together with [[cashflow-batch-transaction-atomicity]] and [[batch-distributed-locking]]. Performance improvements must not be treated as proof of all-or-nothing behavior.
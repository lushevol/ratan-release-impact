---
type: concept
title: Cashflow Batch Transaction Atomicity
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, transactions, atomicity, batch-processing, consistency]
related: [lifecycle-batch-status-update-api, cashflow-status-write-back, cashflow-release-and-netting-race-condition, release-time-cashflow-status-gating, hot-nstp-rule-exception-reconciliation, non-blocking-message-retry]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/Batch Status Update API Tuning.md"]
---
# Cashflow Batch Transaction Atomicity

Cashflow batch transaction atomicity is the requirement that a batch status update either commits as one logical unit or rolls back without leaving a partially applied batch.

## Design context

The source reports that an existing multi-thread transaction model works in most cases but cannot guarantee that all operations commit or roll back together in edge cases. The proposed alternative is to retrieve data once, process it in memory, persist changes in a batch, and then run post-processing.

Parallelism can reduce elapsed time, but `CompletableFuture` and similar concurrency mechanisms do not automatically provide a shared transaction boundary. Parallel computation must therefore be distinguished from parallel database writes.

## Transaction boundary questions

The design does not establish whether the following operations are inside one atomic boundary:

- Cashflow status and sub-status persistence.
- Distributed-lock acquisition and release.
- SSI exception closure.
- NSTP exception closure.
- CQRS actions.
- Kafka-triggered STP processing.

Database atomicity does not automatically extend to external service calls or message publication. Those operations may require idempotency, retries, an outbox, compensation, or reconciliation.

## Validation requirements

A complete design should define:

- Failure behavior when one cashflow cannot be processed.
- Rollback behavior for already calculated or persisted cashflows.
- Lock cleanup after partial acquisition, timeout, or process failure.
- Optimistic-locking and version-conflict semantics.
- Downstream retry and duplicate-message handling.
- Reconciliation for database state and external side effects.

The concept is closely related to [[cashflow-release-and-netting-race-condition]] and [[cashflow-status-write-back]].
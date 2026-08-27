---
type: concept
title: Cash Settlement Asynchronous Batch Processing
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, asynchronous-processing, batch-processing, notification-center, reliability]
related: [lifecycle-batch-status-update-api, cashflow-batch-transaction-atomicity, non-blocking-message-retry, kafka-dual-cluster-disaster-recovery, netting-service, cashflow-lifecycle-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/Batch Status Update API Tuning.md"]
---
# Cash Settlement Asynchronous Batch Processing

Cash Settlement asynchronous batch processing accepts a large batch request without keeping the initiating synchronous request open until all cashflows and downstream operations complete.

## Rationale

The source identifies unrestricted batch volume and large request bodies as a long-term risk. Moving netting to an asynchronous mechanism, potentially through a notification center, can reduce API timeout exposure and allow work to be queued and controlled.

Asynchronous processing is complementary to moving netting and Unnet logic into [[cashflow-lifecycle-service]]. Co-location reduces one synchronous service boundary; asynchronous execution removes the requirement for the request to remain open during the complete batch lifecycle.

## Required API contract

An implementation should define:

- Request acceptance and job identifier.
- Batch state and progress visibility.
- Completion and failure states.
- Retry behavior.
- Duplicate-request detection and idempotency.
- Maximum batch size and payload limits.
- Queue capacity, concurrency, and back-pressure.
- Dead-letter or operational recovery handling.
- User-visible handling of partial failures.

## Consistency considerations

Asynchronous execution does not resolve transaction-boundary questions. Database updates, SSI and NSTP exception closure, CQRS actions, and Kafka-triggered STP processing may complete at different times. The design therefore requires explicit retry, idempotency, and reconciliation semantics, as described in [[cashflow-batch-transaction-atomicity]] and [[non-blocking-message-retry]].
---
type: query
title: What Retry Backoff and Terminal Failure Policy Governs Ratan Query Service Consumption?
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, message-consumption, retry, backoff, dead-letter, failure-handling]
related: [ratan-query-service, cashflow-locking-and-retry-policy, what-are-the-bounded-retry-idempotency-and-dead-letter-controls-for-cashflow-processing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Ratan query service message consuming control.md"]
---
# What Retry Backoff and Terminal Failure Policy Governs Ratan Query Service Consumption?

The source asks whether `retryNum > 3` should throw an exception and what delay should apply. It does not state that three retries are configured or approved.

## Questions to resolve

- Which failures are retryable and which must fail immediately?
- Is `retryNum > 3` an existing behavior, a proposal, or an illustrative threshold?
- What retry schedule is required: fixed delay, exponential backoff, jitter, or broker-native redelivery?
- What is the terminal disposition after retry exhaustion: durable failed-event record, dead-letter destination, exception-only handling, alerting, or compensation?
- Who owns alert response and manual or automated replay?
- How are retries made idempotent and protected from duplicate state changes?
- Which metrics record retry count, exhaustion, latency, and replay outcomes?

## Scope

This query concerns [[ratan-query-service]] consumption. It contributes consumer-specific evidence to [[what-are-the-bounded-retry-idempotency-and-dead-letter-controls-for-cashflow-processing]] and does not establish a cross-system retry standard.
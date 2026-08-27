---
type: concept
title: Fixing Notification Event Ordering
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, event-ordering, concurrency, fixing-flag]
related: [fixing-flag-notification-processing, lifecycle-service, cashflow-reinstatement-and-replay, cash-settlement-exception-handling, cashflow-status-change-event-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Fixing flag notification.md"]
---
# Fixing Notification Event Ordering

Fixing notification event ordering covers the processing of fixing notifications when they arrive before, after, or concurrently with the associated cashflow, including after withdrawal or failure.

## Required Scenarios

The draft design requires the system to handle:

- A notification received before the cashflow.
- Multiple notifications that change the fixing flag over time.
- A notification received after withdrawal, while preserving cancellation.
- A notification received after `failed` or `techfailed`, enabling reinstatement.
- A cashflow and notification arriving at approximately the same time.

The expected results imply eventual convergence on the latest valid fixing information, while preserving terminal business states such as cancellation.

## Missing Precedence Controls

The source does not identify:

- A sequence number or event version.
- The authoritative event timestamp.
- An ordering key or partitioning strategy.
- An idempotency key.
- Duplicate-detection behavior.
- Optimistic-locking or atomic-update requirements.
- Late-event handling.
- Rules for repeated notifications after re-queueing or reinstatement.

These controls are necessary before concurrent and out-of-order processing can be implemented safely.

## Cancellation and Failure Precedence

Cancellation should prevent re-queueing or reinstatement, but Case 3 indicates that the latest fixing flag can still be persisted and displayed. By contrast, `failed` and `techfailed` cashflows may be reinstated after a new notification. The precise precedence rules remain open.

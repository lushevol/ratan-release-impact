---
type: query
title: What Are the Atomicity, Idempotency, and Event-Ordering Rules for FXU Settlement-Method Stamping?
created: 2026-08-24
updated: 2026-08-24
tags: [fxu, settlement-method, atomicity, idempotency, event-ordering]
related: [utilization-service, gross-util-settlement-method-transition, cashflow-settlement-method-event-consistency, past-due-accounting-reversal]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FXU Technical Design/Draft Design For Phase2.md"]
---
# What Are the Atomicity, Idempotency, and Event-Ordering Rules for FXU Settlement-Method Stamping?

The draft proposes per-trade results for a batch settlement-method endpoint but does not define whether changes are atomic per cashflow, per trade, or across the batch.

It also omits duplicate-request behavior despite DLQ redelivery for utilization processing. The required contract should establish:

- The idempotency key or natural deduplication key.
- The result returned for repeated manual-stamping requests.
- Whether a trade's listed cashflows succeed or fail as one unit.
- The ordering of settlement-method updates, `New`, `Withdrawal`, utilization, and past-due reversal events.
- The source of truth for the latest `New` event under delayed or out-of-order delivery.
- Compensating behavior when a settlement-method update and accounting reversal do not both complete.

This query extends the lifecycle concerns in [[what-is-the-authoritative-current-and-history-lifecycle-for-cashflow-data]] and identity concerns in [[what-is-the-canonical-cashflow-data-identity-and-version-key]].
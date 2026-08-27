---
type: query
title: How Are Razor Cashflow Status Change Events Deduplicated, Ordered, and Applied?
tags: [cashflow, razor, idempotency, ordering, versioning, replay]
related: [razor, fx-cashflow-status-write-back, cashflow-status-change-event-contract, cashflow-version-tuple-comparison, what-is-the-canonical-cashflow-data-identity-and-version-key]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FX Replication Status Write Back.md"]
---
# How Are Razor Cashflow Status Change Events Deduplicated, Ordered, and Applied?

The sample supplies Razor `cashflowId`, trade `linkId`, tracking ID, and a scalar version-like `id`, but does not define recipient matching, uniqueness, sequencing, or stale-event handling.

Clarify:

- the authoritative identity key and any composite-key requirement;
- the meaning and comparison policy for `scb:id`;
- treatment of duplicate, missing, lower-version, and out-of-order events;
- whether `Insert` causes event insertion, status-history insertion, current-state update, or another action;
- valid state transitions, including `isPaymentReversal=true`; and
- replay, dead-letter, and reconciliation behavior.

These rules are required before a `Settled` event can be safely projected into a current-state or notification model.
---
type: query
title: How Does RATAN Prevent Stale or Ambiguous Razor Events from Updating the Wrong Stella Cashflow Version?
tags: [versioning, idempotency, concurrency, matching, fx, ratan, razor, stella]
related: [six-economic-field-cashflow-matching, fx-cashflow-status-write-back, cashflow-event-versioning, cashflow-amendment-supersession, ratan, razor, stella]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/FX Cashflow Status Write Back - Razor to Stella.md"]
---
# How Does RATAN Prevent Stale or Ambiguous Razor Events from Updating the Wrong Stella Cashflow Version?

Razor does not supply a trade version. The requirement therefore maps each eligible Razor event to the latest Stella cashflow version using six economic fields. This approach can update an incorrect version when events are delayed, out of order, or economically ambiguous.

The persistence layout includes a `version` field described as optimistic locking, but does not define transactional, uniqueness, concurrency, or rollback behavior.

## Questions to resolve

- How is “latest” determined at matching time, and is that selection transactionally protected?
- What happens when multiple latest-version candidate cashflows have the same six-field tuple?
- How are late Razor events distinguished from current-version events?
- What unique constraint or idempotency mechanism prevents concurrent successful processing of the same Razor cashflow ID?
- How does a `Correction` event interact with an already processed or `SUSPENDED-MATURED` Stella cashflow?
- Can RATAN reverse or remediate a status applied to the wrong Stella version?
- What audit trail links each Razor event, candidate set, match decision, write-back request, and Stella response?

A complete answer is required to assess whether the design's latest-version matching can safely support its duplicate-payment objective.
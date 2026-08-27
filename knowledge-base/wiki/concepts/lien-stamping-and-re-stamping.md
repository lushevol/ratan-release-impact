---
type: concept
title: LIEN Stamping and Re-stamping
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, lien, stamping, lifecycle, data-consistency]
related: [lien, pending-fixing-flag-processing, lifecycle-service, netting-service, scbml, cashflow-status-change-event-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/LIEN Processing & Pending Fixing Flag Technical Design.md"]
---
# LIEN Stamping and Re-stamping

## Definition

**LIEN stamping** writes the current LIEN amount onto the cashflow, apparently in its SCBML representation. **LIEN re-stamping** refreshes that value after a lifecycle transition or other event where the previously recorded amount may no longer be current.

## Proposed lifecycle behavior

The source proposes attempting re-stamping whenever the target status is `QUEUED`. Relevant transitions include:

- `PROJECTED` to `QUEUED` through auto-materialization.
- `QUEUED + TechFail` through reinstatement.
- `WAITING + Pending Netting` or `WAITING + Pending AnotherLeg` through netting or reversion to `QUEUED`.
- `WAITING + Pending Exception` through reversion to `QUEUED` or `READY`.
- `CASHFLOW_SUPPRESSED` through unsuppression.
- `SWIFT_SUPPRESSED` through manual unsuppression or approval.
- `READY + NA + NA` through reversion to `QUEUED`.
- `NETTED` through un-netting.

The action and destination for `WAITING + Pending Fixing` are not specified.

## Resultant-generation behavior

During resultant generation, `ratan-cash-settlement-netting-service` should query LIEN amounts for each component before generation and use the LIEN amount from component 2. This is a late-refresh requirement intended to avoid generating a resultant from a stale LIEN value.

## Reliability questions

The source does not specify:

- Whether stamping occurs before or after the status transition.
- Whether status change and stamping share a transaction.
- How API latency, timeouts, and unavailable LIEN data are handled.
- Whether retries are idempotent.
- How concurrent lifecycle updates are serialized.
- Whether duplicate Trade Event Notifications are deduplicated.
- Whether an unchanged LIEN value should generate an event.

These gaps should be resolved before this concept is used as an implementation contract.

## Related concepts

This concept intersects with [[concepts/fixing-flag-notification-processing]], [[concepts/fixing-notification-event-ordering]], and [[concepts/cash-settlement-exception-handling]].
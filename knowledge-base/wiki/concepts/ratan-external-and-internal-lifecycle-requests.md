---
type: concept
title: RATAN External and Internal Lifecycle Requests
tags: [ratan, cashflow, lifecycle, api, event-processing]
related: [ratan-cashflow-lifecycle-state-machine, cashflow-lifecycle-versioning, ratan, stella, murex-2-11, scbml]
created: 2026-08-22
updated: 2026-08-22
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/LifeCycle/Status Machine.md"]
---
# RATAN External and Internal Lifecycle Requests

The lifecycle design separates upstream external requests from RATAN-originated internal requests.

## External requests

External requests originate from [[stella]] or [[murex-2-11]] and are intended for STP processing only.

They are admitted for:

- `PROJECTED` cashflows with `New`, `Amendment`, or `Withdrawal`.
- `RELEASED`, `SETTLED`, or `NETTED` cashflows with `Withdrawal` or `Withdrawal & New`.

An external request includes cashflow ID, Business Version, Cashflow Version, and action. It updates Business Version, Cashflow Version, and Minor Version.

## Internal requests

Internal requests originate within [[ratan]] for STP or manual actions, including stamping operations. They include cashflow ID, Minor Version, and action. They do not change Business Version or Cashflow Version.

Lifecycle status-update responses return previous and next cashflow status indexes, including the applicable Minor Version. Event payloads use a `Cashflow` aggregate and documented event types such as `CashflowCreationEvent`, `CashflowAmendEvent`, and `CashflowStatusUpdateEvent`.

The source specifies interface shapes and intended admission rules but does not define rejection, idempotency, or conflict-resolution behavior for invalid versions. See [[cashflow-lifecycle-versioning]].
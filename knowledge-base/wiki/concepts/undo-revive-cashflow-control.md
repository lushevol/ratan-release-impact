---
type: concept
title: Undo Revive Cashflow Control
tags: [cashflow, undo, revive, duplicate-payment-risk, lifecycle-control, settlement-control]
related: [ratan, stella, fmsre, cashflow-event-control, released-settled-amendment-control, cashflow-netting-and-auto-un-netting]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade & Cashflow Events Control/Cashflow Events Control.md"]
---
# Undo Revive Cashflow Control

Undo/Revive control governs the reinstatement of cashflows after withdrawals, termination, or expiry. It is a high-risk control because a revived cashflow can duplicate an original payment or conflict with an already settled reversal.

## Permitted outcomes

- If an original cashflow was not released or settled, a revive may restore it to a live lifecycle and submit it to normal STP/NSTP evaluation.
- If the original payment was released but its cancellation is not yet released, the cancellation may be ignored and the original may remain released.
- Where a prior cashflow was settled and the reversal remains in `WAITING`, examples propose copying the historical settled status to version 3. The source marks this as additional development work.
- For a netted cashflow with a pending acknowledgement, examples propose restoring component `NETTED` state and the resultant `READY_PendingACK` state without creating a new resultant.

## Prohibited and exceptional outcomes

When cancellation messages such as MT192 or MT292 are settled, FO and MO should be blocked from performing Undo in Blade/Stella. If an unexpected revive still arrives, Ratan should block it or hold the new cashflow in an exception state. Operations may inspect payment outcomes in [[fmsre]] before deciding on an exceptional rebook.

## Risk

The source explicitly identifies duplicate-payment risk, including a netted Undo scenario that could create a duplicate payment. State copying, rebook creation, exception routing, and event blocking are not unified into one approved algorithm.

Expiry is an exception: both expiry and its revive events are discarded as non-economic.

See [[what-is-the-authoritative-ratan-undo-revive-state-restoration-policy]].
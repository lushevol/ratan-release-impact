---
type: query
title: What Is the Authoritative Ratan Undo Revive State Restoration Policy?
tags: [ratan, undo, revive, lifecycle-state, duplicate-payment-risk]
related: [undo-revive-cashflow-control, cashflow-lifecycle-state-model, cashflow-version-concurrency-control, fmsre]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade & Cashflow Events Control/Cashflow Events Control.md"]
---
# What Is the Authoritative Ratan Undo Revive State Restoration Policy?

The source presents several incompatible or incomplete revival outcomes: normal lifecycle restart, restoration of historical `SETTLED` state, restoration of `NETTED` and `READY_PendingACK` state, exceptional rebooking, and complete event blocking.

## Questions to resolve

- Under which exact prior states may a revived version inherit `SETTLED`, `NETTED`, or `READY_PendingACK`?
- Is state copying permitted only while the cancellation/reversal is unexecuted?
- What idempotency and audit evidence are required before state restoration?
- What exception and approval path applies when MT192/MT292 was released or settled?
- How does Ratan prevent a second payment when netted resultants and revive messages overlap?

The source marks several proposed behaviours as requiring additional development and UAT verification.
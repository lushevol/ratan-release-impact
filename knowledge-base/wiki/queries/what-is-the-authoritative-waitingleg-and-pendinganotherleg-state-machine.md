---
type: query
title: What Is the Authoritative WaitingLeg and PendingAnotherLeg State Machine?
tags: [cashflow, lifecycle, state-machine, waiting-state, irs]
related: [irs-counterpart-leg-matching, irs-cashflow-processing, lifecycle-service, pending-fixing-and-waiting-another-leg, fixing-flag-notification-processing]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/IRS Cashflow Processing Design.md"]
---
# What Is the Authoritative WaitingLeg and PendingAnotherLeg State Machine?

The IRS design states that `WaitingLeg` changes a cashflow from `QUEUED` to `WAITING + PendingAnotherLeg`. Existing wiki material also uses related `WaitingAnotherLeg` terminology in a fixing-notification context.

## Questions to Resolve

- Are `PendingAnotherLeg` and `WaitingAnotherLeg` identical canonical values, aliases, or separate domain states?
- Is `WaitingLeg` the canonical action name for the stated `QUEUED` to `WAITING` transition?
- Which transitions enter and exit this state?
- Which service owns validation and persistence of the transition?
- Can an already waiting cashflow be retried, cancelled, reinstated, or netted?
- Does IRS counterpart-leg coordination share a state machine with fixing-notification processing?

The cited source supports only the stated transition for the IRS design; it does not resolve these questions.
---
type: query
title: What Is the Canonical UnHold and Suppression Reject Behavior?
tags: [ratan, lifecycle, hold, suppression, maker-checker]
related: [ratan-cashflow-lifecycle-state-machine, cashflow-hold-unhold, swift-versus-cashflow-suppression, cashflow-suppression-rules]
created: 2026-08-22
updated: 2026-08-22
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/LifeCycle/Status Machine.md"]
---
# What Is the Canonical UnHold and Suppression Reject Behavior?

The transition matrix leaves the target state undefined for:

- `HOLD / Pending Verification / NA` with action `UnHold`.
- `WAITING / Pending Verification / Cashflow Suppression` with action `Reject`.
- `WAITING / Pending Verification / Undo Cashflow Suppression` with action `Reject`.
- `WAITING / Pending Verification / Swift Suppression` with action `Reject`.
- `WAITING / Pending Verification / Undo Swift Suppression` with action `Reject`.

The requirements use `NA` for every target-state field in these cases. The intended restoration behavior must be specified rather than inferred, because possible outcomes include restoring a previous state, returning to `QUEUED`, retaining workflow state, or applying conditional routing.
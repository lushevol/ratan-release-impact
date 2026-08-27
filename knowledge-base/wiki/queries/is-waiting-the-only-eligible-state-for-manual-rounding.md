---
type: query
title: Is WAITING the Only Eligible State for Manual Rounding?
created: 2026-08-23
updated: 2026-08-23
tags: [manual-rounding, cashflow-lifecycle, waiting, settlement]
related: [manual-cashflow-rounding, cashflow-amendment-maker-checker-control]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Manual Rounding.md"]
---
# Is WAITING the Only Eligible State for Manual Rounding?

The requirement asks whether the cashflow state for Manual Rounding is `WAITING`. It does not confirm whether `WAITING` is the only permitted state or merely the expected state at the time of adjustment.

## Investigation scope

Confirm eligibility for cashflows that are:

- in `WAITING`;
- released or already sent to downstream processing;
- netted or split;
- subject to another pending amendment;
- cancelled, failed, or otherwise non-payable.

The answer should identify the lifecycle owner and define the state transition, locking behavior, and treatment of a cashflow whose state changes while maker/checker approval is pending.

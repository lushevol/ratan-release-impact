---
type: concept
title: Cashflow HOLD/UNHOLD Authorization
tags: [cashflow, hold, unhold, authorization, maker-checker, operations-controls]
related: [cashflow-hold-and-unhold, ratan, suppression-maker-checker-workflow, swift-value-date-maker-checker-control, fmo-ops, how-are-unhold-authorization-limits-calculated-for-non-usd-and-bulk-cashflows]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Hold UnHold.md"]
---
# Cashflow HOLD/UNHOLD Authorization

The HOLD/UNHOLD requirement separates visibility, role eligibility, segregation of duties, and monetary authority for Ratan cashflows.

## HOLD permissions

HOLD is available to all users regardless of operations-profile access. Both Maker and Checker users may apply HOLD. The requirement specifies no amount-limit validation for HOLD.

## UNHOLD permissions

UNHOLD is limited to Checker users with operations profiles `BOC`, `BO`, `BOL`, or `BOM`.

`FMO_OPS_MKR` is explicitly prohibited from UNHOLD and must not see the UNHOLD button. A user who applied HOLD to a given cashflow cannot UNHOLD that same cashflow, even if otherwise eligible.

This is a maker/checker control aligned in purpose with [[suppression-maker-checker-workflow]], but applies specifically to restoration from `HOLD`.

## Amount authorization

An eligible user can see the UNHOLD button, but completion requires a cashflow amount below that user's profile USD operation limit. The requirement example denies a user under profile `BOC` with an allowed amount of 100 from UNHOLDing a cashflow of amount 1000.

The source does not define the amount basis, whether “below” is strict or inclusive, how non-USD amounts are converted, or how mixed-eligibility rows behave in bulk submissions. These questions are tracked in [[how-are-unhold-authorization-limits-calculated-for-non-usd-and-bulk-cashflows]].
---
type: concept
title: Forward-Trade UTIL Stamping
tags: [forward-trades, UTIL, utilization, cashflow-materialization, EBBS]
related: [fxu, ratan, ebbs, value-date-based-cashflow-materialization, cashflow-status-lifecycle, cashflow-accounting-eligibility, cashflow-accounting-stamping]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/FXU - RATAN analysis/Dependencies for expansion to other Markets.md"]
---
# Forward-Trade UTIL Stamping

Forward-trade UTIL stamping is the requirement to represent a trade as utilized even when its future cashflows have not yet materialized.

## Timing model

The source describes a utilization window for forward trades:

1. If utilization occurs within the window, RATAN moves the trade status to `Utilized`.
2. The EBBS accounting entry is not passed immediately.
3. The EBBS entry is passed on value date.

This means that `Utilized` status in RATAN must not automatically be interpreted as eligibility for immediate EBBS accounting feed.

## Model implications

The design must distinguish:

- Trade utilization status.
- Cashflow materialization status.
- Cashflow-level UTIL stamping.
- EBBS accounting-feed eligibility and timing.

The requirement may extend or challenge assumptions in [[concepts/value-date-based-cashflow-materialization]] and should be reconciled with [[concepts/cashflow-accounting-eligibility]] and [[concepts/cashflow-accounting-stamping]].
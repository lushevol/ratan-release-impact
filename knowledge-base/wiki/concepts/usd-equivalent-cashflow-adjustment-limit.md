---
type: concept
title: USD-Equivalent Cashflow Adjustment Limit
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, fx, authorization, financial-control, manual-rounding]
related: [manual-cashflow-rounding, cashflow-amendment-maker-checker-control]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Manual Rounding.md"]
---
# USD-Equivalent Cashflow Adjustment Limit

The USD-Equivalent Cashflow Adjustment Limit is the proposed control that keeps a Manual Rounding increase or decrease below USD 1 when converted using an exchange rate from upstream.

The source refers to the existing authorization-limit process as the model for this validation. It does not identify the upstream system, rate type, rate timestamp, precision, fallback behavior, or conversion direction.

## Unresolved semantics

The requirement does not establish:

- whether the comparison is strictly `< USD 1.00` or allows `≤ USD 1.00`;
- whether the absolute value of the delta is tested;
- whether multiple adjustments are evaluated cumulatively;
- whether the control is applied at maker entry, checker approval, or both;
- how USD-denominated cashflows and non-USD currencies are handled;
- how FX rounding affects the threshold decision.

These details are necessary before the control can be implemented or tested reliably.

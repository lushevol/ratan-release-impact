---
type: concept
title: Cashflow Remaining Amount
tags: [cash-settlement, cashflow, amount, blotter]
related: [ratan, cashflow-blotter, trade-to-cashflow-navigation, what-is-the-authoritative-fxu-remaining-amount-calculation, which-ratan-data-source-populates-remaining-amount]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FXU Technical Design/FXU Remaining Amount via OpenFin.md"]
---
# Cashflow Remaining Amount

Cashflow remaining amount is a user-visible value displayed for cashflows in the [[cashflow-blotter]] after a user navigates from [[blade]] to [[ratan]].

## Observed behavior

The source demonstrates that cashflows for a selected trade are displayed with a remaining amount.

## Unresolved semantics

The source does not define:

- The formula or source fields used to determine the amount.
- Whether it is persisted, calculated at read time, or supplied by another system.
- Currency, precision, rounding, sign, and null-value conventions.
- Treatment of partial settlements, cancellations, amendments, or multiple settlement events.
- Whether the value is cashflow-level, trade-level, currency-level, or settlement-level.

The display behavior must not be interpreted as evidence of calculation correctness. The definition and provenance remain open in [[what-is-the-authoritative-fxu-remaining-amount-calculation]] and [[which-ratan-data-source-populates-remaining-amount]].
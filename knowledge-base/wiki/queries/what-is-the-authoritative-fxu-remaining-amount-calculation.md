---
type: query
title: What Is the Authoritative FXU Remaining Amount Calculation?
tags: [fxu, cashflow, remaining-amount, business-rules]
related: [cashflow-remaining-amount, ratan, cashflow-blotter]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FXU Technical Design/FXU Remaining Amount via OpenFin.md"]
---
# What Is the Authoritative FXU Remaining Amount Calculation?

The documented workflow shows a remaining amount in the Ratan cashflow blotter but supplies no calculation definition.

## Questions to resolve

- Which fields and business rules determine remaining amount?
- Is it original amount less settled amount, and if so, which settlement states are included?
- How are partial settlements, amendments, cancellations, reversals, and multiple currencies handled?
- What precision, rounding, sign, and null-value rules apply?
- Is the value defined at cashflow, trade, currency, or settlement level?

## Current evidence

[[fxu-remaining-amount-via-openfin]] confirms display behavior only. It does not provide formula, reconciliation, or test evidence.
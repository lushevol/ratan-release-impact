---
type: concept
title: Cashflow Payment Amount Canonicalization
created: 2026-08-24
updated: 2026-08-24
tags: [cashflow, payment-amount, settlement, swift, accounting, data-contract]
related: [automated-cashflow-rounding, ratan, settlement-accounting, cash-settlement-home-page, what-is-the-authoritative-cashflow-rounding-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/Rounding Rule - Tactical solution for H1 2024 Cashflow Migration.md"]
---
# Cashflow Payment Amount Canonicalization

`Cashflow.Payment_Amount` is the canonical post-rounding amount for the settlement process described in the source.

After [[automated-cashflow-rounding]] in [[ratan]], this field is the only amount available downstream. It is used for:

- GUI display in [[cash-settlement-home-page]].
- SWIFT-message generation.
- Accounting generation, including [[settlement-accounting]] processing.

This contract prevents downstream consumers from independently selecting an original amount or applying different rounding behavior.

## Representation uncertainty

The source requires removal of trailing zeros, such as representing rounded `3.10` as `3.1`. It does not state whether `Cashflow.Payment_Amount` is persisted as a numeric value with display formatting or as formatted text. Interface and audit implications remain open in [[what-is-the-authoritative-cashflow-rounding-contract]].
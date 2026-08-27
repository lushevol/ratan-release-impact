---
type: concept
title: FMRP Payment Eligibility and Suppression
created: 2026-08-24
updated: 2026-08-24
tags: [FMRP, eligibility, suppression, payment-flow, static-data]
related: [fmrp, cashflow-suppression-rules, precious-metal-cashflow-vostro-requirement, netting-eligibility-static-data, is-fmrp-cpt-eligibility-logic-inverted]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Murex 2.11 workflow change.md"]
---
# FMRP Payment Eligibility and Suppression

FMRP insertion uses layered filters before an eligible payment flow is published to RATAN.

## Static-data filters

A flow is discarded when:

1. Its entity is not present in `FMRP_ENTITY_DBF`.
2. Its currency has `M_NDF_CCY='Y'` in `CURRENCY_DBF`.
3. Its amount is exactly zero.

The entity formula derives the payment entity from `client.scb.pay.flow.entity`. The currency formula derives the currency from `MxPayML/currency`.

## Trade-related filters

When `tradePaymentCheck='Y'`, the flow is discarded if any of the following returns `Y`:

- `isPreciousMetalDealFlow`
- `fxdSupprission`
- `isCPT`

The precious-metal check examines currency fields associated with the trade. The FXD check permits only the configured subset, including `FEDSVALIDATOR`, qualifying `FX_DCD`, `NDF`, `NDS Fixing`, and `INTL/%` counterparty cases.

## CPT ambiguity

`cptCheck` searches family-specific deal-comment fields for the literal value `fmrp_test`. `isCPT` returns `Y` when the query returns zero rows, and the insertion filter discards when the result is `Y`. Therefore, the literal implementation suppresses flows with no matching `fmrp_test` record. It is unresolved whether this is intentional or inverted; see [[queries/is-fmrp-cpt-eligibility-logic-inverted]].

These rules are specific to the FMRP workflow and should not automatically be generalized to all cash-settlement routes.
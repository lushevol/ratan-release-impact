---
type: source
title: Draft Product-Agnostic Aggregation Based on Normalized Payment Schedule
created: 2026-08-29
updated: 2026-08-29
tags: [cash-settlement, netting, auto-aggregation, normalized-payment-schedule, draft]
related: [product-agnostic-cashflow-aggregation, normalized-payment-schedule, normalized-payment-schedule-completeness-check, entities/fmrp-flow]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/[Draft] Auto Aggregation based on Normalized Payment Schedule.md"]
---
# Draft Product-Agnostic Aggregation Based on Normalized Payment Schedule

## Purpose

This draft proposes replacing taxonomy-specific aggregation with a product-agnostic approach driven by the normalized payment schedule. It is intended to cover cashflow structures that the existing IRS and CCS auto-netting supplements do not support.

## Business drivers

- Same-trade cashflow aggregation exists in Murex 2.11 but is not implemented in the FMRP Flow cashflow generator, Stella.
- RATAN's existing IRS Netting and CCS Auto Netting behavior is limited to selected taxonomies.
- New taxonomies, including `InterestRate:LoanDeposit`, broaden the required aggregation scope.
- Some IRS trades contain multiple cashflows in the second leg, which the existing IRS Netting model does not support.

The proposed direction is therefore [[concepts/product-agnostic-cashflow-aggregation]] based on an upstream normalized payment schedule rather than product-specific rules.

## Evidence and limitations

The source points to ADO Story `14618546` for the requirement and Story `15005868` for the multi-cashflow IRS example. Detailed happy, negative, and historical-data cases are held in an attached workbook and screenshots that are not present in the raw export.

This page is evidence of a draft direction, not a complete behavioral contract. Eligibility keys, completeness checks, exception handling, historical-data behavior, and rollout rules remain unresolved in the available Markdown source.

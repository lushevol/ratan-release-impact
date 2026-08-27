---
type: concept
title: CCIL Netting Eligibility Key
created: 2026-08-23
updated: 2026-08-23
tags: [ccil, netting, eligibility, validation, cashflow]
related: [ccil-manual-netting, netting-static-blotter, bulk-cashflow-selection-homogeneity]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Business User Case/02 CCIL Netting.md"]
---
# CCIL Netting Eligibility Key

The CCIL acceptance cases require selected cashflows to share the same booking entity, currency, and value date. A selected cohort with different values in any of these dimensions must fail CCIL netting validation.

The source also repeatedly qualifies active CCIL scenarios with counterparty FMID not equal to `400021949`.

## Expected Eligible State

When a live manual rule applies, qualifying components are expected to have:

- Cashflow state: `WAITING`
- Cashflow sub-state: `Pending Netting`

## Validation Limitation

The specified popup wording is:

> Validation failed ,Cash flow selected are not eligible for netting as either the same booking entity, value date,currency .

The wording appears inverted and should not be treated as authoritative UI copy. The scenario itself makes the intended common-key requirement clear.

The source does not establish whether additional eligibility-key fields apply.
---
type: query
title: How Should Malformed FMRP Action Matrix Rows Be Interpreted?
created: 2026-08-22
updated: 2026-08-22
tags: [fmrp, action-eligibility, requirements-ambiguity, data-quality]
related: [cashflow-blotter-action-eligibility, cashflow-failure-and-reinstatement]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Cashflow Blotter/User Actions on Cashflow Blotter.md"]
---
# How Should Malformed FMRP Action Matrix Rows Be Interpreted?

Rows 3, 5, 16, 21, 26, 40, and 41 appear to be continuation clauses but are structurally presented as standalone rows. This affects ReInstate, Settle As Gross, Suppress Cashflow, Manual Fail, CCIL netting, and Settlement Method Update interpretation.

Obtain or reconstruct an authoritative matrix with each condition assigned to a named action before implementation or test-case derivation.
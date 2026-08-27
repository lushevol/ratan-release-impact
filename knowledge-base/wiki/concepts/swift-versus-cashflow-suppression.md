---
type: concept
title: SWIFT versus Cashflow Suppression
created: 2026-08-22
updated: 2026-08-22
tags: [suppression, swift, settlement-accounting, maker-checker]
related: [cashflow-suppression, cashflow-suppression-rules, maker-checker-settlement-control, amh, oscar]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Cashflow Blotter/User Actions on Cashflow Blotter.md"]
---
# SWIFT versus Cashflow Suppression

The FMRP requirements distinguish two controlled suppression workflows.

- **SWIFT suppression** applies when payment is not required. Maker initiation changes the cashflow to `WAITING` with sub-state type `Swift Suppression` and `Pending Verification`; checker approval produces `SWIFT_SUPPRESSED`.
- **Cashflow suppression** applies when both payment and settlement accounting are not required. Maker initiation creates `Cashflow Suppression` pending verification; checker approval produces `CASHFLOW_SUPPRESSED`.

Both workflows may be reversed only until value date. A post-value-date payment need after SWIFT suppression must be handled through [[amh]] / [[oscar]]. A post-value-date need for both payment and accounting after full cashflow suppression must be handled through [[oscar]].

This distinction is functional-requirements evidence and should not be treated as confirmation of accounting implementation.
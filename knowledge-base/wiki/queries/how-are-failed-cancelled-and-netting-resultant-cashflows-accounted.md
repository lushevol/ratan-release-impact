---
type: query
title: How Are Failed, Cancelled, and Netting-Resultant Cashflows Accounted?
created: 2026-08-23
updated: 2026-08-23
tags: [open-question, failed-cashflow, cancellation, netting, accounting, settlement]
related: [failed-cashflow-accounting, cashflow-withdrawal-and-new, cashflow-netting-and-un-netting-state-transitions, reversal-and-correction-cashflow-processing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Failed Process/Failed Cashflow Accounting.md"]
---

# How Are Failed, Cancelled, and Netting-Resultant Cashflows Accounted?

## Question

How should the process account for failed cashflows that are cancelled, are netting resultants, or were settled on Value Date and later amended before failing?

## Cases Identified by the Source

- `FAILED` followed by trade cancellation.
- `FAILED` on a netting-resultant cashflow.
- Settled on Value Date, followed by a trade amendment on VD+1 and then a failure.
- Past Value Date booking.

## Why It Matters

These cases may require different reversal, withdrawal, replacement, or component-level accounting behavior. In particular, a netting resultant may require rules for both the resultant and its underlying cashflows.

## Current Position

No authoritative behavior is specified. The cases should remain open until accounting, netting, cancellation, and post-settlement correction rules are confirmed.
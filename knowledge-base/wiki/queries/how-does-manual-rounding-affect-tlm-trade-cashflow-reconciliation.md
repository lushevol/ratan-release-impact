---
type: query
title: How Does Manual Rounding Affect TLM Trade/Cashflow Reconciliation?
created: 2026-08-23
updated: 2026-08-23
tags: [manual-rounding, reconciliation, trade, cashflow, tlm]
related: [manual-cashflow-rounding, tlm]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Manual Rounding.md"]
---
# How Does Manual Rounding Affect TLM Trade/Cashflow Reconciliation?

The requirement identifies a possible break between the trade and cashflow when the payment amount is manually adjusted. It calls for alignment with the Recon team and asks whether TLM should check the break.

## Required resolution

Confirm whether TLM is the authoritative reconciliation system, whether it compares original or updated amounts, and whether the USD-equivalent threshold is also a permitted reconciliation tolerance.

The investigation should define how an expected rounding difference is recorded, surfaced, matched, overridden, and reported, together with ownership of unresolved breaks.

---
type: query
title: How Are PROJECTED IRS Fixed-Leg Cashflows Netted with Later Floating Legs?
created: 2026-08-22
updated: 2026-08-22
tags: [irs, projected-cashflow, netting, settlement, ratan]
related: [irs-fix-leg-floating-leg-netting, ratan-netting-rule-check, ratan, murex-cashflow-status-lifecycle]
sources: ["RATAN - 51358/RATAN/RATAN -Core Function/RATAN-Settlement  4_Netting Rule Check.md"]
---
# How Are PROJECTED IRS Fixed-Leg Cashflows Netted with Later Floating Legs?

The source states that IRS fixed-leg cashflows can arrive in RATAN in `PROJECTED` status before the corresponding floating-leg payment is generated, normally on VD-2. It also states the expectation to settle both legs as a net amount per schedule.

## Questions to resolve

- Can a `PROJECTED` fixed-leg cashflow enter a netting set before the floating leg arrives?
- Which identifier defines the fixed-leg and floating-leg schedule relationship?
- What event re-evaluates the netting set after floating-rate fixing?
- How are late, amended, cancelled, or failed component cashflows handled?
- Is the status lifecycle specific to RATAN, an upstream booking system, or both?

Authoritative lifecycle and event-processing documentation is required.
---
type: concept
title: IRS Fix-Leg and Floating-Leg Netting
created: 2026-08-22
updated: 2026-08-22
tags: [irs, settlement, netting, projected-cashflow, floating-rate]
related: [ratan, ratan-netting-rule-check, murex-cashflow-status-lifecycle, irs-projected-cashflow-netting-timing]
sources: ["RATAN - 51358/RATAN/RATAN -Core Function/RATAN-Settlement  4_Netting Rule Check.md"]
---
# IRS Fix-Leg and Floating-Leg Netting

IRS fix-leg and floating-leg netting describes the settlement expectation that fixed-leg and floating-leg payments are settled as a net amount for each schedule.

According to the available source, IRS trades booked through Blade or Stella can produce fixed-leg cashflows in advance because the fixed rate is known. These cashflows may arrive in RATAN in `PROJECTED` status. The corresponding floating-leg payment is generated when the floating rate is fixed, normally on VD-2.

## Unresolved processing behavior

The source describes the business expectation but does not specify:

- whether a `PROJECTED` fixed-leg cashflow is eligible for netting before its floating leg exists;
- the grouping key for a schedule;
- the event that triggers re-evaluation after the floating-leg arrival; or
- amendment, cancellation, failure, and delay handling.

These timing and eligibility questions are tracked in [[irs-projected-cashflow-netting-timing]].
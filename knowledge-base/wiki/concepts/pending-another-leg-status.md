---
type: concept
title: Pending Another Leg Status
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow-status, WAITING, IRS, pending-fixing, netting]
related: [irs-fixed-floating-leg-netting, murex-pending-fixing-flag-processing, cashflow-netting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/IRS Fix Leg & Floating leg payment handling.md"]
---
# Pending Another Leg Status

`Pending Another Leg` is a `WAITING` sub-status used to prevent an IRS coupon from progressing while RATAN expects a corresponding leg for the same payment schedule.

For Murex cashflows, the stated entry condition is an eligible non-withdrawal cashflow with `pending_fixing flag='Y'`. For Stella cashflows, entry depends on IRS taxonomy, fixed or floating coupon type, a non-withdrawal event, and a TDX/TDSX-based expected-leg check.

The status is a workflow control rather than an absolute netting prohibition. The source explicitly permits an operator to manually net an IRS fixed leg in `WAITING` / `Pending Another Leg` with CDS cashflows. The later treatment of that manually netted resultant when the floating leg arrives is unspecified.

A separate `Fixing Unknown` NSTP exception is used for provisional Murex `X` values. It is not equivalent to `Pending Another Leg`; a later `FMRP_MUREX_FIX_FLAG` update determines whether the cashflow moves to `Pending Another Leg` or resumes STP processing.
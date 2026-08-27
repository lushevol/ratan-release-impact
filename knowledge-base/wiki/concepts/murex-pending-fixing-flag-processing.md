---
type: concept
title: Murex Pending-Fixing Flag Processing
created: 2026-08-23
updated: 2026-08-23
tags: [Murex, pending-fixing, Fixing-Unknown, NSTP, IRS]
related: [murex, pending-another-leg-status, irs-fixed-floating-leg-netting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/IRS Fix Leg & Floating leg payment handling.md"]
---
# Murex Pending-Fixing Flag Processing

Murex pending-fixing flag processing controls whether an IRS cashflow can continue through settlement processing or must wait for floating-leg resolution.

The functional requirement specifies these intended outcomes:

- `Y`: put the eligible cashflow in `WAITING` with `Pending Another Leg`.
- `N`: continue remaining STP checks.
- `X`: apply the `Fixing Unknown` NSTP rule and await an `FMRP_MUREX_FIX_FLAG` update.

The `X` pathway is described for UK and DE real-time delivery. It applies both to initial fixed-leg cashflows and to net resultants sent after floating-leg fixing. The later Murex file may resolve the condition to `Y` or `N`.

For CN, SG, IN, and MY real-time processing, the fixed leg is sent with `Y`; after fixing, Murex reverses the fixed leg and supplies the net cashflow. For UK and DE batch processing, direct batch delivery with `N` can proceed without the provisional exception flow.

The source does not formally define the semantic meaning or allowed domain of `X`, nor correlation, ordering, or duplicate-file controls for flag updates. See [[what-is-the-authoritative-meaning-of-murex-pending-fixing-values]] and [[what-is-the-fmrp-murex-fix-flag-file-correlation-and-retry-contract]].
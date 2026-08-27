---
type: concept
title: Murex 2.11 CN Derivative Settlement
created: 2026-08-23
updated: 2026-08-23
tags: [murex-2-11, china, derivatives, settlement, nstp]
related: [murex-2-11, fmrp, razor, opics, cn-settlement, murex-2-11-field-20-format, agency-payment-identification, pre-trade-settlement-accounting-exceptions, is-auto-split-in-scope-for-fmrp-cn-settlement]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/CN Settlement Ops weekly session/2022-11-16.md"]
---
# Murex 2.11 CN Derivative Settlement

Murex 2.11 CN derivative settlement is the operational process discussed for China derivative-product payments, SWIFT generation, payment splitting, and settlement exceptions.

## Scope Recorded in the Session

- Field 20 follows a reported, but unvalidated, legacy format.
- Agency-profile bookings may not be detected by portfolio-based payment identification.
- Field 72 may contain an agency-payment indicator.
- No auto split was identified as a Murex 2.11 derivative requirement.
- Manual splits are performed in [[opics]] at client request and have no parent-payment linkage.
- Missing Vostro or Nostro SSI is the principal reported payment-stage exception.
- Some `P2P` portfolios reportedly fail before payment creation because trade or settlement accounting is not generated.

## Boundary

[[razor]] provides a reference implementation for auto split and SWIFT Field 72 lineage, but its behavior must not be generalized to Murex 2.11 CN derivatives. Likewise, this concept does not establish behavior for RATAN or [[murex-korea]].

The reported `CN 150 as NSTP daily` figure is insufficiently defined for sizing or performance conclusions.
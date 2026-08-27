---
type: concept
title: Post-Settlement Amendment and Cancellation Handling
created: 2026-08-22
updated: 2026-08-22
tags: [murex, ratan, cashflow, amendment, cancellation, reversal, nstp]
related: [murex, ratan, mxml-to-scbml-conversion, released-resultant-amendment-handling, cashflow-netting-renetting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/Ratan MxML- SCBML Adaptor ( Entity CN, SG, IN, MY).md"]
---
# Post-Settlement Amendment and Cancellation Handling

The Murex 2.11–Ratan integration distinguishes post-settlement trade amendments from cancellations. Both may create a reversal, but their STP treatment differs.

## Amendment handling

For Cancel & Reissue, Restructure, or Modify events affecting a released or settled cashflow:

- Murex generates a reversal to offset the original cashflow and a rebook payment with updated economics.
- The reversal is identified through a comment beginning with `Reverse`.
- The reversal is treated as NSTP.
- Murex does not provide a direct marker for the rebook payment.
- The documented CN Day 1 proxy treats new payments with value dates within 30 days after the reversal as NSTP with a rebook rationale.
- Payments outside the 30-day window are treated as STP.

This is a heuristic rather than a deterministic linkage and may classify unrelated payments as rebooks.

## Cancellation handling

For trade cancellation or a similar event such as early termination:

- Murex generates a reversal;
- Ratan treats it as a withdrawal;
- the withdrawal is STP.

A cancellation reversal must not be assigned the amendment NSTP behavior solely because it is a reversal.

## Event indicators

| Amendment event | MxML attribute | Value |
|---|---|---|
| Cancel & Reissue | `/MxPayML/scbExtraInfoBlock/tradeLastMKT` | `RPL_M` |
| Restructure | `/MxPayML/scbExtraInfoBlock/tradeLastMKT` | `RPL` |
| Modify | `/MxPayML/scbExtraInfoBlock/action` | `MOD` |

The document does not establish a complete event taxonomy for cancellation or an authoritative method to link rebook payments to their reversal.
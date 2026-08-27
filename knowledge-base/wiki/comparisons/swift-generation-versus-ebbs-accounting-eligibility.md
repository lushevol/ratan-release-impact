---
type: comparison
title: SWIFT Generation Versus eBBS Accounting Eligibility
tags: [swift, ebbs, payment-accounting, settlement]
related: [ebbs-payment-accounting-integration, ebbs, ratan, failed-cashflow-accounting]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Payment Accounting/Cash Settlement - EBBS Accounting.md"]
---
# SWIFT Generation Versus eBBS Accounting Eligibility

The requirement treats SWIFT generation and eBBS accounting as related but separate decisions.

| Cashflow condition | SWIFT implication | Accounting implication |
|---|---|---|
| `SWIFT_SUPPRESSED` | No SWIFT message is generated. | Accounting may still be required on value date if Nostro data is available. |
| `CASHFLOW_SUPPRESSED` | Payment is suppressed. | No accounting is generated. |
| UK entity with payment currency in CIS external codes | SWIFT remains generated. | Accounting is suppressed. |
| `RELEASED` or `SETTLED` | SWIFT behavior depends on payment flow. | Accounting is eligible subject to timing and duplicate prevention. |
| `FAILED` | Payment has failed. | Accounting may still be generated, with different timing for manual and automatic failure. |

## Consequence

A payment can require accounting without a corresponding SWIFT message, and a payment can generate SWIFT while accounting is suppressed. Operational controls must therefore monitor both lifecycles rather than treating either one as a proxy for the other.
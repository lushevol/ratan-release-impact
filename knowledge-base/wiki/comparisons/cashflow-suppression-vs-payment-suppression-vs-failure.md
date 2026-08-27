---
type: comparison
title: Cashflow Suppression versus Payment Suppression versus Cashflow Failure
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, lifecycle-controls, suppression, payment-failure]
related: [cashflow-suppression-vs-payment-suppression, cashflow-fail-and-reinstatement, settlement-suppression-exceptions]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/MX2.11 Decomm - Cash Settlement Business Workflow/NSTP Workflow.md"]
---
# Cashflow Suppression versus Payment Suppression versus Cashflow Failure

| Control | Intended condition | Normal outcome | Manual control | After value date |
|---|---|---|---|---|
| Cashflow Suppression | Payment and settlement accounting are not required | Suppress the cashflow | Maker–Checker for manual suppression | Use Oscar if payment and accounting are required |
| Payment Suppression | Payment is not required | Suppress payment while other processing may remain relevant | Maker–Checker for manual suppression | Use AMH or Oscar if payment is required |
| Cashflow Failure | Payment is expected but cannot be processed on value date | Move cashflow to Failed for later payment | Maker or Checker may fail; Maker reinstatement requires Checker validation | AMH or Oscar handles failed settlements identified after value date |

Suppression represents an intentional decision not to perform a required activity. Failure represents an unsuccessful attempt or inability to process an activity that remains expected. The source does not define whether cashflow and payment suppression can coexist or establish status precedence for overlapping rules.

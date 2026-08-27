---
type: concept
title: Cashflow Fail and Reinstatement
created: 2026-08-22
updated: 2026-08-22
tags: [cashflow-failure, reinstatement, back-value-payment, payment-operations]
related: [cashflow-suppression-vs-payment-suppression, korea-mx-exception-replay-and-recovery, pending-reversal-acknowledgement]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/MX2.11 Decomm - Cash Settlement Business Workflow/NSTP Workflow.md"]
---
# Cashflow Fail and Reinstatement

Cashflow failure is used when payment remains expected but Operations cannot process the cashflow on value date, for example because instructions are missing or a payment is disputed.

RATAN should automatically move unreleased cashflows to Failed at end of day. Maker or Checker may also mark a cashflow Failed during the day. After value date, a Maker may reinstate a failed cashflow when Investigations confirms that it is good to pay; the reinstatement requires Checker validation.

Because reinstatement creates a back-value payment, both Maker and Checker must independently select the payment value date and agree on the choice. A cashflow already in RELEASED or SETTLED status cannot be manually failed, protecting against duplicate payment.

Failed settlements identified after value date from a Nostro statement are handled through [[entities/amh]] or [[entities/oscar]]. Trade amendments or cancellations create a new system version and lifecycle rather than modifying the prior failed lifecycle.

---
type: query
title: Which Currency Code Is Valid for Netting Eligibility?
created: 2026-08-22
updated: 2026-08-22
tags: [open-question, currency, netting-eligibility, data-quality]
related: [netting-eligibility-rule, client-level-cashflow-netting, fmrp-china-cash-settlement]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/FMRP China Cash Settlement Delivery Plan/2023 Q2 Demo 1 - FMRP China Cash Settlement Deliveries.md"]
---

# Which Currency Code Is Valid for Netting Eligibility?

## Question

Is `CNO` in the documented netting eligibility rule an intentional system-specific payment-currency code, or should it be `CNY`?

## Evidence

The rule lists:

```text
Cashflow.Payment_Currency IN CNO,USD
```

The test scenarios use `CNY` and `USD`, while one expected-result description refers to a `JPY` group. Because payment currency controls eligibility and grouping, this discrepancy affects interpretation of the demonstrated behavior.

## Required resolution

Confirm the valid code set with the system owner and reconcile the rule against the test dataset and application configuration. Do not replace `CNO` with `CNY` in the source record until the discrepancy is resolved.

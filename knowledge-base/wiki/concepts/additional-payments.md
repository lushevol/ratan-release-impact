---
type: concept
title: Additional Payments
created: 2026-08-22
updated: 2026-08-22
tags: [cashflows, payment-schedules, auto-aggregation, product-agnostic]
related: [schedule-to-cashflow-matching, normalized-payment-schedule, expected-payment-count-for-auto-netting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Product Agnostic model to identify all cashflows for a specific value date to support Auto Aggregation.md"]
---
# Additional Payments

Additional Payments are a product-agnostic schedule category included in the functional requirement's expected-payment model.

The source maps the category through these fields:

```text
Payment taxonomy: Additional_Payment.Additional_Party_Payment_type
Schedule_Date: Additional_Payment.Additional_Party_Payment_Date
Schedule_Currency: Additional_Payment.Additional_Party_Payment_Amount_Currency
```

A scheduled Additional Payment is eligible for Expected Payment Count only when its schedule date and currency exactly match the current cashflow's payment date and currency.

The source does not specify which `Additional_Payment.Additional_Party_Payment_type` values are in scope for Auto Aggregation.
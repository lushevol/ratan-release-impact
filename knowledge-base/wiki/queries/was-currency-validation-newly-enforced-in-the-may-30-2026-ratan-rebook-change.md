---
type: query
title: Was Currency Validation Newly Enforced in the May 30, 2026 Ratan Rebook Change?
created: 2026-08-23
updated: 2026-08-23
tags: [ratan, currency, rebook-exception, production-change]
related: [ratan, rebook-exception, payment-date-proximity-matching]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Ingenuine Rebook Exception in Ratan.md"]
---
# Was Currency Validation Newly Enforced in the May 30, 2026 Ratan Rebook Change?

The source describes the former 15-day workaround as requiring the same Trade ID and currency. It also describes the 2026-05-30 change as “5-day window + CCY validation.”

The documented change clearly reduced the payment-date threshold from 15 days to 5 days. It is unclear whether same-currency matching was already implemented in production, was introduced on 2026-05-30, or was present in requirements but not prior executable logic.

## Evidence needed

- Versioned pre- and post-deployment Ratan rule configuration or code.
- Production test evidence showing comparator-currency behavior before deployment.
- Change record acceptance criteria identifying the exact functional delta.
- Confirmation of whether the rule differs for [[stella]] and [[murex]] cashflows.
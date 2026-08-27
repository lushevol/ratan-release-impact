---
type: query
title: What Is the Schedule Currency Rule for CCS Amortization Payments?
created: 2026-08-22
updated: 2026-08-22
tags: [ccs, amortization, payment-schedules, currency, auto-netting]
related: [ccs, schedule-to-cashflow-matching, normalized-payment-schedule, expected-payment-count-for-auto-netting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Product Agnostic model to identify all cashflows for a specific value date to support Auto Aggregation.md"]
---
# What Is the Schedule Currency Rule for CCS Amortization Payments?

The source requires exact matching of schedule currency and payment currency, but its CCS amortization rows specify only:

```text
Swap_Instrument.IR_Leg.First_Leg.Step_Schedule.Notional_Amortization_Schedule_Date
Swap_Instrument.IR_Leg.Second_Leg.Step_Schedule.Notional_Amortization_Schedule_Date
```

No `Schedule_Currency` is supplied for either amortization row.

## Decision Needed

Define the authoritative currency source for fixed and floating amortization exchanges, including whether the rule uses `Cash_Settlement_Currency`, `Notional_Amount_Currency`, a payment-type-specific field, or another normalized value.

## Why It Matters

Without the currency derivation, amortization schedules cannot safely participate in the date-and-currency matching rule required for [[expected-payment-count-for-auto-netting]].
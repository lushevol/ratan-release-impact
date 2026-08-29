---
type: concept
title: Schedule-to-Cashflow Matching
created: 2026-08-22
updated: 2026-08-22
tags: [payment-schedules, cashflows, matching, auto-aggregation]
related: [expected-payment-count-for-auto-netting, normalized-payment-schedule, product-agnostic-cashflow-aggregation, irs, ccs, what-is-the-schedule-currency-rule-for-ccs-amortization-payments]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Product Agnostic model to identify all cashflows for a specific value date to support Auto Aggregation.md"]
---
# Schedule-to-Cashflow Matching

Schedule-to-cashflow matching compares normalized trade schedule data with current cashflow data to determine whether a cashflow belongs in the Expected Payment Count used for product-agnostic Auto Aggregation.

## Required Equality Conditions

The functional requirement requires exact equality on both fields:

```text
trade.Schedule_Currency = Cashflow.Payment_Currency
trade.Schedule_Date = Cashflow.Payment_Date
```

A matching schedule record may arise from Additional Payments, coupon schedules, CCS principal exchanges, or CCS amortization schedules.

## Product Coverage

- [[additional-payments]] apply to any product through Additional Payment type, date, and amount-currency fields.
- [[irs]] coupons use periodic adjusted interest payment dates across both swap legs.
- [[ccs]] coupons use both legs; non-MTM CCS principal exchanges use periodic notional exchange dates; amortizing CCS uses step-schedule amortization dates.

The supplied mapping does not provide a `Schedule_Currency` for CCS amortization rows, so those entries cannot fully satisfy the stated two-field match without a separate derivation rule. See what is the schedule currency rule for ccs amortization payments.

## Identity and Multiplicity

Date and currency do not uniquely identify a schedule event where multiple payments share the same values. The source does not specify schedule-event identity, deduplication, or whether a cashflow that matches both legs is counted once or twice. This is tracked in how are duplicate or multi matching schedule events counted.
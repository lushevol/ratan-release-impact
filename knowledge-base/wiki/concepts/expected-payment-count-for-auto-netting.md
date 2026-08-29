---
type: concept
title: Expected Payment Count for Auto Netting
created: 2026-08-22
updated: 2026-08-22
tags: [auto-netting, payment-completeness, cashflows, aggregation]
related: [schedule-to-cashflow-matching, normalized-payment-schedule, product-agnostic-cashflow-aggregation, cashflow-auto-netting, what-are-the-normalized-payment-schedule-aggregation-keys, which-cashflow-statuses-contribute-to-actual-payment-count]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Product Agnostic model to identify all cashflows for a specific value date to support Auto Aggregation.md"]
---
# Expected Payment Count for Auto Netting

Expected Payment Count is the number of scheduled trade payments that exactly match a current cashflow's payment date and payment currency. It provides the expected side of a completeness control for [[cashflow-auto-netting]].

## Matching Rule

A schedule entry is included only when both conditions hold:

```text
trade.Schedule_Currency = Cashflow.Payment_Currency
trade.Schedule_Date = Cashflow.Payment_Date
```

Date-only matching is insufficient. This distinction is material where a [[ccs]] has payments in different currencies on the same value date.

## Completeness Gate

Within the stated netting group, cashflows remain `Pending Another Leg` while Actual Payment Count is below Expected Payment Count. The source's example permits `Netted` status when the counts are equal.

```text
Actual Payment Count < Expected Payment Count  => Pending Another Leg
Actual Payment Count = Expected Payment Count  => Netted
```

The behavior for Actual Payment Count greater than Expected Payment Count is not specified.

## Dual-Leg Products

For [[irs]] and [[ccs]], schedule matching must evaluate both first-leg and second-leg schedule entries. A match on either leg is eligible for Expected Payment Count calculation.

The requirement does not define whether one cashflow matching multiple schedule entries is counted once or multiple times. See how are duplicate or multi matching schedule events counted.

## Related Controls

Expected Payment Count is schedule-derived; Actual Payment Count appears to be based on cashflows received in the same netting group. The statuses that qualify for the actual count remain open in which cashflow statuses contribute to actual payment count.
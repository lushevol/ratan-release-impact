---
type: source
title: Product-Agnostic Model for Value-Date Cashflow Auto Aggregation
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, auto-netting, auto-aggregation, payment-schedules, functional-requirement]
related: [expected-payment-count-for-auto-netting, schedule-to-cashflow-matching, normalized-payment-schedule, product-agnostic-cashflow-aggregation, cashflow-auto-netting, what-are-the-normalized-payment-schedule-aggregation-keys]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Product Agnostic model to identify all cashflows for a specific value date to support Auto Aggregation.md"]
authors: []
year: 0000
url: ""
venue: ""
---
# Product-Agnostic Model for Value-Date Cashflow Auto Aggregation

This functional requirement defines a product-agnostic schedule model for determining whether all cashflows expected for a payment date and currency have arrived before Auto Netting proceeds.

It specifies exact schedule-date and schedule-currency matching, evaluation of both IRS and CCS legs, and a completeness gate based on Expected Payment Count versus Actual Payment Count. It is a requirements fragment, not a complete implementation or lifecycle specification.

## Payment-Schedule Mapping

| Product_ISDA | Cashflow Type | Payment taxonomy | Schedule_Date | Schedule_Currency |
| --- | --- | --- | --- | --- |
| any | Additional Payments | Additional_Payment.Additional_Party_Payment_type | Additional_Payment.Additional_Party_Payment_Date | Additional_Payment.Additional_Party_Payment_Amount_Currency |
| IRS (deliverable/ND), CCS (deliverable/ND) | Coupons | Coupon/<Fixed/Float> | Swap_Instrument.IR_Leg.First_Leg.Periodic_Cash_Flow.Periodic_Adjusted_Interest_Payment_Date | coalesce (Swap_Instrument.IR_Leg.First_Leg.Cash_Settlement_Currency, Swap_Instrument.IR_Leg.First_Leg.Notional_Amount_Currency) |
| | Coupons | Coupon/<Fixed/Float> | Swap_Instrument.IR_Leg.Second_Leg.Periodic_Cash_Flow.Periodic_Adjusted_Interest_Payment_Date | coalesce (Swap_Instrument.IR_Leg.Second_Leg.Cash_Settlement_Currency, Swap_Instrument.IR_Leg.Second_Leg.Notional_Amount_Currency) |
| CCS (deliverable/ND) - non MTM | Principal | <Initial/Final/Amortization>Exchange/Fixed | Swap_Instrument.IR_Leg.First_Leg.Periodic_Cash_Flow.Periodic_Notional_Exchange_Date | coalesce (Swap_Instrument.IR_Leg.First_Leg.Cash_Settlement_Currency, Swap_Instrument.IR_Leg.First_Leg.Notional_Amount_Currency) |
| | | <Initial/Final/Amortization>Exchange/Fixed | Swap_Instrument.IR_Leg.Second_Leg.Periodic_Cash_Flow.Periodic_Notional_Exchange_Date | coalesce (Swap_Instrument.IR_Leg.Second_Leg.Cash_Settlement_Currency, Swap_Instrument.IR_Leg.Second_Leg.Notional_Amount_Currency) |
| | Amortizing | AmortizationExchange/Fixed | Swap_Instrument.IR_Leg.First_Leg.Step_Schedule.Notional_Amortization_Schedule_Date | |
| | | AmortizationExchange/Float | Swap_Instrument.IR_Leg.Second_Leg.Step_Schedule.Notional_Amortization_Schedule_Date | |
| | | | | |

Blank cells in the source table appear to inherit context from prior rows, but this inheritance is not explicitly defined. In particular, the amortization rows provide no `Schedule_Currency`.

## Expected Payment Matching

A scheduled payment contributes to Expected Payment Count only when both comparisons are true:

```text
trade.Schedule_Currency = Cashflow.Payment_Currency
trade.Schedule_Date = Cashflow.Payment_Date
```

For [[irs]] and [[ccs]], both legs must be evaluated. A schedule match on either leg makes the current payment eligible for Expected Payment Count calculation.

## Completeness-Gated Auto Netting

| Cashflow ID | Payment Date | Currency | Expected Payment Count | Actual Payment Count | Cashflow In the Same Group | Cashflow Status |
| --- | --- | --- | --- | --- | --- | --- |
| C01 | 2025 Sep 15 | USD | 4 | 1 | C01 | Pending Another Leg |
| C02 | 2025 Sep 15 | USD | 4 | 2 | C01, C02 | Pending Another Leg |
| C03 | 2025 Sep 15 | USD | 4 | 3 | C01, C02, C03 | Pending Another Leg |
| C04 | 2025 Sep 15 | USD | 4 | 4 | C01, C02, C03, C04 | Netted |

The stated netting key is:

```text
Same trade ID + Payment Date +Payment Currency + Entity + Counterparty
```

The source states that the aggregation resultant cashflow can be netted once the group is complete, but does not define resultant-cashflow creation, calculation, lifecycle, or downstream interface behavior.

## Open Specification Gaps

- The schedule-currency derivation rule for CCS amortization is absent.
- The source does not define whether multi-matching schedule events are counted once or multiple times.
- Actual Payment Count does not define qualifying cashflow statuses or duplicate treatment.
- The canonical source fields, normalization, and null handling for the netting key remain unspecified.

See [[expected-payment-count-for-auto-netting]], [[schedule-to-cashflow-matching]], and what are the normalized payment schedule aggregation keys.
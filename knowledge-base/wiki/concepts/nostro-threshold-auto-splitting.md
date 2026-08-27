---
type: concept
title: Nostro-Threshold Auto Splitting
created: 2026-08-22
updated: 2026-08-22
tags: [cashflow, auto-splitting, nostro, threshold, swift]
related: [cashflow-splitting, nostro-threshold-static, nostro-static, nostro-static-validation, split-cashflow-swift-annotation, netting-resultant-cashflow, what-is-the-authoritative-nostro-threshold-auto-split-allocation-algorithm]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting.md"]
---
# Nostro-Threshold Auto Splitting

Nostro-threshold auto splitting is a pre-SWIFT process that automatically distributes an eligible SCB pay cashflow into lower-value child cashflows when it matches a [[nostro-threshold-static]] record and its amount is greater than or equal to the configured threshold.

It applies to gross cashflows, netting resultants, and existing split children. It is distinct from cashflow netting: its purpose is payment-threshold compliance, not aggregation or offsetting.

## Matching conditions

The static check occurs before cashflow SWIFT generation and requires:
- An SCB pay cashflow.
- Cashflow amount `>= threshold`.
- A matching threshold-static record using currency, booking entity, and Nostro Agent.

The stated priority for multiple matches is:

```text
CCY > Booking Entity > Nostro Agent
```

This order does not define whether more-specific records override less-specific records, nor how ties are resolved.

## Failure behavior

Any auto-split exception moves the cashflow to:

```text
Cashflow State = READY
Cashflow Sub Status Type = Pending Exception
```

The only given example is a calculated deduction amount below 1. The source does not specify transaction boundaries, partial-child rollback, retry behavior, or a complete exception taxonomy.

## Unspecified allocation algorithm

The source delegates the calculation to `Auto Split Samples.xlsx`, which is not available in the imported material. The relationship among `Threshold`, `Amount`, and `Limitation`, the residual allocation rule, and exact-threshold treatment therefore require confirmation in [[what-is-the-authoritative-nostro-threshold-auto-split-allocation-algorithm]].
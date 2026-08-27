---
type: entity
title: Nostro Threshold Static Data
created: 2026-08-23
updated: 2026-08-23
tags: [nostro, static-data, threshold, cash-settlement, razor]
related: [razor, nostro-static, ratan, cashflow-auto-distribution, nostro-threshold-splitting-algorithm]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting/Cashflow Auto Distribution Design.md"]
---
# Nostro Threshold Static Data

Nostro Threshold Static Data configures the threshold-based distribution of large cashflows. The source describes this data as being maintained in [[razor]] and consumed by [[ratan]].

## Configuration fields

The described fields are:

- `threshold` — maximum target amount used as the basis for child cashflow calculation.
- `deductAmount` — amount accumulated to reduce successive child amounts.
- `limitation` — lower-bound trigger at which `deductAmount` is reduced.

Example:

```text
threshold = 80,000,000
deductAmount = 200,000
limitation = 60,000,000
```

## Operational importance

Incorrect or pathological static data can cause the auto-distribution algorithm to continue indefinitely or fail when `deductAmount` becomes less than `1`. The proposed recovery process requires a user to correct the static configuration before failing and reinstating the affected cashflow.

The source does not define ownership, approval controls, effective dating, currency precision, or validation rules for this configuration.
---
type: concept
title: Nostro Threshold Splitting Algorithm
created: 2026-08-23
updated: 2026-08-23
tags: [nostro, threshold, algorithm, cashflow-splitting, razor, ratan]
related: [nostro-threshold-static-data, cashflow-auto-distribution, razor, ratan, cashflow-auto-split-failure]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting/Cashflow Auto Distribution Design.md"]
---
# Nostro Threshold Splitting Algorithm

The Nostro threshold splitting algorithm is the RAZOR-derived procedure referenced for generating RATAN child cashflows from a cashflow that exceeds a configured threshold.

## Core formulas

The source provides these formulas:

```text
accDeductAmount = accDeductAmount + deductAmount
xchild = threshold - accDeductAmount
restAmount = restAmount - xchild
```

With `threshold = 80,000,000` and `deductAmount = 200,000`, the first candidate is `79,800,000`.

## Special behavior

### Ten-iteration skip

The algorithm skips a split child every ten times. The source does not define whether this means iterations 10, 20, 30, and so on, or how the skipped iteration affects the accumulator and residual.

### Duplicate final child

If the last child duplicates an earlier child, the design describes splitting the residual into:

```text
restAmount - deductAmount
deductAmount
```

The worked example instead states `78,980,000` and `200,000` for a residual of `79,000,000`. Those values do not reconcile, so the rule is not yet authoritative.

### Limitation and deduction shrinkage

When `xchild` is less than or equal to `limitation`, the deduction is reduced:

```text
deductAmount = deductAmount / 10
```

For the example configuration, the first reduction changes `200,000` to `20,000`. The source does not define repeated reductions, minimum currency units, rounding, or whether the accumulator is reset.

### Termination guard

When `deductAmount` becomes less than `1`, the design proposes raising an exception to prevent infinite splitting. The resulting status and action are discussed in [[cashflow-auto-split-failure]].

## Specification boundary

The algorithm is attributed to [[razor]], while execution and workflow status management belong to [[ratan]]. The RAZOR reference behavior should therefore be validated against the RATAN implementation rather than copied as an assumed complete contract.
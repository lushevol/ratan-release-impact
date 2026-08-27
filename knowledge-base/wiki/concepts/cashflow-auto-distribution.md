---
type: concept
title: Cashflow Auto Distribution
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, auto-distribution, splitting, settlement, nostro]
related: [ratan, razor, nostro-threshold-static-data, nostro-threshold-splitting-algorithm, cashflow-auto-split-failure, cashflow-withdrawal-during-split-failure]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting/Cashflow Auto Distribution Design.md"]
---
# Cashflow Auto Distribution

Cashflow auto distribution is the automatic partitioning of a large cashflow into child cashflows when its amount exceeds a configured Nostro threshold.

## Processing model

[[ratan]] detects the threshold breach and creates child cashflows using configuration maintained in [[razor]]. The output consists of one or more threshold-based child cashflows followed by a residual amount when the remaining cashflow no longer meets the split condition.

```text
if cashflow amount > threshold:
    create child cashflows
else:
    retain the amount without further splitting
```

The source does not specify whether the parent is retained, replaced, or marked as split, nor does it define parent-child identifiers, atomicity, idempotency, or reconciliation behavior.

## Child amount calculation

For the example configuration:

```text
threshold = 80,000,000
deductAmount = 200,000
```

the initial child sequence is:

```text
79,800,000
79,600,000
79,400,000
79,200,000
79,000,000
78,800,000
```

The residual is recalculated after each child. A residual below the threshold is normally not split further, except that duplicate-child handling may cause an additional branch.

## Important controls

The design references:

- A skip rule for every tenth split iteration.
- Deduction shrinkage when a candidate child reaches the configured `limitation`.
- An infinite-splitting guard when `deductAmount` becomes less than `1`.
- Failure processing through [[cashflow-auto-split-failure]].

These behaviors require a formal contract before implementation or testing.
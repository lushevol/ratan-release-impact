---
type: concept
title: Cashflow Un-Split
tags: [cashflow, settlement, operations, reversal]
related: [manual-cashflow-splitting, split-cashflow-amendment, murex-2-11-cashflow-suppression, authoritative-split-cashflow-lifecycle]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting/Split Demo Cases.md"]
---
# Cashflow Un-Split

Cashflow un-split reverses a prior manual split when Operations identifies an issue with the split arrangement.

## Eligibility

The stated eligible statuses are:

```text
QUEUED
WAITING
FAILED
HOLD
READY(NA)
CASHFLOW_SUPPRESSED
```

## Result

- The parent cashflow moves to `WAITING`.
- The parent receives an `Un-Split` exception.
- Child cashflows move to `DEAD`.
- The `Splitting Id` is removed.

## Open implementation boundary

The requirement does not state whether eligibility is evaluated for the selected parent, a selected child, or the split group as a whole. It also does not define whether a split group containing released children can be un-split.

Although `CASHFLOW_SUPPRESSED` is listed as eligible, this requirement does not identify its origin or extend the behavior defined by [[murex-2-11-cashflow-suppression]].
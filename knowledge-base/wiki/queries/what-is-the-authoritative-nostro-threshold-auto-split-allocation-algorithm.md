---
type: query
title: What Is the Authoritative Nostro-Threshold Auto-Split Allocation Algorithm?
created: 2026-08-22
updated: 2026-08-22
tags: [auto-splitting, nostro, allocation, static-data, requirements-gap]
related: [nostro-threshold-auto-splitting, nostro-threshold-static, cashflow-splitting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting.md"]
---
# What Is the Authoritative Nostro-Threshold Auto-Split Allocation Algorithm?

The requirement refers to `Auto Split Samples.xlsx` for the system allocation logic, but that attachment is not present in the imported source.

The missing specification must define:
- How many children are produced and how residual amounts are assigned.
- The meaning and interaction of `Threshold`, `Amount`, and `Limitation`.
- Exact behavior when the amount equals a threshold.
- Rounding, minimum-unit, and calculated-deduction behavior.
- The deterministic selection and tie-break rule for multiple matching static records.
- Whether failed processing atomically rolls back all generated children.
- Retry and recovery behavior after an auto-split exception.

Without this algorithm, the stated `READY` / `Pending Exception` failure state is insufficient to implement or reconcile automatic splitting safely.
---
type: query
title: What Are the Authoritative Split Rule Formula, Rounding, and Child-Count Limits?
tags: [cashflow-splitting, static-data, rounding, validation, auto-split]
related: [split-rule-maker-checker-lifecycle, nostro-threshold-splitting-algorithm, cashflow-auto-distribution, split-cashflow-api-contract]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting/Splitting Tech Design.md"]
---
# What Are the Authoritative Split Rule Formula, Rounding, and Child-Count Limits?

## Question

How do `threshold`, `amount`, and `limitation` determine automatic split output, including residual amounts, rounding, and the maximum number of children?

## Evidence

The split-rule APIs persist these fields as strings and provide no formal formula. Currency precision can be retrieved from `/v1/cashflow/lifecycle/getRoundingConfig/{currency}`.

UAT showed a failure when a cashflow of approximately `10000000` used `threshold: 1000`, `amount: 100`, and `limitation: 200`, described as an unreasonable configuration that creates too many child cashflows.

## Needed Resolution

Specify the formula and boundary cases; enforce numeric-scale validation; define residual allocation; and set a maximum child count enforced during rule creation, checker confirmation, and execution.
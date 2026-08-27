---
type: concept
title: Manual Rounding Amendment
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, manual-rounding, cashflow, amendment]
related: [camunda-task-bulk-amend-rounding-api, maker-checker-rounding-workflow, cashflow-versioning]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Manual Rounding/Api design.md"]
---
# Manual Rounding Amendment

A manual rounding amendment is a maker-initiated change to the amount of a cashflow. In the documented example, the maker submits `amendAmount: "100.01"` with `currency: "USD"` for cashflow `M00000049915`.

The amendment is submitted through the `AmendRounding` action of the [[camunda-task-bulk-amend-rounding-api]]. A checker subsequently uses `Approve` or `Reject` without resubmitting the amount or currency.

## Documented characteristics

- The operation targets a cashflow identified by `cashflowId`.
- The amount is represented as a string in the example.
- The currency is supplied with the maker amendment.
- The operation is separated into maker submission and checker review.
- The example advances `minorVersion` from `"5"` to `"6"` between submission and review.

The source does not define the rounding calculation, permitted precision, amount validation, persistence mechanism, rejection result, or downstream effects. It also does not establish that the example cashflow identifier or amount represents a production rule.

This workflow is distinct from generic [[bulk-manual-stp]] despite the endpoint path containing `/bulk/`.

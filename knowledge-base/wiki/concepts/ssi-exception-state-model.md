---
type: concept
title: SSI Exception State Model
created: 2026-08-23
updated: 2026-08-23
tags: [SSI, exception, state-model, cashflow, status]
related: [adhoc-ssi-workflow, adhoc-si, cash-settlement-home-page, dashboard-cashflow-status-counting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/Adhoc SI.md"]
---

# SSI Exception State Model

The SSI exception state model separates a cashflow's primary status from the fields that describe an SSI-related workflow.

## State dimensions

- **Cashflow Status:** The primary status, explicitly shown as `WAITING` or `READY`.
- **Sub Status Type:** The exception grouping, shown as `Pending Exception` or `NA`.
- **Sub Status:** The current operator/checker stage, shown as `Pending Operator`, `Pending Verification`, or `NA`.
- **SSI Exception Type:** The SSI exception classification, shown as `Adhoc SI` or `NA`.

## State relationships

A `WAITING` cashflow with `Pending Exception`, `Pending Operator`, and `NA` can enter the Adhoc SSI workflow through `Maker Adhoc SSI`.

A `WAITING` cashflow with `Pending Exception`, `Pending Verification`, and `Adhoc SI` becomes `READY` with all exception fields set to `NA` after `Checker Approve`.

A `READY` cashflow can carry `Pending Exception`, `Pending Verification`, and `Adhoc SI`. This means that primary readiness does not necessarily mean that all SSI workflow fields are clear.

## Data semantics requiring confirmation

The source does not define whether `NA` is a stored enumeration, null, empty value, or display placeholder. It also uses `READY` and `Ready` inconsistently and leaves several target fields blank in the `READY` matrix.

These semantics should be resolved before implementation, dashboard counting, or downstream eligibility rules are finalized.
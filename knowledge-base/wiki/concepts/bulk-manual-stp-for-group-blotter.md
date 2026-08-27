---
type: concept
title: Bulk Manual STP for Group Blotter
tags: [cash-settlement, manual-stp, group-blotter, cashflow-processing]
related: [group-blotter, group-major-version-completion-rules, trade-validation-gated-group-processing, allocation-cashflow-state-handling, cashflow-migration, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--12-2025-changes--38-bulk--4160up]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2025 changes/Bulk manual stp for group blotter test.md"]
---
# Bulk Manual STP for Group Blotter

Bulk manual STP is an operator-driven processing action tested against grouped records in the [[group-blotter]]. The available evidence specifies intended lifecycle transitions, not confirmed production behavior.

## Selection Granularity

The test matrix covers:

- Selection of a group-major-version with many pending child cashflows.
- Selection of one pending child cashflow at a time.
- Scenarios in which a selected group-major-version is accompanied by related, unselected records.

For `T1_G1_V1`, cases 3.1 through 3.3 specify that processing `C292`, then `C293`, then `C294` changes only the selected cashflow from `PENDING` to `END`. The parent remains `PENDING_TRADE_VALIDATION` until the final displayed pending cashflow, `C294`, is processed, at which point it becomes `COMPLETED`.

## Boundaries of the Evidence

Cases 2.1 through 2.3 record `N/A` rather than an outcome, so they do not establish whether the action is unavailable, rejected, a no-op, or undocumented for those selections.

The source does not identify the UI action, workflow, API, batch process, authorization model, or retry behavior behind “bulk manual STP.” It also does not establish impacts on SWIFT, netting, clearing, liens, or upstream trade ingestion.
---
type: query
title: What Is the Authoritative is_trade_validated Rule?
created: 2026-08-23
updated: 2026-08-23
tags: [open-question, trade-validation, is-trade-validated, major-version, bulk-manual-stp]
related: [bulk-manual-stp-group-blotter, trade-major-version-manual-stp-ordering, group-blotter-cashflow-state-lifecycle]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2025 changes/Bulk manual stp for Group Blotter.md"]
---
# What Is the Authoritative `is_trade_validated` Rule?

## Question

How does `is_trade_validated` control eligibility and processing of later major-version groups?

## Evidence

The scenarios show three outcomes:

- A later `PENDING_TRADE_VALIDATION` group with `is_trade_validated=false` does not complete when an earlier group is processed.
- A later `PENDING_TRADE_VALIDATION` group with `is_trade_validated=true` can complete.
- A later `PENDING_PRE_GROUP` group with `is_trade_validated=true` can complete.

The source does not specify when the flag is evaluated or its precedence relative to group status and major-version ordering.

## Required Resolution

Define whether `is_trade_validated` is checked during precheck, immediately before execution, or both. Confirm the valid combinations of group status and flag, and explain whether validation of one group permits all later groups for the trade to proceed.
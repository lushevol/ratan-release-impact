---
type: query
title: Is Bulk Manual STP Atomic per Trade?
created: 2026-08-23
updated: 2026-08-23
tags: [open-question, atomicity, concurrency, bulk-manual-stp, transaction-boundary]
related: [bulk-manual-stp-group-blotter, trade-major-version-manual-stp-ordering, group-blotter-cashflow-state-lifecycle, cashflow-migration-readiness]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2025 changes/Bulk manual stp for Group Blotter.md"]
---
# Is Bulk Manual STP Atomic per Trade?

## Question

When multiple group messages are processed using multiple threads, what are the transaction and failure boundaries?

## Evidence

The requirement mandates a full trade-level precheck before execution and returns precheck failures to the frontend. It does not state whether a failed precheck prevents all execution for that trade, whether an unrelated trade can proceed, or what happens if one execution thread succeeds while another fails.

## Required Resolution

Confirm whether bulk manual STP is atomic per trade, group, or cashflow. Document rollback, retry, idempotency, partial-success reporting, and isolation between different trades. Clarify whether major-version ordering governs execution start, commit order, or only eligibility.
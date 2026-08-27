---
type: concept
title: Cashflow Withdrawal During Split Failure
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, withdrawal, auto-split, lifecycle, techfail, pending-exception]
related: [cashflow-auto-split-failure, cashflow-auto-distribution, ratan, ratan-fail-and-autofail-status-transitions, cashflow-pre-fail-state-restoration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting/Cashflow Auto Distribution Design.md"]
---
# Cashflow Withdrawal During Split Failure

This concept describes the lifecycle conflict that occurs when a withdrawal message arrives while a cashflow is held in the proposed split-failure status `READY+NA+Pending_Exception`.

## Identified gap

Under the original `AutoSplitFail` proposal:

1. Auto-splitting fails.
2. The cashflow moves to `READY+NA+Pending_Exception`.
3. A withdrawal message arrives.
4. RATAN cannot move the cashflow from that status to process the withdrawal.

The source warns that the withdrawal cashflow may consequently be lost.

## Relationship to TechFail

The recommended solution is to use the existing `TechFail` behavior instead of `AutoSplitFail`. This is intended to preserve production-compatible workflow behavior, but the source does not prove that `TechFail` supports all required withdrawal scenarios.

A complete contract should define behavior for withdrawals received before failure, while the cashflow is in failure handling, and after static-data correction and reinstatement.

## Required controls

The implementation should clarify:

- Whether the original cashflow remains addressable after failure.
- Whether withdrawal messages are queued, rejected, or applied directly.
- How parent and child cashflows are correlated.
- Whether duplicate withdrawal messages are idempotent.
- What audit comments and result codes are recorded.
- How a failed or partially split cashflow is reinstated.
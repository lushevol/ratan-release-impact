---
type: query
title: What Is the Authoritative Split Cashflow Lifecycle?
tags: [cashflow, split, lifecycle, settlement, open-question]
related: [manual-cashflow-splitting, cashflow-un-split, split-cashflow-amendment, threshold-based-cashflow-auto-distribution, cashflow-lineage-and-amendment-correlation, ratan]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting/Split Demo Cases.md"]
---
# What Is the Authoritative Split Cashflow Lifecycle?

The functional requirement defines portions of the manual split, un-split, amendment, withdrawal, and auto-distribution lifecycles, but leaves group-level and implementation-level behavior unresolved.

## Evidence established

Manual splitting places the parent in `SPLIT`, children in `WAITING`, assigns `Split Cashflow` exceptions, and uses a shared `Splitting Id`. Un-split restores the parent to `WAITING` with an `Un-Split` exception, moves children to `DEAD`, and removes the identifier. Amendments can change only `WAITING` children while preserving the total amount across all children.

Withdrawal behavior distinguishes unreleased children from children released from [[ratan]], with released-child withdrawal events held in `NSTP` pending user action.

## Questions requiring confirmation

- Can a split operation create more than two children?
- What is the authoritative identifier field and split-group selection behavior?
- Must initial split amounts conserve the parent amount, and how are rounding residuals allocated?
- What fields, validation, and authorization controls apply to affirmation and SI selection?
- What event establishes that a child has been released from Ratan?
- Can released children be amended or un-split?
- What completes the withdrawal lifecycle after released-child `NSTP` handling?
- Do automatically distributed cashflows use the manual split lineage, status, exception, and reversal model?
- What threshold-record precedence, distribution algorithm, and idempotency controls apply to auto distribution?

Resolution should preserve the distinction between [[manual-cashflow-splitting]] and [[threshold-based-cashflow-auto-distribution]] unless a shared contract is explicitly approved.
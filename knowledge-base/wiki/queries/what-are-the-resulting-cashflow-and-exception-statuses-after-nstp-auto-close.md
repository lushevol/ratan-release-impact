---
type: query
title: What Are the Resulting Cashflow and Exception Statuses After NSTP Auto-Close?
tags: [nstp, cashflow-status, exception-status, state-machine, camunda]
related: [confirmation-driven-nstp-exception-auto-closure, cash-settlement-exception-handling, what-is-the-canonical-cash-settlement-exception-state-machine, ratan-cash-settlement-orchestration]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/NSTP Maker-Checker Separation From Code/NSTP exception auto close design-Confirmation status handling.md"]
---
# What Are the Resulting Cashflow and Exception Statuses After NSTP Auto-Close?

## Question

After a successful `mutiException/syncSummary` call, what exact exception status and cashflow status must result, and are all supplied exceptions transitioned atomically?

## Evidence

The source requires a cashflow to be in `WAITING` status and provides a sample exception in `PENDING_OPERATOR` status. It says the Camunda operation will close exceptions, synchronize their summaries, and update cashflow status.

It does not name the target state for either object, define partial-success behavior for the `exceptions` array, or state whether the successful HTTP response proves all downstream changes were committed.

## Required Clarifications

- Exception destination status and summary semantics.
- Cashflow destination status.
- Atomicity across the cashflow update and all exception updates.
- Handling when some exceptions are no longer eligible.
- Audit, authorization, and maker-checker implications of the automatic submission.
---
type: comparison
title: Cashflow Suppression versus SWIFT Suppression
created: 2026-08-22
updated: 2026-08-22
tags: [cashflow, suppression, SWIFT, approval, settlement]
related: [cashflow-lifecycle-state-machine, cashflow-suppression-vs-payment-suppression, settlement-suppression-exceptions, nstp-exception-handling]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/Batch Status Update API Tuning/lifecycle service - state machine.md"]
---
# Cashflow Suppression versus SWIFT Suppression

The lifecycle service models cashflow suppression and SWIFT suppression as separate outcomes with separate status values and approval-controlled undo workflows.

## Comparison

| Dimension | Cashflow suppression | SWIFT suppression |
| --- | --- | --- |
| Direct status | `CASHFLOW_SUPPRESSED+NA+NA` | `SWIFT_SUPPRESSED+NA+NA` |
| Direct action | `Suppress` | `SwiftSuppress` |
| Manual action | `ManualSuppress` | `ManualSwiftSuppress` |
| Manual approval state | `WAITING+Cashflow Suppression+Pending Verification` | `WAITING+Swift Suppression+Pending Verification` |
| Approval result | `CASHFLOW_SUPPRESSED+NA+NA` | `SWIFT_SUPPRESSED+NA+NA` |
| Undo action | `ManualUnSuppress` | `ManualSwiftUnSuppress` |
| Undo approval state | `WAITING+Undo Cashflow Suppression+Pending Verification` | `WAITING+Undo Swift Suppression+Pending Verification` |
| Approved undo result | `QUEUED+NA+NA` | `QUEUED+NA+NA` |

Cashflow suppression prevents the cashflow from proceeding through normal processing. SWIFT suppression is represented independently and concerns SWIFT generation or transmission. The source does not state whether either status suppresses all downstream payment or accounting effects.

## Common controls

Both suppression types support rejection, withdrawal, technical-failure recovery, failure, and state-dependent `UnNet` behavior. Rejection from a manual suppression approval state leads to `NA+NA+NA`, whose operational meaning is not defined in the source.
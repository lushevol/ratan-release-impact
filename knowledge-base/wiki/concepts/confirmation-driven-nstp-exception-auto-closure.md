---
type: concept
title: Confirmation-Driven NSTP Exception Auto-Closure
tags: [nstp, exception-handling, trade-confirmation, cashflow, camunda]
related: [trade-cashflow-exception-version-correlation, cash-settlement-exception-handling, trade-confirmation-driven-payment-stp, ratan-cash-settlement-orchestration, ratan-stella-message-event-source]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/NSTP Maker-Checker Separation From Code/NSTP exception auto close design-Confirmation status handling.md"]
---
# Confirmation-Driven NSTP Exception Auto-Closure

Confirmation-driven NSTP exception auto-closure is a bounded cash-settlement flow that closes NSTP exceptions after a qualifying trade confirmation event.

## Trigger and Eligibility

The source requires all of the following:

```text
event status is MATCHED
AND EG Confirmation Status is Confirm or Affirm
AND a related CN Settlement cashflow is found
AND cashflow status is WAITING
AND action is isNstp
```

A qualifying event is consumed from [[trade-service-trade-events]]. Cashflow lookup is performed through [[ratan-stella-message-event-source]], using trade identity and version correlation.

## Processing Outcome

For eligible cashflows, the consumer calls:

```text
POST /v1/camunda/task/mutiException/syncSummary
```

on [[ratan-cash-settlement-orchestration]]. The intended operation is to close exception records, synchronize their summaries, and update cashflow status.

The source documents a `PENDING_OPERATOR` NSTP exception in the sample request but does not state the destination exception status or cashflow status. It also does not define whether multi-exception processing is atomic.

## Scope

This rule extends [[cash-settlement-exception-handling]] with a specific confirmation-triggered path. It must not be treated as a general rule for all cashflow exceptions, all trade confirmations, or all payment-STP processing.

The 404 response for a missing Cashflow fixing task creates a dependency on task lifecycle state but does not establish that `WAITING` or `isNstp` is equivalent to PendingFixing.
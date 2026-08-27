---
type: concept
title: Cashflow Lifecycle State Machine
created: 2026-08-22
updated: 2026-08-22
tags: [cashflow, lifecycle, state-machine, settlement, exception-handling]
related: [murex-cashflow-status-lifecycle, cashflow-fail-and-reinstatement, nstp-exception-handling, cashflow-splitting, inter-entity-netting, cashflow-suppression-vs-payment-suppression]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/Batch Status Update API Tuning/lifecycle service - state machine.md"]
---
# Cashflow Lifecycle State Machine

The cashflow lifecycle state machine maps a composite previous status and action to a composite next status. It is the principal behavioral model described by the batch status update design.

## Status structure

A status has three components:

```text
<primary lifecycle status>+<processing or exception subtype>+<operational state>
```

Examples include:

```text
QUEUED+Pending Exception+Pending Operator
NETTED+Pending Ack+NA
WAITING+Cashflow Suppression+Pending Verification
```

The primary status covers settlement progression. The second and third components identify processing context, exception category, acknowledgement state, and maker/checker responsibility.

## Main lifecycle paths

The ordinary settlement path is:

```text
NA+NA+NA
  --New--> PROJECTED+NA+NA
  --Materialize--> QUEUED+NA+NA
  --ValidateDirect--> READY+NA+NA
  --Release--> RELEASED+NA+NA
  --Settle--> SETTLED+NA+NA
  --NostroMatch--> NOSTRO_MATCHED+NA+NA
```

From projected or queued states, a cashflow can instead be netted, split, cashflow-suppressed, SWIFT-suppressed, withdrawn, or routed to an exception workflow.

## Recovery and operational paths

`TechFail` generally returns the cashflow to:

```text
QUEUED+Pending Exception+NA
```

`Fail` generally produces:

```text
FAILED+NA+NA
```

Exception states support operator submission, checker verification, approval, rejection, enrichment events, reversal to queued, and withdrawal. `ReplayStatusWriteBack` is idempotent for several netted and settled states: it writes the status without advancing the lifecycle.

## Netting semantics

Netting can be entered from projected, queued, and several waiting states. A netted cashflow may progress through acknowledgement, release, settlement, and Nostro matching. Withdrawal from a netted state normally returns to `QUEUED+NA+NA`.

`UnNet` is not uniform. For some netted states it returns to `QUEUED+NA+NA`; for queued, waiting, held, or suppressed states it can result in `DEAD+NA+NA`. This state-dependent behavior requires explicit business documentation and test coverage.

## Split lifecycle

Split cashflows retain distinct states:

```text
SPLIT+NA+NA
SPLIT+Released+NA
SPLIT+Settled+NA
SPLIT+NostroMatched+NA
```

`UnSplit` returns an unprocessed split to `QUEUED+NA+NA`. Withdrawal from any split stage also returns to queued, while technical failure routes to the pending-exception state.

## Evidence boundary

This model is a design target, not evidence of production runtime behavior. Implementation ownership, transition validation, API behavior, and UAT coverage are not established by the source.
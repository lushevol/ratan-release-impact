---
type: concept
title: PendingFixing and WaitingAnotherLeg
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, IRS, fixing-flag, lifecycle-state]
related: [fixing-flag-notification-processing, netting-service, fixing-notification-event-ordering, cashflow-reinstatement-and-replay]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Fixing flag notification.md"]
---
# PendingFixing and WaitingAnotherLeg

`PendingFixing` and `WaitingAnotherLeg` are fixing-related states used in the draft design for IRS cashflow processing.

## Intended Meaning

- `PendingFixing` is illustrated as the state of a cashflow received with fixing flag `X`.
- `WaitingAnotherLeg` is illustrated as the state reached after a notification with fixing flag `Y`, when another IRS leg or fixing event is still required.
- A later notification with flag `N` removes the `WaitingAnotherLeg` condition in the example.

The source does not establish whether these values are persisted lifecycle statuses, derived rule results, fixing sub-states, or GUI labels.

## Example Transition

For cashflow `C1`:

```text
flag X -> PendingFixing
notification flag Y -> WaitingAnotherLeg
notification flag N -> not WaitingAnotherLeg
```

The examples are illustrative. The canonical meanings of `X`, `Y`, and `N` have not been confirmed.

## Ownership Question

The [[entities/netting-service]] evaluates the IRS waiting-fixing-flag rule, but the source does not state whether it owns the final state transition or returns a result to the [[entities/lifecycle-service]].

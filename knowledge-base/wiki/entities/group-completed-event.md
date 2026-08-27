---
type: entity
title: GroupCompletedEvent
created: 2026-08-23
updated: 2026-08-23
tags: [RATAN, domain-event, completion, unlocking, cashflow-groups]
related: [cashflow-group, cashflow-group-lifecycle, group-ready-event, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2025 changes/Bulk manual stp for Group Blotter Detail.md"]
---
# GroupCompletedEvent

`GroupCompletedEvent` is published when a cashflow group has no pending messages and changes to `COMPLETED`.

## Completion handling

The source describes the following sequence:

```text
noPendingMessage
    => groups.status=COMPLETED
    => unLockPrevious
    => publish GroupCompletedEvent
```

`GroupCompletedEventHandler` then:

1. Finds the next uncompleted groups.
2. Checks `NoPreviousGroupPending`.
3. Selects a next group with status `PENDING_PRE_GROUP`.
4. Enables that group.
5. Moves it to `PENDING_TRADE_VALIDATION` when its trade is validated.

The completion chain also references `FXStatusWriteBackEventHandler`, which writes `cashflowStatus=SUSPENDED`. The source does not establish whether that write-back applies to every completed group.
---
type: concept
title: Cashflow Group Lifecycle
created: 2026-08-23
updated: 2026-08-23
tags: [RATAN, cashflow-groups, state-machine, sequencing, orchestration]
related: [cashflow-group, cashflow-group-message, ratan, trade-validation-group-advancement, trade-validated-event, group-ready-event, group-completed-event]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2025 changes/Bulk manual stp for Group Blotter Detail.md"]
---
# Cashflow Group Lifecycle

A cashflow group is the ordered processing unit used by [[entities/ratan]] to collect related cashflow messages, wait for trade validation, prevent premature progression, and initiate downstream orchestration.

## States

| State | Meaning in the source |
|---|---|
| `PENDING` | Initial group state while inbound messages and prerequisites are being evaluated. |
| `PENDING_PRE_GROUP` | The group is blocked by an earlier pending group or version. |
| `PENDING_TRADE_VALIDATION` | Previous-group conditions are satisfied, but trade validation is not yet complete. |
| `READY` | The group can publish [[entities/group-ready-event]] and proceed to `Cash_Settlement_Orchestration_Inbound`. |
| `COMPLETED` | No pending group messages remain; completion handling unlocks and advances dependent groups. |

## Transition model

```text
PENDING
    -> previous minor version exists in pending
       => PENDING_PRE_GROUP

PENDING_PRE_GROUP
    -> noPreviousGroupPending
       and is_trade_validated=false
       => PENDING_TRADE_VALIDATION

PENDING_TRADE_VALIDATION
    -> is_trade_validated=true
       => READY

READY
    -> noPendingMessage
       => COMPLETED
```

The source also describes `PENDING` and `PENDING_TRADE_VALIDATION` as inputs to the `noPreviousGroupPending` check. The exact precedence between these branches is not fully specified.

## Event relationships

- [[entities/trade-validated-event]] updates groups for a trade and can enable a transition to `READY`.
- [[entities/group-ready-event]] signals downstream orchestration through `Cash_Settlement_Orchestration_Inbound`.
- [[entities/group-completed-event]] initiates unlocking and searches for the next uncompleted group.
- `GroupCompletedEventHandler` enables a `PENDING_PRE_GROUP` group when no previous group remains pending.

## Ordering ambiguity

The source retrieves groups using `batchId`, `tradeId`, and `majorVersion`, but describes an earlier “minor version” as a sequencing dependency. It does not define the authoritative ordering key or the relationship between major and minor versions.

`cashflowStatus=SUSPENDED` is also mentioned in the completion chain through `FXStatusWriteBackEventHandler`; the source does not establish that this is a universal completion outcome.
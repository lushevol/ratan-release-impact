---
type: source
title: "Bulk Manual STP for Group Blotter Detail"
authors: []
year: 2025
url: "https://confluence.global.standardchartered.com/display/DSP/Cashflow+Events+Control"
venue: "Derivative Strategy Projects Confluence"
created: 2026-08-23
updated: 2026-08-23
tags: [RATAN, cash-settlement, cashflow-groups, group-blotter, functional-requirement]
related: [ratan, cash-settlement-home-page, tds3, cashflow-group, cashflow-group-message, cashflow-group-lifecycle, trade-validation-group-advancement, cashflow-group-message-deduplication, trade-validated-event, group-ready-event, group-completed-event]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2025 changes/Bulk manual stp for Group Blotter Detail.md"]
---
# Bulk Manual STP for Group Blotter Detail

## Scope

This functional requirement is associated with the Cash Settlement Home Page and the Group Blotter Detail context. Despite its filename, the supplied content primarily documents event-driven cashflow-group ingestion, trade validation, sequencing, orchestration, and completion. It does not fully specify the user interface or operator workflow for bulk manual STP.

The process is centered on [[entities/ratan]], with trade-validation input from [[entities/tds3]] and downstream delivery to `Cash_Settlement_Orchestration_Inbound`.

## Topic and processing mapping

| Topic / input | Processing |
|---|---|
| `Cash_Settlement_Group_Message_Inbound` (`upstream-inbound.topic`) | For `cashflowinfo`, obtain `cashflowInfo` from `scbml`; `businessEvent` values include `New` and `Withdrawal`; `countSeq` uses `batchId_seq_count/seq_count`. For `event`, build and save `CashflowGroupMessage` (`ratan_cashflow_group_message`) with `status=PENDING`; key fields include `businessEvent`, `New`, `Withdrawal`, `batchId`, and `major_version`. Perform duplicate checking on `tradeId`, `majorVersion`, `batchId`, `businessVersion`, and `cashflowId`. Build and save `CashflowGroup` (`ratan_cashflow_group`). |
| `TDS3_Trade_Message_Process_In` (`tds3-trade-inbound`) | Obtain `TradeInfo` from `scbml`; update `ratan_trade`; emit `TradeValidatedEvent`; update all groups grouped by `tradeId` with `isTradeValidated=true`; retrieve groups in `PENDING_TRADE_VALIDATION`. |
| `TDS3_Trade_Murex_Message_Process_In` (`tds3-trade-murex-inbound`) | Same trade-validation behavior as `TDS3_Trade_Message_Process_In`, specifically for the Murex trade-message path. |
| `Cash_Settlement_Orchestration_Inbound` | Receives the group message after the group reaches `READY` and emits or processes the `GroupReadyEvent` flow. |

## Inbound group-message processing

A `MessageInboundEvent` results in a [[entities/cashflow-group-message]] being built and persisted to `ratan_cashflow_group_message` with `status=PENDING`. The system then builds or retrieves a [[entities/cashflow-group]] using:

- `batchId`
- `tradeId`
- `majorVersion`

The group is initially locked. The source indicates that earlier groups or versions for the same trade can prevent the current group from advancing.

The duplicate-check fields are:

```text
tradeId, majorVersion, batchId, businessVersion, cashflowId
```

## Cashflow-group state flow

The documented state identifiers are:

- `PENDING`
- `PENDING_PRE_GROUP`
- `PENDING_TRADE_VALIDATION`
- `READY`
- `COMPLETED`

The process is described as follows:

```text
PENDING
    -> previous minor version exists in pending
       => group.status=PENDING_PRE_GROUP

    -> noPreviousGroupPending
       (PENDING, PENDING_TRADE_VALIDATION)
       and group.status=PENDING_PRE_GROUP
       and is_trade_validated=false
       => PENDING_TRADE_VALIDATION

    -> is_trade_validated=true
       => group.status=READY

    -> noPendingMessage
       => group.status=COMPLETED
```

The key control principle is that a later group cannot progress solely because its own messages have arrived. Previous-group dependencies must also be satisfied.

## Trade-validation flow

For both `TDS3_Trade_Message_Process_In` and `TDS3_Trade_Murex_Message_Process_In`:

1. `TradeInfo` is obtained from `scbml`.
2. `ratan_trade` is updated.
3. [[entities/trade-validated-event]] is emitted.
4. All groups associated with the relevant `tradeId` are updated with `isTradeValidated=true`.
5. Groups in `PENDING_TRADE_VALIDATION` are retrieved and evaluated for advancement.

When sequencing and message-completeness conditions permit, a validated group moves to `READY` and publishes [[entities/group-ready-event]].

## Readiness, orchestration, and completion

The source describes the following sequence:

```text
TradeValidatedEvent
    => groups/trade is_trade_validated=true
    => group.status=READY
    => publish GroupReadyEvent
       => cashflowGroupMessage.status=END
       => send group message to topic:
          Cash_Settlement_Orchestration_Inbound
       => noPendingMessage
          => groups.status=COMPLETED
          => unLockPrevious
          => publish GroupCompletedEvent
```

`GroupReadyEvent` therefore acts as a gateway to downstream orchestration rather than being only an internal status notification.

On completion, [[entities/group-completed-event]] triggers unlocking of the previous group and evaluation of later incomplete groups. `GroupCompletedEventHandler` finds the next uncompleted group, checks `NoPreviousGroupPending`, and enables a group whose status is `PENDING_PRE_GROUP`. If its trade has already been validated, the next group is moved to `PENDING_TRADE_VALIDATION`.

The source also references `FXStatusWriteBackEventHandler`, which writes:

```text
cashflowStatus=SUSPENDED
```

The supplied material does not establish whether this write-back applies to every completed group or only to particular FX or cashflow conditions.

## Message-count overflow control

The source includes this defensive control:

```java
if (groupMessageList.size() > cashflowGroupMessage.getCashflowCnt()) {
    log.info("All group message has been arrived already for group: {}, change the current message: {} status to ERROR.",
        cashflowGroup.getAggregateRootId(),
        cashflowGroupMessage.getAggregateRootId());
    cashflowGroupMessage.changeToError(cashflowGroupMessageRepository);
    return;
}
```

When the number of received group messages exceeds `cashflowCnt`, the current message is changed to `ERROR`. This is distinct from the multi-field duplicate check and appears to protect against excess or unexpected arrivals.

The source does not define behavior for missing messages, retries, late arrivals, concurrent arrivals, or recovery from an `ERROR` offset.

## Scope limitations and open points

The document does not fully define:

- Bulk manual STP selection criteria in Group Blotter Detail.
- Operator permissions or authorization.
- Audit requirements for manual actions.
- Idempotency and retry behavior for manual STP.
- The authoritative ordering relationship between `majorVersion` and the referenced minor-version dependency.
- Whether `cashflowGroupMessage.status=END` is written before or after successful downstream publication.
- Whether `cashflowStatus=SUSPENDED` is generic or FX-specific.
- Whether `COMPLETED` can be reached directly from `PENDING` or only through the preceding states.

These gaps should be resolved before treating the document as a complete specification for bulk manual STP.
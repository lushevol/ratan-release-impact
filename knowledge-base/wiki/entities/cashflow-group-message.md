---
type: entity
title: CashflowGroupMessage
created: 2026-08-23
updated: 2026-08-23
tags: [RATAN, domain-object, inbound-messaging, cashflow-groups]
related: [cashflow-group, cashflow-group-message-deduplication, cashflow-group-lifecycle, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2025 changes/Bulk manual stp for Group Blotter Detail.md"]
---
# CashflowGroupMessage

`CashflowGroupMessage` is the inbound message record persisted as `ratan_cashflow_group_message`.

## Creation

A `MessageInboundEvent` builds and saves the record with:

```text
status=PENDING
```

Relevant source fields include:

```text
businessEvent: New, Withdrawal
batchId
major_version
tradeId
majorVersion
businessVersion
cashflowId
```

The record is associated with a `CashflowGroup` identified by `batchId`, `tradeId`, and `majorVersion`.

## Status handling

When a group becomes ready, the source associates the group flow with:

```text
cashflowGroupMessage.status=END
```

When the number of received messages exceeds `cashflowCnt`, the current message is changed to:

```text
status=ERROR
```

The source does not clarify whether `END` is applied to every message in the group or only to the processed offset.
---
type: concept
title: Cashflow Group Message Deduplication
created: 2026-08-23
updated: 2026-08-23
tags: [RATAN, cashflow-groups, deduplication, message-integrity, error-handling]
related: [cashflow-group-message, cashflow-group, cashflow-group-lifecycle, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2025 changes/Bulk manual stp for Group Blotter Detail.md"]
---
# Cashflow Group Message Deduplication

The inbound cashflow-group flow applies duplicate and message-count controls before allowing a group to progress.

## Duplicate-check fields

The source identifies the following fields for duplicate checking on `CashflowGroupMessage`:

```text
tradeId, majorVersion, batchId, businessVersion, cashflowId
```

A message is built and persisted to `ratan_cashflow_group_message` with `status=PENDING`. The group is built or retrieved using `batchId`, `tradeId`, and `majorVersion`.

The source does not state whether these fields are enforced through a database constraint, an application-level lookup, or both.

## Message-count overflow

The source provides this rule:

```java
if (groupMessageList.size() > cashflowGroupMessage.getCashflowCnt()) {
    log.info("All group message has been arrived already for group: {}, change the current message: {} status to ERROR.",
        cashflowGroup.getAggregateRootId(),
        cashflowGroupMessage.getAggregateRootId());
    cashflowGroupMessage.changeToError(cashflowGroupMessageRepository);
    return;
}
```

When the received message count exceeds the expected `cashflowCnt`, the current message is marked `ERROR`. This protects the group from excess arrivals but does not explain how missing or late messages are recovered.

## Unspecified controls

The source does not define:

- Behavior when the received count is below `cashflowCnt`.
- Retry and replay semantics after an `ERROR` status.
- Concurrency handling for simultaneous arrivals.
- Whether an `ERROR` offset is ignored during trade-validation updates.
- The relationship between the multi-field duplicate check and the count-based overflow rule.
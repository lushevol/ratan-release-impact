---
type: source
title: Fixing Flag Notification Technical Design
authors: []
year: 0000
url: ""
venue: ""
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, fixing-flag, IRS, technical-design]
related: [murex, ratan, fixing-flag-notification-processing, pending-fixing-and-waiting-another-leg, fixing-notification-event-ordering, cashflow-reinstatement-and-replay, cash-settlement-exception-handling]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Fixing flag notification.md"]
---
# Fixing Flag Notification Technical Design

## Summary

This draft technical design describes processing fixing-flag notifications for IRS cashflows in the cash-settlement platform. The proposed flow separates file ingestion, lifecycle handling, and IRS netting-rule evaluation across the [[entities/batch-service]], [[entities/lifecycle-service]], and [[entities/netting-service]].

The design covers notification persistence, fixing-flag application, cashflow re-queuing, cancellation precedence, failure recovery, and event-ordering scenarios. It does not yet define the authoritative event schema, file contract, acknowledgement behavior, ordering mechanism, or canonical relationship between fixing flags and cashflow lifecycle states.

## Context

The design references the **LIEN Processing & Pending Fixing Flag Technical Design** and the requirement for IRS fixed-leg and floating-leg payment handling. Murex is implied to participate in the file-transfer flow, while Ratan receives and processes the resulting notifications.

The proposed NAS locations are:

```text
/apps/ratannas/murex_ratan_transfer/fixing/ack

/apps/ratannas/murex_ratan_transfer/fixing/payment

/apps/ratannas/murex_ratan_transfer/fixing/payment/Done

/apps/ratannas/murex_ratan_transfer/fixing/payment/Error
```

The following file-transfer details remain to be confirmed:

- Naming convention
- File content
- ACK/NACK behavior
- File movement between input, completion, and error folders
- Duplicate, malformed, and partial-file handling

## Proposed Lifecycle Workflow

| Service Name | Responsibilities |
| --- | --- |
| Batch Service | Process the new folder, validate the file, and send a notification to Kafka |
| Lifecycle Service | Consume the batch-file notification, persist the original notification for batch and real-time processing, and apply the fixing flag. If the cashflow is eligible, revert it to `queued` for reprocessing |
| Netting Service | Call the IRS check API and determine whether the cashflow matches the waiting-fixing-flag rule |

The source states that a cancelled cashflow should not be reprocessed. Case 3 additionally states that a cancelled cashflow remains cancelled while its fixing flag changes and the GUI displays the latest value. The likely interpretation is that cancellation suppresses lifecycle transition, re-queueing, and reinstatement, but does not suppress notification persistence or fixing-flag/read-model updates. This interpretation requires confirmation.

## Event-Ordering Scenarios

### Case 1: Fixing flag changes through successive notifications

For the illustrative cashflow `C1`:

1. `C1` arrives with flag `X` and becomes `PendingFixing`.
2. A notification with flag `Y` arrives and `C1` becomes `WaitingAnotherLeg`.
3. A notification with flag `N` arrives and `C1` is no longer `WaitingAnotherLeg`.

The design uses `X`, `Y`, and `N` as example values. Their canonical meanings and production status are not defined.

### Case 2: Notification arrives before the cashflow

1. A notification for `C1` with flag `Y` arrives.
2. `C1` subsequently arrives with flag `X`.
3. `C1` ends in `WaitingAnotherLeg`.

This requires durable notification persistence, correlation with a later cashflow, or an equivalent reconciliation mechanism.

### Case 3: Withdrawal precedes a fixing notification

1. `C1` arrives with flag `X` and becomes `PendingFixing`.
2. `C1` is withdrawn.
3. A fixing notification arrives.
4. `C1` remains cancelled, but its fixing flag changes and the GUI can display the latest flag.

This scenario separates the business lifecycle state from the fixing-flag value and its presentation in the read model.

### Case 4: Failure or technical failure precedes a fixing notification

1. `C1` arrives with flag `X` and becomes `PendingFixing`.
2. `C1` enters `failed` or `techfailed`.
3. A notification with flag `Y` arrives.
4. `C1` is reinstated and stamped with `Y`.

The design does not specify whether business and technical failures use identical reinstatement rules.

### Case 5: Cashflow and notification arrive concurrently

A cashflow with flag `X` and a notification with flag `Y` arrive at approximately the same time. The expected result is that `C1` becomes `WaitingAnotherLeg`.

The source does not define whether precedence is controlled by a sequence number, event version, source timestamp, processing timestamp, or last-write-wins policy.

## Design Implications

The design implies four distinct pieces of information that should not be conflated:

1. The persisted fixing-flag notification.
2. The fixing flag applied to the cashflow.
3. The cashflow lifecycle state, including cancelled, failed, and `techfailed`.
4. The derived or displayed GUI state, including `PendingFixing` and `WaitingAnotherLeg`.

The proposed workflow also implies that updating a fixing flag and re-queuing a cashflow may need to be atomic. Otherwise, a flag can be persisted without the corresponding reprocessing request, or a cashflow can be re-queued using stale fixing information.

Relevant existing concepts include [[concepts/cashflow-reinstatement-and-replay]], [[concepts/cash-settlement-exception-handling]], [[concepts/cashflow-notification-and-auto-refresh]], and [[concepts/cash-settlement-service-landscape]].

## Unresolved Contracts

The source does not provide:

- A file schema
- A Kafka topic, key, or message payload
- An API signature
- An idempotency key or duplicate-detection rule
- A version or sequence field
- A retry and dead-letter policy
- A canonical state machine
- Eligibility rules for re-queueing or reinstatement
- ACK/NACK payloads and folder-transition rules

These omissions prevent the document from serving as an implementation-ready contract.

## Assessment

The design provides a useful intended workflow and identifies important ordering cases, especially notification-before-cashflow processing, cancellation precedence, and reinstatement after failure. It should be treated as a draft proposal rather than validated implementation evidence until the state model, event precedence, persistence behavior, and file-transfer contracts are confirmed.

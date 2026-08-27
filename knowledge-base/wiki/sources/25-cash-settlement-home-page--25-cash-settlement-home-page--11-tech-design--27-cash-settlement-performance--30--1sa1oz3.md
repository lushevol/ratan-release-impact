---
type: source
title: Cash Settlement Performance — Batch Status Update API Tuning and Lifecycle Service State Machine
authors: []
year: 2026
url: ""
venue: "Technical design specification"
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, performance, batch-status-update, lifecycle-service, state-machine, Ratan]
related: [cashflow-lifecycle-state-machine, business-versioned-cashflow-persistence, cashflow-technical-failure-recovery, cashflow-suppression-vs-swift-suppression, cashflow-splitting, ratan, stella, razor, murex]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/Batch Status Update API Tuning/lifecycle service - state machine.md"]
---

# Cash Settlement Performance — Batch Status Update API Tuning and Lifecycle Service State Machine

## Scope

This technical design describes batch status updates for the cashflow lifecycle service. It covers business-version-dependent persistence, the `CashflowMessageEventSource` record, and a composite lifecycle state machine used by Ratan.

The document is strong evidence of intended design behavior. It does not establish that the transitions are implemented, tested, deployed, or enabled in production. It also provides no API signature, database DDL, load-test measurements, or performance results.

## Business-version persistence scenarios

| Scenario | Description | ratan_stella_message_event_source | ratan_cashflow_scbml_history | ratan_cashflow_scbml_message | ratan_cashflow_cutoff_info | ratan_cashflow_holding_message | ratan_cashflow_affirmation_status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Cashflow Id is New | Insert | Insert | Insert | Insert | NA | Insert if Affirmed in SCBML |
| 2 | Business version downgrade(late start, early arrival) eg: 005564082752 | Insert | Insert new and update current | Update | Insert | NA | Insert if Affirmed in SCBML |
| 3 | Business version upgrade | Insert | Insert new and update current | Update | Insert | Update current on demand | Insert if Affirmed in SCBML |
| 4 | Business version not change | Update | Insert new and update current | Update | Insert if not exists | Insert on demand | Insert if Affirmed from request |

The design separates append-oriented SCBML history from the current SCBML representation. It also avoids unnecessary writes when the cashflow business version is unchanged. The affirmation source differs by scenario: SCBML for scenarios 1–3 and the request for scenario 4.

## Event-source field inventory

The source identifies the following fields for `CashflowMessageEventSource` and `ratan_stella_message_event_source`:

```text
allotment
bicNetFlag
bodyEventRowkey
bookingSystemEvent
businessEvent
businessEventRatan
businessUnitId
captureSystem
cashflowAggId
cashflowEventReason
cashflowVersion
cashflowWorkflowStatus
cfiCode
clearingAlpha
clientType
counterpartFmcode
counterpartFmid
counterpartyBic
counterpartyDomicileCountry
countryCode
createTime
deliveryMethod
description
domainName
entityFmcode
entityFmid
eventDate
eventType
initialRatanEvent
initiatedTimestamp
isCommodity
isPva
isPvb
isUnnet
lienMonitor
majorVersion
messageSender
murexFamily
murexGroup
murexStrategy
murexType
murexTypology
ndParentTradeId
ndParentTradeTypology
nettingId
originatingTradeId
passed
payerParty
pendingFixingFlag
portfolioName
portfolioUniqueName
prevBusinessEvent
prevBusinessVersion
prevCashflowId
prevCashflowVersion
prevCashflowWorkflowStatus
prevEventDate
prevPayerParty
prevReceiverParty
prevSettlementAmount
prevSettlementCurrency
prevSettlementDate
productTaxonomy
receiverParty
settlementAmount
settlementCurrency
settlementDate
settlementMethod
settlementType
stackFlow
stpIndicator
trackingId
trackingUuid
tradeId
tradeOriginalSourceSystem
tradeVersion
tradeWorkflowStatus
versionedTradeId
```

The inventory includes current and previous lifecycle data, business-version lineage, settlement economics, trade and portfolio identifiers, counterparty and entity data, netting and STP indicators, and Murex metadata.

## Composite lifecycle status

Statuses are represented as three-part values:

```text
QUEUED+Pending Exception+Pending Operator
NETTED+Pending Ack+NA
WAITING+Cashflow Suppression+Pending Verification
```

The apparent dimensions are:

1. Primary lifecycle status, such as `QUEUED`, `READY`, `NETTED`, `FAILED`, or `WAITING`.
2. Processing or exception subtype, such as `Pending Exception`, `Pending Ack`, or `Cashflow Suppression`.
3. Operational responsibility or verification state, such as `Pending Operator`, `Pending Verification`, or `NA`.

## Representative transitions

The following transitions illustrate the intended normal, exception, netting, split, and suppression paths:

| previousStatus | action | nextStatus |
| --- | --- | --- |
| NA+NA+NA | New | PROJECTED+NA+NA |
| PROJECTED+NA+NA | Materialize | QUEUED+NA+NA |
| QUEUED+NA+NA | ValidateDirect | READY+NA+NA |
| READY+NA+NA | Release | RELEASED+NA+NA |
| RELEASED+NA+NA | Settle | SETTLED+NA+NA |
| SETTLED+NA+NA | NostroMatch | NOSTRO_MATCHED+NA+NA |
| PROJECTED+NA+NA | Net | NETTED+NA+NA |
| QUEUED+NA+NA | Split | SPLIT+NA+NA |
| QUEUED+NA+NA | Suppress | CASHFLOW_SUPPRESSED+NA+NA |
| QUEUED+NA+NA | SwiftSuppress | SWIFT_SUPPRESSED+NA+NA |
| QUEUED+NA+NA | TechFail | QUEUED+Pending Exception+NA |
| QUEUED+NA+NA | Fail | FAILED+NA+NA |
| NETTED+NA+NA | UnNet | QUEUED+NA+NA |
| QUEUED+Pending Exception+NA | UnNet | DEAD+NA+NA |
| WAITING+Pending Exception+Pending Operator | Submit | WAITING+Pending Exception+Pending Verification |
| WAITING+Pending Exception+Pending Verification | Approve | READY+NA+NA |
| WAITING+Pending Exception+Pending Verification | Reject | WAITING+Pending Exception+Pending Operator |
| CASHFLOW_SUPPRESSED+NA+NA | ManualUnSuppress | WAITING+Undo Cashflow Suppression+Pending Verification |
| WAITING+Undo Cashflow Suppression+Pending Verification | Approve | QUEUED+NA+NA |
| SPLIT+NA+NA | Release | SPLIT+Released+NA |
| SPLIT+Released+NA | Settle | SPLIT+Settled+NA |
| SPLIT+Settled+NA | NostroMatch | SPLIT+NostroMatched+NA |
| NETTED+Settled+NA | ReplayStatusWriteBack | NETTED+Settled+NA |

The complete transition matrix is retained in the source document. Notable action semantics are state-dependent: `UnNet` can reopen a netted cashflow to `QUEUED` or terminate a queued/exception cashflow as `DEAD`.

## Persistence objects

The design references these persistence objects:

- `ratan_stella_message_event_source` — event-source and business-lineage attributes.
- `ratan_cashflow_scbml_history` — SCBML history and current-version maintenance.
- `ratan_cashflow_scbml_message` — current SCBML message representation.
- `ratan_cashflow_cutoff_info` — cashflow cutoff information.
- `ratan_cashflow_holding_message` — holding messages updated or inserted on demand.
- `ratan_cashflow_affirmation_status` — affirmation status persisted conditionally.

## Design implications and unresolved semantics

The design distinguishes recoverable technical failures from terminal business failures, preserves a split-specific lifecycle, and models cashflow suppression separately from SWIFT suppression. It also supports maker/checker workflows and idempotent replay status write-back.

The source does not define the operational meaning of `NA+NA+NA`, the precise distinction between `Fail`, `TechFail`, and `TestFail`, the precedence between SCBML and request affirmation, or which event-source fields are immutable during updates. The spellings `ReInstate`, `RevertToQueued`, and `RevertPenVerfication`, as well as the distinction between `NOSTRO_MATCHED+NA+NA` and `NETTED+NostroMatched+NA`, require implementation validation.
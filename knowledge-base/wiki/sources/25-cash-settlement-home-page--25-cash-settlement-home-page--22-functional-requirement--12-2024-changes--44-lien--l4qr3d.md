---
type: source
title: RATAN Cashflow Process with Lien - Function Specs
authors: []
year: 2024
url: ""
venue: Internal functional requirements
created: 2026-08-23
updated: 2026-08-23
tags: [ratan, lien, cashflow-migration, nstp, tds3, netting]
related: [ratan, tds3, murex, tds3-es, settlement-ops, lien-driven-cashflow-nstp, lien-aware-netting-and-auto-unnetting, trade-lien-notification-reconciliation, how-is-lien-removal-or-zero-lien-processed-in-ratan, what-is-the-authoritative-parent-trade-id-scbml-path-for-lien-correlation, can-tds3-es-support-per-cashflow-lien-lookups-at-ratan-volume, cashflow-migration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/Lien Settlement Process - Cashflow Migration/RATAN Cashflow Process with Lien - Function Specs.md"]
---
# RATAN Cashflow Process with Lien - Function Specs

## Summary

This functional requirement specifies that [[ratan]] must use trade-level lien information supplied by [[tds3]] to apply the system-defined **“LIEN on Trade”** maker/checker NSTP exception to associated cashflows received from [[murex]].

The requirement covers gross cashflows, interest cashflows, netting-resultant cashflows, lien-triggered reprocessing, and conditional auto-un-netting. The document is incomplete: its Function Flow section ends mid-sentence and provides no complete operational sequence, API contract, test evidence, or error-handling design.

## Core Requirement

When lien is placed on a trade or its lien amount changes, all associated cashflows, including interest, must be NSTP in RATAN with the **“LIEN on Trade”** exception.

The exception is system predefined and maker/checker controlled. Settlement Ops users, including business-rule and data-ops profiles, cannot update or remove it.

RATAN uses `Lien_Monitoring`, a new internal logical-model field copied from the parent trade. The stated NSTP condition is:

```text
Cashflow.Lien_Monitoring != empty
```

## Correlation and Latest-Event Lookup

RATAN must correlate a cashflow to its parent trade by original trade ID:

- Cashflow field: `Parent_Trade_Id`
- TDS3 trade field: `Trade_Id`

For each gross cashflow, RATAN is expected to obtain the lien state from the latest event of the corresponding parent trade. The source does not define the event version, timestamp, ordering rule, response contract, or failure handling that makes a trade record authoritative as the latest event.

## Netting and Reprocessing Rules

For a netting-resultant cashflow, RATAN must evaluate every component cashflow's parent trade. If any component parent trade has lien, RATAN must apply **“LIEN on Trade”** to the resultant cashflow.

A netted cashflow may be auto-un-net when all of the following are true:

- It is not `READY + Pending Ack`, `RELEASED`, or `SETTLED`.
- It does not already have **“LIEN on Trade.”**
- The latest parent-trade event indicates lien placement.

A cashflow must be reprocessed to create the exception when lien is newly detected and it meets one of these conditions:

- `WAITING` with `Sub Status Type == 'Pending Exception'`
- `HOLD`
- `READY`

The cashflow must not already have the lien exception.

## TDS3 Query and Notification Pattern

The proposed initial processing pattern is one [[tds3-es]] trade query per Murex cashflow, using the trade identifier from the cashflow. The document projects approximately 50,000 Murex cashflows daily. This is a projected workload, not demonstrated capacity evidence.

The source acknowledges an out-of-order arrival condition: a cashflow can arrive before the relevant trade update and initially lack the lien exception. A subsequent trade notification should update affected cashflows by original trade ID. The current design consumes `VALD` and `COMP` trade notifications “by priority,” but does not define treatment of other statuses.

## Logical and Physical Field Definitions

The source field definitions are reproduced verbatim. The `Parent_Trade_Id` path is visibly malformed or truncated and must not be treated as an implementation-ready contract.

```text
| Logical Model Fiedl | SCBML Path |
| --- | --- |
| Lien_Monitoring | (/scb:SCBML/scb:payload/scb:FPMLPayload/conf:trade|/scb:SCBML/scb:payload/scb:FPMLPayload/((*/(*:originalTrade|*:trade))|((*:novation|*:cancelReissue)/*:newTrade)))/conf:tradeHeader/conf:partyTradeInformation/scbextn:lienMonitoring |
```

```text
| **Logical Model Field** | **SCBML Path** |
| --- | --- |
| Parent_Trade_Id | /scb:SCBML/scb:payload/scb:cashflowPayload/scb:tradeReferenceInformation/scb:partyTradeIdentifier/conf:linkId[@linkIdScheme="[http://www.sc.com/coding-scheme/linkId/eve](http://www.sc.com/coding-scheme/linkId/eventId) |
```

```text
| **Logical Model Field** | **SCBML Path** |
| --- | --- |
| Trade_Id | (/scb:SCBML/scb:payload/scb:FPMLPayload/conf:trade|/scb:SCBML/scb:payload/scb:FPMLPayload/((*/(*:originalTrade|*:trade))|((*:novation|*:cancelReissue)/*:newTrade)))/conf:tradeHeader/conf:partyTradeIdentifier[conf:partyReference/@href="party1"]/conf:tradeId[@tradeIdScheme=[http://www.sc.com/coding-scheme/tradeId](http://www.sc.com/coding-scheme/tradeId)] |
```

## Limitations and Open Issues

- Lien removal, zero lien, cancellation, correction, and reversal behavior are unspecified.
- The immutable exception's system-resolution behavior is unspecified.
- `READY + Pending Ack` is not formally defined as a status/substatus combination.
- Auto-un-netting recovery, concurrency, audit, and component-state outcomes are unspecified.
- TDS3 ES capacity, caching, batching, retries, throttling, and fallback behavior are unspecified.
- The complete Function Flow is absent.

See [[lien-driven-cashflow-nstp]], [[lien-aware-netting-and-auto-unnetting]], and [[trade-lien-notification-reconciliation]].
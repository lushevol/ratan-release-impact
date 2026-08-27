---
type: source
title: Uber Message Analysis
authors: []
year: 2026
url: ""
venue: "Functional Requirement"
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, uber-message, functional-requirement, trade, cashflow]
related: [uber-message, full-state-event-attributed-messaging, fixing-schedule-cashflow-correlation, cashflow-sequence-and-count-completeness-control, pending-trade-validation-cashflow-control, non-economic-cashflow-amendment-handling, cashflow-business-and-message-versioning, cashflow-lineage-and-operational-visibility, trade-cashflow-correlation-by-trade-version, mo]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Uber Message Analysis.md"]
---
# Uber Message Analysis

## Source character

This document is an early-stage functional-requirement and scenario-analysis note. It proposes expectations for a consolidated Uber message covering trade, fixing notice, cashflow, and schedule activity. It is not an approved interface specification or tested implementation record.

## Proposed functional scope

Trade-level, cashflow-level, and fixing-notice-level activities are proposed triggers for Uber message generation. The listed triggers are trade booking and market events, trade-status updates, fixing and re-fixing, new cashflow generation, and cashflow-status updates.

Each message is expected to capture the latest and complete state for the parent trade, including trade, fixing notice, cashflow, and schedule information. For a business event, the message should also identify the cashflows published because of that event, although the mechanism is unresolved.

Fixing and re-fixing require a unique correlation identifier linking the fixing notice, schedule, and underlying cashflow. The note also proposes a generation timestamp and investigates whether trade tracking and cashflow versions can provide the required technical sequence identifier.

## Settlement scenarios

### Cashflow processing

The source illustrates five new cashflows for one trade. `Sequence` ranges from 1 to 5 and `Count` is 5 for every row; the final row carries an exception.

| | Trade ID | Cashflow ID | Business Event | Sequence | Count | Exception |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | T1 | C1 | New | 1 | 5 | |
| 2 | T1 | C2 | New | 2 | 5 | |
| 3 | T1 | C3 | New | 3 | 5 | |
| 4 | T1 | C4 | New | 4 | 5 | |
| 5 | T1 | C5 | New | 5 | 5 | Exception |

The document does not establish whether these rows represent separate messages, elements within one message, or a generic event batch.

### Non-economic amendment control

The example shows two new cashflows for `T1`, followed by withdrawal events for those cashflows and replacement new cashflows for `T2`. The withdrawal of `T1/C2` is flagged as potentially causing duplicate payment.

| | Trade ID | Cashflow ID | Business Event | Sequence | Count | Exception |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | T1 | C1 | New | 1 | 2 | |
| 2 | T1 | C2 | New | 2 | 2 | |
| 3 | T1 | C1 | Withdrawal | 1 | 4 | |
| 4 | T1 | C2 | Withdrawal | 2 | 4 | Exception, may have duplicate payment |
| 5 | T2 | C3 | New | 3 | 4 | |
| 6 | T2 | C4 | New | 4 | 4 | |

The source does not explain the `T1` to `T2` replacement linkage or define whether withdrawal is a distinct stamped event or a direct cancellation.

### Middle Office trade validation

The validation example marks every cashflow as `PENDING_TRADE_VALIDATION = Yes`. The final row carries an exception. Trade confirmation is expected to match the trade and cashflow business version/event.

| | Trade ID | Cashflow ID | Business Event | PENDING_TRADE_VALIDATION | Sequence | Count | Exception |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | T1 | C1 | New | Yes | 1 | 5 | |
| 2 | T1 | C2 | New | Yes | 2 | 5 | |
| 3 | T1 | C3 | New | Yes | 3 | 5 | |
| 4 | T1 | C4 | New | Yes | 4 | 5 | |
| 5 | T1 | C5 | New | Yes | 5 | 5 | Exception |

## Operational and technical questions

The note identifies unresolved requirements for an exception-resolution SLA, Middle Office ownership, latest trade and cashflow version handling, error-message inclusion in Uber, and production failure turnaround metrics.

It also raises whether Settlement Instruction can be included in Protocol Buffers, to be checked with Olexiy, and proposes an ad hoc retrieval query based on `Trade ID + Asof Time`.

No Protocol Buffers schema, API signature, event envelope, identifier algorithm, retry model, access-control model, or operational runbook is supplied. These omissions are tracked in [[what-is-the-authoritative-uber-message-schema-and-event-envelope]], [[what-is-the-authoritative-uber-withdrawal-and-cancellation-semantics]], and [[what-is-the-uber-exception-sla-and-middle-office-operating-model]].
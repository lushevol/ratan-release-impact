---
type: entity
title: Uber Message
created: 2026-08-24
updated: 2026-08-24
tags: [uber-message, integration, trade, cashflow, settlement]
related: [full-state-event-attributed-messaging, fixing-schedule-cashflow-correlation, cashflow-sequence-and-count-completeness-control, pending-trade-validation-cashflow-control, cashflow-business-and-message-versioning, cashflow-lineage-and-operational-visibility]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Uber Message Analysis.md"]
---
# Uber Message

## Definition

The Uber message is a proposed consolidated integration payload for trade, fixing notice, cashflow, and schedule activity under a parent trade.

The requirements propose that it contain the latest and complete parent-trade state while identifying the cashflows affected by the business event that triggered message generation. The message is therefore related to [[full-state-event-attributed-messaging]] rather than a simple event delta.

## Proposed triggers

Message generation is proposed for:

- Trade booking and market events
- Trade-status updates
- Fixing and re-fixing
- New cashflow generation
- Cashflow-status updates

## Expected controls

The source proposes:

- A unique fixing–schedule–cashflow correlation ID
- Trade and cashflow version information
- A message-generation timestamp
- `Sequence` and `Count` fields for publication completeness
- An ad hoc query using `Trade ID + Asof Time`
- Possible inclusion of Settlement Instruction in Protocol Buffers

## Ownership and implementation status

The producer, consumers, technical owner, serialization contract, message boundary, and operational ownership are unknown. Middle Office is named as the proposed exception-handling team, but this is not an approved operating model.

The Uber message should not be treated as an authoritative production interface until the questions in [[what-is-the-authoritative-uber-message-schema-and-event-envelope]] and [[what-is-the-uber-exception-sla-and-middle-office-operating-model]] are resolved.
---
type: concept
title: Full-State Event-Attributed Messaging
created: 2026-08-24
updated: 2026-08-24
tags: [messaging, event-attribution, full-state, trade, cashflow]
related: [uber-message, cashflow-business-and-message-versioning, cashflow-lineage-and-operational-visibility, trade-cashflow-correlation-by-trade-version, cashflow-version-concurrency-control]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Uber Message Analysis.md"]
---
# Full-State Event-Attributed Messaging

## Definition

Full-state event-attributed messaging combines a complete latest-state snapshot with an explicit indication of the objects affected by the triggering business event.

For the proposed [[uber-message]], the snapshot covers the parent trade, fixing notices, schedules, and cashflows. The event-attribution element must identify which cashflows were published because of the current event, even when all latest cashflows are included.

## Why it matters

A full snapshot supports consumer reconciliation and recovery, while event attribution supports incremental processing, audit, and prevention of unnecessary downstream actions. Without both dimensions, a consumer may be unable to distinguish newly affected cashflows from unchanged state.

## Unresolved design

The source suggests investigating trade tracking version and cashflow version, but does not define whether attribution uses versions, event IDs, correlation IDs, explicit flags, or a separate event section. It also does not establish that trade and cashflow versions can share the same numeric value.

This open design is tracked in [[how-are-event-published-cashflows-identified-in-a-full-uber-snapshot]] and [[what-is-the-authoritative-uber-message-schema-and-event-envelope]].
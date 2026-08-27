---
type: concept
title: LMS Business Event Tracking
created: 2026-08-24
updated: 2026-08-24
tags: [lms, business-events, topic-listening, cash-settlement, integration]
related: [lms, lifecycle-service, trade-service, cash-settlement-orchestration-process-in, cash-settlement-cashflow-domain-events, trade-service-trade-events, what-is-the-lms-integration-contract, what-filtering-and-event-selection-rules-govern-lms-topic-consumption]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/LMS Integration.md"]
---
# LMS Business Event Tracking

LMS Business Event Tracking is the source's mapping of named business milestones to listening topics:

- Lifecycle Service publishing a cashflow event to a query service: [[cash-settlement-orchestration-process-in]].
- Cashflow stamping completion: [[cash-settlement-cashflow-domain-events]].
- Trade Service successfully obtaining `leid` and trader information: [[trade-service-trade-events]].

This is only a topic-association inventory, not a complete integration contract. No filter logic is recorded for any row, and the source does not specify producers, consumers, payloads, processing actions, monitoring, retries, or reconciliation.

The documented topic names should not by themselves be interpreted as evidence of Kafka or of a relationship to a specific Query Service or stamping implementation.
---
type: query
title: What Filtering and Event-Selection Rules Govern LMS Topic Consumption?
created: 2026-08-24
updated: 2026-08-24
tags: [lms, event-filtering, topic-consumption, idempotency, cash-settlement]
related: [lms-business-event-tracking, cash-settlement-orchestration-process-in, cash-settlement-cashflow-domain-events, trade-service-trade-events, what-is-the-lms-integration-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/LMS Integration.md"]
---
# What Filtering and Event-Selection Rules Govern LMS Topic Consumption?

## Question

Which messages on the three documented topics should be processed, and what rules govern selection, validation, ordering, and duplicate handling?

## Evidence

The source includes a `Filter logic` column, but all three rows are blank. It supplies no authoritative event-type, key, status, legal-entity, trader, currency, or cashflow criteria.

## Information needed

- Event-type and payload-field selection rules for each topic.
- Whether all messages are consumed when no explicit filter applies.
- Keying, deduplication, idempotency, versioning, and ordering requirements.
- Handling of missing or invalid `leid`, trader, and cashflow data.
- Offset, retry, DLQ, and replay behavior for rejected or failed events.
- Ownership and test evidence for the filtering policy.
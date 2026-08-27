---
type: entity
title: cash_settlement_cashflow_domain_events
created: 2026-08-24
updated: 2026-08-24
tags: [messaging-topic, cash-settlement, cashflow-stamping, event-integration, Kafka, domain-events, reinstatement]
related: [lms-business-event-tracking, ssi-stamping-service, ssi-stamping-message-contract, what-is-the-lms-integration-contract, what-filtering-and-event-selection-rules-govern-lms-topic-consumption, cashflow-status-restoration, reinstatement-domain-event-history, process-in-topic, kafka-persistent-retry-and-dlt-recovery]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/LMS Integration.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Uber Development Testing/Uber Dev Testing Question.md"]
---
# cash_settlement_cashflow_domain_events

`cash_settlement_cashflow_domain_events` is a domain-event topic associated with cash settlement.

## Business event

The LMS Integration source lists this topic for the business event **“Cashflow stamping complete.”**

That source does not identify the publisher, subscriber, schema, event type, or the state transition that constitutes stamping completion. Its association with [[ssi-stamping-service]] and [[ssi-stamping-message-contract]] is thematic only; it does not establish a canonical SSI Stamping contract or producer.

## Reinstatement test notes

The reinstatement test notes also name `cash_settlement_cashflow_domain_events` as the domain-event topic involved in reinstatement testing.

For `C06810142009`, the Camunda task-fail API was called, but the UI history did not show the event. The notes attribute this to a message-format error on this topic and mark the issue as fixed. They do not provide the corrected schema, version, serialized message, or downstream projection evidence.
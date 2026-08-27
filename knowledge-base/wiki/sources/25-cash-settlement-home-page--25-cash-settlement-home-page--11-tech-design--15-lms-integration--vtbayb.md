---
type: source
title: LMS Integration
authors: []
year: 2023
url: ""
venue: Internal technical design
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, lms, integration, event-tracking, technical-design]
related: [lms, trade-service, cash-settlement-orchestration-process-in, cash-settlement-cashflow-domain-events, trade-service-trade-events, lms-business-event-tracking, what-is-the-lms-integration-contract, what-filtering-and-event-selection-rules-govern-lms-topic-consumption, does-query-service-in-lms-integration-mean-ratan-query-service, lifecycle-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/LMS Integration.md"]
---
# LMS Integration

## Summary

This outline-level technical-design document records three business-event-to-topic associations for an LMS integration. It does not define LMS, the messaging transport, publishers, consumers, message schemas, filtering, delivery guarantees, failure handling, or test results.

The document contains headings for requirements, BAU test cases, and a developer mind map. The referenced class-diagram image, `attachments/image2023-4-19_15-31-41.png`, is unavailable in the supplied source content.

## Business event tracking

| SN | Business Event Tracking | Topic Listening | Filter logic |
| --- | --- | --- | --- |
| 1 | Lifecycle service publish cashflow event to query service | Cash_Settlement_Orchestration_Process_In | |
| 2 | Cashflow stamping complete | cash_settlement_cashflow_domain_events | |
| 3 | trade service got leid and trader successfully | Trade_Service__Trade_Events | |

The source directly associates the three stated milestones with [[cash-settlement-orchestration-process-in]], [[cash-settlement-cashflow-domain-events]], and [[trade-service-trade-events]]. Every `Filter logic` cell is blank.

## Scope and limitations

- The first row names [[lifecycle-service]] and a generic “query service,” but does not identify the actual consumer implementation. It does not establish that the recipient is [[ratan-query-service]].
- The cashflow-stamping row does not name a producer, consumer, event type, or completion-state definition. It does not establish that [[ssi-stamping-service]] produces the event.
- The Trade Service row does not define `leid`, trader-data semantics, or the meaning of successful processing.
- The source names `LMS Integration Test case recording` but contains no test scenarios, expected outcomes, execution evidence, owner, or result.
- The source does not state that the listed topic identifiers use Kafka; Kafka-specific implementation assumptions are unsupported.

## Open contract gaps

The incomplete design is tracked by [[what-is-the-lms-integration-contract]]. The missing event-selection, filtering, idempotency, and ordering rules are tracked by [[what-filtering-and-event-selection-rules-govern-lms-topic-consumption]]. The identity of the generic query service is tracked by [[does-query-service-in-lms-integration-mean-ratan-query-service]].
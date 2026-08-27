---
type: source
title: Kafka Listener Consumption Time Tracking Design Scheme
authors: []
year: 2026
url: "https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/11472308"
venue: "Cash Settlement Home Page technical design"
created: 2026-08-24
updated: 2026-08-24
tags: [kafka, spring-kafka, observability, cash-settlement, ratan, central-monitoring]
related: [ratan, ratan-pss, murex, tds3, kafka-listener-consumption-time-tracking, spring-kafka-record-interceptor, ratan-central-business-monitoring, authoritative-kafka-consumer-timing-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Kafka Listener Consumption Time Tracking Design Scheme.md"]
---
# Kafka Listener Consumption Time Tracking Design Scheme

## Summary

This proposed technical design addresses non-intrusive consumption-time tracking for Kafka listeners in the RATAN cash-settlement group service. It supports Story 11472308, “RATAN business monitor--central monitoring,” and the related PSS central-monitoring requirement.

The design proposes a shared `KafkaConsumerTimingInterceptor` implementing Spring Kafka `RecordInterceptor<K,V>`. The interceptor receives the complete `ConsumerRecord`, extracts a tracking identifier from the record headers, builds a monitoring trace string, logs it, and forwards the original record without modification to the existing listener.

The document is a design proposal. It does not provide implementation details, benchmark results, test evidence, or production observations.

## In-Scope Topic and Listener Inventory

The source provides the following inventory verbatim:

| topic name | Business | source | comment |
| --- | --- | --- | --- |
| Cash_Settlement_Group_Message_Inbound | scbml cashflow | 1, MB 2, adapor service(when message from murex, change to scbml) | CashflowInboundListener scbml |
| TDS3_Trade_Message_Process_In | stell trade | | TDS3DefaultTradeInboundListener |
| TDS3_Trade_Murex_Message_Process_In | murex trade | | TDS3MurexTradeInboundListener |
| cash_settlement_cashflow_domain_events | | | CashflowDomainEventListener |
| Cash_Settlement_Cashflow_Status_Response_In | stell ack | | CashflowStatusSyncUpAckListener |
| tdsx_uber_message_json_inbound | | MB | TdsxUberMessageListener uber |
| Cash_Settlement_Mxg_Group_Complete_Event | murex , adaptor service | | MxgGroupCompleteListener |

The inventory covers SCBML cashflow inbound messages, STELL trade messages, Murex trade messages, cashflow domain events, cashflow status acknowledgements, Uber orchestration messages, and Murex group-completion events.

The source uses the terms `adapor service` and `stell`; these spellings are preserved in the inventory, but the authoritative service and source-system names require confirmation.

## Proposed Design

The proposed processing flow is:

```text
ConsumerRecord arrives
  -> KafkaConsumerTimingInterceptor implements RecordInterceptor<K,V>
  -> Extract trackingId from header
  -> Build log trace string
  -> log.info(trace string)
  -> Existing listener handles the message
```

The interceptor is intended to transmit the original record without modification. Existing listeners such as `CashflowInboundListener`, `TDS3DefaultTradeInboundListener`, `TDS3MurexTradeInboundListener`, `CashflowDomainEventListener`, `CashflowStatusSyncUpAckListener`, `TdsxUberMessageListener`, and `MxgGroupCompleteListener` remain responsible for their existing business processing.

The illustrative trace string is:

```text
.#|#.ms_in#ratan-cash-settlement-group-management-service_**businessDescription**#${trackingId}#Timer#end#1750063879234
```

The apparent fields include a millisecond timing value or marker, `ms_in`, the service identifier `ratan-cash-settlement-group-management-service`, a business description, a tracking identifier, `Timer`, `end`, and an epoch timestamp. The source does not define a formal grammar for this string.

## Design Goals

| **Zero Intrusion** | No modification to any existing Listener source code |
| --- | --- |

| **Full Coverage** | One codebase automatically applies to all existing/future Listeners |
| --- | --- |

| **Extensible** | Tracking string format, Header Key, and output method can all be independently extended |
| --- | --- |

| **Testable** | Each component has a single responsibility, facilitating unit testing |
| --- | --- |

| **Disabled** | Interceptor activation can be controlled via configuration switches, without affecting business logic |
| --- | --- |

These goals describe intended properties rather than demonstrated runtime results.

## Interception-Mechanism Comparison

| Solution | Advantages | Disadvantages |
|---|---|---|
| **Spring Kafka RecordInterceptor** ✅ | Native Spring support; no need to modify any Listeners; always obtains the complete `ConsumerRecord` (including headers); automatically adapts to all new Listeners | Requires Spring Kafka 2.3+ |
| Spring AOP Aspect | Framework independent | Some Listener method signatures lack the `ConsumerRecord` parameter, making it impossible to directly retrieve headers; requires writing pointcuts for each signature, resulting in high maintenance costs |
| Kafka's native ConsumerInterceptor | Decoupled from the framework | Cumbersome registration; not managed by the Spring container; cannot inject Spring Beans |
| Modifying each Listener | Intuitive | Highly intrusive; requires adding logic every time a new Listener is added; violates the Open/Closed Principle |

The conclusion is that `RecordInterceptor` is the preferred mechanism for a Spring Kafka implementation because it provides access to the complete record, including headers, without requiring changes to each listener.

## Evidence Boundaries and Open Issues

The source does not establish:

- The exact meaning of `ms_in`, including whether it represents consumer delay, listener processing duration, or another latency.
- The canonical Kafka header key for `trackingId`.
- Whether timing is recorded once per record or once per retry or redelivery attempt.
- The trace-string grammar, escaping rules, versioning policy, or downstream parser.
- Behavior for missing, malformed, or duplicated tracking headers.
- Logging behavior when listener processing fails or a record reaches a dead-letter topic.
- The deployed Spring Kafka version.
- How the interceptor is registered across all listener containers.
- Whether the topic and listener inventory is complete and authoritative.
- Privacy, security, and log-volume controls for tracking identifiers.
- Monitoring thresholds or service-level indicators derived from the timing records.

The claim of full listener coverage therefore depends on deployment configuration and consistent use of the Spring Kafka container integration.

## Related Wiki Context

This design extends the existing RATAN and cash-settlement knowledge base with a cross-cutting observability mechanism. It is related to [[ratan]], [[murex]], [[tds3]], and [[ratan-pss]]. It concerns transport-level consumer observability and does not alter the business semantics of existing cashflow events, status contracts, or query-service read models.

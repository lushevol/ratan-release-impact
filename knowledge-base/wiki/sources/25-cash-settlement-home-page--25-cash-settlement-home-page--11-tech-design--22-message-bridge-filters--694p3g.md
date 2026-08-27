---
type: source
title: Message Bridge Filters
authors: []
year: 2026
url: ""
venue: Internal technical design
tags: [message-bridge, messaging, filtering, solace, kafka, cash-settlement]
related: [message-bridge, domain-owned-message-filtering, message-topic-consolidation, message-header-propagation, message-bridge-filtering-vs-domain-service-filtering, should-message-bridge-own-business-filters, can-domain-services-handle-pass-through-message-volume, what-is-the-canonical-message-filter-sdk-and-configuration-contract, ratan, scbml]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Message Bridge Filters.md"]
---
# Message Bridge Filters

This technical-design document evaluates whether [[message-bridge|Message Bridge]] (MB) should retain first-level business filters after consuming messages from Solace queues, or become a technical pass-through routing layer with filtering owned by domain services.

The document presents a proposed direction, not an approved decision. Its conclusion section is blank.

## Current and Proposed Responsibilities

MB currently applies configured first-level filters and routes selected messages after consumption from Solace queues. The proposed model moves business filtering to domain services while MB passes consumed messages through and carries headers onward.

The stated trade-off is between centralized operational efficiency and clearer domain ownership:

- MB-managed filtering centralizes configuration and reduces downstream processing, log volume, and Kafka storage.
- Domain-owned filtering separates business logic from the integration layer but increases downstream processing, logs, and Kafka usage.
- The source specifically states that 99% of BCS settlement-flow volume would be filtered. This claim applies only to that flow and is not supported by a measurement period or capacity test.

## Source Plan

|  | MB filter | MB remove filter |
| --- | --- | --- |
| PROs | Filter centrally managed Low pressure on domain service Less log space Less Kafka space | Clear domain service boundary |
| CONs | MB maintain business logic | Higher pressure on domain service for additional filter, such as for BCS settlement flow, 99% of volume will be filtered More log space required More kafka space required |
| Changes required | NA | 1. Message Bridge to remove the Filter logic 1. Pass through on consumption 2. Headers carrier 2. Target topics need to be combined: 1. 1. 4, TDS3_All_Trade_Message_Process_In,Confirmation_Orchestration_Process_In,TDS3_Trade_Murex_Message_Process_In,TDS3_Trade_Message_Process_In 2. 2, Settlement_Orchestration_Process_In, Cash_Settlement_Group_Message_Inbound 3. 2, Settlement_Ssi_Notification_Event_In, Settlement_Ssi_Notification_Event_In_RT_Decom 4. 2, Settlement_Cashflow_Status_In, Cash_Settlement_Cashflow_Status_In 5. 2, Settlement_Receiver_Ack_Nack_In, Cash_Settlement_Receiver_Ack_Nack_In 3. Additional filters: 1. Integrate with the new config solution ?? 2. A SDK to be provided to each service to filter on 1. SCBML 2. UBER/JSON 3. Header 3. Group Service 1. Cashflow: consuming to new topic & Filter out BCS 2. Trade: self routing logic on sender 4. Trade service: self routing logic on sender & Filter on capture system 5. Trade control service: Filter on capture system 6. LMS Service: build filter on publishing based on BIC 7. BCS Cashflow Service: 1. Build filter on consuming cashflow scbml 2. build filter on publishing based on BIC for LMS |
| Conclusion |  |  |

## Proposed Scope

The proposed migration includes:

- removing MB filter logic;
- pass-through consumption and header carriage;
- consolidation of five sets of target topics;
- a proposed configuration solution and reusable filtering SDK for [[scbml|SCBML]], UBER/JSON, and headers;
- service-specific filter and routing changes for Group Service, Trade service, Trade control service, LMS Service, and BCS Cashflow Service.

The source does not define filter expressions, header semantics, ownership, rollout sequencing, compatibility criteria, rollback procedures, or acceptance metrics.

## Related Architecture

The proposal affects message ingress to [[ratan|RATAN]] and may affect [[kafka-consumer-poll-timeout|Kafka consumer poll timing]], [[environment-specific-kafka-consumer-configuration|consumer configuration]], and [[kafka-listener-consumption-time-tracking|consumer timing observability]]. It also proposes SCBML-aware filtering and references TDS3 and Murex-related topics.

See [[domain-owned-message-filtering]] for the responsibility model, [[message-topic-consolidation]] for the exact topic scope, and [[message-bridge-filtering-vs-domain-service-filtering]] for the documented trade-off.
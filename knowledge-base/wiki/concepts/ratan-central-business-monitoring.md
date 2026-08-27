---
type: concept
title: RATAN Central Business Monitoring
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, business-monitoring, central-monitoring, cash-settlement, pss]
related: [ratan, ratan-pss, kafka-listener-consumption-time-tracking, kafka-consumer-timing-interceptor]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Kafka Listener Consumption Time Tracking Design Scheme.md"]
---
# RATAN Central Business Monitoring

## Definition

RATAN central business monitoring is the monitoring capability motivating the proposed Kafka listener consumption-time tracking design. Its purpose in this source is to make message-consumption timing visible for cash-settlement processing across multiple Kafka listener flows.

The related requirement is associated with Story 11472308 and the PSS central-monitoring context represented by [[ratan-pss]].

## Technical Contribution

The proposed [[kafka-consumer-timing-interceptor]] emits a trace containing timing information, a service identifier, business description, tracking identifier, and an end timestamp. This creates a possible bridge between Kafka transport activity and business-oriented monitoring.

The source does not define the monitoring platform, parser, alert thresholds, service-level indicators, retention policy, or ownership model.

## Scope Boundary

The design instruments RATAN’s Kafka consumer pipeline. It does not instrument Murex, MB, STELL, or the adaptor service as producer systems. Those systems are identified as sources for selected topics, while the listeners are the monitored consumers.

## Open Monitoring Questions

A usable central-monitoring contract still needs to define the authoritative duration, trace schema, retry representation, missing-header behavior, downstream ingestion path, privacy controls, and alerting thresholds. These questions are tracked in [[authoritative-kafka-consumer-timing-contract]].

---
type: query
title: Can Domain Services Handle Pass-Through Message Volume?
tags: [open-question, messaging, capacity, kafka, performance, bcs]
related: [domain-owned-message-filtering, message-bridge, message-bridge-filtering-vs-domain-service-filtering, kafka-consumer-poll-timeout, environment-specific-kafka-consumer-configuration, kafka-listener-consumption-time-tracking]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Message Bridge Filters.md"]
---
# Can Domain Services Handle Pass-Through Message Volume?

Moving filters from [[message-bridge|Message Bridge]] to domain services would increase the number of messages that services consume, inspect, log, and retain through Kafka.

The source states that 99% of BCS settlement-flow volume would be filtered downstream. This claim is material but unsubstantiated, and it applies only to the BCS settlement flow.

## Measurements Needed

- current and forecast message volume for every affected topic;
- matched, discarded, malformed, retried, and dead-lettered message counts;
- consumer CPU, memory, batch, and poll-time performance;
- Kafka traffic, retention, storage, and partition capacity;
- filtering latency and end-to-end processing latency;
- impact of replay and failure recovery;
- validation of the BCS settlement-flow 99% discard-rate claim.

Measurement should use the observability mechanisms described by [[kafka-listener-consumption-time-tracking]] and account for consumer limits described by [[kafka-consumer-poll-timeout]].
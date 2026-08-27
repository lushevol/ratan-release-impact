---
type: entity
title: RecordInterceptor<K,V>
created: 2026-08-24
updated: 2026-08-24
tags: [spring-kafka, kafka, extension-point, interception]
related: [spring-kafka-record-interceptor, kafka-consumer-timing-interceptor, kafka-listener-consumption-time-tracking]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Kafka Listener Consumption Time Tracking Design Scheme.md"]
---
# RecordInterceptor<K,V>

## Identity

`RecordInterceptor<K,V>` is the Spring Kafka interception extension point selected by the design for observing consumed records. It is used as the implementation contract for [[kafka-consumer-timing-interceptor]].

## Function in the Design

The interceptor receives the complete `ConsumerRecord`, including headers, before the existing listener handles the message. This enables header-based tracking-ID extraction while preserving the original record and avoiding changes to individual listener implementations.

The mechanism is intended to support all configured listeners, including the cashflow, trade, acknowledgement, Uber, and Murex group-completion listeners listed in the source design.

## Constraints

The source states that Spring Kafka 2.3 or later is required. Actual compatibility depends on the deployed Spring Kafka version and the listener-container registration configuration.

`RecordInterceptor<K,V>` provides an interception point, but it does not define the business meaning of “consumption time,” the monitoring trace grammar, or retry and failure semantics. Those remain open in [[authoritative-kafka-consumer-timing-contract]].

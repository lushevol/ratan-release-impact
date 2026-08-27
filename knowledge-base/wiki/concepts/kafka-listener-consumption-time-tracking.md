---
type: concept
title: Kafka Listener Consumption-Time Tracking
created: 2026-08-24
updated: 2026-08-24
tags: [kafka, observability, listener, latency, cash-settlement]
related: [kafka-consumer-timing-interceptor, spring-kafka-record-interceptor, ratan-central-business-monitoring, authoritative-kafka-consumer-timing-contract, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Kafka Listener Consumption Time Tracking Design Scheme.md"]
---
# Kafka Listener Consumption-Time Tracking

## Definition

Kafka listener consumption-time tracking is the instrumentation of Kafka consumer processing so that each consumed record can be associated with a tracking identifier, timing data, and a monitoring event. In the proposed RATAN design, tracking is added through a shared interceptor rather than by changing individual business listeners.

The design applies to multiple cash-settlement message flows, including SCBML cashflow messages, STELL and Murex trade messages, cashflow domain events, acknowledgements, Uber messages, and Murex group-completion events.

## Proposed Lifecycle

```text
ConsumerRecord arrives
  -> Read trackingId from record headers
  -> Construct monitoring trace
  -> Log the trace
  -> Forward the unchanged record
  -> Existing listener processes the record
```

This is transport observability. It should not be interpreted as a change to the business processing performed by the listener or the source system that produced the message.

## Intended Properties

- **Zero intrusion:** existing listener source code is not modified.
- **Coverage:** one configured interceptor can apply across listener containers.
- **Extensibility:** the tracking format, header key, and output method can evolve independently.
- **Testability:** extraction, trace construction, and logging can be separated into independently testable responsibilities.
- **Configuration control:** activation can be enabled or disabled without changing listener business logic.

These properties are proposed design goals, not verified implementation or production results.

## Timing Semantics That Require Definition

The phrase “consumption time” is ambiguous. It may refer to record arrival, listener invocation delay, listener processing duration, end-to-end message latency, or time until acknowledgement or offset commit. The source does not select one of these meanings.

A production contract should define:

1. The start and end timestamps.
2. The unit and clock source.
3. Whether the duration measures each delivery attempt.
4. How retries, redeliveries, and dead-letter processing are represented.
5. Whether records without a tracking identifier are logged, rejected, or sampled.

The unresolved contract is tracked in [[authoritative-kafka-consumer-timing-contract]].

## Relationship to Business Monitoring

The timing event is intended to connect Kafka processing behavior with [[ratan-central-business-monitoring]]. It should retain a clear distinction between:

- The Kafka record and its transport metadata.
- The listener’s processing lifecycle.
- The business event represented by the record.
- The monitoring system’s interpretation of the emitted log.

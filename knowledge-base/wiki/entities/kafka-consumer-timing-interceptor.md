---
type: entity
title: KafkaConsumerTimingInterceptor
created: 2026-08-24
updated: 2026-08-24
tags: [kafka, spring-kafka, interceptor, observability, ratan]
related: [spring-kafka-record-interceptor, kafka-listener-consumption-time-tracking, ratan-central-business-monitoring, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Kafka Listener Consumption Time Tracking Design Scheme.md"]
---
# KafkaConsumerTimingInterceptor

## Identity

`KafkaConsumerTimingInterceptor` is a proposed shared component for RATAN Kafka listener observability. It is intended to implement `RecordInterceptor<K,V>` and intercept `ConsumerRecord` instances before they reach existing listeners.

## Responsibilities

The proposed flow assigns the component these responsibilities:

1. Receive a `ConsumerRecord`.
2. Extract `trackingId` from the record header.
3. Build a monitoring trace string.
4. Emit the trace through `log.info`.
5. Forward the original record without modification.

The component is not intended to replace or alter `CashflowInboundListener`, `TDS3DefaultTradeInboundListener`, `TDS3MurexTradeInboundListener`, `CashflowDomainEventListener`, `CashflowStatusSyncUpAckListener`, `TdsxUberMessageListener`, or `MxgGroupCompleteListener`.

## Illustrative Trace

```text
.#|#.ms_in#ratan-cash-settlement-group-management-service_**businessDescription**#${trackingId}#Timer#end#1750063879234
```

This example is not yet a formal monitoring contract. The source does not specify the header key, timing definition, failure behavior, retry semantics, or downstream parser.

## Configuration

The design proposes configuration-controlled activation so that the interceptor can be enabled or disabled without changing listener business logic. The specific configuration property, default value, rollout process, and behavior during configuration failure are not defined.

## Evidence Status

This component is a design proposal. No implementation, unit test, integration test, performance result, or production observation is provided.

---
type: concept
title: Spring Kafka RecordInterceptor
created: 2026-08-24
updated: 2026-08-24
tags: [spring-kafka, kafka, interception, observability, open-closed-principle]
related: [kafka-consumer-timing-interceptor, kafka-listener-consumption-time-tracking, ratan-central-business-monitoring]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Kafka Listener Consumption Time Tracking Design Scheme.md"]
---
# Spring Kafka RecordInterceptor

## Role

`RecordInterceptor<K,V>` is the proposed Spring Kafka extension point for observing consumed `ConsumerRecord` instances before existing listener handling. It provides access to the complete record, including its headers, which enables extraction of a tracking identifier without changing listener method signatures or listener source code.

## Why It Is Preferred

The design selects `RecordInterceptor<K,V>` because it:

- Integrates with the Spring Kafka listener infrastructure.
- Avoids modifications to each existing listener.
- Provides access to the complete `ConsumerRecord`, including headers.
- Can apply to future listeners when they use the configured listener-container integration.
- Supports separation of extraction, trace construction, and logging for testing.

The proposed implementation component is [[kafka-consumer-timing-interceptor]].

## Alternatives Considered

### Spring AOP Aspect

Spring AOP is framework-independent at the interception level, but some listener signatures do not expose `ConsumerRecord`. Retrieving headers would therefore be unreliable or impossible without pointcuts tailored to individual signatures, increasing maintenance cost.

### Kafka Native `ConsumerInterceptor`

Kafka’s native `ConsumerInterceptor` is decoupled from Spring, but the source identifies cumbersome registration, lack of Spring-container management, and inability to inject Spring beans as disadvantages.

### Per-Listener Modification

Adding timing code to every listener is direct but intrusive. It would require repeated changes when listeners are added and conflicts with the Open/Closed Principle, which favors extending behavior without modifying established business logic.

## Compatibility Constraint

The source states that Spring Kafka 2.3 or later is required. The deployed version is not supplied and must be verified before implementation.

## Coverage Limitation

Using `RecordInterceptor<K,V>` does not by itself prove full coverage. All target listeners must be attached to listener containers where the interceptor is registered. Registration scope, configuration, and exceptions must be documented.

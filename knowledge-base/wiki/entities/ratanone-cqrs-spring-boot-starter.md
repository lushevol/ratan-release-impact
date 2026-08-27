---
type: entity
title: ratanone-cqrs-spring-boot-starter
created: 2026-08-24
updated: 2026-08-24
tags: [ratanone, cqrs, kafka, jdbc, jackson]
related: [domain-event-serializer-registration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratanone-Foundation release note.md"]
---
# ratanone-cqrs-spring-boot-starter

`ratanone-cqrs-spring-boot-starter` provides CQRS domain-event infrastructure for Kafka publishing and JDBC mapping.

## ObjectMapper integration

The release changes both the Kafka domain-event publisher and the domain-event JDBC mapper to use the `ObjectMapper` automatically injected by Spring. Independently created mappers should not be used when custom payload serializers or deserializers must participate in domain-event processing.

This supports type-specific handling for `DomainEvent<T>`, including payloads such as `RatanCashSettlementData`.

## Shared topic agreement

The release note records an agreement to use:

```text
cash_settlement_cashflow_domain_events
```

The topic name alone is not a complete event contract. Envelope structure, schema versioning, partitioning, ordering, retention, and consumer compatibility remain unspecified.

See [[domain-event-serializer-registration]] for the registration pattern.

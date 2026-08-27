---
type: concept
title: Domain-Event Serializer Registration
created: 2026-08-24
updated: 2026-08-24
tags: [domain-events, jackson, objectmapper, kafka, jdbc, serialization]
related: [ratanone-cqrs-spring-boot-starter]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratanone-Foundation release note.md"]
---
# Domain-Event Serializer Registration

Domain-event serializer registration configures type-specific Jackson serializers and deserializers for `DomainEvent<T>` payloads through the Spring-managed `ObjectMapper`.

## Required integration pattern

A custom Jackson module is registered on the injected mapper:

```java
@Configuration
public class ObjectMapperConfig {
    @Autowired
    private ObjectMapper objectMapper;

    @PostConstruct
    public void registerModules() {
        objectMapper.registerModule(
            new SimpleModule("RatanCashSettlementDataModel")
                .addSerializer(
                    RatanCashSettlementData.class,
                    new RatanCashflowRecordJacksonSerializer()
                )
                .addDeserializer(
                    RatanCashSettlementData.class,
                    new RatanCashflowRecordJacksonDeserializer()
                )
        );
    }
}
```

Both the Kafka publisher and JDBC mapper must use this same Spring-managed mapper for the registration to affect domain-event processing.

The release note names `cash_settlement_cashflow_domain_events` as the shared Kafka topic by agreement, but does not define the complete event contract.

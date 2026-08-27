---
type: source
title: RatanOne Foundation Release Note
authors: []
year: 2025
url: ""
venue: ""
created: 2026-08-24
updated: 2026-08-24
tags: [ratanone, foundation, release-note, distributed-locking, cash-settlement]
related: [ratanone-lock-spring-boot-starter, ratanone-data-model, ratanone-cqrs-spring-boot-starter, cashflow-message-parsing-and-enrichment, domain-event-serializer-registration, tdsx-schema-migration, watchdog-lock-renewal, ratan-distributed-lock-ownership, redisson, redis]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratanone-Foundation release note.md"]
---
# RatanOne Foundation Release Note

This release note covers `6.7.3.14-lock-SNAPSHOT`, `6.7.3.13-lock-SNAPSHOT`, and `6.7.3.12-SNAPSHOT`. Its main areas are distributed locking, foundation framework upgrades, cashflow data-model changes, message parsing and enrichment, domain-event serialization, CQRS infrastructure, and SCBML/XPath mapping.

## Release 6.7.3.14-lock-SNAPSHOT

The release note states:

> Fixed dead lock issue

No affected service, deadlock mechanism, or validation evidence is provided. This statement should be treated as a release outcome rather than evidence that all deadlock classes have been eliminated.

## Release 6.7.3.13-lock-SNAPSHOT

### Foundation upgrades

`ratanone-lock-spring-boot-starter` adds Redisson as the distributed-lock framework and upgrades:

- Spring Boot from `3.4.1` to `3.4.4`
- Spring Cloud from `2024.0.0` to `2024.0.1`

Camunda is upgraded to `7.23.0`. Domain services must upgrade their Spring Boot parent to `3.4.4`.

### Lock API semantics

The second `run` parameter changes from lock expiration time to lock-acquisition wait time.

Previous form:

```java
public void run(String key, long expireMilliSeconds, String actionInProgress, CommandNoReturn commandNoReturn) {
```

The second parameter represented lock expiration time in milliseconds. If execution exceeded that duration, the lock would be released.

New form:

```java
public void run(String key, long waitTimeSeconds, String actionInProgress, CommandNoReturn commandNoReturn)
```

The second parameter represents how long the application waits to acquire a lock that is currently unavailable, in seconds. Fixed expiration is deprecated for this use case because Redisson is expected to retain the lock while the application is executing through its watchdog behavior.

Failsafe is not required for lock scenarios because Redisson provides automatic acquisition retry. The release note does not define retry intervals, maximum attempts, interruption behavior, or failure exceptions.

This change is specific to the `ratanone-lock-spring-boot-starter` API and its domain-service consumers. It should not be generalized to all Redis or Redisson locking implementations.

## Release 6.7.3.12-SNAPSHOT

### `ratanone-data-model`

The data model changes include:

1. TDSX proto schema upgrade from `V7.1-RELEASE` to `V7.8-RELEASE`.
2. Conversion of some fields from single values to arrays according to the upgraded schema.
3. Corrections to internal field value types.
4. Addition of a new internal field for FXU.

The affected fields are not enumerated, so downstream compatibility and migration requirements require further verification. TDSX is kept distinct from the existing `TDS3` entity unless another source establishes that they are aliases or connected systems.

### `ratanone-commons`

`ProtoTypeUtils.class` converts `Timestamp` values using UTC.

The commons library also provides format-independent cashflow parsing and enrichment through `CashflowMessageHolder<?>`, `CashflowParserHelper`, and `XpathEnum`:

```java
CashflowMessageHolder<?> messageHolder =
    CashflowParserHelper.init({your scmbl or json});

messageHolder.parseString(XpathEnum.CASHFLOW__CASHFLOW_ID);

Map<XpathEnum, Object> fieldMap = Maps.newHashMap();
fieldMap.put(CASHFLOW__EVENT_REASON, "Reversal");
fieldMap.put(CASHFLOW__MINOR_VERSION, 10);

messageHolder.enrich(fieldMap);
messageHolder.getMessage();
```

The intended workflow is to initialize a holder from an SCBML or JSON message, parse a field through `XpathEnum`, provide updates in a field map, enrich the message, and retrieve the resulting message. The source contains formatting and identifier inconsistencies in this example, so it should not be treated as a complete authoritative API specification without checking foundation-code unit tests.

`XpathEnum.class` provides cashflow mappings between the logical model and XPath, including value types. Derived fields are supported separately.

### `ratanone-cqrs-spring-boot-starter`

The Kafka domain-event publisher and domain-event JDBC mapper use the `ObjectMapper` automatically injected by Spring rather than independently created mappers. This permits `DomainEvent<T>` payload types to use type-specific Jackson serializers and deserializers.

Example configuration:

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

The source records an agreement to use the shared Kafka topic:

```text
cash_settlement_cashflow_domain_events
```

The topic name is specified, but the release note does not define the event envelope, schema versioning, partition key, ordering, retention, or consumer compatibility contract.

The source also provides this context example:

```java
RatanApiContextHolder.getContext().set("payloadStrategy", "JSON");
RatanApiContextHolder.getContext().get("payloadStrategy");
```

The lifecycle and allowed values for `payloadStrategy` are not defined.

### `ratanone-scbml-lm-converter`

The converter:

1. Upgrades the Rosetta mapping version to `v7.8-RELEASE`.
2. Adds automatic generation of `XpathEnum`.

The release note does not specify the generation source, build stage, generated-file ownership, or validation process.

## Migration and verification considerations

Consumers should distinguish lock-acquisition wait time from execution duration and lock retention. Redisson watchdog configuration, client timeouts, process pauses, network failures, and long-running actions require verification.

The scalar-to-array data-model changes may affect serializers, XPath mappings, persistence, and downstream consumers. The complete event contract for `cash_settlement_cashflow_domain_events` also requires separate documentation.

## Related wiki topics

The locking changes provide release-level evidence for [[watchdog-lock-renewal]], [[lock-ttl-and-expiry]], and [[ratan-distributed-lock-ownership]]. They are related to [[redisson]] and [[redis]], but the release-specific API semantics should remain scoped to `ratanone-lock-spring-boot-starter`.

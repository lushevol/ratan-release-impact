---
type: source
title: Settlement Processing Optimization Data Flow Segregation
authors: []
year: 2026
url: "https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/6325957"
venue: Internal technical design
tags: [cash-settlement, kafka, data-flow-segregation, partitioning, technical-design]
related: [cash-settlement-home-page, query-service, kafka-country-based-data-flow-segregation, two-level-kafka-domain-partitioning, ratan-domain-partitioner, kafka-topic-vs-partition-data-segregation, what-is-the-authoritative-kafka-country-partitioning-and-fallback-contract, does-country-based-kafka-partitioning-improve-query-service-status-sync-latency]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/[Settlement processing optimization", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/[Settlement processing optimization] Data flow segregation.md"] Data flow segregation.md"] Data flow segregation.md"]
created: 2026-08-24
updated: 2026-08-24
---
# Settlement Processing Optimization Data Flow Segregation

This technical-design proposal addresses cross-country contention in Cash Settlement processing. It identifies a shared workflow as a potential source of payment-processing lag and reports slow cashflow-status synchronization from [[query-service]] to the UI.

The motivating scenario is a UK batch job delaying CN real-time payments. The proposed mitigation is country-based Kafka workload segregation.

## Observed country distribution

| Country | FMID amount |
| --- | ---: |
| SG | 4 |
| GB | 2 |
| IN | 2 |
| CN | 30 |
| DE | 1 |
| MY | 2 |

The proposal's illustrative allocation gives GB 80% of partitions and groups CN with lower-volume countries in the remaining 20%. The document does not provide throughput, processing-cost, or SLA evidence to justify that allocation.

## Options considered

### Topic-level segregation

Each country receives a dedicated Kafka topic derived from the base topic, such as `Cash_Settlement_Orchestration_Process_In`.

- Producers determine the target country topic from onboarded-country configuration.
- Consumers subscribe to every country-specific topic.
- This provides stronger topic-level isolation but adds topic, consumer, ACL, monitoring, retention, replay, and onboarding overhead.

### Partition-level segregation

One topic is retained, but its partitions are logically allocated to configured country groups.

- Producers send a `DomainPartitionKey`.
- `RatanDomainPartitioner` routes messages with a custom two-level strategy.
- Existing producers without the custom key should use Kafka's built-in partitioning behavior.
- The source states that consumers need “No change,” but its configuration changes the consumer key deserializer. Compatibility is therefore unproven.

The partition-level option is the more developed proposal. See [[kafka-topic-vs-partition-data-segregation]].

## Design principles

1. Partition groups are logical and configuration-driven.
2. The design supports exactly two partitioning levels: a group key and an intra-group key.
3. Only producers using `DomainPartitionKey` should receive segregated routing; unchanged producers should retain existing behavior.
4. Partition-group ranges are recalculated when topic partitions are increased. Groups therefore do not permanently own fixed partition ranges.
5. Default routing is required to avoid message loss when custom routing cannot be applied.

## Configuration model

```java
@ConfigurationProperties(prefix = "ratanone.kafka-producer")
public class PartitionProperties {

    private List<PartitionGroup> partitionGroup;

    @Getter
    @Setter
    public static class PartitionGroup {

        private List<String> groupName;

        private Double rate;
    }

}
```

```yml
spring:
  kafka:
    consumer:
      key-deserializer: com.scb.ratan.cashflow.entrypoint.message.config.DomainPartitionKeyDeserializer
    producer:
      key-serializer: com.scb.ratan.cashflow.entrypoint.message.config.DomainPartitionKeySerializer
      properties:
        partitioner.class: com.scb.ratan.cashflow.entrypoint.message.config.RatanDomainPartitioner

ratanone:
  kafka-producer:
    strategy: cashflow-country
    partition-group:
      - groupName:
        - GB
        rate: 0.8
      - groupName:
        - SG
        - IN
        - CN
        - DE
        - MY
        rate: 0.2
```

The configuration definition calls the nested type `PartitionGroup`, while implementation excerpts use `PartitionProperties.PartitionGroupRate` and `getPartitionGroups()`. The authoritative configuration and implementation contract is unresolved.

## Routing behavior

`RatanDomainPartitioner` applies the following routing sequence:

1. Use partition `0` when the topic has one partition.
2. Use round-robin routing when the key is null.
3. Use Kafka's built-in key partitioner when no configured helper is available.
4. Delegate `DomainPartitionKey` routing to `DomainPartitionHelper`.
5. Use Kafka's built-in key partitioner for all other key types.

The domain helper:

- identifies the configured partition group from `partitionGroupKey`;
- computes a weighted partition range from group rates and topic partition count;
- hashes `partitionKey` within that range; and
- falls back to Kafka's built-in partitioner for unconfigured groups, insufficient partition capacity, or out-of-range calculations.

See [[two-level-kafka-domain-partitioning]] and [[ratan-domain-partitioner]].

## Key serialization contract

```java
public class DomainPartitionKeySerializer implements Serializer<DomainPartitionKey> {

    @Override
    public void configure(Map<String, ?> configs, boolean isKey) {
        Serializer.super.configure(configs, isKey);
    }

    @Override
    public byte[] serialize(String topic, DomainPartitionKey domainPartitionKey) {

        String keyStr = domainPartitionKey.getPartitionGroupKey() + "." + domainPartitionKey.getPartitionKey();
        return keyStr.getBytes();
    }

    @Override
    public byte[] serialize(String topic, Headers headers, DomainPartitionKey dataPartitioningKey) {
        return Serializer.super.serialize(topic, headers, dataPartitioningKey);
    }

    @Override
    public void close() {
        Serializer.super.close();
    }

}
```

```java
public class DomainPartitionKeyDeserializer implements Deserializer<DomainPartitionKey> {

    @Override
    public void configure(Map<String, ?> configs, boolean isKey) {
        Deserializer.super.configure(configs, isKey);
    }

    @Override
    public DomainPartitionKey deserialize(String s, byte[] bytes) {

        String keyStr = new String(bytes);

        String[] keyAttrs = keyStr.split("\\.");

        DomainPartitionKey dataPartitioningKey = new DomainPartitionKey();

        dataPartitioningKey.setPartitionGroupKey(keyAttrs[0]);
        dataPartitioningKey.setPartitionKey(keyAttrs[1]);

        return dataPartitioningKey;
    }

    @Override
    public DomainPartitionKey deserialize(String topic, Headers headers, byte[] data) {
        return Deserializer.super.deserialize(topic, headers, data);
    }

    @Override
    public DomainPartitionKey deserialize(String topic, Headers headers, ByteBuffer data) {
        return Deserializer.super.deserialize(topic, headers, data);
    }

    @Override
    public void close() {
        Deserializer.super.close();
    }

}
```

The delimiter-based format does not define escaping, null handling, explicit character encoding, schema versioning, or backward compatibility for legacy key types.

## Distribution-test findings

For a 36-partition topic configured with `GB=0.8` and `SG, IN, CN, DE, MY=0.2`, the samples show:

- GB traffic is directed to the first 29 partitions.
- Configured non-GB traffic is directed to the final seven partitions.
- HK, which is not configured, follows the default partitioner and is distributed across all partitions.
- Larger random samples produce relatively even distribution within an assigned range.
- Small samples exhibit expected hash-distribution variance.

The test cases also show that:

- a one-partition topic sends all traffic to partition `0`;
- partition groups may overlap when there are more groups than partitions;
- changing the topic partition count changes calculated group ranges; and
- changing group rates or adding groups can remap future records.

The tests demonstrate routing distribution, not improved end-to-end payment latency or UI synchronization latency.

## Risks and unresolved decisions

- The expected rate-validation behavior is unspecified for totals other than `1.0`, zero or negative rates, duplicate country membership, and missing countries.
- Rounding each weighted allocation to at least one partition can exceed the topic partition count and create overlap.
- `Math.abs(partitionKey.hashCode())` does not safely normalize `Integer.MIN_VALUE`.
- Increasing Kafka partitions can break stable per-key partition assignment for future records and may affect ordering, consumer load, replay, and diagnosis.
- The stated “consumer side — No change” conflicts with the configured `DomainPartitionKeyDeserializer`.
- Default partitioner fallback protects availability but can reintroduce cross-country contention for unknown or invalidly configured traffic.
- The capacity allocation shown is not aligned to the listed FMID counts: CN has 30 FMIDs while GB has two.

This is a proposal, not evidence of a production decision or demonstrated performance improvement. Open governance and validation work is tracked in [[what-is-the-authoritative-kafka-country-partitioning-and-fallback-contract]] and [[does-country-based-kafka-partitioning-improve-query-service-status-sync-latency]].
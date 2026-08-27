---
type: entity
title: RatanDomainPartitioner
tags: [kafka, partitioner, cash-settlement, ratanone]
related: [two-level-kafka-domain-partitioning, kafka-country-based-data-flow-segregation, what-is-the-authoritative-kafka-country-partitioning-and-fallback-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/[Settlement processing optimization", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/[Settlement processing optimization] Data flow segregation.md"] Data flow segregation.md"] Data flow segregation.md"]
created: 2026-08-24
updated: 2026-08-24
---
# RatanDomainPartitioner

`RatanDomainPartitioner` is a proposed custom Kafka `Partitioner` for Cash Settlement producer routing.

It selects a partition through a configured `PartitionHelper` when a message key is a `DomainPartitionKey`. The proposed country strategy is implemented by `DomainPartitionHelper`; it first chooses a logical partition group and then hashes the secondary key inside that group's allocated range.

## Fallback contract

The proposed behavior preserves message delivery by falling back when custom routing is unavailable:

- one topic partition: return partition `0`;
- null key: use round-robin routing;
- unavailable helper or configuration: use Kafka's built-in key partitioner;
- non-`DomainPartitionKey`: use Kafka's built-in key partitioner;
- invalid domain-helper result: use Kafka's built-in key partitioner.

This is availability-oriented rather than strict isolation: unconfigured or malformed traffic can return to shared partitioning. See [[two-level-kafka-domain-partitioning]].

## Implementation uncertainty

The source uses inconsistent configuration names: `PartitionGroup` in the configuration class but `PartitionGroupRate` in helper code. It also asserts that consumers need no change despite configuring a custom key deserializer. These interfaces require validation before implementation.
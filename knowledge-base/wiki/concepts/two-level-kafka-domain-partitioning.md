---
type: concept
title: Two-Level Kafka Domain Partitioning
tags: [kafka, partitioning, hashing, weighted-routing, cash-settlement]
related: [ratan-domain-partitioner, kafka-country-based-data-flow-segregation, what-is-the-authoritative-kafka-country-partitioning-and-fallback-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/[Settlement processing optimization", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/[Settlement processing optimization] Data flow segregation.md"] Data flow segregation.md"] Data flow segregation.md"]
created: 2026-08-24
updated: 2026-08-24
---
# Two-Level Kafka Domain Partitioning

Two-level Kafka domain partitioning is a proposed routing model in which a `DomainPartitionKey` has two roles:

1. The first-level `partitionGroupKey` identifies a configured logical group, such as a country.
2. The second-level `partitionKey` is hashed to select a partition within that group's assigned range.

The model explicitly excludes partitioning deeper than two levels.

## Weighted group allocation

Each partition group has a relative rate. Given a topic partition count, the partitioner calculates a group offset and size from the configured rates, then maps the secondary key into that range.

For the illustrative 36-partition configuration, GB at rate `0.8` receives approximately 29 partitions, while the `0.2` group containing SG, IN, CN, DE, and MY receives approximately seven.

## Fallback and overlap

The design deliberately accepts fallback and partition overlap to avoid message loss:

- unknown groups use Kafka's built-in partitioner;
- a one-partition topic ignores group allocation;
- if partition capacity is insufficient, groups may share partitions;
- invalid computed ranges use the built-in partitioner.

This makes the design tolerant but prevents a guarantee of strict country isolation.

## Stability caveat

Partition ranges are recalculated after topic scaling or configuration changes. Future records for the same secondary key can therefore be routed to another partition. Any ordering, replay, consumer-assignment, or observability contract must account for remapping.

The proposed implementation also needs a formal allocation invariant. Per-group rounding with a minimum allocation of one can create ranges beyond the available partition count. See [[what-is-the-authoritative-kafka-country-partitioning-and-fallback-contract]].
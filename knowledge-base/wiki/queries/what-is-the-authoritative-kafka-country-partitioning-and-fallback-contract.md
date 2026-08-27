---
type: query
title: What Is the Authoritative Kafka Country Partitioning and Fallback Contract?
tags: [kafka, partitioning, configuration, fallback, cash-settlement]
related: [two-level-kafka-domain-partitioning, kafka-country-based-data-flow-segregation, ratan-domain-partitioner, kafka-topic-vs-partition-data-segregation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/[Settlement processing optimization", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/[Settlement processing optimization] Data flow segregation.md"] Data flow segregation.md"] Data flow segregation.md"]
created: 2026-08-24
updated: 2026-08-24
---
# What Is the Authoritative Kafka Country Partitioning and Fallback Contract?

The proposed country-based partitioning design does not define a complete operational contract.

## Decisions needed

- Which producer owns the authoritative country-to-FMID mapping?
- Must configured rates sum exactly to `1.0`, and how are under-allocation and over-allocation handled?
- Are zero, negative, null, or duplicate group rates valid?
- Can a country belong to more than one group?
- Is an unconfigured country sent to a dedicated default partition or Kafka's built-in partitioner?
- What allocation algorithm guarantees that all selected partitions are valid and that no unintentionally idle partitions remain?
- Under what conditions may groups share partitions?
- Is ordering by secondary key required across partition scaling or group-configuration changes?
- Is `PartitionGroup` or `PartitionGroupRate` the canonical configuration type?
- How will serializers and deserializers support mixed legacy and `DomainPartitionKey` producers and consumers?

## Why it matters

Fallback protects against message loss, but it can return unknown or invalid traffic to the shared workload that the proposal intends to isolate. A formal, tested contract is needed before this can be treated as a production routing decision.

See [[ratan-domain-partitioner]] and [[two-level-kafka-domain-partitioning]].
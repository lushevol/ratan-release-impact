---
type: concept
title: Kafka Country-Based Data Flow Segregation
tags: [kafka, cash-settlement, workload-isolation, country-routing]
related: [two-level-kafka-domain-partitioning, kafka-topic-vs-partition-data-segregation, ratan-domain-partitioner, query-service, cash-settlement-home-page]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/[Settlement processing optimization", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/[Settlement processing optimization] Data flow segregation.md"] Data flow segregation.md"] Data flow segregation.md"]
created: 2026-08-24
updated: 2026-08-24
---
# Kafka Country-Based Data Flow Segregation

Kafka country-based data flow segregation separates workloads by country or country group so that a batch workload in one jurisdiction is less likely to delay real-time processing in another.

The Cash Settlement proposal is motivated by a scenario in which UK batch activity can contend with CN real-time payment activity, contributing to processing and [[query-service]] status-synchronization lag.

## Isolation approaches

Segregation can occur at two levels:

- **Topic-level segregation:** publish each country to its own topic. This provides clearer operational isolation but requires consumers to subscribe to all relevant topics and increases Kafka operational overhead.
- **Partition-level segregation:** preserve one topic and assign country groups to logical partition ranges. This reduces consumer changes but supplies capacity-oriented, not absolute, isolation.

The source develops the partition-level option through [[two-level-kafka-domain-partitioning]].

## Limitations

Country isolation is conditional:

- groups may share partitions when topic capacity is insufficient;
- traffic for countries absent from configuration uses the default partitioner;
- group ranges change when a topic's partition count changes;
- configured capacity weights must be justified by actual workload and service objectives.

Accordingly, routing-distribution samples do not establish lower payment latency or faster UI synchronization. Those outcomes need end-to-end measurement.
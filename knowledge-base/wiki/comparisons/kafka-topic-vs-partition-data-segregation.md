---
type: comparison
title: Kafka Topic vs Partition Data Segregation
tags: [kafka, architecture, workload-isolation, cash-settlement]
related: [kafka-country-based-data-flow-segregation, two-level-kafka-domain-partitioning, ratan-domain-partitioner]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/[Settlement processing optimization", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/[Settlement processing optimization] Data flow segregation.md"] Data flow segregation.md"] Data flow segregation.md"]
created: 2026-08-24
updated: 2026-08-24
---
# Kafka Topic vs Partition Data Segregation

The Cash Settlement proposal compares country-specific Kafka topics with weighted partition groups in a single topic.

## Topic-level segregation

Topic-level routing sends each country to a distinct topic.

- **Isolation:** Stronger operational separation between country workloads.
- **Producer work:** Determine country-specific topic names.
- **Consumer work:** Subscribe to all country topic variants.
- **Operations:** More topics, ACLs, retention policies, monitoring, replay procedures, and onboarding configuration.
- **Scaling:** Country capacity can be managed independently at the topic level.

## Partition-level segregation

Partition-level routing keeps one topic and directs selected producers into country-group partition ranges.

- **Isolation:** Capacity-oriented; it weakens when groups overlap or fallback traffic uses default routing.
- **Producer work:** Use `DomainPartitionKey`, compatible serializer, and `RatanDomainPartitioner`.
- **Consumer work:** Claimed to be unchanged, but custom key deserialization makes that claim unverified.
- **Operations:** Fewer topics, but more complex partition-allocation configuration and skew monitoring.
- **Scaling:** Increasing topic partitions recalculates ranges and can remap future keys.

## Assessment

The source develops partition-level routing as the preferred implementation because it aims to avoid consumer subscription changes. That advantage must be tested against serializer compatibility, ordering requirements, partition scaling, and actual latency outcomes.

Topic-level segregation is operationally heavier but offers a clearer boundary where strict workload isolation is required. Neither option has measured evidence in the source demonstrating improvement to Query Service UI synchronization.
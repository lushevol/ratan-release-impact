---
type: query
title: Does Country-Based Kafka Partitioning Improve Query Service Status Sync Latency?
tags: [kafka, query-service, latency, performance, cash-settlement]
related: [query-service, kafka-country-based-data-flow-segregation, two-level-kafka-domain-partitioning, cash-settlement-home-page]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/[Settlement processing optimization", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/[Settlement processing optimization] Data flow segregation.md"] Data flow segregation.md"] Data flow segregation.md"]
created: 2026-08-24
updated: 2026-08-24
---
# Does Country-Based Kafka Partitioning Improve Query Service Status Sync Latency?

The source reports lag in cashflow-status synchronization to the UI and proposes country-based Kafka routing as a mitigation. Its distribution tests show partition selection behavior, but they do not measure processing latency, consumer lag, throughput, error rate, or UI synchronization time.

## Evidence required

A decision should be based on before-and-after tests covering:

- UK batch and CN real-time workloads running concurrently;
- producer throughput and partition-level traffic skew;
- Kafka consumer lag by country group and partition;
- end-to-end cashflow-status synchronization latency to the UI;
- effects of unknown-country fallback traffic;
- effects of topic partition scaling and configuration changes;
- failure, replay, and mixed key-serialization scenarios.

## Capacity concern

The sample configuration allocates 80% of partitions to GB, while the supplied FMID counts list CN as substantially larger. Allocation should be tied to measured message volume, processing cost, and agreed service-level objectives rather than FMID count alone.

This question connects the routing proposal to the reported [[query-service]] behavior.
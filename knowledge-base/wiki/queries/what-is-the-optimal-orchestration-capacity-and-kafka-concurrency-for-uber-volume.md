---
type: query
title: What Is the Optimal Orchestration Capacity and Kafka Concurrency for Uber Volume?
tags: [uber, cash-settlement, capacity-planning, kafka, orchestration, performance]
related: [cash-settlement-orchestration-inbound, orchestration, kafka, group-service, cashflow-lifecycle-service, synchronous-kafka-to-camunda-orchestration, cash-settlement-performance-and-stress-testing]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/PT Orchestration Stg.md"]
---
# What Is the Optimal Orchestration Capacity and Kafka Concurrency for Uber Volume?

The staging study changed Kafka partitions and consumer-thread counts together and observed a 19.6% reduction in elapsed time from the lowest to highest tested configuration. It did not independently test Orchestration instance count, CPU allocation, Group or Lifecycle capacity, database capacity, or downstream-service scaling.

## Evidence

- 36 partitions and 9 consumers: 6,255 seconds.
- 36 partitions and 18 consumers: 5,927 seconds.
- 72 partitions and 9 consumers: 5,287 seconds.
- 72 partitions and 18 consumers: 5,027 seconds.
- Maximum CPU reached 98.2%–99.7% for Group, Lifecycle, and Orchestration in the fastest scenario.

## Open Work

Determine the best coordinated capacity configuration through repeated controlled tests that vary one dimension at a time:

1. Topic partitions and consumer threads.
2. Orchestration instances and CPU allocation.
3. Group, Lifecycle, Netting, and other downstream-service capacity.
4. Database and connection-pool capacity.
5. End-to-end completion, retry, duplicate, and tail-latency outcomes.

The tests should report P50, P95, P99, throughput, CPU profiles, queue lag, and business-level processing completeness for the 56,000-cashflow workload.
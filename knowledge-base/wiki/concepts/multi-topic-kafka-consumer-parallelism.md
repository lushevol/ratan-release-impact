---
type: concept
title: Multi-Topic Kafka Consumer Parallelism
created: 2026-08-24
updated: 2026-08-24
tags: [kafka, consumer-parallelism, throughput, cash-settlement]
related: [kafka, uber-message-topics, fmrp2, staging, database-connection-pool-saturation, synchronous-kafka-to-camunda-orchestration, downstream-http-limited-workflow-throughput, what-partition-and-db-pool-configuration-sustains-uber-message-load]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/[group", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/[group] PT of consuming messages on multiple Uber topics.md"] PT of consuming messages on multiple Uber topics.md"] PT of consuming messages on multiple Uber topics.md"]
---
# Multi-Topic Kafka Consumer Parallelism

Multi-topic Kafka consumer parallelism distributes a logical inbound workload across multiple Kafka topics so that more partitions and consumer assignments can process messages concurrently.

## Capacity Model

Topic splitting can increase available ingress parallelism, but useful concurrency is bounded by the smallest downstream capacity:

1. Active Kafka partitions and consumer assignments determine the maximum number of concurrently processed partitions.
2. Consumer concurrency and instance count determine how much of that partition capacity is used.
3. Group, lifecycle, orchestration, and database operations determine whether concurrent consumers can complete work.
4. Database connection-pool limits can turn additional concurrency into timeouts and retries rather than higher completed throughput.

## Evidence from Uber Message Tests

The seven-topic test used twelve configured partitions in both environments. [[fmrp2]] activated only nine partitions, while [[staging]] activated twelve.

For the staging 6-cashflow workload with database pool maximum 24, increasing from six to twelve partitions reduced completion time for 7,000 messages from 655 seconds to 431 seconds. This supports higher active partition count as a useful scaling lever for that specific condition.

The evidence does not establish a universally optimal partition count. Payload size, retry behavior, pool size, and environment configuration varied across other runs.

## Operational Guardrails

- Measure active assignments, not only configured partition count.
- Measure completed messages and cashflows separately from ingress and retry traffic.
- Establish database pool utilization and wait metrics before increasing consumer concurrency.
- Hold payload mix, retry accounting, pool configuration, and environment capacity constant when comparing configurations.
- Treat high CPU as a signal for further profiling, not proof of a single-component bottleneck.

This concept complements [[synchronous-kafka-to-camunda-orchestration]]: Kafka parallelism cannot by itself overcome synchronous downstream workflow limits.
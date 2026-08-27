---
type: query
title: What Partition and DB-Pool Configuration Sustains Uber Message Load?
created: 2026-08-24
updated: 2026-08-24
tags: [kafka, database-connection-pool, capacity-planning, uber-messages, performance-testing]
related: [multi-topic-kafka-consumer-parallelism, database-connection-pool-saturation, fmrp2, staging, kafka, uber-message-topics, grouping-management-service, cashflow-lifecycle-service, orchestration, cash-settlement-performance-and-stress-testing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/[group", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/[group] PT of consuming messages on multiple Uber topics.md"] PT of consuming messages on multiple Uber topics.md"] PT of consuming messages on multiple Uber topics.md"]
---
# What Partition and DB-Pool Configuration Sustains Uber Message Load?

## Question

What active Kafka partition count, consumer concurrency, and database connection-pool configuration can sustain the intended Uber-message workload with acceptable completion latency, retry rate, and error rate?

## Current Evidence

The strongest like-for-like staging comparison used 7,000 messages with one trade and six cashflows per message and a pool maximum of 24:

- Six partitions completed in 655 seconds.
- Twelve partitions completed in 431 seconds.

In [[fmrp2]], a maximum pool size of eight was associated with database timeout and connection-limit errors at higher producer rates. The source does not show pool utilization or database-side evidence sufficient to select a safe pool size.

## Gaps to Resolve

- Why were only nine of twelve configured partitions active in [[fmrp2]]?
- What exactly does the reported “Kafka consume TPS” measure?
- What pool utilization, wait time, active session, and database-limit values occur before failures?
- What production mix of 6-, 12-, and 40-cashflow trades must be supported?
- What latency, retry-rate, and error-rate thresholds define acceptance?
- Are Group Management Service and Group Service the same measured component?

## Proposed Test Design

Run repeated tests with a fixed payload mix and identical environment capacity. Vary one factor at a time: active partitions, consumer concurrency, and pool maximum. Report completed unique messages, completed cashflows, retries, errors, end-to-end latency percentiles, consumer lag, CPU saturation duration, and database pool/database metrics.

This query extends [[what-is-the-optimal-orchestration-capacity-and-kafka-concurrency-for-uber-volume]] with specific seven-topic and pool-sizing evidence.
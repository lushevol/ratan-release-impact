---
type: entity
title: Staging
created: 2026-08-24
updated: 2026-08-24
tags: [environment, cash-settlement, performance-testing]
related: [multi-topic-kafka-consumer-parallelism, cash-settlement-performance-and-stress-testing, kafka, cashflow-lifecycle-service, orchestration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/[group", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/[group] PT of consuming messages on multiple Uber topics.md"] PT of consuming messages on multiple Uber topics.md"] PT of consuming messages on multiple Uber topics.md"]
---
# Staging

Staging is a Cash Settlement performance-test environment used to test seven-topic Uber message consumption under six- and twelve-partition configurations.

## Recorded Configuration

- Four instances.
- Twelve Kafka partitions and twelve active concurrencies.
- Consumer concurrency of three.
- Database pool configurations with minimum two and maximum 24 or 56 connections.

## Observed Behavior

For the 6-cashflow workload with pool maximum 24, twelve partitions completed 7,000 messages in 431 seconds versus 655 seconds with six partitions.

The tested services—Group, [[cashflow-lifecycle-service]], and [[orchestration]]—reported CPU maxima between approximately 84% and 92% in staging runs. These peaks indicate high load, but the source does not provide profiling or saturation-duration evidence to identify a sole bottleneck.
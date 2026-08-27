---
type: entity
title: fmrp2
created: 2026-08-24
updated: 2026-08-24
tags: [environment, cash-settlement, performance-testing]
related: [multi-topic-kafka-consumer-parallelism, database-connection-pool-saturation, uber-message-topics, kafka]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/[group", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/[group] PT of consuming messages on multiple Uber topics.md"] PT of consuming messages on multiple Uber topics.md"] PT of consuming messages on multiple Uber topics.md"]
---
# fmrp2

fmrp2 is a Cash Settlement performance-test environment used for seven-topic Uber message consumption tests.

## Recorded Configuration

- Three instances.
- Twelve configured Kafka partitions, of which only nine were actually used.
- Consumer concurrency of three.
- Database pool configuration of minimum two and maximum eight connections.

## Observed Behavior

Database timeout and connection-limit errors were reported at higher send rates for 6-, 12-, and 40-cashflow payloads. Messages in at least one test were routed to retry queues after the database exception.

The reported successful consumer maximum TPS was generally close to 3 TPS for 6- and 12-cashflow workloads. These observations are environment-specific and do not establish a production capacity limit.

See [[multi-topic-kafka-consumer-parallelism]] and [[database-connection-pool-saturation]].
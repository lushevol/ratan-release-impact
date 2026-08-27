---
type: concept
title: Kafka Consumer Rebalance Risk in Cash Settlement
tags: [kafka, consumer-groups, rebalance, cash-settlement, reliability]
related: [kafka, ratan, cash-settlement-asynchronous-batch-processing, cash-settlement-batch-job-performance]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/PT Batch Group Stg.md"]
---
# Kafka Consumer Rebalance Risk in Cash Settlement

## Definition

Kafka consumer rebalance risk is the possibility that long-running message processing causes a consumer to exceed its liveness or polling limits, leading Kafka to redistribute partitions within the consumer group.

## Evidence from the staging test

The PT batch-group staging test split one input topic into seven topics and consumed Uber messages with four instances, twelve partitions, and concurrency of three. Longer processing times were identified as increasing the likelihood of Kafka rebalances.

In the worst-case workload, every message had a different `cashflowId`, preventing group-level filtering and maximizing downstream processing. The test recorded retry errors and duplicate consumption:

- 13,455 consumptions for 7,000 messages in one initial run.
- 13,549 consumptions for 7,000 messages after JVM and thread-pool tuning.

These observations are test-specific. They demonstrate that long processing and retries affected the measured workload, but they do not establish the exact rebalance mechanism without rebalance counts, partition assignments, consumer lag, and polling configuration.

## Operational implications

Performance validation should measure both throughput and processing correctness. In particular, test reports should distinguish:

- Messages polled.
- Messages successfully completed.
- Messages retried.
- Messages consumed more than once.
- Messages sent to a dead-letter path.
- Consumer-group lag and rebalance events.

A higher TPS result is not sufficient evidence of reliable once-only business processing.

## Missing configuration evidence

The source does not specify:

- `max.poll.interval.ms`.
- Poll interval.
- Consumer batch size.
- Partition assignments.
- Rebalance counts.
- Consumer lag.
- Retry limits or dead-letter behavior.

These values are required to determine whether processing duration is compatible with the Kafka consumer contract.

## Related concepts

This page extends the Kafka and asynchronous-processing context in [[kafka]] and [[cash-settlement-asynchronous-batch-processing]].
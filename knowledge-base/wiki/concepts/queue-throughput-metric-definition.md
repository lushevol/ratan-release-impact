---
type: concept
title: Queue Throughput Metric Definition
created: 2026-08-24
updated: 2026-08-24
tags: [performance-metrics, throughput, queueing, tps, observability]
related: [solace, solace-queue-splitting-for-asset-class-workloads, cash-settlement-performance-and-stress-testing, 25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--27-cash-settlement-performance--30-s--3u93uv]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/solace queue split PT for Uber.md"]
---
# Queue Throughput Metric Definition

Queue performance reporting must distinguish elapsed-time average throughput from sampled, peak, ingress, consumer, and end-to-end completion rates.

The Uber staging test reports both `average rate(msg/sec)` and `TPS(msg/sec)` without defining TPS. For example, `interestrate-msg` reports 26.7 average msg/s and 39 TPS, while `loan-msg` reports 8.4 average msg/s and 53 TPS. These values cannot be compared or used for sizing as equivalent measures.

A usable metric contract should specify:

- the measurement layer, such as broker ingress, queue consumption, Kafka processing, or successful downstream completion;
- the sampling or aggregation window;
- whether failures, retries, duplicates, and dead-lettered messages are included;
- whether the value is an average, percentile, maximum, or fixed-window sample; and
- the workload interval and concurrency configuration.

Until defined, the source's TPS column is ambiguous. The elapsed-time average is reproducible from total message count divided by total reported duration, but it also does not independently demonstrate end-to-end business completion.
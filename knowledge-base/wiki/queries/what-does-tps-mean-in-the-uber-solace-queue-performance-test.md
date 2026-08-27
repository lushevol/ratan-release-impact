---
type: query
title: What Does TPS Mean in the Uber Solace Queue Performance Test?
created: 2026-08-24
updated: 2026-08-24
tags: [solace, tps, performance-metrics, uber, staging]
related: [queue-throughput-metric-definition, solace-queue-splitting-for-asset-class-workloads, 25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--27-cash-settlement-performance--30-s--3u93uv]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/solace queue split PT for Uber.md"]
---
# What Does TPS Mean in the Uber Solace Queue Performance Test?

The test table reports both an elapsed-time `average rate(msg/sec)` and `TPS(msg/sec)`, but provides no definition of TPS, monitoring source, or aggregation window.

The distinction matters because TPS is higher than the reported average for every substantive queue and the total row has no TPS value. TPS may be a peak or sampled rate, but the current evidence does not establish this.

## Required Evidence

- The monitoring system and query used to obtain TPS.
- The sampling interval and aggregation method.
- Whether TPS measures Solace ingress, queue consumption, Kafka processing, or successful end-to-end completion.
- Treatment of retries, errors, duplicate processing, and backlog.
- The configuration and concurrency state during the sample.

Resolving this definition is required before the metric is used for capacity planning or compared with the 42.8 msg/s elapsed-time average reported for the full staging run.
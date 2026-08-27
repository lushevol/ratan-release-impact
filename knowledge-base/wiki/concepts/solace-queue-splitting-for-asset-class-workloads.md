---
type: concept
title: Solace Queue Splitting for Asset-Class Workloads
created: 2026-08-24
updated: 2026-08-24
tags: [solace, queueing, workload-partitioning, performance, cash-settlement]
related: [solace, queue-throughput-metric-definition, cash-settlement-performance-and-stress-testing, inbound-cashflow-group-management-bottleneck-control, 25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--27-cash-settlement-performance--30-s--3u93uv]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/solace queue split PT for Uber.md"]
---
# Solace Queue Splitting for Asset-Class Workloads

Solace queue splitting partitions heterogeneous inbound messages into separate queues, allowing queue-specific throughput, completion duration, and backlog behavior to be observed independently.

In the documented Uber staging test, traffic was split into asset-class or message-category queues. `interestrate-msg` and `com-msg` carried about 92.7% of all reported messages and ran substantially longer than the smaller queues. This makes them the primary capacity concerns for that specific run.

## Operational Value

Partitioning can support workload isolation by preventing a high-volume category from being indistinguishable within a shared queue. It can also make targeted scaling, consumer allocation, lag monitoring, and operational triage possible.

## Evidence Boundary

The available source has no pre-split control run, queue configuration, or demonstrated downstream bottleneck. It therefore does not prove that queue splitting improved throughput, reduced latency, or prevented a Group or Orchestration bottleneck.

Queue partitioning should be evaluated alongside downstream capacity controls described in [[inbound-cashflow-group-management-bottleneck-control]] and staging-test limitations described in [[cash-settlement-performance-and-stress-testing]].
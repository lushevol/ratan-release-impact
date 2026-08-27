---
type: query
title: What Caused Rule-Service Throughput to Plateau Below 31% CPU?
created: 2026-08-24
updated: 2026-08-24
tags: [performance-investigation, throughput, cpu, ratan-one, rule-service]
related: [rule-service-performance-testing, rule-service-performance-testing, ratan-one-rule-service, does-the-archived-rule-service-test-support-the-120-consumer-capacity-claim]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/Rule Service Performance Testing.md"]/Rule Service Performance Testing.md"]/Rule Service Performance Testing.md"]
---
# What Caused Rule-Service Throughput to Plateau Below 31% CPU?

## Observation

In the archived rule-service tests, throughput was reported as 11.04 requests per second at 10 users, 9.86 at 15 users, 9.42 at 20 users, and 10.17 at 30 users. Reported CPU stayed below 31%.

This pattern suggests saturation or variability outside aggregate CPU utilisation. The source does not investigate the cause.

## Candidate causes

- Downstream service, database, HBase, or network latency.
- Server-side request-thread, connection-pool, or HTTP-client limits.
- Rule-session locking, synchronization, or contention.
- Rule evaluation, payload parsing, serialization, or garbage-collection overhead.
- Load-generator capacity, test pacing, or connection reuse behaviour.
- Uneven load-balancer distribution across rule-service instances.
- Incomplete telemetry or aggregation that obscures per-instance saturation.

## Evidence needed

Collect per-instance request rate and latency, CPU breakdown, JVM heap and GC metrics, thread-pool and connection-pool occupancy, downstream-call timings, I/O waits, datastore telemetry, and JMeter client resource metrics. Repeat the test with controlled load increments and a verified request-arrival model.

The investigation should use the original report artifacts referenced by [[rule-service-performance-testing]] before interpreting the historical numbers as a current capacity baseline.
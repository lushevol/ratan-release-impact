---
type: concept
title: Netting Service Performance Testing
created: 2026-08-24
updated: 2026-08-24
tags: [netting, performance-testing, backend-elapsed-time, workload-benchmarking]
related: [netting-service, murex, 25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--22-netting-service-design--24-netti--1598489, what-are-the-netting-service-performance-slos-and-test-conditions, does-netting-service-meet-peak-murex-volume-and-retry-resilience-requirements]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Netting Service Design/Netting performance test.md"]
---
# Netting Service Performance Testing

Netting Service performance testing measures completion time and success for workload-defined Netting and Un-net operations. It must distinguish recorded point-test observations from validated operational capacity, scalability, and resilience claims.

## Documented Observations

The available test note reports successful standalone operations:

- Netting: 2,000 items in 53 seconds and 3,400 items in 83 seconds.
- Un-net: 2,000 items in 47 seconds and 3,400 items in 78 seconds.
- Combined scenario: Netting 1,996 items in 53 seconds, Un-net 1,996 items in 78 seconds, and one withdrawal retry operation in 64 seconds.

The test volumes were compared with a limited historical [[murex]] sample ranging from 1,250 to 1,960 items. The 3,400-item case is above that displayed range.

## Evidence Boundary

The source does not identify timing boundaries, environment, infrastructure, service release, data characteristics, run count, concurrency, or the criterion represented by `Success = true`. Its timings are therefore individual observations, not percentile latency measurements or contractual capacity figures.

In particular, a single successful “Withdrawal retry endurance” operation cannot validate endurance or retry recovery behavior.

## Scenario Sensitivity

At approximately 2,000 items, standalone Un-net took 47 seconds, while combined-scenario Un-net took 78 seconds for 1,996 items. This suggests that scenario conditions may affect elapsed time, but the test note does not identify the cause.

## Required Controls for Capacity Claims

A performance qualification should define:

- Workload shape, data composition, and expected peak volume.
- Environment, deployment version, database state, and dependent-service configuration.
- Timing start and end boundaries.
- Repetition count, variance, percentile targets, and throughput measures.
- Sequential and concurrent execution models.
- Failure injection, retry behavior, and recovery criteria.
- Explicit Netting Service SLOs or acceptance thresholds.

Open evidence and acceptance questions are tracked in [[what-are-the-netting-service-performance-slos-and-test-conditions]] and [[does-netting-service-meet-peak-murex-volume-and-retry-resilience-requirements]].
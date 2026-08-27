---
type: concept
title: FXU Operation Performance Testing
created: 2026-08-24
updated: 2026-08-24
tags: [fxu, performance-testing, load-testing, rate-limiting, sustained-load]
related: [fxu, find-currency2-by-currency1, apache-jmeter, what-are-the-performance-results-for-find-currency2-by-currency1]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FXU Technical Design/FXU Test Case/PT.md"]
---
# FXU Operation Performance Testing

FXU operation performance testing evaluates a named FXU operation under explicit workload-generation, rate-limiting, and duration settings. The available evidence concerns only [[find-currency2-by-currency1]].

## Recorded test dimensions

The source varies:

- **Rate Limiter:** `10`, `20`, and `ultimate`.
- **JMeter throughput:** `10` in the first two runs; not set in the `ultimate` runs.
- **Duration:** `360s` and `3600s`.

The two 360-second tests with nominal JMeter throughput `10` isolate the change between limiter values `10` and `20`. The `ultimate` tests change both limiter semantics and JMeter throughput configuration, so they are not directly comparable without workload details and observed metrics.

## Evidence required for conclusions

A test configuration alone cannot demonstrate operational performance. Each run should retain:

- Actual achieved throughput and its unit.
- Response-time percentiles and maximum response time.
- Error, timeout, and rejected-request counts.
- JMeter thread, ramp-up, connection, and dataset settings.
- Service, database, and infrastructure resource utilization.
- Limiter configuration semantics and observed enforcement.
- Environment, deployment version, test-data profile, acceptance thresholds, and pass/fail decision.

## Sustained-load scope

The recorded 3600-second run is a one-hour sustained-load configuration. Its existence does not establish that the operation remained stable for that period; completion and degradation evidence must be obtained from its dashboard or another authoritative report.

API load-test throughput is not necessarily equivalent to queue throughput or TPS. Metric names, units, and measurement boundaries need alignment before comparison with [[queue-throughput-metric-definition]].
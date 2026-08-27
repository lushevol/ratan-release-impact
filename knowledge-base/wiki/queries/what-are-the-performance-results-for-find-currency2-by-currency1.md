---
type: query
title: What Are the Performance Results for findCurrency2ByCurrency1?
created: 2026-08-24
updated: 2026-08-24
tags: [fxu, performance-testing, apache-jmeter, rate-limiting, open-question]
related: [find-currency2-by-currency1, apache-jmeter, fxu-operation-performance-testing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FXU Technical Design/FXU Test Case/PT.md"]
---
# What Are the Performance Results for findCurrency2ByCurrency1?

The test-case record links four Apache JMeter dashboards for [[find-currency2-by-currency1]], but does not capture their measured results in text.

## Evidence needed

For each run, obtain and record:

- Achieved throughput, including its unit.
- Response-time percentiles, mean, and maximum.
- Error, timeout, and rate-limit rejection counts.
- Test thread count, concurrency, ramp-up, and connection configuration.
- Environment, deployment version, and dataset equivalence.
- CPU, memory, database, and network saturation indicators.
- Acceptance threshold and pass/fail conclusion.

## Specific clarifications

1. What numeric limit and runtime behavior does `Rate Limiter ultimate` represent?
2. Why is the JMeter throughput setting absent in the `ultimate` configurations?
3. Did the 3600-second run complete without degradation, throttling anomalies, or resource exhaustion?
4. Are the attached screenshots or the linked dashboards the authoritative source for result values?

The configurations are preserved in [[25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--20-fxu-technical-design--13-fxu-test--s9nfxk]]. Until outcome evidence is recovered, no performance or SLA conclusion should be attributed to this operation.
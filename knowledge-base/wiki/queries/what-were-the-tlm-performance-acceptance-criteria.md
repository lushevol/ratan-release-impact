---
type: query
title: What Were the TLM Performance Acceptance Criteria?
created: 2026-08-22
updated: 2026-08-22
tags: [tlm, performance-testing, reconciliation, open-question]
related: [chg1016055, reconciliation, 51358-ratan-cash-settlement-accounting-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/FMRP China Cash Settlement Delivery Plan/Cash Settlement RATAN ONE 2026 Release Plan/Release On 2026-08-01 CR    RATAN Settlement Korea & FMRP FXO Tech Go-Live.md"]
---
# What Were the TLM Performance Acceptance Criteria?

## Question

What latency, throughput, concurrency, duration, error-rate, and resource-utilization thresholds governed the Korea TLM reconciliation API performance test?

## Current Evidence

The source links to Grafana and an Apache JMeter dashboard and records:

`response total item: 20286`

The release summary marks Performance Test as complete.

## Limitation

A response volume of 20,286 items does not by itself establish acceptable performance. The source does not transcribe:

- Response-time percentiles.
- Throughput.
- Concurrent users or requests.
- Test duration.
- Error rate.
- CPU, memory, or database utilization.
- Acceptance thresholds.
- Explicit pass/fail outcome.

## Evidence Needed

- Approved non-functional requirements.
- Apache JMeter aggregate and percentile reports.
- Grafana resource and service metrics.
- Test workload and data-volume definition.
- QA sign-off explicitly comparing actual results with thresholds.
---
type: query
title: Does Netting Meet the Required Throughput SLA at Production Volume?
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, netting, performance-sla, production-volume, benchmarking]
related: [cashflow-netting-performance, cash-settlement-performance-and-stress-testing, netting-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/Netting Test Result.md"]
---
# Does Netting Meet the Required Throughput SLA at Production Volume?

## Current evidence

[[cashflow-netting-performance]] records two indicative execution observations:

- 5,000 cashflows in 1.9 minutes.
- 1,994 cashflows in 47.3 seconds.

The reported throughputs are approximately 43.9 and 42.2 cashflows per second respectively. One record in the 5,000-cashflow run moved to `TechFailed` because booking-entity or counterparty `fmcode` was missing.

## Why this remains open

The source does not state a formal throughput, maximum-duration, availability, or error-rate target. It also omits the test environment, capacity configuration, workload concurrency, data mix, repetitions, and percentile results. The two measurements cannot yet validate production readiness or an SLA.

## Questions to resolve

1. What throughput, end-to-end duration, success rate, and error-rate criteria apply at expected and peak production volume?
2. Does `1.9min` mean exactly 114 seconds?
3. Were the two measurements executed with equivalent environment, configuration, data distribution, and concurrent workload?
4. How should `TechFailed` records be counted in netting acceptance metrics?
5. What repetition count, percentile measures, and load profile are required for a repeatable benchmark?

## Evidence needed

Obtain an approved performance test plan with production-like data, documented environment and configuration, repeated runs, concurrency conditions, output reconciliation, and acceptance thresholds.
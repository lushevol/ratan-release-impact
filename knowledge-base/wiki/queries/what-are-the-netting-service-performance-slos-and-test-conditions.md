---
type: query
title: What Are the Netting Service Performance SLOs and Test Conditions?
created: 2026-08-24
updated: 2026-08-24
tags: [netting, performance-slo, test-environment, un-net, performance-testing]
related: [netting-service, netting-service-performance-testing, 25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--22-netting-service-design--24-netti--1598489]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Netting Service Design/Netting performance test.md"]
---
# What Are the Netting Service Performance SLOs and Test Conditions?

The available performance note records successful Netting and Un-net point tests but provides no stated SLO, test environment, or measurement methodology.

## Questions

- What application version, infrastructure, database configuration, and dependent-service configuration produced the recorded timings?
- What records and data shape were included in each workload?
- What event marks the beginning and end of reported backend elapsed time?
- Are the reported durations individual runs, averages, medians, maxima, or another statistic?
- What duration, throughput, error-rate, or business cut-off requirement makes `Success = true`?
- Were Netting and Un-net tests isolated, sequential, or concurrent?
- Why did Un-net take 78 seconds for 1,996 items in the combined scenario but 47 seconds for 2,000 items in the standalone scenario?
- Are resource consumption, queue depth, database contention, and dependent-service latency measured?

## Known Evidence

[[25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--22-netting-service-design--24-netti--1598489]] reports:

- Netting at 2,000 and 3,400 items: 53 and 83 seconds.
- Un-net at 2,000 and 3,400 items: 47 and 78 seconds.
- Combined-scenario Un-net at 1,996 items: 78 seconds.

The source does not resolve the questions above.
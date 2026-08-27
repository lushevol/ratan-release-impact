---
type: query
title: What Caused Netting Performance Variance Between 2025-07-14 and 2025-07-15?
created: 2026-08-24
updated: 2026-08-24
tags: [netting, performance, benchmark-variance, dev, observability]
related: [netting-batch-processing-performance, 25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--27-cash-settlement-performance--19-n--qhw0o4, which-netting-batch-strategy-meets-performance-and-correctness-requirements, cash-settlement-performance-and-stress-testing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/Netting Test Result/Netting Cost Comparation.md"]
---
# What Caused Netting Performance Variance Between 2025-07-14 and 2025-07-15?

The recorded 1,999-cashflow Dev benchmarks differ substantially between 2025.07.14 and 2025.07.15. For the old `for each` implementation, `net` changed from 54.33s to 40.7s and `unet` changed from 42.84s to 36.19s.

The batch-size-1,000 key-holder `net` database time changed from 10,244ms to 5,947ms. These differences make direct cross-date ranking uncertain without environmental and workload controls.

## Questions to resolve

- Were the same code versions, configurations, and database schemas used on both dates?
- Did cashflow composition, data distribution, database size, indexes, cache state, or warm-up differ?
- What concurrent application and database load was present?
- Did transaction boundaries, connection-pool behavior, locks, or retries differ?
- Were the test harness, timing method, and start/end boundaries consistent?
- Can repeated runs provide median, percentile, and variance measurements for each variant?

## Decision impact

Until the variance is explained or bounded by controlled repeated trials, the results in [[netting-batch-processing-performance]] support a candidate for further testing but not a durable performance conclusion.
---
type: query
title: What Evidence Validates Ultra Cashflow Query Performance Against Legacy?
tags: [cash-settlement, cashflow-blotter, performance-testing, regression-testing, staging]
related: [ultra-cashflow-query, legacy-cashflow-query, cashflow-blotter-query-performance]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/Cashflow Blotter Page Size Performance.md"]
---
# What Evidence Validates Ultra Cashflow Query Performance Against Legacy?

The source reports that [[ultra-cashflow-query|Ultra]] has no performance shortcoming relative to [[legacy-cashflow-query|Legacy]], with an overall scale factor “around 5%,” under a Staging workload of 1,357,121 total records, 84,141 VD records, 50 users, and target TPS 1.

## Evidence Needed

- The missing Legacy performance report and the versioned test artifacts for both implementations.
- The formula, weighting, and sample population used for the reported “around 5%” factor.
- Confirmation that page size, request payloads, data snapshot, cache state, ramp-up, duration, and error thresholds were equivalent.
- Defined regression acceptance thresholds, including percentile and treatment of individual regressions.
- Production-like validation for expected volume, concurrency, resource saturation, and critical saved filters.
- Reproducible execution instructions and results for `RATAN_ADVANCED_SEARCH_PT.jmx`.

## Current Assessment

Ultra is faster in many documented rows but slower in some individual readings. The current evidence supports no demonstrated broad regression for the stated Staging test only; it does not prove production performance equivalence.
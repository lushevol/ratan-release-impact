---
type: concept
title: Cashflow Data Provider Query Performance
created: 2026-08-24
updated: 2026-08-24
tags: [cashflow-data, query-performance, performance-testing, cash-settlement]
related: [cashflow-data-provider, multi-version-cashflow-query, cashflow-blotter-query-performance, cash-settlement-performance-and-stress-testing, denormalized-cashflow-query-read-model, which-indexes-and-data-retention-controls-are-required-for-cashflow-query-tables]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Expose The Cashflow Data Design/Cashflow data provider query solution for big volume/Cashflow data provider query with multiple versions.md"]
---
# Cashflow Data Provider Query Performance

Cashflow Data Provider query performance is the runtime behavior of the provider when retrieving cashflow data across multiple versions and at large data volumes.

## Benchmark Evidence

The source records two observations:

| Environment | Count | Reported cost |
|---|---:|---:|
| `uat1` | `42w` | `55s` |
| `fmrp1` | `120w` | `133s` |

The `120w` test takes approximately `2.42×` the reported time of the `42w` test, while the reported count is approximately `2.86×` larger. These ratios are descriptive only; they do not demonstrate linear, sublinear, or superlinear scaling.

## Comparability Constraints

The tests use different environments and different counts. Consequently, the results cannot isolate:

- the effect of volume;
- differences in CPU, memory, storage, or database configuration;
- index and statistics differences;
- warm-cache versus cold-cache behavior;
- query-plan selection; or
- concurrency and competing workload.

The source also does not define whether `cost` is a wall-clock, database, or end-to-end measurement.

## Required Benchmark Contract

A useful follow-up benchmark should preserve the environment, data volume, query shape, version-selection semantics, database state, cache state, concurrency, repetitions, percentile statistics, and acceptance threshold. Query plans and index definitions should be captured with each result.

These observations are related to, but distinct from, [[concepts/cashflow-blotter-query-performance]] and other performance tests for [[entities/cashflowsnew]] or the cashflow blotter.
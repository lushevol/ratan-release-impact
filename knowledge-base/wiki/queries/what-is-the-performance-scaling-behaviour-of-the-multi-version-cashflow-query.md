---
type: query
title: What Is the Performance Scaling Behaviour of the Multi-Version Cashflow Query?
created: 2026-08-24
updated: 2026-08-24
tags: [open-question, cashflow-data, query-performance, scalability, indexing]
related: [cashflow-data-provider, multi-version-cashflow-query, cashflow-data-provider-query-performance, cashflow-data, cashflow-data-history, which-indexes-and-data-retention-controls-are-required-for-cashflow-query-tables, denormalized-cashflow-query-read-model]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Expose The Cashflow Data Design/Cashflow data provider query solution for big volume/Cashflow data provider query with multiple versions.md"]
---
# What Is the Performance Scaling Behaviour of the Multi-Version Cashflow Query?

## Question

Does the multi-version cashflow query meet its production volume and latency requirements, and which query, schema, indexing, and read-model choices determine its scaling behavior?

## Current Evidence

The Cashflow Data Provider test reports:

- `uat1`: `42w` with a cost of `55s`;
- `fmrp1`: `120w` with a cost of `133s`.

The larger test is slower, but the measurements are confounded by environment and volume. The units of `w` and the meaning of `cost` are not documented.

## Evidence Needed

1. Define the units represented by `42w` and `120w`.
2. Define whether `cost` is wall-clock, database execution, or end-to-end time.
3. Capture the query text, schema, indexes, statistics, and version-selection predicates.
4. Confirm whether the result returns all versions, the latest version, or a deduplicated version-aware result.
5. Repeat the test at controlled volumes in equivalent environments.
6. Measure cold-cache and warm-cache runs under documented concurrency.
7. Record query plans, execution statistics, throughput, and latency percentiles.
8. Compare the results with the production volume and approved performance target.

## Scope Boundary

This query concerns the tested Cashflow Data Provider path only. It does not establish performance for [[entities/cashflowsnew]], [[entities/cashflow-blotter]], [[entities/ultra-cashflow-query]], [[entities/legacy-cashflow-query]], or the general [[entities/query-service]].
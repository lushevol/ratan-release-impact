---
type: concept
title: Cashflow Blotter Query Performance
tags: [cash-settlement, cashflow-blotter, performance-testing, pagination, nfr]
related: [cashflow-blotter, value-date-bounded-cashflow-queries, ultra-cashflow-query, legacy-cashflow-query, cash-settlement-cashflow-read-model, what-cashflow-blotter-queries-are-covered-by-the-performance-sla]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/Cashflow Blotter Page Size Performance.md"]
---
# Cashflow Blotter Query Performance

Cashflow Blotter query performance depends on both requested page size and filter shape. The source reports an overall 1.5× response-time scaling factor when increasing a page from 1,000 to 5,000 results, but individual filters range from faster at the larger size to approximately four times slower.

Complex UK and PAYDOL filters demonstrate that page size alone does not predict latency. Some 5,000-result cases without a VD bound remain substantially above the source's proposed 7.5-second maximum. Any service-level commitment must therefore identify eligible query profiles rather than apply uniformly to all searches.

## Evidence Boundary

The reported aggregate factors are source-reported rather than independently reproducible: the report does not specify aggregation, weighting, cache state, dataset details for the first test round, duration, or request mix. A “90% Response Time” label is also ambiguous where cells contain multiple readings.

Performance implications for [[cash-settlement-cashflow-read-model]] should be validated through documented indexes, predicate cardinality, and `EXPLAIN (ANALYZE, BUFFERS)` evidence. The source does not establish a particular schema or index design.

## Proposed NFR Boundary

The report proposes that indexed, selective queries using positive constraints such as `=`, `IN`, and `BET` are suitable for NFR coverage. It identifies unindexed fields, nonselective values, `NOTIN`, `!=`, and `LIKE` as potential latency risks.

This is a useful investigation heuristic, not a universal operator rule. Optimizer behavior depends on data distribution, statistics, indexes, and the complete query plan. The formal eligibility criteria and measurement target remain open in [[what-cashflow-blotter-queries-are-covered-by-the-performance-sla]].
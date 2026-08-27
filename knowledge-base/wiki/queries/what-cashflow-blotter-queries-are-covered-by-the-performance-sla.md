---
type: query
title: What Cashflow Blotter Queries Are Covered by the Performance SLA?
tags: [cash-settlement, cashflow-blotter, sla, nfr, query-performance]
related: [cashflow-blotter, cashflow-blotter-query-performance, value-date-bounded-cashflow-queries, cash-settlement-cashflow-read-model]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/Cashflow Blotter Page Size Performance.md"]
---
# What Cashflow Blotter Queries Are Covered by the Performance SLA?

The source proposes a 7.5-second maximum and three-second average for 5,000-record Cashflow Blotter loading, based on a source-reported 1.5× page-size scaling factor. It also proposes that only indexed, selective, positively constrained queries should receive NFR coverage.

## Questions to Resolve

- Is the proposed 7.5-second target approved, and is it a maximum, p90, p95, p99, or end-to-end user-perceived measure?
- Which page sizes, VD ranges, concurrency levels, data volumes, and saved filters are covered?
- Must every eligible query include a VD constraint?
- Which business-critical unbounded searches require a separate target or redesign?
- What error-rate, warm-up, cache-state, duration, and repeatability criteria apply?
- Which indexes and execution-plan evidence support the eligibility classification?

## Current Evidence

The source shows filter-specific variability and includes several 5,000-result complex queries that exceed 7.5 seconds without VD limits. Consequently, any adopted SLA needs an explicit query-shape boundary and cannot safely be inferred as a guarantee for unrestricted Blotter searches.
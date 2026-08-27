---
type: concept
title: Value-Date-Bounded Cashflow Queries
tags: [cash-settlement, cashflow-blotter, value-date, query-performance, selectivity]
related: [cashflow-blotter, cashflow-blotter-query-performance, cash-settlement-cashflow-read-model, what-cashflow-blotter-queries-are-covered-by-the-performance-sla]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/Cashflow Blotter Page Size Performance.md"]
---
# Value-Date-Bounded Cashflow Queries

Value-date (VD) bounding restricts a Cashflow Blotter search to a defined date or date interval, for example `VD = T`, `VD in [T, T+2]`, or `VD between [T, T+10]`.

The performance report presents VD constraints as the strongest general mitigation for expensive broad searches. It reports a 0.3 overall scaling factor—described as three times faster—for 5,000-result tests with a VD bound compared with tests without one. Several filter profiles improve substantially, although bounded UK Commodity queries still show multi-second to tens-of-seconds response times.

VD bounding should be treated as a performance optimization pattern, not as a functional replacement for business cases requiring broader historical searches. Its effectiveness depends on data distribution, query composition, and available indexes in the [[cash-settlement-cashflow-read-model|cashflow read model]].

A performance SLA that depends on VD bounds must state the permitted range, whether the bound is mandatory, the supported page size, and the applicable percentile and workload.
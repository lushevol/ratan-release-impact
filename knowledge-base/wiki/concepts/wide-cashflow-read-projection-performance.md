---
type: concept
title: Wide Cashflow Read Projection Performance
created: 2026-08-24
updated: 2026-08-24
tags: [cashflow-data, query-performance, wide-projection, JSONB, pagination]
related: [query-service, cash-settlement-query-cn-cashflow-data, ssdr, jsonb-expression-indexed-query-performance, does-ssdr-cashflow-exposure-meet-its-required-latency-and-pagination-sla]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Expose The Cashflow Data Design/PT-Ratan expose the cashflow data to SSDR.md"]
---
# Wide Cashflow Read Projection Performance

Wide cashflow read projections retrieve a large cross-domain payload in one request, including cashflow, trade, entity, portfolio, instrument, and Settlement Instruction fields. Their performance must be evaluated separately from narrow, selective consumer queries because projection width, serialization cost, row size, and result-set size may dominate latency.

In the cited DEV benchmark against `cash_settlement_query_cn.cashflow_data`, a broad `LIMIT ... OFFSET 0` projection was consistently slower through the tested JSONB API than through the column API. At 5,000 returned records, average latency was 85.012 seconds versus 16.29 seconds without indexes, and 15.23 seconds versus 7.34 seconds with indexes.

These results are limited to the tested broad projection. They do not demonstrate that SSDR requires this payload, that all JSONB access is unsuitable, or that the measurements predict production behavior. The query also has no `ORDER BY`, so it does not define stable pagination.

A consumer exposure should specify a bounded projection, maximum page size, ordering and continuation semantics, expected selectivity, and target percentile latency. See [[does-ssdr-cashflow-exposure-meet-its-required-latency-and-pagination-sla]].
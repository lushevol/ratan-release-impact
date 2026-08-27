---
type: concept
title: Cashflow Blotter Default Query
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, cashflow-blotter, default-query, query-performance]
related: [cashflow-blotter-query-performance, value-date-bounded-cashflow-queries, cashflow-data, postgresql, payment-date-scoping-for-cashflow-blotter]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Expose The Cashflow Data Design/Cashflow Blotter default query solution.md"]
---
# Cashflow Blotter Default Query

The Cashflow Blotter default query retrieves up to 500 recent cashflows from `cashflow_data`. Its default predicate excludes `DEAD` and `NETTED` states, extracts `Cashflow_State` from the `cashflow` JSON document, and orders results by `created_at DESC`.

In the reported test, this broad predicate matched 445,240 cashflows and took 11.87 seconds without the added `created_at` index, or 6.11 seconds with the index. The result is materially slower than an interactive query target and indicates that an unrestricted default is not suitable at the tested data volume.

A half-month Payment_Date bound reduced the measured latency to 1.96 seconds. This supports a bounded default search, but a date range must remain a product and operational policy decision because a narrow default can hide older relevant cashflows.

The query behavior is specific to the tested `cashflow_data` table, schema, query shape, and environment. It should not be generalized automatically to [[entities/ultra-cashflow-query]], other services, or other schemas.

See [[cashflow-blotter-query-performance]] and the source benchmark in [[25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--29-cash-settlement-system-design--3--1a4v5av]].
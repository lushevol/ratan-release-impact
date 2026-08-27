---
type: concept
title: Cashflow State Filtering Performance
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, cashflow-state, jsonb, query-performance, postgresql]
related: [cashflow-data, cashflow-blotter-default-query, postgresql-jsonb-expression-index-matching, jsonb-expression-indexed-query-performance, cashflow-blotter-query-performance]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Expose The Cashflow Data Design/Cashflow Blotter default query solution.md"]
---
# Cashflow State Filtering Performance

Cashflow state filtering reads `Cashflow_State` from the nested `cashflow` JSON document using `jsonb_extract_path_text`. Query cost varies substantially by state population and predicate shape.

In the source measurements:

- `READY` matched 93 rows and completed in approximately 0.376 seconds without the added `created_at` index, or 0.353 seconds with it.
- `QUEUED` matched 18,422 rows and completed in approximately 1.12 seconds with the index.
- `WAITING` matched 68,867 rows and took approximately 11.04 seconds without the index, or 6.00 seconds with it.
- The combined `WAITING`, `READY`, and `QUEUED` predicate matched 87,382 rows and took 11.32 seconds without the index, or 5.92 seconds with it.
- The broad `NOT IN (DEAD, NETTED)` predicate matched 445,240 rows and took 11.87 seconds without the index, or 6.11 seconds with it.

These results show that a state predicate does not guarantee a selective or fast query. The JSON extraction expression and the `created_at DESC` ordering may still require substantial scanning or sorting, particularly for high-population states.

The measurements are workload-specific and do not include `EXPLAIN (ANALYZE, BUFFERS)`, exact index definitions, cache conditions, or production concurrency. They should be used as evidence for investigating [[concepts/postgresql-jsonb-expression-index-matching]] and [[queries/which-expression-indexes-support-cashflow-data-date-filters-and-sorts]], not as a general PostgreSQL benchmark.
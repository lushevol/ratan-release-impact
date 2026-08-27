---
type: query
title: Does Cashflow Payment-Date Search Require an Ordering or Index Policy?
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, cashflow, payment-date, query-performance, open-question]
related: [cash-settlement-query-cn-cashflow-data, postgresql-lossy-bitmap-scan, postgresql-jsonb-expression-index-matching, value-date-bounded-cashflow-queries, value-date-query-performance-guardrail, cashflow-query-indexing-options]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/PostgreSQL performance/SQL performance summary.md"]
---
# Does Cashflow Payment-Date Search Require an Ordering or Index Policy?

## Question

Should Cash Settlement payment-date searches retain `ORDER BY created_at DESC`, use a predicate-aligned ordering column, require a bounded date range, require a booking-entity predicate, or use a dedicated composite or expression index?

## Evidence

The source reports that a payment-date-only range query is slow only for certain dates in the staging environment:

```sql
jsonb_extract_path_text(cfd1_0.cashflow, 'Cashflow', 'Payment_Date')
between ('2025-04-01') and ('2025-05-07')
order by cfd1_0.created_at desc
fetch first 1000 rows only
```

The date-specific behavior may reflect selectivity, data distribution, physical clustering, cache state, or concurrent workload. It does not establish that changing `ORDER BY` is safe or universally effective.

## Required evidence

Resolve this question with comparable staging and production-like data by collecting:

- Actual `EXPLAIN (ANALYZE, BUFFERS)` plans.
- Latency percentiles for representative date ranges.
- Payment-date selectivity and row counts.
- Existing expression, composite, and ordering indexes.
- Sort memory and spill information.
- The required user-visible ordering semantics.
- Results for bounded-date and booking-entity-constrained variants.

## Decision criteria

Any optimization must preserve the required ordering and pagination behavior. A plan that improves database latency but changes the meaning of “most recent” results should not be adopted without product approval.
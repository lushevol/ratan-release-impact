---
type: concept
title: JSONB Expression-Indexed Query Performance
tags: [postgresql, jsonb, expression-index, query-performance, cash-settlement]
related: [postgresql, cash-settlement-query-cn-cashflow-data, postgresql-sequential-scan-triage, cashflow-blotter-query-performance, cashflow-blotter-query-optimization-options, which-expression-indexes-support-cashflow-data-date-filters-and-sorts]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/PostgreSQL performance/SQL performance  in different condition.md"]
---
# JSONB Expression-Indexed Query Performance

A JSONB expression index indexes a value extracted from a JSONB document, such as:

```sql
jsonb_extract_path_text(cashflow, 'Cashflow', 'Payment_Date')
```

It can support filtering and, for suitable query shapes, ordering on that same extracted value. The expression used by a predicate or `ORDER BY` must match the indexed expression in semantics and representation. A different JSON path, function, cast, collation, or numeric conversion can prevent direct use of an otherwise related index.

## Application to cashflow_data

The benchmark source compares `created_at DESC` with ordering by JSONB-extracted `Payment_Date` or `Event_Date` on [[cash-settlement-query-cn-cashflow-data]]. It reports variable timings: JSONB `Payment_Date` ordering is fast in some narrow-range runs, but slower in other runs. The source also states that `Event_Date` and `Booking_System_Event` have no index.

These results are hypotheses, not proof that a particular expression index is present or used. No index DDL or complete plan output is included.

## Design considerations

- A text-extracted date range is chronologically reliable only when values use a consistently sortable format, such as `YYYY-MM-DD`.
- Numeric filtering with `to_number(jsonb_extract_path_text(...), ...)` requires an index on the same numeric conversion if index access is expected.
- An index that assists filtering may not eliminate sorting unless the index order, predicate constraints, and requested ordering are compatible.
- Ordering by an indexed expression can still be slow if a broad predicate requires scanning many entries or if the plan must fetch, filter, or sort many rows.
- Frequently queried JSONB attributes may be candidates for typed generated columns or a dedicated read model when expression-index maintenance and query complexity become excessive.

Validate any proposal with actual plans, buffer metrics, returned-row counts, and the exact index definitions. The required evidence is tracked in [[which-expression-indexes-support-cashflow-data-date-filters-and-sorts]].
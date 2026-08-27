---
type: concept
title: PostgreSQL JSONB Expression-Index Matching
created: 2026-08-24
updated: 2026-08-24
tags: [postgresql, jsonb, expression-index, query-performance, cash-settlement]
related: [postgresql, cash-settlement-query-cn-cashflow-data, postgresql-index-cond-vs-filter, cashflow-query-indexing-options]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/PostgreSQL performance/SQL performance summary.md"]
---
# PostgreSQL JSONB Expression-Index Matching

## Definition

An expression index stores the result of an expression applied to a column. For a JSONB document, an index may be defined over an expression such as `jsonb_extract_path_text(cashflow, ...)`.

For the planner to use that index as an index condition, the query expression must match the indexed expression sufficiently. Wrapping the extraction in another function, changing casts, or using a different expression pattern can prevent the expected index from being used.

## Cash Settlement example

The source queries fields from `cash_settlement_query_cn.cashflow_data.cashflow` with repeated `jsonb_extract_path_text` calls. It notes that an expression involving `to_number(jsonb_extract_path_text(...))` may not use an index defined directly on `jsonb_extract_path_text(...)` because the expressions do not align.

The source's broader statement that an immutable function cannot be used by an index is imprecise. Expression indexes require immutable expressions, but immutable functions can be used when the complete indexed expression is valid and the query uses a compatible expression.

## Diagnostic approach

Compare the index definition with the exact predicate expression and inspect `EXPLAIN (ANALYZE, BUFFERS)`:

- Confirm whether the predicate appears under `Index Cond` or only under `Filter`.
- Check casts and wrapper functions.
- Check the expression's data type and comparison operator.
- Confirm that the expression satisfies PostgreSQL index requirements.
- Compare the estimated and actual selectivity.

Generated columns or normalized relational columns may be preferable when the same JSONB attributes are queried frequently and require consistent typing or range comparisons.
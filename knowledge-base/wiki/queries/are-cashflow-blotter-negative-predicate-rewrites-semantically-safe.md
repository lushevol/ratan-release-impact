---
type: query
title: Are Cashflow Blotter Negative-Predicate Rewrites Semantically Safe?
tags: [cash-settlement, cashflow-blotter, sql, null-semantics, query-optimization]
related: [cash-settlement-query-cn-cashflow-data, jsonb-expression-indexed-query-performance, cashflow-blotter-query-performance, cashflow-blotter-query-optimization-options]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/PostgreSQL performance/SQL performance  in different condition.md"]
---
# Are Cashflow Blotter Negative-Predicate Rewrites Semantically Safe?

The benchmark source reports substantial timing improvements after changing some negative conditions to positive `IN` conditions and ordering by a condition field. The exact rewritten SQL for one complex scenario is not recorded.

`NOT IN (...) OR field IS NULL` and `IN (...)` are not generally logically equivalent. A replacement is safe only if its allow-list is the intended complete complement of the deny-list for the applicable business domain, including current and future values and explicit null behavior.

## Questions

1. Which Cashflow State, counterparty, product, taxonomy, and client-type values must be included or excluded by business rules?
2. How should absent JSONB fields and SQL `NULL` values be handled?
3. Is the proposed allow-list complete as reference data changes?
4. Can a more selective equivalent formulation be defined without changing functional results?
5. Can before-and-after queries be tested against representative production-like data using result-set comparisons?

## Decision boundary

Do not adopt `NOT IN` to `IN` rewrites solely from timing results. First establish functional equivalence, add regression coverage for null and newly introduced values, then validate the final query plan and performance characteristics.
---
type: query
title: Which Expression Indexes Support cashflow_data Date Filters and Sorts?
tags: [postgresql, jsonb, expression-index, query-planning, cash-settlement]
related: [cash-settlement-query-cn-cashflow-data, postgresql, jsonb-expression-indexed-query-performance, postgresql-sequential-scan-triage, are-lifecycle-precheck-indexes-proven-by-query-plans]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/PostgreSQL performance/SQL performance  in different condition.md"]
---
# Which Expression Indexes Support cashflow_data Date Filters and Sorts?

The SQL benchmark reports highly variable results for JSONB `Payment_Date`, `Event_Date`, and other extracted fields, but does not include available index definitions or complete query plans. It explicitly describes `Event_Date` and `Booking_System_Event` as unindexed.

## Questions

1. Which indexes existed on `cash_settlement_query_cn.cashflow_data` during each benchmark?
2. Do expression indexes exactly match the `jsonb_extract_path_text(...)` filter and ordering expressions?
3. Are `Payment_Date` and `Event_Date` stored in an ISO-sortable and validated date representation?
4. Does `created_at DESC` use an index that can efficiently coexist with each JSONB predicate?
5. Which plan nodes account for reported multi-second runs: sequential scans, bitmap heap scans, sorting, disk spills, rechecks, or repeated JSONB evaluation?

## Evidence required

For each representative query, collect:

```sql
EXPLAIN (ANALYZE, BUFFERS, VERBOSE, SETTINGS)
```

Also retain `pg_indexes` or equivalent index DDL, PostgreSQL version, actual parameters, row counts, offset, cache condition, execution order, and concurrent-load context.

This investigation should distinguish evidence of index use from elapsed-time observations in [[25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--27-cash-settlement-performance--22-p--21esao]].
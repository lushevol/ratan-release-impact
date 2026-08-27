---
type: source
title: Cashflow Blotter Default Query Solution
authors: []
year: 2024
url: ""
venue: "Cash Settlement technical design"
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, cashflow-blotter, query-performance, postgresql, jsonb]
related: [cashflow-blotter-default-query, payment-date-scoping-for-cashflow-blotter, cashflow-state-filtering-performance, cashflow-blotter-query-performance, value-date-bounded-cashflow-queries, cashflow-data, postgresql]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Expose The Cashflow Data Design/Cashflow Blotter default query solution.md"]
---
# Cashflow Blotter Default Query Solution

## Summary

This technical design evaluates the default queries used by the Cashflow Blotter against the `cashflow_data` table. The queries extract `Cashflow_State` and `Payment_Date` from the `cashflow` JSON document, order results by `created_at DESC`, and return at most 500 rows.

The unrestricted default query excludes only `DEAD` and `NETTED` cashflows. In the reported test, it matched 445,240 rows and took 11.87 seconds without the added `created_at` index, or 6.11 seconds with that index. Adding a payment-date bound produced the strongest measured improvement: a half-month window reduced the same broad query to 1.96 seconds.

The results support bounded Payment_Date searches for interactive Cashflow Blotter use, but they do not establish a final product policy or a universal PostgreSQL benchmark. The source does not provide execution plans, exact index definitions, concurrency conditions, cache state, or percentile latency.

## Workload

The tested query shape is:

- Filter by one or more values extracted from `cashflow->Cashflow->Cashflow_State`.
- Optionally filter by `cashflow->Cashflow->Payment_Date`.
- Order by `created_at DESC`.
- Limit the response to 500 rows.

The query is served in the context of the [[cashflow-blotter-default-query]] and applies specifically to the tested `cashflow_data` workload.

## Results Without Payment-Date Scope

| Cashflow State | Count | Time(s) | If added Index for "created_at" Time(s) |
| --- | ---: | ---: | ---: |
| NOT IN (DEAD, NETTED) **Current default** | 445240 | 11.87 | 6.11 |
| WAITING | 68867 | 11.04 | 6 |
| READY | 93 | 0.376 | 0.353 |
| QUEUED | 18422 | 1.12 | 1.12 |
| IN (WAITING, READY, QUEUED) | 87382 | 11.32 | 5.92 |

### SQL Tested

```sql
SELECT * FROM cashflow_data where jsonb_extract_path_text(cashflow, 'Cashflow', 'Cashflow_State') not in ('DEAD','NETTED') order by created_at desc limit 500;
SELECT * FROM cashflow_data where jsonb_extract_path_text(cashflow, 'Cashflow', 'Cashflow_State') = 'WAITING' order by created_at desc limit 500;
SELECT * FROM cashflow_data where jsonb_extract_path_text(cashflow, 'Cashflow', 'Cashflow_State') = 'READY' order by created_at desc limit 500;
SELECT * FROM cashflow_data where jsonb_extract_path_text(cashflow, 'Cashflow', 'Cashflow_State') = 'QUEUED' order by created_at desc limit 500;
SELECT * FROM cashflow_data where jsonb_extract_path_text(cashflow, 'Cashflow', 'Cashflow_State') in ('WAITING', 'READY', 'QUEUED') order by created_at desc limit 500;
```

## Results With Payment-Date Scope

The following results include Payment_Date filtering and the added `created_at` indexes described by the source.

| Cashflow State | Payment date within 1 month — Count | Time(s) | Payment date within 0.5 month — Count | Time(s) |
| --- | ---: | ---: | ---: | ---: |
| NOT IN (DEAD, NETTED) **Current default** | 46146 | 10.11 | 19944 | 1.96 |
| WAITING | 29069 | 1.70 | 8114 | 1.05 |
| READY | 7 | 0.356 | 7 | 0.351 |
| QUEUED | 3784 | 1.01 | 1998 | 0.96 |
| IN (WAITING, READY, QUEUED) | 32860 | 1.56 | 10119 | 1.48 |

The broad default query improved from 10.11 seconds with a one-month range to 1.96 seconds with a half-month range. `READY` was already fast because its matching population was very small. The improvement was therefore state-dependent rather than uniform.

### Active-State SQL Tested

```sql
SELECT * FROM cashflow_data where jsonb_extract_path_text(cashflow, 'Cashflow', 'Cashflow_State') not in ('DEAD','NETTED') and jsonb_extract_path_text(cashflow, 'Cashflow', 'Payment_Date') between '2024-05-22' and '2024-06-06' order by created_at desc limit 500;
SELECT * FROM cashflow_data where jsonb_extract_path_text(cashflow, 'Cashflow', 'Cashflow_State') = 'WAITING' and jsonb_extract_path_text(cashflow, 'Cashflow', 'Payment_Date') between '2024-05-22' and '2024-06-06' order by created_at desc limit 500;
SELECT * FROM cashflow_data where jsonb_extract_path_text(cashflow, 'Cashflow', 'Cashflow_State') = 'READY' and jsonb_extract_path_text(cashflow, 'Cashflow', 'Payment_Date') between '2024-05-22' and '2024-06-06' order by created_at desc limit 500;
SELECT * FROM cashflow_data where jsonb_extract_path_text(cashflow, 'Cashflow', 'Cashflow_State') = 'QUEUED' and jsonb_extract_path_text(cashflow, 'Cashflow', 'Payment_Date') between '2024-05-22' and '2024-06-06' order by created_at desc limit 500;
SELECT * FROM cashflow_data where jsonb_extract_path_text(cashflow, 'Cashflow', 'Cashflow_State') in ('WAITING', 'READY', 'QUEUED') and jsonb_extract_path_text(cashflow, 'Cashflow', 'Payment_Date') between '2024-05-22' and '2024-06-06' order by created_at desc limit 500;
```

## Terminal-State Query

A terminal-state query scoped to the previous seven days returned 1,070 rows in 1.17 seconds.

```sql
SELECT * FROM cashflow_data where jsonb_extract_path_text(cashflow, 'Cashflow', 'Cashflow_State') in ('NETTED', 'DEAD', 'CANCELLED', 'SETTLED') and jsonb_extract_path_text(cashflow, 'Cashflow', 'Payment_Date') between '2024-06-01' and '2024-06-07' order by created_at desc limit 500;
```

This result supports treating active-state searches and historical or terminal-state searches as different workloads rather than applying one date-range policy to all queries.

## Interpretation

The evidence indicates that:

1. The unrestricted active-state default query is unsuitable as an interactive default at the measured data volume.
2. A `created_at` index helps broad queries but does not resolve their latency.
3. Payment-date bounds reduce the candidate population and can bring the broad query below two seconds with a half-month window.
4. State selectivity has a major effect: `READY` is fast, while `WAITING` and the combined active states remain substantially more expensive.
5. The results do not prove that Payment_Date alone, or any specific index, is sufficient under production concurrency.

The source does not identify the exact `CREATE INDEX` statements or show whether Payment_Date was indexed. Execution-plan evidence is required before selecting a final indexing strategy.

## Open Questions

- What exact indexes were created for `created_at`, `Payment_Date`, and extracted JSON expressions?
- What do `EXPLAIN (ANALYZE, BUFFERS)` plans show for each query?
- Were timings collected with warm caches, cold caches, or both?
- What p95 and p99 latency targets apply under production concurrency?
- Should the UI enforce a maximum search range, provide a narrow default, or require a date range?
- How should users retrieve older cashflows without reintroducing an unrestricted expensive query?
- Is `created_at DESC` the required business ordering, or should results use Payment_Date or another cashflow timestamp?

## Conclusion

Shortening the Payment_Date period reduced the reported broad-query latency from more than 11 seconds to less than two seconds. The result strengthens the case for bounded Cashflow Blotter searches, while leaving the final date-range policy, index design, and production SLA validation open.

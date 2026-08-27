---
type: concept
title: JSONB Numeric Expression Indexing
created: 2026-08-24
updated: 2026-08-24
tags: [postgresql, jsonb, expression-index, numeric-filtering, cash-settlement]
related: [to-number-ratan, ultra-cashflow-query, cashflow-blotter-query-performance, postgresql-sequential-scan-triage]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/PostgreSQL performance/PostgreSQL increase work_mem up to 30MB & user define pg function risk analyze.md"]
---
# JSONB Numeric Expression Indexing

## Definition

JSONB numeric expression indexing indexes a value computed from JSONB content rather than a directly stored relational column. In this case, `Payment_Amount` is extracted from `cashflow` as text and converted to a numeric value with [[to-number-ratan]].

## Tested expression

```sql
CASH_SETTLEMENT_QUERY_CN.TO_NUMBER_RATAN(
    JSONB_EXTRACT_PATH_TEXT(
        CFD1_0.CASHFLOW,
        'Cashflow',
        'Payment_Amount'
    ),
    '99999999999999999.999999'
)
```

The tested predicate compares the expression with `43454.7` and orders results by `CREATED_AT`.

## Reported effect

On approximately four million rows, the query execution time changed from `339,321.217 ms` when using the `created_at` index to `0.323 ms` when using the `to_number_ratan()` expression index.

The corresponding 500-user Query Service test reported `5.4` QPS before the numeric-field index and `45.4` QPS after it. Most baseline requests were invalid because they took minutes, so the QPS comparison is directional.

## Correctness and operating risks

Before production use, the function and index contract should specify:

- Function volatility and immutability.
- Numeric format, precision, and rounding.
- Handling of `NULL`, missing JSON paths, empty strings, and malformed values.
- Handling of negative and locale-specific values.
- Query-plan confirmation and returned-row validation.
- Storage and write-latency overhead from index maintenance.

This technique is specifically evidenced for `Cashflow.Payment_Amount`; its results should not automatically be generalized to other JSONB fields or query operations.

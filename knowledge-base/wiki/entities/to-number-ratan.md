---
type: entity
title: to_number_ratan()
created: 2026-08-24
updated: 2026-08-24
tags: [postgresql, function, jsonb, expression-index, cash-settlement]
related: [jsonb-numeric-expression-indexing, postgresql-work-mem-sizing, ultra-cashflow-query]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/PostgreSQL performance/PostgreSQL increase work_mem up to 30MB & user define pg function risk analyze.md"]
---
# to_number_ratan()

## Role

`to_number_ratan()` is a user-defined PostgreSQL function that delegates numeric text conversion to PostgreSQL's inner `to_number` function. It is used to make numeric values embedded in the JSONB `cashflow` column available to an expression index.

The source states that the wrapper was introduced because the inner `to_number` function's immutability characteristics did not support the required expression index. The exact volatility declaration and function body are not included and require confirmation.

## Tested usage

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

The test compared a query using the `created_at` index with a query using an expression index on this conversion expression. Execution time changed from `339,321.217 ms` to `0.323 ms` on approximately four million rows.

## Validation status

The source states that function testing was covered by QA regression testing. It does not document:

- The function definition or declared volatility.
- The exact expression-index definition.
- Behavior for `NULL`, empty, malformed, negative, or locale-specific values.
- Precision and rounding behavior.
- Index maintenance cost during writes.

These details should be recorded before treating the function as a general-purpose numeric JSONB contract.

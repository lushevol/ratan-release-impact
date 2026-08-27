---
type: query
title: Is the to_number_ratan() Expression Index Correct for All Payment Amount Values?
created: 2026-08-24
updated: 2026-08-24
tags: [postgresql, jsonb, expression-index, data-quality, numeric-precision]
related: [to-number-ratan, jsonb-numeric-expression-indexing, ultra-cashflow-query]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Performance/PostgreSQL performance/PostgreSQL increase work_mem up to 30MB & user define pg function risk analyze.md"]
---
# Is the to_number_ratan() Expression Index Correct for All Payment Amount Values?

## Question

Does the `to_number_ratan()` expression index return correct and complete results for every supported `Cashflow.Payment_Amount` value?

## Evidence

The documented test extracts `Cashflow.Payment_Amount` from JSONB and applies the format mask:

```text
99999999999999999.999999
```

For the tested value `43454.7`, execution time changed from `339,321.217 ms` to `0.323 ms` on approximately four million rows. The source also states that function testing was covered by QA regression testing.

## Open validation

The implementation and index DDL are not included. The contract should be tested for:

- Missing and `NULL` JSONB values.
- Empty and malformed numeric text.
- Negative values.
- Maximum supported precision and scale.
- Rounding behavior.
- Locale-specific formatting.
- Equality semantics and returned-row completeness.
- Index behavior after inserts and updates.

Execution plans should confirm index usage, and results should be compared against a trusted non-indexed implementation.

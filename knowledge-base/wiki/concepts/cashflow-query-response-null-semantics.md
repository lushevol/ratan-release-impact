---
type: concept
title: Cashflow Query Response Null Semantics
created: 2026-08-24
updated: 2026-08-24
tags: [cashflow, graphql, nullability, data-quality, api-contract]
related: [cashflowsnew, cash-settlement-query-service-graphql-read-model, cash-settlement-cashflow-read-model]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Cash Settlement Query Service Design/Cash flow query model.md"]
---
# Cashflow Query Response Null Semantics

The documented [[cashflowsnew]] response uses multiple representations for absent or unavailable values:

- JSON `null`, including `Settlement_Instruction`, `is_stp`, and some position or comment fields.
- Empty strings, including `netting_id`, `settlement_method`, and person-role identifiers.
- Literal strings containing `"null"`, including `execution_date_time`, trade-lake timestamps, and `fmo_comment_timestamp`.

## Implications

Clients cannot rely solely on JSON nullability to identify missing information. Generated types, UI rendering, validation, sorting, filtering, and date parsing should distinguish valid values from empty strings and literal `"null"` values.

The source does not establish whether this behavior is intentional compatibility handling, source-data quality, serialization behavior, or a defect. It also does not define field-level nullability guarantees.
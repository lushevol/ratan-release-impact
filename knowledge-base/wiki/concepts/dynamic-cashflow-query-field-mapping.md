---
type: concept
title: Dynamic Cashflow Query Field Mapping
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, dynamic-query, graphql, database-mapping, jsonb]
related: [centralized-cashflow-field-mapping-governance, rule-service, query-service, cash-settlement-query-service-graphql-read-model, cashflow-data, which-cashflow-dynamic-query-mappings-are-missing-duplicated-or-unused]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cashflow Query Service - GraghQL schema and DB column mapping for dynamic query.md"]
---
# Dynamic Cashflow Query Field Mapping

Dynamic cashflow query field mapping translates logical-model filter fields into physical database representations and maps database values into GraphQL response fields.

The source provides an inventory of candidate field-to-column mappings across Cashflow, Data Flow, Entity, Entity Person, Instrument, Portfolio, SSI, and Trade domains. The complete catalogue is preserved in [[25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--79-cashflow-query-service-graghql-s--1j6395i]].

## Default naming policy

The proposed default physical column derivation is:

- `.` becomes `__`;
- `Settlement_Instruction` becomes `ssi`;
- the result becomes lowercase.

For example, `Cashflow.Payment_Date` maps to `cashflow__payment_date`.

## Limitations

The naming rule is not a sufficient contract by itself. The source marks `Instrument_Common.Equity_Instrument_Reference` and `Instrument_Common.Parent_Trade_Instrument` as missing. It also identifies candidate duplicate and unused columns.

The source provides no actual GraphQL type definitions, filter operators, nullability semantics, database column types, or authorization policy. Its mapping catalogue is therefore a reconciliation input, not an authoritative GraphQL contract.
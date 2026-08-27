---
type: query
title: What Is the Authoritative Cashflow Dashboard GraphQL Contract?
tags: [cash-settlement, graphql, query-service, dashboard, api-contract]
related: [cash-settlement-dashboard-operational-read-model, cash-settlement-query-service-graphql-read-model, query-service, cash-flow-query-model, cash-settlement-query-service-design]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Query Service -Dashboard.md"]
---

# What Is the Authoritative Cashflow Dashboard GraphQL Contract?

The dashboard design contains material differences between its declared GraphQL model and its example query. The authoritative contract must be confirmed before implementation, client generation, or production documentation.

## Conflicting Contract Areas

- `Wating_Today_Num` is misspelled in the declared model and query. The correction and backward-compatibility policy are unknown.
- The model defines `Group_Error_Num` and `Group_Pending_Num`, while the query requests `Group_Num`.
- The model defines `VD_Exceptions` as a list of `VDException` records, while the query requests separate `VD_Exception`, `VD1_Exception`, `VD2_Exception`, and `VDM_Exception` objects.
- The model defines `Exception_Code` and value-date counts, while the query requests named exception metrics such as `High_Value_Num` and `Pending_Affirmation_Num`.
- The model does not explicitly define nullability, although the example returns null `Counter_Party` and `Type` values.
- `Amount:String` does not define currency, precision, sign, aggregation, or ranking semantics.
- `page` and `size` do not have a documented scope across summary data, exposure records, and drill-down cashflow details.

## Evidence Needed

Resolve the contract by identifying:

1. The deployed GraphQL schema and resolver implementation.
2. The client version that consumes `cashflowDashboard`.
3. The intended group-status fields.
4. The canonical exception response shape and vocabulary.
5. Nullability, amount, currency, and ordering rules.
6. The relationship between dashboard pagination and detail-query pagination.
7. Compatibility requirements for existing clients.

Until these points are resolved, the source should be treated as a design proposal rather than the canonical API specification.

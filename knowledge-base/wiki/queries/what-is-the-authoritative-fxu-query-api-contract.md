---
type: query
title: What Is the Authoritative FXU Query API Contract?
created: 2026-08-24
updated: 2026-08-24
tags: [fxu, graphql, api, cashflow, contract, open-question]
related: [fxu, ratan-query-service, cash-settlement-query-service-graphql-read-model, denormalized-cashflow-query-read-model, fxu-technical-design]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FXU Technical Design.md"]
---

# What Is the Authoritative FXU Query API Contract?

The source documents a POST GraphQL operation named `cashflowUtilizeQuery` at `/api/ratan/stmcn/v1/cashflows`, but several contract details require confirmation.

## Unresolved contract points

- The development host and linked endpoint use different host and port combinations.
- The `Country` header example contains malformed quotation and mixed punctuation.
- MVP uses `Trade.Trade_Id`, while Phase 2 also uses `Trade_Id`.
- Amounts and prices appear both as strings and numeric values.
- The type and scope of `Is_Client_Clearing_Trade` are not defined.
- `totalResult` is not defined as a cashflow, trade, or result-record count.
- Pagination, authorization, nullability, version selection, and ordering guarantees are unspecified.

Confirm whether this is a separate contract from the existing query-service GraphQL APIs and identify the authoritative schema and environment configuration.
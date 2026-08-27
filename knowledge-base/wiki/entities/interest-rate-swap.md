---
type: entity
title: Interest Rate Swap
tags: [irs, financial-product, cashflow, settlement]
related: [irs-cashflow-aggregation, cashflow-aggregation-lineage, net-function]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Aggregation.md"]
---
# Interest Rate Swap

An Interest Rate Swap (IRS) is the financial-product context for the proposed cashflow aggregation change.

The source states that an IRS has two cashflow legs which must be combined for settlement when the upstream system sends them as separate cashflows. It does not define the product-identification rule, the authoritative relationship key between the legs, or the settlement eligibility criteria.

See [[irs-cashflow-aggregation]] for the proposed settlement behavior and [[cashflow-aggregation-lineage]] for the required but unspecified relationship model.
---
type: query
title: Why Does cashflowsNew Response Not Match the Cashflow ID Filter?
created: 2026-08-24
updated: 2026-08-24
tags: [cashflow, graphql, filtering, data-quality, query-service]
related: [cashflowsnew, cash-settlement-query-service-graphql-read-model, query-service, 25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--29-cash-settlement-system-design--3--1tc15rv]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Cash Settlement Query Service Design/Cash flow query model.md"]
---
# Why Does cashflowsNew Response Not Match the Cashflow ID Filter?

## Question

Why does the documented `cashflowsNew` request filter on `Cashflow.Cashflow_Id = "12070687922588"` while the sample response reports 42 hits and returns different cashflow IDs?

## Evidence

The source shows a filter using the `EQ` operator, but returns IDs `002022111701`, `012022111601`, `003690235976`, `008888000004`, and `113690235975`.

## Possible Explanations

- The request and response were copied from separate executions.
- The documented filter was not applied by the service or gateway.
- The filter field or operator has semantics different from strict identifier equality.
- `Cashflow_Id` is not unique in the queried model.

## Required Resolution

Obtain a reproducible request and response, confirm the GraphQL schema and resolver behavior, and document identifier uniqueness, filter operators, value typing, combination semantics, sorting, and error handling.
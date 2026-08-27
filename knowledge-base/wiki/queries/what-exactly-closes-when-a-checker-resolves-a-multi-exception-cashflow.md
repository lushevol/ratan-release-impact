---
type: query
title: What Exactly Closes When a Checker Resolves a Multi-Exception Cashflow?
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, exceptions, checker, closure, workflow]
related: [multi-exception-resolution-handling, high-value-exception-dependency, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--16-multi-exceptions--38--1pgj0j1]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Multi Exceptions/High Value Exception Scenario Analysis.md"]
---
# What Exactly Closes When a Checker Resolves a Multi-Exception Cashflow?

The requirement states that if a Checker manually fixes an exception, “All exception closed as multi exception handling.” It does not define the scope of that closure.

## Required Clarification

Determine whether Checker resolution closes:

1. Only the High Value exception.
2. The resolved companion exception and High Value.
3. Every co-existing exception on the cashflow.
4. Only exceptions eligible for the same Checker action.

The decision should also specify state transitions, audit records, authorization boundaries, and whether remaining exceptions can prevent STP after the Checker action.
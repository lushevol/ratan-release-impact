---
type: query
title: Does a Maker-Only Exception Trigger or Only Retain High Value Exception?
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, high-value, maker, checker, exception-rule]
related: [high-value-exception-dependency, multi-exception-resolution-handling, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--16-multi-exceptions--38--1pgj0j1]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Multi Exceptions/High Value Exception Scenario Analysis.md"]
---
# Does a Maker-Only Exception Trigger or Only Retain High Value Exception?

The source contains a material inconsistency:

- The narrative says High Value must be triggered only when another exception requires manual Checker action.
- The generation table says `High Value Exception + Maker only Exception` is triggered.
- The technical predicate classifies Checker exceptions as `operationLevel in (CHECKER_ONLY, MAKER_CHECKER)`, excluding `MAKER_ONLY`.

Clarify whether High Value generation is based on any co-existing exception while Checker visibility or retention is based on Checker-action eligibility, or whether the Maker-only generation table is incorrect.

## Required Decision

Define the authoritative generation predicate, visibility predicate, and retention predicate for High Value, including the role of `MAKER_ONLY`.
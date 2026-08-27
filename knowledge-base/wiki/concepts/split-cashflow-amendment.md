---
type: concept
title: Split Cashflow Amendment
tags: [cashflow, settlement, amendment, amount-conservation]
related: [manual-cashflow-splitting, cashflow-lineage-and-amendment-correlation, authoritative-split-cashflow-lifecycle]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting/Split Demo Cases.md"]
---
# Split Cashflow Amendment

Split cashflow amendment enables Operations to correct amounts for the remaining unreleased portions of a split group after some child cashflows may already have been released.

## Rules

- At least two child cashflows must be in `WAITING`.
- Only amounts of `WAITING` children may be updated.
- The total of all child cashflows must equal the original parent amount.

## Result

- The parent remains in `SPLIT`.
- Updated child cashflows remain in `WAITING`.
- Updated children receive an additional `Split Amend` exception.

The amount-conservation requirement is explicit for amendment. The imported requirement does not explicitly define the equivalent conservation validation, residual allocation, or atomicity behavior for the original split operation.
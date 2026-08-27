---
type: concept
title: Split Amount Amendment
created: 2026-08-22
updated: 2026-08-22
tags: [cashflow-splitting, amendment, validation, settlement]
related: [cashflow-splitting, cashflow-unsplit, ratan-cashflow-lifecycle-state-machine]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting/Cashflow Splitting UAT.md"]
---

# Split Amount Amendment

Split amount amendment changes allocations among eligible child cashflows after a parent has been split.

## Rules

Released children are disabled and cannot be amended. Unreleased children remain eligible for amount changes.

The amended child amounts must sum to the parent amount. If the total is incorrect, Ratan displays a validation error indicating that the amounts do not match the total. If the total is correct, the child amounts are updated and the cashflow enters `WAITING` with a `Split Amend` exception.

The amendment flow therefore preserves the parent-child monetary balance while allowing operational correction before all children are released.
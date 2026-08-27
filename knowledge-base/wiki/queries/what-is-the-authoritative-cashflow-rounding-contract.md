---
type: query
title: What Is the Authoritative Cashflow Rounding Contract?
created: 2026-08-24
updated: 2026-08-24
tags: [cashflow, rounding, static-data, migration, open-question]
related: [automated-cashflow-rounding, cashflow-payment-amount-canonicalization, currency-rounding-static-data, stella, ratan, murex-2-11, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--11-static-data--64-round--10xd1dk]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/Rounding Rule - Tactical solution for H1 2024 Cashflow Migration.md"]
---
# What Is the Authoritative Cashflow Rounding Contract?

The imported requirement defines a tactical Ratan rounding process but leaves material implementation and lifecycle questions unresolved.

## Questions to resolve

- What are the complete target, GUI, SWIFT, and accounting mappings for the incomplete Stella SCBML row?
- For negative values, does `Round Down` mean mathematical floor or truncation toward zero?
- What is the behavior when `Cashflow.Payment_Currency` is null, malformed, or absent from the matrix?
- Is rounding idempotent when a cashflow is received or processed more than once?
- Is `Cashflow.Payment_Amount` a numeric field or a formatted string, and where are trailing zeros removed?
- How are exact halfway negative amounts handled under `Round Off`?
- Who owns, approves, versions, audits, and effective-dates the currency rounding matrix?
- Are historical cashflows recalculated during migration?
- How does Ratan identify Stella-booked versus Murex 2.11-booked cashflows?
- What event retires the tactical Ratan logic after Stella provides strategic rounding?
- Was the H1 2024 implementation formally tested and signed off?

## Evidence

[[25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--11-static-data--64-round--10xd1dk]] establishes the broad process and currency matrix, but provides no API contract, implementation artifact, formal test evidence, or lifecycle transition plan.
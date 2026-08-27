---
type: query
title: Are Split Child Cashflows Excluded from All Netting Rules?
created: 2026-08-22
updated: 2026-08-22
tags: [query, cashflow-splitting, netting, nds, scope]
related: [split-cashflow-netting-exclusion, cashflow-splitting, pending-nds-netting, nds-auto-netting, netting-eligibility-rules]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting/Cashflow Split Static.md"]
---
# Are Split Child Cashflows Excluded from All Netting Rules?

The source explicitly excludes split child cashflows from the pending NDS auto-netting rule by requiring `Cashflow__Splitting_Id` to be null or empty. It does not state that the exclusion applies to all netting rules or downstream processing.

## Evidence needed

Determine whether the same condition is required for other NDS, NDS Fixing, manual, resultant-cashflow, product-agnostic, or inter-entity netting flows. Do not generalize the pending NDS rule change until this scope is confirmed.
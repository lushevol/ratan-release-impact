---
type: query
title: What Is the Authoritative Matching Algorithm for Non-Economic Cashflow Amendments?
created: 2026-08-24
updated: 2026-08-24
tags: [cashflows, matching, amendments, ratan, lineage]
related: [six-attribute-cashflow-equivalence, non-economic-cashflow-amendment-handling, cashflow-version-concurrency-control]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade & Cashflow Events Control/Non Economic amendment(FMRP) Cashflows.md"]
---
# What Is the Authoritative Matching Algorithm for Non-Economic Cashflow Amendments?

The source defines six attributes for determining equivalence between withdrawn and replacement cashflows but does not specify a deterministic matching algorithm.

## Questions

- How are pairs selected when multiple cashflows have identical values across all six attributes?
- Are cashflow IDs, trade-leg identifiers, event order, netting context, or another key used as a tie-breaker?
- How are one-to-many, many-to-one, split, merged, and unmatched cashflow events handled?
- Must matching account for amount scale, rounding, value-date normalization, or currency-code normalization?
- What persistence and recovery guarantees protect lineage mappings across replay or restart?
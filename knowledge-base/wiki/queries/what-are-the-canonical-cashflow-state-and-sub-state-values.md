---
type: query
title: What Are the Canonical Cashflow State and Sub-State Values?
created: 2026-08-22
updated: 2026-08-22
tags: [cashflow, state-machine, data-model, requirements-ambiguity]
related: [cashflow-blotter-action-eligibility, cashflow-failure-and-reinstatement, cashflow-hold-unhold]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Cashflow Blotter/User Actions on Cashflow Blotter.md"]
---
# What Are the Canonical Cashflow State and Sub-State Values?

The source uses inconsistent forms including `HOLD` and `ON HOLD`, `SWIFT_SUPPRESSED` and “SWIFT SUPPRESSED”, `CASHFLOW_SUPPRESSED` and “CASHFLOW SUPPRESSED”, and `FAILED` and “FAIELD”.

Identify authoritative persisted main-state, sub-state, and sub-state-type enumerations; map UI labels to these values; and determine which variants are typographical errors.
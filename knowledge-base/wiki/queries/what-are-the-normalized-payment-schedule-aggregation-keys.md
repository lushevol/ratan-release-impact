---
type: query
title: What Are the Normalized Payment Schedule Aggregation Keys?
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, aggregation, payment-schedule, data-modeling, requirements-gap]
related: [normalized-payment-schedule, product-agnostic-cashflow-aggregation, 2026-brp-q3-ratansett-product-agnostic-aggregation, ratan, fmrp-flow]
sources: ["auto-netting-page-md-files/Cash Settlement Home Page -- Cash Settlement Home Page -- Functional Requirement -- Netting -- [Draft", "auto-netting-page-md-files/Cash Settlement Home Page -- Cash Settlement Home Page -- Functional Requirement -- Netting -- [Draft] Auto Aggregation based on Normalized Payment Schedule.md"] Auto Aggregation based on Normalized Payment Schedule.md"] Auto Aggregation based on Normalized Payment Schedule.md"]
---
# What Are the Normalized Payment Schedule Aggregation Keys?

The draft proposes [[normalized-payment-schedule]] as the basis for [[product-agnostic-cashflow-aggregation]] but does not state the attributes that determine whether cashflows may aggregate.

## Questions to resolve

- Which system owns the schedule and its identifiers?
- Is aggregation keyed by trade ID, normalized schedule ID, legal entity, currency, settlement date, account, SSI, payment type, direction, or another attribute set?
- What is the schedule granularity?
- What cardinality is supported between source cashflows and normalized schedules?
- How are multiple second-leg IRS cashflows represented and aggregated?
- How are conflicting, missing, or partially eligible attributes handled?
- Which attributes must remain identical in the resulting settlement instruction?

The detailed happy and negative user cases are deferred to an unavailable `analysis.xlsx` attachment and screenshots. The data-model specification and acceptance criteria for ADO Story 14618546 are required to answer this query.
---
type: query
title: How Will Normalized Payment Schedule Aggregation Coexist with IRS and CCS Auto Netting?
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, aggregation, netting, migration, duplicate-prevention]
related: [normalized-payment-schedule, product-agnostic-cashflow-aggregation, irs-interest-auto-netting, ccs-auto-netting, 2026-brp-q3-ratansett-product-agnostic-aggregation, duplicate-payment-prevention]
sources: ["auto-netting-page-md-files/Cash Settlement Home Page -- Cash Settlement Home Page -- Functional Requirement -- Netting -- [Draft", "auto-netting-page-md-files/Cash Settlement Home Page -- Cash Settlement Home Page -- Functional Requirement -- Netting -- [Draft] Auto Aggregation based on Normalized Payment Schedule.md"] Auto Aggregation based on Normalized Payment Schedule.md"] Auto Aggregation based on Normalized Payment Schedule.md"]
---
# How Will Normalized Payment Schedule Aggregation Coexist with IRS and CCS Auto Netting?

The source describes [[normalized-payment-schedule]] aggregation as strategic while describing IRS Netting and [[ccs-auto-netting]] as existing supplementary, taxonomy-specific mechanisms. It does not state whether the new path replaces, bypasses, retains, or coordinates with those mechanisms.

## Decisions needed

- Will IRS Netting and CCS Auto Netting be retired, retained, or used as fallbacks?
- What precedence applies when a cashflow is eligible for both a legacy mechanism and Normalized Payment Schedule aggregation?
- What controls prevent duplicate aggregation or duplicate settlement output?
- What is the migration and rollback sequence?
- How will results be reconciled between legacy and new processing paths?
- Are product-specific exceptions preserved after the strategic mechanism is introduced?

Resolution is necessary before release of [[2026-brp-q3-ratansett-product-agnostic-aggregation]], particularly because the source does not define a common eligibility model.
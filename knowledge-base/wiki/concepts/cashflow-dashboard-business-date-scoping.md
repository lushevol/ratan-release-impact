---
type: concept
title: Cashflow Dashboard Business-Date Scoping
tags: [cash-settlement, cashflow, business-date, value-date, queued, dashboard]
related: [value-date-bounded-cashflow-queries, cash-settlement-dashboard-operational-read-model, cashflow-blotter-query-performance]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Query Service -Dashboard.md"]
---

# Cashflow Dashboard Business-Date Scoping

The cashflow dashboard design defines special business-date rules for queue and value-date metrics.

## Queued Scope

`QUEUED` should include only cashflows scheduled within the next five business days. The requirement is intended to prevent distant future work from inflating the operational queue and notes that queued volume would normally be expected to be zero.

The source does not define:

- Whether the current business day is included.
- How holidays are calculated.
- Which timezone determines the current date.
- Whether the rule applies to status counts only or also to drill-down results and exposure.
- How the rule interacts with payment date, value date, or other date fields.

## Friday `VD-1` Rule

On Friday, `VD-1` should include Saturday, Sunday, and Monday. This is a special weekend treatment for value-date aggregation and must be implemented consistently with the canonical business-day calendar.

The source does not specify holiday behavior or whether the rule applies to exception counts, volume counts, filters, or detail queries.

## Implementation Boundary

These rules are dashboard requirements, not general status semantics. They should not automatically be applied to other Query Service operations or to the [[entities/cashflow-blotter]] without confirming their contracts.

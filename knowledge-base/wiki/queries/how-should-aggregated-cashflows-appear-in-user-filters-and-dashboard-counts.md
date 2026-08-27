---
type: query
title: How Should Aggregated Cashflows Appear in User Filters and Dashboard Counts?
tags: [cashflow, aggregation, user-filters, dashboard, aggregated-status]
related: [irs-cashflow-aggregation, cashflow-aggregation-state-model, ratan-cashflow-dashboard, dashboard-cashflow-status-counting]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Aggregation.md"]
---
# How Should Aggregated Cashflows Appear in User Filters and Dashboard Counts?

## Question

How should the proposed `AGGREGATED` status appear in user filters, search results, operational queues, reports, and dashboard status counts?

## Evidence

The source identifies user filters as an outstanding scope item but defines no visibility, default-filter, search, or reporting requirement. It does not state whether aggregated source legs, an aggregate result, or both should be counted.

## Required resolution

Confirm whether `AGGREGATED` is:

- Visible by default or only through a dedicated filter.
- Included or excluded from active settlement queues.
- Counted as a standalone dashboard status.
- Represented as one item or multiple linked items in search and reporting.
- Subject to distinct entitlement or audit-display rules.

This decision should be reconciled with [[ratan-cashflow-dashboard]] and [[dashboard-cashflow-status-counting]] without assuming that their existing rules apply.
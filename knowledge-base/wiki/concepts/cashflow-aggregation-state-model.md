---
type: concept
title: Cashflow Aggregation State Model
tags: [cashflow, aggregation, status, lifecycle, unaggregate]
related: [irs-cashflow-aggregation, cashflow-aggregation-lineage, what-is-the-authoritative-unaggregate-state-and-lineage-behavior, how-should-aggregated-cashflows-appear-in-user-filters-and-dashboard-counts, dashboard-cashflow-status-counting]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Aggregation.md"]
---
# Cashflow Aggregation State Model

The source proposes a preliminary lifecycle model for IRS cashflow aggregation. It introduces `AGGREGATED` as a new status and names three actions: `Aggregate`, `AggregateNew`, and `UnAggregate`.

| Source status | Source sub-status | Source sub-status type | Action | Target status |
|---|---|---|---|---|
| `WAITING` | `Pending Operator` | `Pending Another Leg` | `Aggregate` | `AGGREGATED` |
| `QUEUED` | `NA` | `NA` | `Aggregate` | `AGGREGATED` |
| `NA` | `NA` | `NA` | `AggregateNew` | `QUEUED` |
| `AGGREGATED` | `NA` | `NA` | `UnAggregate` | `QUEUED` |
| `QUEUED`, `WAITING`, `HOLD`, `FAILED`, `SWIFT_SUPPRESSED`, `CASHFLOW_SUPPRESSED`, `READY` | `ALL` | `ALL` | `UnAggregate` | `DEAD` |

## Interpretation limits

This is not an authoritative state machine. The source does not establish:

- Whether transitions apply to source legs, a new aggregate cashflow, or both.
- Whether `AggregateNew` creates a cashflow and how it relates to `Aggregate`.
- Why `UnAggregate` can result in either `QUEUED` or `DEAD`.
- Whether the final row denotes a set of source statuses.
- Whether any action is automated, manual, or subject to authorization controls.
- Notification, audit, and downstream-feed behavior.

The ambiguous `UnAggregate` outcomes are tracked in what is the authoritative unaggregate state and lineage behavior. Any presentation of `AGGREGATED` in dashboards or filters requires separate confirmation; see how should aggregated cashflows appear in user filters and dashboard counts.
---
type: source
title: Cashflow Aggregation
authors: []
year: 2026
url: ""
venue: ""
tags: [cash-settlement, cashflow, aggregation, irs, functional-requirement]
related: [cash-settlement-home-page, interest-rate-swap, irs-cashflow-aggregation, cashflow-aggregation-state-model, cashflow-aggregation-lineage, net-function, what-is-the-authoritative-irs-leg-correlation-and-aggregation-eligibility-rule, is-irs-cashflow-aggregation-fully-automated-or-user-initiated, what-is-the-authoritative-unaggregate-state-and-lineage-behavior, what-are-the-tlm-lms-and-cis-impacts-of-irs-cashflow-aggregation, how-should-aggregated-cashflows-appear-in-user-filters-and-dashboard-counts]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Aggregation.md"]
---
# Cashflow Aggregation

This functional proposal introduces a dedicated **Aggregation** function for combining the two settlement cashflow legs of an [[interest-rate-swap]]. It is intended to replace use of the existing [[net-function]] for this use case.

The stated rationale is semantic clarity: Net supports a user-initiated merger of different cashflows, whereas IRS leg combination is required for settlement because the upstream system does not supply a pre-merged cashflow.

## Proposed lifecycle changes

The document proposes `Aggregate`, `AggregateNew`, and `UnAggregate` actions and introduces an `AGGREGATED` status. The following source table is preserved verbatim.

```text
| Source Cashflow Status | Source Cashflow Sub Status | Source Cashflow Sub Status Type | Action | Target Cashflow Status | Target Cashflow Sub Status | Target Cashflow Sub Status Type | | --- | --- | --- | --- | --- | --- | --- | | WAITING | Pending Operator | Pending Another Leg | Aggregate | AGGREGATED | NA | NA | | QUEUED | NA | NA | Aggregate | AGGREGATED | NA | NA | | NA | NA | NA | AggregateNew | QUEUED | NA | NA | | AGGREGATED | NA | NA | UnAggregate | QUEUED | NA | NA | | QUEUED WAITING HOLD FAILED SWIFT_SUPPRESSED CASHFLOW_SUPPRESSED READY | ALL | ALL | UnAggregate | DEAD | NA | NA |
```

Read as separate rows, the proposed transition matrix is:

| Source cashflow status | Source sub-status | Source sub-status type | Action | Target cashflow status | Target sub-status | Target sub-status type |
|---|---|---|---|---|---|---|
| `WAITING` | `Pending Operator` | `Pending Another Leg` | `Aggregate` | `AGGREGATED` | `NA` | `NA` |
| `QUEUED` | `NA` | `NA` | `Aggregate` | `AGGREGATED` | `NA` | `NA` |
| `NA` | `NA` | `NA` | `AggregateNew` | `QUEUED` | `NA` | `NA` |
| `AGGREGATED` | `NA` | `NA` | `UnAggregate` | `QUEUED` | `NA` | `NA` |
| `QUEUED WAITING HOLD FAILED SWIFT_SUPPRESSED CASHFLOW_SUPPRESSED READY` | `ALL` | `ALL` | `UnAggregate` | `DEAD` | `NA` | `NA` |

The document does not define whether these actions are automated, operator-triggered, or both. It also does not define the object affected by each transition or the lineage between the two IRS legs and an aggregated settlement cashflow.

## Outstanding scope

The proposal explicitly leaves the following matters unresolved:

- Whether manual unaggregation is required.
- User-filter treatment for `AGGREGATED` cashflows.
- [[tlm]] impact, marked TBC.
- [[lms]] impact if `WAITING` cashflow feeds are sent.
- [[cis]] impact for PM currency processing.

The incomplete lifecycle and integration definitions are tracked through [[cashflow-aggregation-state-model]], [[cashflow-aggregation-lineage]], and the related open queries.
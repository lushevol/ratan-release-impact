---
type: concept
title: Manual Cashflow Failure
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, failed-status, manual-operation, cashflow-blotter, fmo]
related: [failed-cashflow-status-eligibility, scheduled-failed-cashflow-job, cashflow-blotter-functional-scope, fmo-ops, cash-settlement-home-page, what-is-the-authoritative-failed-cashflow-transition-contract, what-is-the-post-failed-cashflow-processing-model]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Failed Process/Scheduled Failed Job Manual Fail.md"]
---
# Manual Cashflow Failure

Manual Cashflow Failure is an immediate status-change action available from the Cashflow Blotter. An FMO user right-clicks a cashflow and selects `Manual Fail`; an eligible cashflow then moves to `FAILED` immediately.

## Eligibility

The action uses [[failed-cashflow-status-eligibility]]. The source does not permit manual failure of cashflows in the excluded statuses.

## Operational Boundary

Unlike [[scheduled-failed-cashflow-job]], the manual workflow does not state a value-date or failed-cutoff validation. This appears to permit an immediate operational override, but the requirement does not explicitly confirm that bypass behaviour is intentional.

The source also does not specify:

- User permissions or whether the role is limited to [[fmo-ops]].
- Maker-checker approval.
- Required failure reason, audit fields, or audit retention.
- User confirmation, rejection messages, or handling of already-`FAILED` cashflows.
- Downstream effects after the status change.

These omissions are tracked in [[what-is-the-authoritative-failed-cashflow-transition-contract]] and [[what-is-the-post-failed-cashflow-processing-model]].
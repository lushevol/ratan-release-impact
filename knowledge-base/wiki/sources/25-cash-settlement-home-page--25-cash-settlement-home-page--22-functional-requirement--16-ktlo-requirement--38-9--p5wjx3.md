---
type: source
title: "9244099 Add Timer Dashboard Exceptions"
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, dashboard, exceptions, ktlo, timer, monitoring]
related: [cash-settlement-home-page, timer-based-dashboard-exception-visibility, group-pending-monitoring, group-pending-validation-monitoring, pending-trade-validation-investigation, what-starts-the-dashboard-exception-stuck-timer]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/KTLO Requirement/9244099-Add timer Dashboard exceptions.md"]
authors: []
year: 2026
url: "https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/9244099"
venue: "Azure DevOps work item 9244099"
---
# 9244099 Add Timer Dashboard Exceptions

This KTLO requirement requests timer-based filtering for selected Cash Settlement Home Page dashboard exceptions. A qualifying exception should be displayed only after it has remained stuck for more than five minutes.

## Requirement statement

> Add timer Dashboard exceptions - only display if stuck for more than 5 min

The stated threshold is interpreted as a strict aging condition:

```text
elapsed_stuck_time > 5 minutes
```

The source does not define the timer start event, reset conditions, clock source, or the exact dashboard behavior at precisely five minutes.

## Named exception categories

The requirement explicitly lists:

- `QUEUED` status with a pending exception.
- `Group Pending`, described as `group pending + group trade validation待确认`.
- `Group Pending Validation`.

The requirement establishes dashboard-visibility filtering only for these named categories. It does not establish a rule for every cashflow status or every monitoring view.

## Related monitoring scope

The requirement concerns [[cash-settlement-home-page]] and augments the monitoring context documented in [[group-pending-monitoring]] and [[group-pending-validation-monitoring]]. The relationship between `group trade validation待确认` and `Group Pending Validation` remains unconfirmed; it may require alignment with [[pending-trade-validation-investigation]].

## Unresolved implementation semantics

- What event starts the stuck timer?
- Does a retry, validation update, reassignment, or status transition reset the timer?
- Is “stuck” defined as no state transition, unresolved validation, no processing progress, or another condition?
- Are qualifying items hidden only from dashboard rows, or also from counts, alerts, and downstream monitoring?
- What canonical status names and relationships apply to `Group Pending`, `group trade validation待确认`, and `Group Pending Validation`?

See [[what-starts-the-dashboard-exception-stuck-timer]].
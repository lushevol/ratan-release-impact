---
type: concept
title: Timer-Based Dashboard Exception Visibility
created: 2026-08-23
updated: 2026-08-23
tags: [dashboard, exception-management, monitoring, timer, cash-settlement]
related: [cash-settlement-home-page, group-pending-monitoring, group-pending-validation-monitoring, what-starts-the-dashboard-exception-stuck-timer]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/KTLO Requirement/9244099-Add timer Dashboard exceptions.md"]
---
# Timer-Based Dashboard Exception Visibility

Timer-based dashboard exception visibility separates status eligibility from display eligibility: an item may be in a qualifying exception state but remains absent from the dashboard until its qualifying condition has aged past a configured threshold.

For work item 9244099, the threshold is:

```text
elapsed_stuck_time > 5 minutes
```

The rule is scoped to explicitly named dashboard exception categories: `QUEUED` with a pending exception, `Group Pending`, and `Group Pending Validation`. It must not be generalized to other Cash Settlement Home Page statuses without further evidence.

## Required distinction

- **Status eligibility:** the item meets a named exception condition.
- **Display eligibility:** the qualifying condition has remained stuck for more than five minutes.

## Undefined semantics

The available requirement does not define the event that starts the timer, the clock or timezone used, or whether the timer pauses or resets following a retry, status transition, or validation activity. These decisions are tracked in [[what-starts-the-dashboard-exception-stuck-timer]].

This visibility rule is related to [[group-pending-monitoring]] and [[group-pending-validation-monitoring]] but does not establish that those operational states are equivalent.
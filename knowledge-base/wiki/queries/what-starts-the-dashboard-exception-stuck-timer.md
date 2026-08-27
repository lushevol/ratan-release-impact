---
type: query
title: What Starts the Dashboard Exception Stuck Timer?
created: 2026-08-23
updated: 2026-08-23
tags: [dashboard, exceptions, timer, monitoring, cash-settlement]
related: [timer-based-dashboard-exception-visibility, cash-settlement-home-page, group-pending-monitoring, group-pending-validation-monitoring]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/KTLO Requirement/9244099-Add timer Dashboard exceptions.md"]
---
# What Starts the Dashboard Exception Stuck Timer?

Work item 9244099 requires selected dashboard exceptions to be displayed only when stuck for more than five minutes, but it does not define the start timestamp for that interval.

## Candidate timer-start events

Potential interpretations include:

- exception creation;
- entry into `QUEUED` status;
- entry into `Group Pending`;
- entry into `Group Pending Validation`;
- creation of a pending exception; or
- the most recent relevant status transition.

## Decisions needed

Confirm:

1. The canonical event and timestamp that start the timer for each qualifying category.
2. Whether the threshold is strictly greater than five minutes or inclusive at five minutes.
3. Whether retries, status changes, validation updates, reassignment, and temporary recovery reset or pause elapsed time.
4. The authoritative clock source, timezone, and treatment of delayed event delivery.
5. Whether the aging filter applies only to visible rows or also to dashboard counts, alerts, and downstream monitoring.

The answer should preserve the distinction between the `Group Pending` and `Group Pending Validation` monitoring models described in [[group-pending-monitoring]] and [[group-pending-validation-monitoring]].
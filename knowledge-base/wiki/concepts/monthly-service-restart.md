---
type: concept
title: Monthly Service Restart
tags: [service-restart, maintenance-window, scheduling, RATAN]
related: [ratan, rundeck, service-restart-runbook, is-the-ratan-service-restart-schedule-and-rundeck-runbook-current]
created: 2026-08-25
updated: 2026-08-25
sources: ["RATAN/RATAN -SME/RATAN-MISC/RATAN-Service Restart Guide(OLD).md"]
---

# Monthly Service Restart

## Definition

A monthly service restart is a recurring maintenance procedure in which the RATAN service estate is stopped and subsequently restarted on the first Saturday of each month.

## Source-Derived Schedule

The historical guide documents:

- Stop: `RAT_STOP_ALL_SERVICES` at 13:30 GMT.
- Start: `RAT_RESTART_ALL_SERVICES` at 18:15 GMT.
- Nominal stop-to-start interval: 4 hours 45 minutes.

The guide does not specify whether GMT is fixed year-round or operationally equivalent to UTC, and it does not define the services included in “all services.”

## Operational Caveat

Because the source filename includes `OLD`, this schedule is not confirmed as current. Current timing, job authority, service scope, notifications, approvals, health checks, and failure handling should be validated through [[is-the-ratan-service-restart-schedule-and-rundeck-runbook-current]].
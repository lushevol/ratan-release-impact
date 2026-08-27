---
type: query
title: Is the RATAN Service Restart Schedule and Rundeck Runbook Still Current?
tags: [RATAN, service-restart, Rundeck, validation, operations]
related: [ratan, rundeck, monthly-service-restart, service-restart-runbook, ratan-service-restart-guide-old]
created: 2026-08-25
updated: 2026-08-25
sources: ["RATAN/RATAN -SME/RATAN-MISC/RATAN-Service Restart Guide(OLD).md"]
---

# Is the RATAN Service Restart Schedule and Rundeck Runbook Still Current?

## Question

Are the first-Saturday restart schedule, the referenced Rundeck jobs, and the documented full-service and service-specific restart workflows still authoritative for RATAN?

## Validation Questions

1. Are the first-Saturday stop and start schedule and the 13:30 GMT and 18:15 GMT times still active?
2. Are `RAT_STOP_ALL_SERVICES` and `RAT_RESTART_ALL_SERVICES` still the authoritative scheduled jobs?
3. Are the `cluster_controller` and `service_restart_jobs` Rundeck links still valid and accessible?
4. What services are included in “all services”?
5. Who owns the schedule and the Rundeck jobs?
6. What preconditions and permissions are required?
7. What health checks confirm a successful restart?
8. What incident, rollback, or escalation procedure applies if the restart fails?
9. Is there a current replacement for the guide marked `OLD`?

## Current Evidence

The source provides precise job names, times, project identifier `RATANRT`, and two Rundeck URLs. It does not provide current ownership, revision metadata, service scope, validation evidence, or recovery procedures.

Until these questions are answered, [[ratan-service-restart-guide-old]] should be treated as historical operational evidence rather than current production authority.
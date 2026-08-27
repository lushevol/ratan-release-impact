---
type: concept
title: Service Restart Runbook
tags: [service-restart, runbook, operations, automation, RATAN]
related: [ratan, rundeck, monthly-service-restart, is-the-ratan-service-restart-schedule-and-rundeck-runbook]
created: 2026-08-25
updated: 2026-08-25
sources: ["RATAN/RATAN -SME/RATAN-MISC/RATAN-Service Restart Guide(OLD).md"]
---

# Service Restart Runbook

## Definition

A service restart runbook defines the operational workflows used to stop and start services in a controlled manner. The historical RATAN guide distinguishes between a full-estate restart and a targeted restart of an individual service.

## Full-Est​ate Restart

The `cluster_controller` Rundeck job is documented as the one-click restart workflow for the RATAN estate. The source does not establish whether this workflow performs a stop followed by a start, applies dependency ordering, restarts infrastructure components, or performs post-restart health checks.

## Service-Specific Restart

The `service_restart_jobs` Rundeck job is documented for restarting a specific service. Its use is narrower than the `cluster_controller` workflow and should be selected when the operational issue is limited to an individual service.

## Missing Runbook Controls

The source does not document access permissions, preconditions, expected duration, success criteria, rollback, incident escalation, change-control linkage, service dependencies, or the list of services covered by the full restart.

The guide is marked `OLD` in its filename, so the documented workflows require current operational validation.
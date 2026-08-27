---
type: source
title: RATAN Service Restart Guide (Old)
tags: [RATAN, service-restart, Rundeck, operations, historical]
related: [ratan, rundeck, monthly-service-restart, service-restart-runbook, is-the-ratan-service-restart-schedule-and-rundeck-runbook-current]
created: 2026-08-25
updated: 2026-08-25
sources: ["RATAN/RATAN -SME/RATAN-MISC/RATAN-Service Restart Guide(OLD).md"]
authors: []
year: 0
url: ""
venue: ""
---

# RATAN Service Restart Guide (Old)

## Summary

This operational guide documents a recurring monthly stop-and-start schedule for RATAN services and two manual Rundeck restart workflows. The filename includes `OLD`; therefore, the schedule, job names, links, and procedures should be treated as historical and unvalidated until confirmed against current operational documentation.

## Monthly Automatic Restart

The source provides the following schedule:

**Monthly Auto Restart on first Sat of Each month **

| Action | Job name | Time |
| --- | --- | --- |
| STOP | RAT_STOP_ALL_SERVICES | 13:30 GMT |
| START | RAT_RESTART_ALL_SERVICES | 18:15 GMT |

The documented interval between the stop and start actions is 4 hours 45 minutes. The guide does not define the service inventory covered by “all services,” dependency ordering, health checks, retries, or failure recovery.

## Manual Restart Workflows

**One Click restart**:   [Rundeck - cluster_controller](https://rundeckselfservice.global.standardchartered.com/selfservice/project/RATANRT/job/show/71eacd2e-3163-46bc-8a2b-96fe2231cfee)

This is presented as the full-estate or cluster restart workflow in the [[service-restart-runbook]].

**To restart specific service**:  [Rundeck - service_restart_jobs](https://rundeckselfservice.global.standardchartered.com/selfservice/project/RATANRT/job/show/7df689b6-a670-4a25-bbd3-df887390a374)

This is presented as the targeted service-specific workflow and should not be treated as interchangeable with `cluster_controller`.

Both workflows are associated with the Rundeck project identifier `RATANRT`.

## Evidence and Limitations

The guide confirms that the documented procedures and Rundeck references existed when it was written. It does not provide an author, revision date, owner, validation date, access requirements, change record, maintenance notification process, success criteria, rollback steps, or incident procedure.

The explicit use of GMT is preserved from the source. The guide does not clarify whether GMT is intended as fixed year-round time or operational UTC, nor whether local daylight-saving expectations affect the maintenance window.

## Validation Requirement

The current status of this guide is tracked in [[is-the-ratan-service-restart-schedule-and-rundeck-runbook-current]]. Until validation is complete, this page should be used as a historical reference rather than as production authority.
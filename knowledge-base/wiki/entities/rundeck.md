---
type: entity
title: Rundeck
tags: [Rundeck, operations, automation, self-service, service-restart]
related: [ratan, monthly-service-restart, service-restart-runbook, is-the-ratan-service-restart-schedule-and-rundeck-runbook]
created: 2026-08-25
updated: 2026-08-25
sources: ["RATAN/RATAN -SME/RATAN-MISC/RATAN-Service Restart Guide(OLD).md"]
---

# Rundeck

## Role in RATAN Operations

Rundeck is the self-service execution platform referenced by the historical RATAN restart guide. The guide associates the workflows with project `RATANRT`.

## Referenced Jobs

| Scope | Job | Source link |
| --- | --- | --- |
| Full or one-click restart | `cluster_controller` | [Rundeck job](https://rundeckselfservice.global.standardchartered.com/selfservice/project/RATANRT/job/show/71eacd2e-3163-46bc-8a2b-96fe2231cfee) |
| Specific service restart | `service_restart_jobs` | [Rundeck job](https://rundeckselfservice.global.standardchartered.com/selfservice/project/RATANRT/job/show/7df689b6-a670-4a25-bbd3-df887390a374) |

The two jobs have distinct documented scopes and should not be conflated. The guide does not state their permissions, prerequisites, execution duration, validation steps, or recovery behavior.

## Currency

The source is marked `OLD` through its filename. The availability and authority of these Rundeck links and jobs require confirmation.
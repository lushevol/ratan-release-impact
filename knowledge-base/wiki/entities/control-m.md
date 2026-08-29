---
type: entity
title: Control M
created: 2026-08-22
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Auto Netting Technical Design.md"]
tags: ["job-scheduling", "orchestration", "cash-settlement", "job-scheduler", "cashflow-auto-netting", "operations", "scheduler", "workload-automation", "cashflow-publication", "batch-processing", "accounting", "control-m", "scheduling", "ratan", "hashicorp-vault"]
related: ["2025-cash-settlement-tranche-1", "lina-feng", "jie-cai", "cashflow-auto-netting", "auto-netting-rule-check", "ratan", "cn-settlement-murex-211-integration", "murex-ratan-bidirectional-cashflow-integration", "country-local-time-accounting-batch-scheduling", "accounting-feed-file-generation-idempotency", "accounting-aspire-execution", "hashicorp-vault", "ratan-hashicorp-credential-lifecycle", "ratan-secrets-management", "control-m-job-hold", "hygiene-reboot", "5-ratan--28-ratan-service-restart-guide--37-ratan-cve-patching-and-hygiene-reboot--1ij0sni"]
updated: 2026-08-25
---

# Control-M

## Overview

Control-M is referenced in multiple source contexts as a scheduling, orchestration, job-scheduling, or workload-automation tool:

- The 2025 Cash Settlement Tranche 1 runbook associates it with a planned job release.
- The Cashflow Auto Netting Technical Design identifies it as the scheduler for the auto-netting job endpoint.
- The CN Settlement–Murex 2.11 Delivery Plan identifies it as the planned scheduler for cashflow publication.
- The Settlement Accounting for Aspire Technical Design proposes it for accounting-feed generation.
- The RATAN and HashiCorp 51460 source identifies it as the scheduler and orchestrator for RATAN's HashiCorp Vault credential-management operations.
- The RATAN CVE patching and hygiene reboot fragment identifies it as a job-scheduling and workload-automation dependency in a RATAN maintenance sequence.

These contexts and their operational status are described separately below.

## Role in the 2025 Cash Settlement Tranche 1 runbook

The 2025 Cash Settlement Tranche 1 runbook refers to `Control M` as the scheduling or orchestration tool associated with the planned job release on Apr 25.

`Jie Cai` is the named owner for the job release. The runbook source does not report whether the release occurred or whether the job operated as expected.

## Role in cashflow auto netting

The Auto Netting Technical Design identifies Control-M as the scheduler that triggers the netting service's auto-netting job endpoint:

```text
GET /v1/cashflows/autoNetting/job
```

The technical design does not specify the Control-M schedule, timeout, alerting, retry policy, mutual exclusion, or behavior after a failed invocation. These operational details require confirmation before the integration can serve as a production runbook.

## Role in Murex 2.11 cashflow publication

The CN Settlement–Murex 2.11 Delivery Plan identifies Control-M as the planned scheduler for automated publication of cashflows from murex 211 into [[ratan]].

According to that delivery-plan source, scheduler configuration depends on user input about job frequency. The plan does not define the schedule, triggering criteria, failure handling, or whether the scheduled publication was implemented.

## Proposed role in accounting-feed generation

The Settlement Accounting for Aspire Technical Design identifies Control-M as the proposed scheduler for country-local accounting-feed file generation.

The proposed design schedules the generation job every 30 minutes from 22:05 through 02:05 local time, and schedules an empty-file job at 03:30 local time. It is intended to select eligible tasks by payment date and creation-time cutoff, then produce one file for each workday job.

This scheduling behavior is proposed design, not confirmed operational configuration.

## Role in interface 51460

The RATAN and HashiCorp 51460 source identifies Control-M as scheduling and orchestrating RATAN's HashiCorp Vault credential-management operations. The parent folder is `RATAN_FULL_HCV`.

That source associates the parent folder with monthly enablement of HashiCorp, VIP, and clusters on all servers in March, July, and November.

### Jobs

| Job | Documented responsibility |
| --- | --- |
| `RAT_HCV_CHECK` | Check all HashiCorp account rotation information |
| `RAT_HCV_REFRESH` | Refresh all HashiCorp accounts to Redis |
| `RAT_HCV_ROTATE` | Rotate all HashiCorp accounts |
| `RAT_RESTART_ALL_SERV_HCV` | Restart VIP and the whole cluster from ARK servers |
| `RAT_STOP_ALL_SERV_HCV` | Stop all services on the whole cluster |

The source does not specify exact schedules, ordering dependencies, execution owners, retry behavior, alerts, or the conditions under which stop and restart jobs are required.

See ratan hashicorp credential lifecycle for the relationship between rotation and refresh.

## Role in RATAN CVE patching and hygiene reboot

The RATAN CVE Patching and Hygiene Reboot source identifies Control-M as a job-scheduling and workload-automation dependency in the documented RATAN maintenance sequence.

For that maintenance sequence, Control-M jobs are held before the RATAN service is stopped and released after the service is started. The source does not specify:

- The jobs in scope
- The hold or release mechanism
- Whether release must wait for a successful RATAN health check

See control m job hold and what is the authoritative ratan cve patching and hygiene reboot procedure.
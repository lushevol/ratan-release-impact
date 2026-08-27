---
type: query
title: What Is the Authoritative Failed Cashflow Transition Contract?
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, failed-status, status-transition, cutoff, operational-controls]
related: [scheduled-failed-cashflow-job, manual-cashflow-failure, failed-cashflow-status-eligibility, currency-specific-failed-cutoff, ratan, razor, aspire]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Failed Process/Scheduled Failed Job Manual Fail.md"]
---
# What Is the Authoritative Failed Cashflow Transition Contract?

The requirement specifies an eligibility matrix for transition to `FAILED`, but leaves material execution and control details unresolved.

## Questions to Resolve

- What is the scheduled-job execution time, timezone, calendar, and Razor accounting-EOD dependency?
- Does CN Day 1 bypass failed-cutoff validation entirely, or apply a fixed entity-level cutoff?
- Is the long-term cutoff keyed by currency, legal entity and currency, or another static-data dimension?
- Are `CNY`, `CNO`, and `CNH` intended configuration values, and do they share the stated 10:00 am GMT cutoff?
- Does `Manual Fail` deliberately bypass scheduled value-date and cutoff checks?
- What permissions, maker-checker controls, failure reasons, audit attributes, and user feedback govern manual failure?
- How are idempotency, reruns, and concurrent cashflow status changes handled?
- How is the `FAILED` transition versioned and published to downstream consumers?

## Evidence

The source identifies five eligible predecessor statuses—`PROJECTED`, `QUEUED`, `WAITING`, `READY`, and `ONHOLD`—for both automated and manual processing. It describes a CN Day 1 fixed schedule and a future per-currency timing model, but does not define a complete authoritative contract.
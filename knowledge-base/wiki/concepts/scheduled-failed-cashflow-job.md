---
type: concept
title: Scheduled Failed Cashflow Job
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, failed-status, batch-processing, cn-day-1]
related: [failed-cashflow-status-eligibility, currency-specific-failed-cutoff, manual-cashflow-failure, ratan, razor, aspire, what-is-the-authoritative-failed-cashflow-transition-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Failed Process/Scheduled Failed Job Manual Fail.md"]
---
# Scheduled Failed Cashflow Job

The Scheduled Failed Cashflow Job is an automated process that moves eligible cashflows to `FAILED`.

## CN Day 1 Model

The initial CN Day 1 model is a daily job that runs on weekends and holidays as well as business days. It is intended to run at a fixed time before [[razor]] accounting EOD, but the precise execution time remains TBC.

Cashflows must have a value date equal to the current system date. Although the requirement references a currency failed-cutoff condition, it says that this rule need not run for CN Day 1.

## Long-Term Model

The long-term strategy states that [[ratan]] will move cashflows to `FAILED` at different times by currency. This must be coordinated with settlement accounting because [[aspire]] generates trade accounting at a single time across currencies.

The source does not define the rollout trigger, coexistence arrangement, scheduled-job timezone, daylight-saving treatment, rerun behaviour, idempotency, or concurrency handling.

## Shared Eligibility

The job uses [[failed-cashflow-status-eligibility]]. It should not be interpreted as applying to statuses outside that explicit matrix.

## Open Contract Questions

The unclear relationship between the fixed CN Day 1 schedule and the future cutoff-controlled model is tracked in [[what-is-the-authoritative-failed-cashflow-transition-contract]].
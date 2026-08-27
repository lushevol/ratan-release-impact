---
type: project
title: 2025 Cash Settlement Tranche 1
status: planned
owner: FMRP China Cash Settlement
start_date: 2025-04-21
target_date: 2025-05-17
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, release, tranche-1, RATAN-ONE, CPT]
related: ["murex", "control-m", "nds-auto-netting", "cashflow-monitoring", "cashflow-reconciliation", "cashflow-accounting-release"]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/FMRP China Cash Settlement Delivery Plan/Cash Settlement RATAN ONE 2025 Release Plan/2025 Cash Settlement Tranche 1 Ratan Runbook.md"]
---

# 2025 Cash Settlement Tranche 1

## Purpose

This project coordinates the planned release of the first CPT cashflow tranche for the 2025 [[RATAN ONE]] cash settlement delivery plan.

## Scope

The planned scope includes:

- Rule and configuration updates.
- [[Control M]] job release and application change release.
- Controlled CPT cashflow push and cancellation through [[Murex]].
- Monitoring of cashflow counts, statuses, rules, flags, and `Swap Agent`/`RFR` behavior.
- Whole-data publication and [[cashflow-reconciliation]].
- Operations processing and accounting release handling for `SWIFT_SUPP` and `READY` cashflows.

## Milestones

- Apr 21: Rule update by data operations.
- Apr 25: Control M job release.
- Apr 26 at 9 AM: Change release.
- Apr 28–30: Tranche 1 CPT testing, monitoring, and cancellation.
- May 10 at 9 AM: Whole-data publication and reconciliation.
- May 16: Operations processing.
- May 17: Accounting release actions and CPT configuration update.

## Risks and gaps

The source does not provide execution results, acceptance criteria, rollback steps, escalation procedures, or a complete ownership model. The repeated “same behavior” instruction for Apr 29 and Apr 30 is underspecified. The order and authorization of the May 17 accounting actions also require confirmation.

## Retrospective

No retrospective outcomes are recorded in the source. Execution evidence should be added separately from this planned runbook.

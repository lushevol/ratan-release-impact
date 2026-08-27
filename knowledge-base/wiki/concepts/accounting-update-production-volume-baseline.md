---
type: concept
title: Accounting-Update Production Volume Baseline
tags: [cash-settlement, production-baseline, workload-modeling, testing, AccountingUpdate]
related: [accounting-update, uber-scbml-performance-regression-testing, cashflow-lifecycle-state-machine-restructuring, cashflow-stamping-domain-ownership, product-agnostic-cashflow-aggregation, bulk-maker-checker-processing, eventual-consistency-for-cashflow-exceptions-and-swift-status, uber, fxu]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Uber & FXU Technical Live Plan/Production Existing Data Testing Cases.md"]
---
# Accounting-Update Production Volume Baseline

## Definition

An accounting-update production volume baseline is an observed distribution of records by `AccountingUpdate` category that can be used to shape production-like test workloads. The baseline in the [[sources/25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--41-ratanone-cash-settlement-technic--1ijfplm]] source is a workload inventory, not a performance result.

## Workload emphasis

The highest-volume categories in the source are:

- `CashflowStamped`: 20,770,369
- `New`: 20,684,985
- `Materialize`: 19,300,238
- `Net`: 12,074,869
- `Settle`: 8,882,910
- `GenerateSwift`: 8,820,924
- `Suppress`: 6,883,240
- `Release`: 6,628,828
- `IsNettingEligible`: 7,218,543
- `IsAutoNettingEligible`: 4,543,414
- `AccountingUpdate`: 3,116,582
- `SsiStamped`: 2,183,549

These values support prioritizing lifecycle initialization, materialization, stamping, netting, settlement, Swift processing, suppression, release, and eligibility checks in volume or regression scenarios. They do not prove that any of these operations is a performance bottleneck.

## Correctness and recovery coverage

Low-volume categories should remain in correctness and recovery testing even when they are excluded from primary load scenarios. Examples include `ResendToRazor`, `ManualAffirmed`, `UnSplit`, `ReplayStatusWriteBack`, `ReGenerateSwift`, `Split`, `VostroStamped`, and `EarlyReleaseToRazor`.

Potential test families include:

- Creation and lifecycle: `New`, `Materialize`, `AccountingUpdate`, `WaitingAnotherLeg`.
- Netting: `IsNettingEligible`, `IsAutoNettingEligible`, `Net`, `NetNew`, `UnNet`.
- Settlement and release: `Settle`, `SettleAsGross`, `Release`, `EarlyRelease`, `Withdrawal`.
- Swift processing: `GenerateSwift`, `ReGenerateSwift`, `SwiftUpdate`, `Suppress`, `SwiftSuppress`, `ManualSuppress`, `ManualSwiftSuppress`, `ManualSwiftUnSuppress`, `ResendToRazor`.
- Stamping: `CashflowStamped`, `SsiStamped`, `NostroStamped`, `VostroStamped`.
- Approval and exception handling: `Affirmed`, `Approve`, `ApproveOnlyMaker`, `Submit`, `Reject`, `Fail`, `TechFail`, `AutoFail`.
- Holding and recovery: `Hold`, `UnHold`, `RevertToQueued`, `ReInstate`.

These families are analytical test-design groupings and are not stated as formal source-system semantics.

## Provenance constraints

The baseline cannot support daily or hourly workload rates, error rates, trend analysis, or comparative Uber and FXU conclusions because the source omits the extraction query, environment, time window, counting unit, and scope allocation. Counts may also overlap if multiple categories can be recorded for the same underlying cashflow.

The baseline should be attached to [[entities/uber]] only after confirming that the data is Uber-specific. The same validation is required before using it as evidence in [[concepts/uber-scbml-performance-regression-testing]] or in go-live acceptance criteria.
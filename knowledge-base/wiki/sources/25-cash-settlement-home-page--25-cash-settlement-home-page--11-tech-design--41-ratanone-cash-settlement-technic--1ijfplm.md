---
type: source
title: Production Existing Data Testing Cases
authors: []
year: null
url: ""
venue: ""
tags: [cash-settlement, RATANONE, Uber, FXU, production-data, testing]
related: [uber, ratanone, fxu, accounting-update, accounting-update-production-volume-baseline, cashflow-lifecycle-state-machine-restructuring, cashflow-stamping-domain-ownership, product-agnostic-cashflow-aggregation, uber-scbml-performance-regression-testing]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Uber & FXU Technical Live Plan/Production Existing Data Testing Cases.md"]
---
# Production Existing Data Testing Cases

## Summary

This document provides an inventory of existing production data grouped by `AccountingUpdate` value. It is located within the [[ratanone]] Cash Settlement technical design under the [[uber]] and FXU integration live plan.

The table is useful as a candidate workload baseline for production-like testing. The source does not define whether the counts represent database rows, events, state transitions, messages, or distinct cashflows. It also does not specify the environment, measurement period, extraction query, or whether the data is specific to Uber, FXU, or a combined scope.

## Production data inventory

| AccountingUpdate | Count |
| --- | ---: |
| AccountingUpdate | 3116582 |
| Affirmed | 543155 |
| Approve | 389089 |
| ApproveOnlyMaker | 359321 |
| AutoFail | 2915 |
| CashflowStamped | 20770369 |
| Comment | 73127 |
| EarlyRelease | 5966 |
| EarlyReleaseToRazor | 770 |
| Fail | 29425 |
| GenerateSwift | 8820924 |
| Hold | 3567 |
| IsAutoNettingEligible | 4543414 |
| IsNettingEligible | 7218543 |
| IsNstp | 1127938 |
| IsNstpChecker | 6793 |
| ManualAffirmed | 15 |
| ManualSuppress | 34086 |
| ManualSwiftSuppress | 54619 |
| ManualSwiftUnSuppress | 851 |
| ManualUnSuppress | 2703 |
| Materialize | 19300238 |
| Net | 12074869 |
| NetNew | 256742 |
| New | 20684985 |
| NostroStamped | 139380 |
| PaymentDateUpdate | 3100 |
| ReGenerateSwift | 19 |
| ReInstate | 19381 |
| Reject | 12972 |
| Release | 6628828 |
| ReplayStatusWriteBack | 18 |
| ResendToRazor | 6 |
| RevertToQueued | 381666 |
| SentToRazor | 102222 |
| Settle | 8882910 |
| SettleAsGross | 19257 |
| Split | 93 |
| SplitNew | 290 |
| SsiStamped | 2183549 |
| Submit | 307431 |
| Suppress | 6883240 |
| SwiftSuppress | 243122 |
| SwiftUpdate | 942246 |
| TechFail | 3796 |
| UnHold | 3157 |
| UnNet | 1559252 |
| UnSplit | 15 |
| ValidateDirect | 912582 |
| VostroStamped | 279 |
| WaitingAnotherLeg | 323814 |
| Withdrawal | 1042329 |

## Interpretation

The largest observed categories are `CashflowStamped`, `New`, `Materialize`, `Net`, `Settle`, `GenerateSwift`, `Suppress`, `Release`, `IsNettingEligible`, and `IsAutoNettingEligible`. These categories are candidates for representative high-volume test workloads, but the counts do not establish performance bottlenecks or throughput requirements.

Very low-frequency categories include `ResendToRazor`, `ManualAffirmed`, `UnSplit`, `ReplayStatusWriteBack`, `ReGenerateSwift`, `Split`, `VostroStamped`, `SplitNew`, and `EarlyReleaseToRazor`. Their low frequency should not exclude them from correctness, recovery, and exception-path testing.

The categories appear to cover lifecycle creation, materialization, stamping, netting, settlement, Swift processing, maker-checker actions, validation, holding, recovery, and structural cashflow changes. These are analytical groupings rather than classifications explicitly defined by the source.

## Limitations and follow-up

The data should not be used to derive rates, trends, latency targets, failure percentages, or Uber-versus-FXU comparisons until its provenance is confirmed. In particular, the test plan should document:

- The source query or export that produced the counts.
- The environment and extraction date.
- The measurement period.
- The unit represented by each count.
- Whether categories are mutually exclusive.
- The allocation of records between Uber and FXU.
- The mapping from categories to test cases and acceptance thresholds.

This source extends [[concepts/uber-scbml-performance-regression-testing]] with a candidate production-volume baseline, while preserving the distinction between observed counts and inferred testing priorities.
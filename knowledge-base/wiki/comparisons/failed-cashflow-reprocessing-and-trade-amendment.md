---
type: comparison
title: Failed Cashflow Reprocessing and Trade Amendment
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, failed-cashflow, reprocessing, trade-amendment, accounting]
related: [failed-cashflow-accounting, cashflow-event-versioning, reversal-and-correction-cashflow-processing, swift-suppression, ratan, razor]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Failed Process/Failed Cashflow Accounting.md"]
---

# Failed Cashflow Reprocessing and Trade Amendment

The source describes three related flows. They share the initial Value Date failure but differ in event type, status progression, accounting treatment, and Swift timing.

## Flow Comparison

| Flow | Initial event | Later event | Status sequence | Accounting treatment | Swift treatment |
|---|---|---|---|---|---|
| Simple failed reprocessing | `New` | `New` | `FAILED` → `READY` | Initial accounting on VD; later row shows `Y(Reversal &New)` | Bypassed on VD; generated on VD+1 after Swift Value Date update |
| Amendment after accounting | `New` | `Amendment` | `FAILED` → `READY` | Initial accounting, then reversal-and-new for the amended event | Swift generation marked `Y`; Swift Value Date is blank in the table |
| Multiple failure and amendment | `New` | `Amendment` | `FAILED` → `WAITING` → `FAILED` → `READY` | Initial accounting, then reversal-and-new after the amended failure | Bypassed for both failures; generated on VD+2 after re-processing |

## Shared Behavior

All flows use cashflow ID `C101`, begin with a Value Date failure, and send the `FAILED` cashflow to Razor for accounting. Swift generation is not performed while the status is `FAILED`.

## Important Differences

### Simple Reprocessing

The original `New` cashflow remains the event being re-processed. Operations updates the Swift Payment Date to VD+1 and changes the status to `READY`. The source does not explain the `Y(Reversal &New)` accounting value shown for this row.

### Amendment After Accounting

The amount changes from USD 100 to USD 200 and the event changes from `New` to `Amendment`. Because the original cashflow was already accounted for, the source requires reversal-and-new accounting for the amended event.

### Multiple Failure and Amendment

The amendment first remains in `WAITING` and is not sent to Razor. After it fails again, it is sent to Razor with `FAILED` status and receives reversal-and-new accounting. Re-processing on VD+2 changes it to `READY`, assigns 10th May as the Swift Value Date, and enables Swift generation.

## Control Implications

The shared cashflow ID cannot by itself distinguish the original and amended states. The implementation therefore needs an authoritative event, version, or minor-version correlation key. The flows also require explicit rules for the transition from `WAITING` to `FAILED` and for the relationship between accounting correction and Swift generation.

The comparison should be read with [[queries/what-is-the-authoritative-failed-cashflow-state-machine]] and [[queries/what-is-the-authoritative-cashflow-version-key-for-failed-reprocessing]].
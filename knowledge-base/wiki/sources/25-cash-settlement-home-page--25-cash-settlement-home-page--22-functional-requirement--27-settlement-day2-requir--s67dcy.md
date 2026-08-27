---
type: source
title: Split Demo Cases
authors: []
year: 2025
url: ""
venue: Internal functional requirement
tags: [cashflow-splitting, settlement, ratan, functional-requirement]
related: [manual-cashflow-splitting, cashflow-un-split, split-cashflow-amendment, threshold-based-cashflow-auto-distribution, nostro-threshold-static, authoritative-split-cashflow-lifecycle]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting/Split Demo Cases.md"]
---
# Split Demo Cases

This functional requirement specifies manual cashflow splitting for settlement using different vostro/nostro settlement instructions, together with un-split, split-amendment, withdrawal, and threshold-based auto-distribution behavior.

## Manual split

Operations selects a gross cashflow and performs a manual split. The system initially generates a child with the original amount, applies predefined currency-specific decimal and rounding rules, and calculates the remaining balance when the operator enters a lower amount.

The entered amount must be greater than zero and no greater than the available balance. An optional SI lookup supports selection of distinct settlement instructions for child cashflows. The operator completes the operation through **Split Cashflow with Affirmation**, entering affirmation information and confirming the split.

The intended settlement-instruction use case relates to [[vostro-nostro-ssi-selection]] and [[vostro-nostro-ssi-matching]]. The source does not establish that child cashflows follow the full [[ssi-stamping]] workflow.

## Manual split result

| Object | Required result |
|---|---|
| Parent cashflow | Moves to `SPLIT` |
| Child cashflows | Created in `WAITING` |
| Child exception | `Split Cashflow` |
| Discovery key | Shared `Splitting Id` identifies parent and children |

The shared identifier contributes a split-specific form of [[cashflow-lineage-and-amendment-correlation]].

## Un-split

An operator may un-split an eligible cashflow in the following statuses:

```text
QUEUED
WAITING
FAILED
HOLD
READY(NA)
CASHFLOW_SUPPRESSED
```

The specified outcome is:

| Object | Required result |
|---|---|
| Parent cashflow | Moves to `WAITING` with `Un-Split` exception |
| Child cashflows | Move to `DEAD` |
| `Splitting Id` | Removed from the cashflow |

The source does not specify whether the operator must select the parent or may initiate un-split from any member of the split group. `CASHFLOW_SUPPRESSED` is eligible here, but this does not establish equivalent semantics to [[murex-2-11-cashflow-suppression]].

## Split amendment

Split amounts may be amended when at least two child cashflows are in `WAITING`. Only `WAITING` child amounts may change, and the total of all child cashflows must equal the original parent amount.

After amendment, the parent remains `SPLIT`; updated children remain `WAITING` and receive an additional `Split Amend` exception.

## Withdrawal handling

Withdrawal behavior depends on whether children have been released from [[ratan]]:

| Condition | Required behavior |
|---|---|
| No child released from Ratan | Withdrawal event moves to `SPLIT`; child cashflows are cancelled. |
| At least one child released from Ratan | Withdrawal event moves to `SPLIT`; unreleased children are directly cancelled; released children retain corresponding withdrawal events in `NSTP` pending user action. |

The release-defining event and final closure lifecycle are unspecified.

## Auto distribution process

A separate automated process applies when a cashflow exceeds the processing threshold of a nostro agent. At release cut-off time, the system splits the cashflow into lower-value children and directly generates SWIFT and accounting outputs for each child downstream.

The source uses `TRY` only as an example of a currency whose cashflow exceeds a configured threshold. It does not define threshold matching precedence, child status, exception behavior, rounding-residual allocation, idempotency, or downstream failure recovery.

## Nostro Threshold Static

A new static-data blotter manages auto-distribution thresholds:

| Attribute | Requirement |
|---|---|
| Currency | Mandatory |
| Booking entity | Optional |
| Nostro agent BIC | Optional |
| Data Ops access | Create, update, delete |
| Other user access | Read-only |

See [[nostro-threshold-static]] and [[threshold-based-cashflow-auto-distribution]].

## Source attachments

The source references the following screenshots, which are not reproduced in the imported text:

```text
attachments/image-2025-9-25_23-4-16.png
attachments/image-2025-9-25_23-7-40.png
attachments/image-2025-9-25_23-9-47.png
attachments/image-2025-9-25_23-13-35.png
attachments/image-2025-9-25_23-20-25.png
attachments/image-2025-9-25_23-21-22.png
attachments/image-2025-9-25_23-27-14.png
attachments/image-2025-9-26_9-46-9.png
```
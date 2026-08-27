---
type: concept
title: BIC Netting Static Data Lifecycle
tags: [bic-netting, static-data, lifecycle, maker-checker, ratan]
related: [bic-netting-static-tile, beneficiary-bic-netting, bic-net-eligibility-flag, what-is-the-ratan-bic-netting-static-deletion-rejection-and-pending-record-lifecycle, what-is-the-authoritative-beneficiary-bic-netting-static-schema-and-governance]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Ratan One Processing Guide (DOI)/BIC Netting Static.md"]
---

# BIC Netting Static Data Lifecycle

BIC Netting Static changes in [[ratan]] are managed through a maker/checker workflow. A maker submits additions, updates, and deletions; a checker reviews the pending change and approves or rejects it.

## Documented statuses and effects

| Status | Meaning or effect |
|---|---|
| `ADD_PENDING` | A maker added a static record. It is pending checker action and does not yet take effect. |
| `UPDATE_PENDING` | A maker updated a static record and the update is pending checker action. |
| `DELETE_PENDING` | A maker deleted a static record and the deletion is pending checker action. |
| `SAVE_CONFIRMED` | A checker approved an addition or update and it takes effect. The source also uses this status when an update is rejected, in which case the original version remains effective. |
| `DELETE_CONFIRMED` | A checker approved deletion. The record is not shown in the static list but can be seen in audit. |
| `DISCARDED` | A checker rejected an addition. The record is discarded and does not take effect. |

## Lifecycle interpretation

The documented paths are:

- Add → `ADD_PENDING` → checker approval → `SAVE_CONFIRMED`.
- Add → `ADD_PENDING` → checker rejection → `DISCARDED`.
- Update → `UPDATE_PENDING` → checker approval → `SAVE_CONFIRMED`, with the updated version effective.
- Update → `UPDATE_PENDING` → checker rejection → `SAVE_CONFIRMED`, with the original version effective.
- Delete → `DELETE_PENDING` → checker approval → `DELETE_CONFIRMED`, with the record removed from the static list and retained for audit.

The source does not document the result of checker rejection for `DELETE_PENDING`. It also does not document cancellation, editing, or resubmission of pending changes.

## Governance implications

`SAVE_CONFIRMED` is an effective status, but it does not by itself distinguish an approved update from a rejected update whose original version remains active. Action history or another audit attribute may therefore be required to determine how the current version was reached.

The lifecycle describes operational governance only. It does not define the static-data schema, uniqueness rules, effective dates, ownership, approval limits, or downstream netting calculation.

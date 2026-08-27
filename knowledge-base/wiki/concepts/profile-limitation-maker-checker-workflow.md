---
type: concept
title: Profile Limitation Maker-Checker Workflow
created: 2026-08-24
updated: 2026-08-24
tags: [maker-checker, profile-limitation, approval, rejection, audit, soft-delete]
related: [profile-limitation, profile-limitation-check-api, ratanone-rule-service, maker-checker-configuration-governance, pending-configuration-change-isolation, static-configuration-auditability, profile-limitation-lifecycle-and-api-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan Rule Service Technical Design/Profile Limitation Maker Checker Design.md"]
---
# Profile Limitation Maker-Checker Workflow

The Profile Limitation Maker-Checker Workflow requires a checker to confirm or reject changes submitted for a [[profile-limitation]]. It is a specialized instance of [[maker-checker-configuration-governance]] with different outcomes for add, edit, and delete operations.

## States

The documented states are `ADD_PENDING`, `EDIT_PENDING`, `DELETE_PENDING`, `CONFIRMED`, and `ADD_REJECTED`.

## Approval and Rejection Semantics

- Confirming an add or edit changes the record to `CONFIRMED` and records checker identity and action time.
- Confirming a deletion changes the record to `CONFIRMED` and sets `is_delete` to `true`, indicating a soft-delete approach.
- Rejecting an edit or deletion restores the previous limitation value and changes the record to `CONFIRMED`.
- Rejecting an addition is described as changing the record to `ADD_REJECTED` and deleting it directly.

Checker identity and timestamp are mandatory audit attributes, aligning this workflow with [[static-configuration-auditability]].

## Runtime Isolation

The design intends that pending limitation changes are unavailable through the runtime check interface. This applies at least to `EDIT_PENDING`; the source also refers to an undefined `ADD_CONFIRMED` state. The exact visibility behavior, including behavior for pending deletion and any existing confirmed value during a pending edit, remains unresolved.

See [[profile-limitation-lifecycle-and-api-contract]] for the outstanding state-model and persistence questions.
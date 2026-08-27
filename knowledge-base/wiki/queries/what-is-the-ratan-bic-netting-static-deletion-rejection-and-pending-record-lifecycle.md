---
type: query
title: What Is the RATAN BIC Netting Static Deletion Rejection and Pending Record Lifecycle?
tags: [ratan, bic-netting, static-data, lifecycle, open-question]
related: [bic-netting-static-tile, bic-netting-static-data-lifecycle, beneficiary-bic-netting, what-is-the-authoritative-beneficiary-bic-netting-static-schema-and-governance]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Ratan One Processing Guide (DOI)/BIC Netting Static.md"]
---

# What Is the RATAN BIC Netting Static Deletion Rejection and Pending Record Lifecycle?

## Question

What happens when a checker rejects a `DELETE_PENDING` BIC Netting Static record, and what operations are permitted while a record remains in any pending status?

## Evidence currently available

The processing guide states that:

- A maker can delete a `SAVE_CONFIRMED` record.
- The deletion becomes `DELETE_PENDING`.
- Checker approval produces `DELETE_CONFIRMED`; the record is removed from the static list but remains visible in audit.
- The guide does not state the status produced when a checker rejects the deletion.
- The guide does not state whether pending additions, updates, or deletions can be cancelled, edited, or resubmitted.

For additions, checker rejection produces `DISCARDED`. For updates, checker rejection leaves the record in `SAVE_CONFIRMED` and preserves the original version. These documented outcomes do not establish the deletion-rejection outcome.

## Why this matters

The deletion-rejection result is needed to define the complete [[bic-netting-static-data-lifecycle]], user interface behavior, audit interpretation, and eligibility of a record for later maker actions. It also determines whether a rejected deletion restores the previously effective record or creates another status requiring intervention.

## Resolution required

Confirm the authoritative state-transition matrix for:

- Rejection of `DELETE_PENDING`.
- Maker cancellation of pending additions, updates, and deletions.
- Editing or resubmitting pending records.
- Approval and rejection of mixed action types in one batch.
- Partial success, concurrency conflicts, and retry behavior.
- Self-approval prevention when a user has both `FMO_STA_MKR` and `FMO_STA_CKR`.

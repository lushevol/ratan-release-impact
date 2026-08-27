---
type: entity
title: BIC Netting Static Tile
tags: [ratan, bic-netting, static-data, user-interface]
related: [ratan, beneficiary-bic-netting, bic-netting-static-data-lifecycle, bic-net-eligibility-flag, what-is-the-authoritative-beneficiary-bic-netting-static-schema-and-governance]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Ratan One Processing Guide (DOI)/BIC Netting Static.md"]
---

# BIC Netting Static Tile

The **BIC Netting Static** tile is the RATAN ONE interface for maintaining static data used by [[beneficiary-bic-netting]]. It is located under:

`Static → BIC Netting Static`

The tile supports:

- Creating new static records.
- Updating existing records.
- Submitting records for deletion.
- Checker approval or rejection.
- Batch deletion of confirmed records.
- Batch approval or rejection.
- Data extraction after navigating through all pages.

## Access profiles

The source names two RATAN access profiles:

- `FMO_STA_MKR` — maker profile associated with creating, updating, and submitting deletions.
- `FMO_STA_CKR` — checker profile associated with reviewing, approving, or rejecting pending changes.

The source does not provide a complete entitlement matrix or clarify whether the profiles can be combined on one user.

## Record administration

New values are entered according to requirements supplied by the settlement operation team. Values must not contain leading or trailing blanks.

A maker can delete multiple records in one batch when the records have `SAVE_CONFIRMED` status. A checker can approve or reject multiple records after reviewing their details.

The tile uses the status lifecycle described in [[bic-netting-static-data-lifecycle]].

## External access guidance

The processing guide links to the Derivative Strategy Projects Confluence guidance for requesting RATAN ONE access:

[How to apply for RATAN ONE access - Derivative Strategy Projects - Confluence](https://confluence.global.standardchartered.com/display/DSP/How+to+apply+for+RATAN+ONE+access)

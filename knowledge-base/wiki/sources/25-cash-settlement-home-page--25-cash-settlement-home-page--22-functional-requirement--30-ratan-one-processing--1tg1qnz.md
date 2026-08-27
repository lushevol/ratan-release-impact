---
type: source
title: BIC Netting Static Processing Guide
authors: []
year: 2024
url: ""
venue: "RATAN One Processing Guide (DOI)"
tags: [cash-settlement, ratan, bic-netting, static-data, maker-checker]
related: [ratan, bic-netting-static-tile, beneficiary-bic-netting, bic-netting-static-data-lifecycle, what-is-the-ratan-bic-netting-static-deletion-rejection-and-pending-record-lifecycle, what-is-the-authoritative-beneficiary-bic-netting-static-schema-and-governance]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Ratan One Processing Guide (DOI)/BIC Netting Static.md"]
---

# BIC Netting Static Processing Guide

## Scope

This processing guide describes the operational maintenance of BIC Netting Static records in [[ratan]]. It covers access profiles, the location of the BIC Netting Static tile, maker and checker actions, batch operations, status values, and data extraction.

It does not define the record schema, field-level validation rules, API contract, database structure, approval limits, audit-retention period, or downstream beneficiary-BIC matching logic.

## Access and navigation

Users with the RATAN profiles `FMO_STA_CKR` and `FMO_STA_MKR` are described as being able to maintain BIC Netting Static data. The source assigns creation, update, and deletion submission to the maker and approval or rejection to the checker.

The tile is located at:

`Static → BIC Netting Static`

The guide links to the following access-request documentation:

[How to apply for RATAN ONE access - Derivative Strategy Projects - Confluence](https://confluence.global.standardchartered.com/display/DSP/How+to+apply+for+RATAN+ONE+access)

## Operational procedures

### Add

The maker selects **Create**, enters the details required by the settlement operation team, and saves the record. Values must not contain a blank at the beginning or end.

After the maker submits the record, the checker refreshes the page and reviews the new record before approving or rejecting it.

### Update

For an existing record, the maker can initiate an update through the row’s double-click or right-click interaction. After the maker saves the update, the checker can approve or reject it through the corresponding double-click or right-click interaction.

### Delete

A maker can delete a record in `SAVE_CONFIRMED` status.

### Batch operations

A maker can select multiple `SAVE_CONFIRMED` records for batch deletion.

A checker can select multiple records for batch approval or rejection after verifying their details.

The source does not specify whether a batch may contain mixed action types, whether processing is atomic, or how partial failures are reported.

## Static Data Status List

The following table is reproduced from the source:

| | Status | Comment |
| --- | --- | --- |
| 1 | ADD_PENDING | Maker added static record |
| 2 | UPDATE_PENDING | Maker updated static record |
| 3 | DELETE_PENDING | Maker deleted static record |
| 4 | SAVE_CONFIRMED | Checker approved adding/updating static record, which will take effect. Checker rejected updating static record, original version of the static will take effect. |
| 5 | DELETE_CONFIRMED | Checker approved deleting static record. Record can be seen in audit only, which not be shown in static list. |
| 6 | DISCARDED | Checker rejected adding static record, record will be discarded, and not take effect. |

## Extraction constraint

For data extraction, the operator is instructed to click through all pages before extracting the data. This creates a completeness risk if the operator does not visit every pagination page. The guide does not explain whether this behavior results from client-side pagination, export design, or a UI defect.

## Evidence limitations and ambiguities

- The notation `FMO_STA_CKR/FMO_STA_MKR` does not establish whether either profile, both profiles, or a composite entitlement is required.
- The outcome of checker rejection of `DELETE_PENDING` is not specified.
- The guide does not state whether pending records can be cancelled, edited, or resubmitted.
- It does not explicitly state whether self-approval is technically prevented.
- It does not identify which fields are subject to whitespace validation or whether trimming is automated.
- It does not define the authoritative BIC Netting Static schema or data ownership.

---
type: query
title: What Is the Authoritative Group Blotter Bulk STP Eligibility Rule?
created: 2026-08-23
updated: 2026-08-23
tags: [open-question, eligibility, bulk-manual-stp, group-blotter]
related: [bulk-manual-stp-group-blotter, group-blotter-cashflow-state-lifecycle, trade-major-version-manual-stp-ordering, allocation-cashflow-state-handling]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2025 changes/Bulk manual stp for Group Blotter.md"]
---
# What Is the Authoritative Group Blotter Bulk STP Eligibility Rule?

## Question

What is the definitive eligibility rule for `PENDING`, `ERROR`, `PENDING_TRADE_VALIDATION`, `PENDING_PRE_GROUP`, and `DATA_VALIDATION_FAILED` group or message states?

## Evidence

The requirement states that single-group manual STP accepts group-message status `PENDING` or `ERROR` when no previous major version has pending work. Its multi-group logic says to filter group status `DATA_VALIDATION_FAILED/PENDING_PRE_GROUP`, while the scenarios primarily use `PENDING_TRADE_VALIDATION` and `PENDING_PRE_GROUP`.

## Required Resolution

Confirm:

- Which states are eligible for single-group processing.
- Which states are eligible after trade-level precheck.
- Whether `DATA_VALIDATION_FAILED` is a valid recoverable state or a transcription error.
- Whether `ERROR` follows the same retry rules as `PENDING`.
- Whether the UI or backend rejects selections from blocked later major versions.
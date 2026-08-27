---
type: concept
title: Maker-Checker SSI Control
created: 2026-08-23
updated: 2026-08-23
tags: [maker-checker, SSI, Adhoc-SI, segregation-of-duties, workflow]
related: [adhoc-ssi-workflow, ssi, adhoc-si]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/Adhoc SI.md"]
---

# Maker-Checker SSI Control

Maker-checker SSI control is the workflow separation in which a maker initiates or inputs Adhoc SSI information and a checker approves or rejects it.

## Maker actions

- `Maker Adhoc SSI` initiates an Adhoc SSI workflow.
- `Maker Input Adhoc SSI` submits or revises Adhoc SSI information when the exception already exists.

Both actions move the workflow sub-status toward `Pending Verification`.

## Checker actions

- `Checker Approve` completes the verification path.
- `Checker Reject` returns the item to `Pending Operator` for maker processing.

For a `WAITING` cashflow, approval also changes the primary status to `READY`. For a `READY` cashflow, approval leaves the primary status unchanged.

The source implies segregation of duties through the maker and checker action names, but it does not specify user permissions, whether the maker and checker must be different users, validation rules, or audit requirements.
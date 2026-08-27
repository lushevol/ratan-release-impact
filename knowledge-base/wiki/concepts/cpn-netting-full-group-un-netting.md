---
type: concept
title: CPN Netting Full-Group Un-Netting
created: 2026-08-23
updated: 2026-08-23
tags: [cpn, un-netting, netting, maker-checker, cashflow]
related: [cpn-netting, netting-withdrawal-timing, netting-resultant-cashflow-lifecycle, manual-un-netting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/CPN Tech Design - Draft for now.md"]
---
# CPN Netting Full-Group Un-Netting

The CPN design supports full-group un-netting only. A user cannot remove an individual component from an active netting group.

## Manual un-netting

Manual un-netting can be initiated when the resultant is:

- `Pending` / `Netting Review`; or
- `Validated` / `Reviewed`.

The maker submits the un-net request and a checker approves or rejects it. On approval, the pre-release resultant moves to `DEAD`, while every component in the group moves from `Netted` to `Queued`. Components are versioned and sent through Settlement Workflow and CPN Eligibility Checking again.

## Automatic un-netting

A new version caused by a trade amendment or cancellation can trigger automatic un-netting. Before resultant release, the prior resultant moves to `Dead` and components return to workflow. After release, the original resultant remains `Released` and CPN creates a separate reversal cashflow.

The source contains inconsistent component sub-status and Netting ID values after un-netting. These fields should not be treated as authoritative until the state and relationship model is confirmed.
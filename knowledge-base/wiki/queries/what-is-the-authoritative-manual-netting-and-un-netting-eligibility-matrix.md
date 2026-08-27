---
type: query
title: What Is the Authoritative Manual Netting and Un-Netting Eligibility Matrix?
created: 2026-08-23
updated: 2026-08-23
tags: [netting, un-netting, eligibility, cashflow-status, RATAN]
related: [ratan, netting-api-contract, bilateral-netting-eligibility, cashflow-hold-and-unhold]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Netting Service - GUI & API intergration.md"]
---
# What Is the Authoritative Manual Netting and Un-Netting Eligibility Matrix?

The source gives conflicting eligibility rules between GUI guidance and backend API validation.

For netting, the GUI includes `Ready`, `Waiting`, and `Hold`, while the backend only permits `Projected`, `Queued`, `Pending`, and `Validated`.

For un-netting, the high-level GUI guidance includes `Hold`, while detailed GUI and backend rules permit only `Queued`, `Pending`, and `Validated`.

## Required resolution

Define one authoritative matrix that specifies:

- Eligible and ineligible states for manual netting.
- Eligible and ineligible states for manual un-netting.
- Whether `Hold` is supported and under which authorization constraints.
- Whether GUI action availability must exactly mirror backend enforcement.
- Error handling for stale GUI selections when a cashflow state changes before submission.

See [[netting-api-contract]].
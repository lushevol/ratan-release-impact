---
type: entity
title: 51358-ratan-cash-settlement-group-management-service
created: 2026-08-22
updated: 2026-08-22
tags: [ratan, group-management, fmrp-uber, stp, routing]
related: [ratan, chg1016055, fmrp-uber, settlement-message-routing, straight-through-processing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/FMRP China Cash Settlement Delivery Plan/Cash Settlement RATAN ONE 2026 Release Plan/Release On 2026-08-01 CR    RATAN Settlement Korea & FMRP FXO Tech Go-Live.md"]
---
# 51358-ratan-cash-settlement-group-management-service

`51358-ratan-cash-settlement-group-management-service` handles cashflow grouping and related routing behavior within RATAN.

## Release Artifact

- Deployment step: `5`
- Branch: `release/v3.2.3.3`
- Package: `3.2.3.3-20260729.4`
- Pipeline run: `20260729.4`
- Owners: Chen Yang, Junli Gao, Xinmiao Huang, and Yonghua Li
- Rollback: recorded as existing

## Scope

- Skip TDS3 ND parent-information queries for Korea cashflows.
- Apply new [[fmrp-uber]] fields according to Eco/Non eco amendment behavior.
- Change SCBML and downstream-consumer routing.
- Replace a technical warning with a soft warning for specified manual-STP New and Amendment cases.

The source associates Haolin Song and Xinmiao Huang with the warning behavior but does not specify formal decision ownership or rationale.

## Routing Interpretation

The package description says to skip the trade SCBML consumer while keeping LOANIQ/Murex only. Related database configuration describes UBER as enabled for consumers except LOANIQ and SCBML as retained for LOANIQ. These statements should be validated together against the production routing records rather than generalized independently.
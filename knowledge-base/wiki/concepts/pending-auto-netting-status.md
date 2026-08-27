---
type: concept
title: Pending Auto Netting Status
created: 2026-08-22
updated: 2026-08-22
tags: [auto-netting, cashflow-status, settlement, regression-testing]
related: [inter-entity-auto-netting, inter-entity-netting, murex-cashflow-status-lifecycle, regression-failure-triage, uber-regression-testing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Uber Development Testing/UBER regression - round 2.md"]
---
# Pending Auto Netting Status

## Definition

`Pending Auto Netting` is a status label expected by several netting regression cases. The same cases observed `Pending Netting`, creating an unresolved question about whether the labels represent distinct canonical lifecycle states or equivalent presentation and test terminology.

## Regression evidence

Five residual cases remained in the broader `SFMRPNetting` package:

- `CN-API-CCILNetting-NonGuaranteed-018` expected `Pending Auto Netting` but observed `Pending Netting`.
- `CN-API-PendingNettingCfNotAbleNetOverNet-002` expected `Pending Auto Netting` but observed `Pending Netting`.
- `CN-API-CashflowsDoNet-013` expected `WAITING` but observed `SETTLED`.
- `CN-API-BicAterSetAsGros-021` involved timing and settlement-classification differences.
- `CN-API-NDSAutoNetting-001` was identified as a data issue.

The AutoNettingForRefresh package reaching zero failures does not resolve the broader status-semantic question.

## Operational significance

A canonical status contract should define:

- Whether `Pending Auto Netting` is distinct from `Pending Netting`
- Which transitions produce each status
- Whether status is authoritative in the API, UI, database, or event message
- How test assertions should handle asynchronous updates
- How `SETTLED`, `WAITING`, and pending-netting states interact with release and payment controls
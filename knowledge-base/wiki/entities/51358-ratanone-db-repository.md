---
type: entity
title: 51358-ratanone-db-repository
created: 2026-08-22
updated: 2026-08-22
tags: [ratan, database, configuration, rollback, routing]
related: [ratan, chg1016055, ratan-settlement-korea, fmrp-uber, auto-netting, settlement-message-routing, nostro-configuration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/FMRP China Cash Settlement Delivery Plan/Cash Settlement RATAN ONE 2026 Release Plan/Release On 2026-08-01 CR    RATAN Settlement Korea & FMRP FXO Tech Go-Live.md"]
---
# 51358-ratanone-db-repository

`51358-ratanone-db-repository` contains database and configuration changes for [[chg1016055]].

## Release Artifact

- Deployment step: `2`
- Branch record: `feature/korea develop CHG1016055_Korea/ CHG1016055_Korea_Rollback`
- Execute pipeline: `20260722.6`
- Rollback pipeline: `20260722.7`
- Owners: Chongxuan Li and Guiling Wang
- Rollback: recorded as existing

## Korea Scope

- Nostro records.
- Currency cut-offs.
- Rule records.
- EBBS bridge-account and transaction-code configuration.
- SWIFT configuration.
- Auto-netting configuration ID `9`.
- A required netting-service restart after the auto-netting key is applied.

## FMRP UBER Scope

- Retain the SCBML flow for LOANIQ.
- Configure UBER behavior around LOANIQ exclusion.
- Add trade fields for the UI.
- Open UBER filters to consumers except LOANIQ.
- Disable broader SCBML filtering while retaining LOANIQ-specific behavior.

## Removed or Unconfirmed Scope

The source strikes through:

- MB message-type conversion to JSON.
- A new two-way IBMMQ integration between RATAN and Murex KR.

These items must not be treated as deployed without further confirmation.

## Verification

PIT checks static-data counts, EBBS and SWIFT records, auto-netting configuration, rule IDs, accounting schema metadata, UBER flow records, and bridge filters. Many expected and actual values are retained only in screenshots.
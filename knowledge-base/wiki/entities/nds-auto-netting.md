---
type: entity
title: NDS Auto Netting
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, auto-netting, processing]
related: [2025-cash-settlement-tranche-1, cashflow-monitoring, cashflow-reconciliation, what-flag-does-nds-auto-netting-require]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/FMRP China Cash Settlement Delivery Plan/Cash Settlement RATAN ONE 2025 Release Plan/2025 Cash Settlement Tranche 1 Ratan Runbook.md"]
---

# NDS Auto Netting

## Role in the runbook

`NDS Auto Netting` is a processing system or capability whose pending state must be checked during both tranche monitoring and whole-data reconciliation.

The runbook asks whether `NDS Auto Netting` is pending another flag, but it does not identify the required flag, define an expected state, or indicate that the system is defective. No execution result is recorded.

## Required validation

The release team should clarify:

- Which flag permits or explains the pending state.
- Whether pending is expected for the tested cashflows.
- What status or transition constitutes acceptance.
- How exceptions should be escalated.

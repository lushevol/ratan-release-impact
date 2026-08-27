---
type: concept
title: Pending Cashflow Monitoring
created: 2026-08-22
updated: 2026-08-22
tags: [cashflows, monitoring, NSTP, exception-handling, settlement]
related: [fxo-mini-trade-migration-ratan-cash-settlement, high-risk-nstp-rule, cashflow-suppression, murex-2-11, stella]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/FMRP China Cash Settlement Delivery Plan/Cash Settlement RATAN ONE 2026 Release Plan/FXO Mini Trade Migration - Ratan Cash Settlement - RunBook (2026-08-15 weekend).md"]
---
# Pending Cashflow Monitoring

Pending cashflow monitoring is the review of cashflows that have not completed expected netting or settlement processing.

The runbook identifies these states for monitoring:

- `Pending Auto Netting`
- `Pending Netting`
- `Pending Another Leg`

The purpose is to identify in-scope Murex cashflows that do not hit the High Risk NSTP rule and cashflows that are incorrectly `RELEASED` or `SETTLED`. The stated exception path is for the cashflow to enter `WAITING`, receive a reversal after Murex cancellation feeds in, and then be released as a withdrawn Murex or Stella cashflow.

The source does not assign a distinct owner or closure criterion for each exception.
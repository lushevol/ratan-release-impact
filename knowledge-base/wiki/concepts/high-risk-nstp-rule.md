---
type: concept
title: High Risk NSTP Rule
created: 2026-08-22
updated: 2026-08-22
tags: [NSTP, STP, risk-control, cashflows, migration]
related: [fxo-mini-trade-migration-ratan-cash-settlement, murex-2-11, stella, cashflow-suppression, pending-cashflow-monitoring]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/FMRP China Cash Settlement Delivery Plan/Cash Settlement RATAN ONE 2026 Release Plan/FXO Mini Trade Migration - Ratan Cash Settlement - RunBook (2026-08-15 weekend).md"]
---
# High Risk NSTP Rule

A High Risk NSTP rule is an operational control that identifies cashflows requiring non-straight-through processing because of migration risk or exception conditions.

The source defines two named rules:

- `FXO-Mini_TM_Murex_Cfs`
- `FXO-Mini_TM_Stella_Cfs`

The Murex rule initially filters by source system, payment date, and in-scope portfolio. During the migration window, the portfolio criterion is replaced by a cancelled-trade or original-trade-ID list. The Stella rule uses source system, payment date, and in-scope portfolio.

The source does not clearly document the lifecycle relationship between these rules and the similarly named filters `00Elena_TM_Murex_NSTP_Cfs` and `00Elena_TM_Stella_NSTP_Cfs`.
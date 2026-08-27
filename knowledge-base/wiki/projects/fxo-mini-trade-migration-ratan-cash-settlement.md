---
type: project
title: FXO Mini Trade Migration - Ratan Cash Settlement
status: active
owner: "Migration Team"
start_date: 2026-08-03
target_date: 2026-08-15
created: 2026-08-22
updated: 2026-08-22
tags: [FXO, FMRP, migration, cash-settlement, Ratan-Settlement]
related: ["murex-2-11", "stella", "ratan-settlement", "cash-settlement-migration", "high-risk-nstp-rule", "trade-cashflow-reconciliation", "authoritative-migration-date-and-final-scope"]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/FMRP China Cash Settlement Delivery Plan/Cash Settlement RATAN ONE 2026 Release Plan/FXO Mini Trade Migration - Ratan Cash Settlement - RunBook (2026-08-15 weekend).md"]
---
# FXO Mini Trade Migration - Ratan Cash Settlement

## Objective

Coordinate a limited FXO trade migration in which selected [[murex-2-11]] and [[stella]] cashflows are controlled and reconciled through [[ratan-settlement]].

## Scope

The runbook describes more than 100 trades and records an interim count of 130 trades on 2026-08-03. The listed portfolio pairs are:

- `OP_GBL_THO` / `OP_GBL_THO_STL`
- `OP_BTB_THAI` / `OP_BTB_THAI_STL`
- `OP_GBL_CNY` / `OP_GBL_CNY_STL`
- `OP_BTB_TANZNIA` / `OP_BTB_TANZNIA_STL`
- `OP_GBL_ZAR` / `OP_GBL_ZAR_STL`

The final trade population is not confirmed.

## Delivery approach

The project uses [[high-risk-nstp-rule]] controls and temporary [[cashflow-suppression]] to separate migration-related flows from out-of-scope BAU processing. The runbook covers:

1. Portfolio and trade-scope confirmation.
2. Murex High Risk NSTP rule setup and UVT.
3. Pre-window monitoring of pending and incorrectly released or settled cashflows.
4. Final cancellation, settlement, pending-cancellation, and trade-ID mapping reports.
5. Murex and Stella rule configuration during the migration window.
6. Cashflow suppression and un-suppression.
7. Monitoring of Stella and Murex flows into Ratan Settlement.
8. Seven-day forward exports and cross-system [[trade-cashflow-reconciliation]].
9. Rule disablement and restoration of BAU behavior.

## Owners and participants

- Migration Team
- Murex Team
- PSS
- Ops User
- Rule User
- Yonggang Carter Deng
- Cordelia Sumita K Thirunavukarasu
- Kuan Wang (Elena)
- Linzhen Wu (Wythe)
- Nagaraj Ponnuchamy
- Bin Abdul Kadir Abdullah
- Babu

## Status and evidence

The project should be treated as an execution plan with partial completion notes rather than as a completed project retrospective. The source records:

- Murex rule UVT completed on 2026-08-07 by Bin Abdul Kadir Abdullah.
- Cashflow suppression and un-suppression preparation completed by Babu on 2026-08-14.
- Murex rule disablement completed on 2026-08-14.

It does not record final reconciliation results, complete status values, sign-off, or an overall migration outcome.

## Risks and open items

- The runbook contains both `2026-05-16` and an August 2026 migration context.
- The final trade count is not stated.
- The relationship between portfolio-based and trade-ID-based scope controls is undocumented.
- Reconciliation acceptance criteria and sign-off are absent.
- Exception handling for incorrectly released, settled, waiting, or reversed cashflows is incomplete.

See [[authoritative-migration-date-and-final-scope]] for the unresolved date and scope questions.
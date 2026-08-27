---
type: concept
title: Trade and Cashflow Reconciliation
created: 2026-08-22
updated: 2026-08-22
tags: [reconciliation, cashflows, trade-IDs, settlement, controls]
related: [fxo-mini-trade-migration-ratan-cash-settlement, murex-2-11, stella, ratan-settlement, pending-cashflow-monitoring]
sources: ["auto-netting-page-md-files/Cash Settlement Home Page -- Cash Settlement Home Page -- FMRP China Cash Settlement Delivery Plan -- Cash Settlement RATAN ONE 2026 Release Plan -- Cash Settlement RATAN ONE 2026 Release Plan -- FXO Mini Trade Migration - Ratan Cash Settlement - RunBook (2026-08-15 weekend).md", "Cash Settlement Home Page/Cash Settlement Home Page/FMRP China Cash Settlement Delivery Plan/Cash Settlement RATAN ONE 2026 Release Plan/FXO Mini Trade Migration - Ratan Cash Settlement - RunBook (2026-08-15 weekend).md"]
---
# Trade and Cashflow Reconciliation

Trade and cashflow reconciliation compares records across source and target systems to identify missing, duplicated, incorrectly migrated, pending, released, settled, or cancelled cashflows.

The runbook requires:

- Stella versus Ratan Settlement cashflow-feed reconciliation.
- Stella versus Murex2.11 seven-day cashflow reconciliation.
- Murex2.11 versus Ratan cancellation reconciliation.
- Group Blotter and Cashflow Blotter record-count checks.
- Future seven-day exports keyed by original trade ID or mapped trade ID.
- Confirmation that Murex cashflows cancel naturally with trade cancellation.

The source does not define matching logic, tolerances, acceptance criteria, sign-off, or evidence-retention requirements. Therefore, the planned reconciliation framework cannot be treated as evidence of a successful migration.
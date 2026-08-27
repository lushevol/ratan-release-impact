---
type: concept
title: Cashflow Suppression and Un-Suppression
created: 2026-08-22
updated: 2026-08-23
tags: ["cashflows", "suppression", "un-suppression", "BAU", "migration", "cash-settlement", "cashflow", "stp", "nstp"]
related: ["fxo-mini-trade-migration-ratan-cash-settlement", "high-risk-nstp-rule", "murex-2-11", "stella", "pending-cashflow-monitoring", "ratan", "oscar", "suppression-maker-checker-workflow", "suppression-rule-management", "cashflow-status-lifecycle", "cashflow-amendment-supersession", "swift-suppression"]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/FMRP China Cash Settlement Delivery Plan/Cash Settlement RATAN ONE 2026 Release Plan/FXO Mini Trade Migration - Ratan Cash Settlement - RunBook (2026-08-15 weekend).md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Cashflow Swift Suppression.md"]
---
# Cashflow Suppression and Un-Suppression

Cashflow suppression temporarily prevents selected cashflows from normal processing. Un-suppression restores them to processing after the relevant migration control or exception has been handled.

In the Ratan workflow, Cashflow Suppression is intended for cases where **payment and settlement accounting are not required**. An approved manual suppression transitions the cashflow to `CASHFLOW SUPPRESSED`.

Automatic suppression is driven by the Cashflow Suppress Rules Table and does not require a per-cashflow Maker/Checker decision. However, creation and deletion of suppression rules remain Maker/Checker controlled.

## Migration and BAU handling

In the migration runbook, `00Elena_TM_Murex_NSTP_Cfs` identifies Murex2.11 cashflows for suppression and un-suppression. This allows out-of-scope cashflows to continue normal BAU behavior, including STP or NSTP processing.

A similar workflow is planned for Stella using `00Elena_TM_Stella_NSTP_Cfs`.

The runbook records preparation as completed by Babu on 2026-08-14, but does not provide a complete audit trail of all cashflows processed.

## Error correction

A manual undo is permitted only until value date. Checker approval of an undo transitions the cashflow to `QUEUED`.

When payment and accounting are required after value date, the functional requirement directs handling through [[oscar]]. It does not specify accounting, audit, cancellation, or amendment treatment for `CASHFLOW SUPPRESSED` cashflows after value date; see [[what-is-the-post-value-date-processing-model-for-cashflow-suppressed-cashflows]].

## Lifecycle handling

Trade amendments and cancellations are treated as a new version and proceed through a new lifecycle.

The functional requirement does not define the exact rollback status following Checker rejection of a suppression request. See [[what-is-the-authoritative-rollback-status-for-rejected-suppression-actions]].
---
type: project
title: Murex Cashflow Migration to RATAN
status: on-hold
owner: ""
start_date: 2023-09-02
target_date: ""
created: 2026-08-22
updated: 2026-08-22
tags: [murex, ratan, migration, china, settlement]
related: [murex-to-ratan-cashflow-integration, murex-ratan-migration-reconciliation, murex-cashflow-status-lifecycle, razor, stella]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration.md"]
---
# Murex Cashflow Migration to RATAN

## Objective

Migrate eligible China non-precious-metal cashflows from [[murex]] to [[ratan]] ahead of trade migration to [[stella]], while preserving settlement continuity and preventing duplicate settlement.

## Proposed cutover approach

- Complete or manually handle unsettled non-STP cashflows with value date before cutover in Murex.
- Retain or return eligible future cashflows to `INIT` for RATAN dispatch at or after cutover.
- Stop China Murex payment STP one week before migration so post-cutover flows are not settled by Murex.
- Trigger a controlled Murex job during the go-live weekend to dispatch remaining qualifying cashflows.
- Reconcile expected Murex cashflows, Murex `SNTR/RLSR` cashflows, and RATAN receipts using [[murex-ratan-migration-reconciliation]].

## Scope boundary

Precious-metal cashflows remain in Murex. The intended target scope is eligible non-precious-metal cashflows. NDS routing requires a split in which the non-deliverable leg stays in Murex and only the deliverable leg reaches RATAN; the source records this as unresolved.

## Risks and dependencies

- A past-value-date reversal may be manually handled in Murex while RATAN continues to display the original flow as settled.
- A future replacement may be processed in RATAN before its past-dated reversal is resolved, creating duplicate-payment risk.
- During trade migration, Murex-originated future cashflows must be offset before Stella-originated replacements are settled.
- Migration reconciliation, report ownership, rollback behavior, performance evidence, and UAT case design were all recorded as open.

## Status note

The historical source describes a 2023 CPT and go-live proposal. It does not confirm execution or current project status; `on-hold` reflects the absence of implementation evidence.
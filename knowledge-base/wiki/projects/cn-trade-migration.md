---
type: project
title: CN Trade Migration
status: planned
owner: ""
start_date: 2024-05-10
target_date: ""
tags: [cn, trade-migration, settlement, ratan, stella, murex-2-11]
related: [early-settled-cashflow-migration-handling, murex-stella-cashflow-reconciliation, cn-migration-cutover-value-date-rules, murex-2-11, lms, razor, oscar]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/CN Trade Migration - Settlement Process.md"]
created: 2026-08-23
updated: 2026-08-23
---
# CN Trade Migration

## Brief

This planned CN migration moves trades from [[murex-2-11]] to [[stella]] while preserving correct settlement processing in [[ratan]]. The source describes an assumed May 2024 cutover schedule and does not confirm execution, completion, or production deployment.

## Objectives

- Reconcile Murex 2.11 and Stella cashflow generation for migrated trades.
- Prevent duplicate payment when a future-value-date cashflow was settled early through Murex before migration.
- Apply temporary NSTP and suppression controls during migration activity.
- Preserve workable post-migration amendment and netting behaviour.
- Control downstream effects on [[lms]], [[razor]], SWIFT generation, and [[settlement-ops]] workflows.

## Proposed delivery items

- Story 2117128: Murex 2.11 versus Stella cashflow reconciliation.
- Story 2117145: batch status-only update for early-settled overlap cashflows.
- Story 2117158: migration business rules.
- Story 2117161: UAT support.

## Dependencies and risks

- The preferred status-only `SETTLED` approach depends on clear LMS feed semantics.
- Individual recall and resettlement exceptions require [[oscar]] and Settlement Ops support.
- The batch update must avoid Razor messages and SWIFT generation.
- Reconciliation horizon, reversal treatment, and Stella confirmation status remain unresolved.

## Related knowledge

- [[early-settled-cashflow-migration-handling]]
- [[murex-stella-cashflow-reconciliation]]
- [[cn-migration-cutover-value-date-rules]]
- [[cn-settlement]]
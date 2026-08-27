---
type: concept
title: Migration Duplicate-Payment Prevention
created: 2026-08-22
updated: 2026-08-22
tags: [migration, payments, cutover, operational-risk, reconciliation]
related: [cashflow-migration, murex, fmrp, ratan, cashflow-reconciliation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/F2B Milestone Onboarding check list/F2B Milestone check list - FXO.md"]
---
# Migration Duplicate-Payment Prevention

Migration duplicate-payment prevention comprises the controls that stop both a legacy system and a target system from settling the same obligation during cutover.

## FXO Migration Context

The FXO checklist explicitly requires duplicate-payment prevention for migration from [[murex]] to [[fmrp]]. It also identifies cutover handling, historical data, near-value cashflows, and events applied to past-value cashflows after cutover.

These concerns make duplicate prevention more than a one-time data-deduplication task. Controls must account for late events, retries, status changes, and obligations that exist in both systems around the migration boundary.

## Control Design Needs

The source does not define the implementation. A complete design should establish:

- An authoritative payment owner before, during, and after cutover.
- Stable identifiers or idempotency keys.
- Freeze windows and change controls.
- Reconciliation between source, target, messaging, and accounting records.
- Treatment of queued, released, cancelled, and failed payments.
- Handling of near-value and past-value events.
- Rollback and recovery procedures.
- Evidence and sign-off requirements.

This checklist identifies the risk but does not demonstrate that these controls exist.
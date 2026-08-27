---
type: concept
title: Duplicate-Payment Prevention
created: 2026-08-22
updated: 2026-08-22
tags: [duplicate-payment, migration, cash-settlement, controls, reconciliation]
related: [f2b, fmrp, murex, ratan, cash-settlement-migration, auto-netting, settlement-accounting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/F2B Milestone Onboarding check list.md"]
---
# Duplicate-Payment Prevention

Duplicate-payment prevention is the control discipline used to ensure that one settlement obligation is not paid by both a legacy and target flow, or more than once after netting, migration, amendment, or write-back.

## F2B onboarding risks

The checklist identifies duplicate-payment risk in:

- Murex-to-FMRP migration.
- B2B package bookings where only one booking entity is in migration scope.
- Cancellation and replacement trades written back into Murex.
- Murex trades that may already have been paid.
- Swap-agent auto-netting rule changes.
- FMRP event processing during or after cutover.

## Required design evidence

A complete control design should define the authoritative payment key, payment status source, treatment of near-value and past-value cashflows, cancellation and undo behavior, reconciliation points, and the handling of partial-entity package migration.

The source states the requirement but does not provide the algorithm, control owner, test evidence, or production status.

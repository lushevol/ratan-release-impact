---
type: query
title: What Is the Authoritative LIEN Stamping and Re-stamping State Machine?
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, lien, state-machine, lifecycle-processing]
related: [lien, lien-stamping-and-re-stamping, pending-fixing-flag-processing, lien-processing-solution-1-vs-solution-2, lifecycle-service, netting-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/LIEN Processing & Pending Fixing Flag Technical Design.md"]
---
# What Is the Authoritative LIEN Stamping and Re-stamping State Machine?

## Question

What action, LIEN-stamping timing, and next status apply to every lifecycle breakpoint?

## Evidence

The source defines actions for materialization, reinstatement, netting, exception reversion, unsuppression, approval, and un-netting, but leaves `WAITING + Pending Fixing` unresolved. It also does not define the rollback target for `HOLD` or the semantics of `READY` versus `QUEUED`.

## Required resolution

The authoritative contract should specify:

- Source and freshness requirements for the LIEN amount.
- Whether stamping occurs before or after status changes.
- Transaction and failure semantics.
- Retry and idempotency behavior.
- Duplicate and concurrent event handling.
- The exact action and destination for each breakpoint.
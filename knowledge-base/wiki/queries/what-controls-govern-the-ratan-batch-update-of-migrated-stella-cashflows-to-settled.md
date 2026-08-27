---
type: query
title: What Controls Govern the Ratan Batch Update of Migrated Stella Cashflows to Settled?
tags: [ratan, batch-processing, audit, settlement-status, migration, cn]
related: [ratan, stella, early-settled-cashflow-migration-handling, cn-trade-migration, razor]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/CN Trade Migration - Settlement Process.md"]
created: 2026-08-23
updated: 2026-08-23
---
# What Controls Govern the Ratan Batch Update of Migrated Stella Cashflows to Settled?

The source requires a batch script that takes a migration-programme-provided cashflow list and updates selected Stella cashflows from `PROJECTED` to `SETTLED`, without Razor messaging or SWIFT generation.

The required control model is not specified. It should define:

- authorization and dual-control approval;
- input-file validation and eligibility checks;
- Murex payment and Stella cashflow correlation;
- idempotency and safe rerun behaviour;
- audit fields, reason codes, and evidence retention;
- exception handling and rollback or correction; and
- controls preventing updates to non-migration cashflows.
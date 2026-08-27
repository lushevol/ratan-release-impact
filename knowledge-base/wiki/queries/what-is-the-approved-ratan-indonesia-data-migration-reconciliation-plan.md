---
type: query
title: What Is the Approved RATAN Indonesia Data Migration Reconciliation Plan?
tags: [RATAN, Indonesia, data-migration, reconciliation, cutover]
related: [ratan-indonesia-entity-scoped-data-migration, cashflow-sequence-and-count-completeness-control, cashflow-batch-control, production-server-handover-definition-of-done]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Data Migration - Indonesia.md"]
---
# What Is the Approved RATAN Indonesia Data Migration Reconciliation Plan?

## Question

What counts, integrity checks, exception thresholds, sign-offs, cutover controls, and rollback evidence are required to accept the Indonesia migration?

## Evidence

The source identifies candidate tables and extraction keys but does not define row-count reconciliation, checksums, financial aggregates, referential-integrity checks, history completeness, message-payload validation, retry behavior, rollback, or treatment of in-flight cashflows.

## Resolution needed

Define and approve a migration reconciliation plan covering the complete cashflow population, dependent records, current and history tables, operational-message payloads, accounting records, exception records, and post-load business validation.
---
type: project
title: Korea Cash Settlement Migration
status: planned
owner: ""
start_date: 2026-04-27
target_date: 2026-05-15
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, korea, migration, murex, ratan]
related: [cashflow-migration, comp-status-driven-stp, static-data-readiness, ratan-swift-message-generation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement -- Korea Migration.md"]
---
# Korea Cash Settlement Migration

## Purpose

The Korea Cash Settlement Migration is a planned programme to move Korea cash-settlement processing from Murex to RATAN and establish the required downstream integrations.

The source identifies this as a multi-system migration rather than a standalone platform replacement. The schedule metadata uses the 2026 folder context, but the source roster itself does not state a calendar year.

## Scope

- Korea Murex to RATAN migration.
- RATAN to OLTP real-time accounting.
- RATAN to TIS manual-payment API.
- RATAN to TLM accounting-reconciliation API.
- RATAN to ENISIS SWIFT processing.
- Static-data preparation.
- Functional testing and hybrid/end-to-end testing.
- OLA, release documentation, and operational support coverage.

## Readiness Tracks

Functional test cases and hybrid/end-to-end testing are listed as separate tracks. The source provides no execution results, defects, acceptance criteria, or formal sign-off.

Static data and release documentation are explicit dependencies. Completeness and approval status require evidence from the linked primary documents.

## Operational Coverage

The source includes contacts for Overall, TIS, EDMi, ENISIS, PMO, OLTP, Murex, PM, and Operations during an April 27–May 15 window. The meanings of `P`, `L`, and `PH`, coverage hours, escalation paths, and approval status are not defined.

## Key Risks and Open Questions

- The exact definition and authority of `COMP` status are unknown.
- The interaction between `COMP`-driven STP and existing trade-validation or manual-STP controls is unknown.
- Interface contracts and ownership for OLTP, TIS, TLM, and ENISIS require confirmation.
- The calendar year represented by the contact roster requires confirmation.
- Formal testing and production-readiness status are not evidenced by this source.
---
type: concept
title: BCS-to-Strategic Workflow Migration
tags: [bcs, strategic-workflow, fmrp, migration, cash-settlement]
related: [bcs, fmrp, stella, lms, bcs-vs-fmrp-strategic-workflow, ssi-stamping-behavior-differences, cashflow-stamping-versus-settlement-lms-feed]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Migrating BCS to Strategic Workflow.md"]
---
# BCS-to-Strategic Workflow Migration

## Definition

BCS-to-Strategic Workflow migration is the proposed movement of BCS cashflow processing from a legacy flow into Strategic Workflow processing, using FMRP as the target or reference implementation.

## Scope

The migration includes Strategic-format cashflow intake, business-rule review, user-profile changes, static-data configuration, SSI stamping, Swift generation, accounting, confirmation, STP eligibility, LMS integration, Cashflow Blotter enrichment, and possible historical-data migration.

## Current Status

The source is an early discovery and requirements-gap document. It identifies unresolved compatibility questions and does not demonstrate implementation completion, approval, deployment, or UAT validation.

## Critical Validation Areas

The migration requires authoritative decisions and evidence for:

- Strategic-format messages sent by Stella and consumed through the message bridge filter.
- NSTP and Swift/cashflow-suppression rule parity.
- SSI query and fallback behavior.
- Razor-side Swift logic and `DV` versus `EQ` identifiers.
- CDU versus TDS3 confirmation.
- Internal-client STP whitelist behavior.
- LMS release and settlement gating.
- EBBS accounting scope.
- Historical-data migration and reconciliation.
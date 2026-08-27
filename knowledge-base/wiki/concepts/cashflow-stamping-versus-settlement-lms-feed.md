---
type: concept
title: Cashflow Stamping versus Settlement LMS Feed
tags: [lms, cashflow, stamping, release, settlement, bcs, fmrp]
related: [bcs, fmrp, lms, manual-entity-lms-reference-data-feed, bcs-strategic-workflow-migration]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Migrating BCS to Strategic Workflow.md"]
---
# Cashflow Stamping versus Settlement LMS Feed

## Definition

This concept describes the different event gates used by BCS and FMRP when sending cashflow data to LMS.

## Behavior Difference

- BCS sends the LMS feed after the cashflow is stamped.
- FMRP sends the LMS feed only after the cashflow is released or settled.

## Migration Implication

Moving processing from BCS to FMRP may delay LMS delivery even when the cashflow has already been stamped. The migration must confirm the authoritative event, status contract, duplicate behavior, and reconciliation expectations for LMS consumers.

The source does not establish which timing contract should govern migrated BCS cashflows.
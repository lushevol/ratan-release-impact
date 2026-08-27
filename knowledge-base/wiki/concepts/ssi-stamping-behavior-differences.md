---
type: concept
title: SSI Stamping Behavior Differences
tags: [ssi, stamping, nostro, vostro, bcs, fmrp, settlement]
related: [bcs, fmrp, bcs-strategic-workflow-migration, strategic-workflow-static-data-configuration]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Migrating BCS to Strategic Workflow.md"]
---
# SSI Stamping Behavior Differences

## Definition

SSI stamping behavior differences are the identified discrepancies between BCS and FMRP in query conditions and nostro selection during cashflow processing.

## Differences Identified

- FMRP uses `******` in the query condition, while the current BCS behavior does not.
- FMRP SCB receive selects the primary nostro when no vostro exists.
- BCS does not have the stated primary-nostro fallback logic.

## Migration Risk

These differences may alter SSI selection, settlement routing, or exception outcomes. The source does not state whether FMRP behavior is the approved replacement behavior, a compatibility requirement, or a defect requiring alignment.

Validation should define query precedence, fallback conditions, expected outputs, and treatment of missing or conflicting static data.
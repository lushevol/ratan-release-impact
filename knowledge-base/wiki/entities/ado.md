---
type: entity
title: Azure DevOps
created: 2026-08-22
updated: 2026-08-22
tags: [Azure-DevOps, ADO, work-items, pipelines, release-management]
related: [servicenow, release-readiness-attestation, ratan-bau-release-pre-cab-checklist]
sources: ["RATAN - 51358/RATAN/RATAN -Release/Ratan Release Plan 2026/Ratan Pre-Cab Checklist 2026/2026_08_29_CHG1053540_Ratan BAU Release - 29th Aug.md"]
---

# Azure DevOps

## Role in the RATAN release

Azure DevOps, referred to as **ADO** in the source, is the work-item and pipeline platform used for the RATAN BAU release scheduled for 29 August 2026.

The release checklist identifies six ADO work items as the complete change scope. It also states that **All ADO pipelines** are intended to perform both implementation and rollback.

## Work-item scope

The associated work items cover:

- Archival and retrieval production technical-live Phase 1.
- NSTP exception checker rejection with approval to Ready status.
- Prevention of automatic affirmation for specified auto-netted cashflows.
- Last Mile Check backend service development.
- Renaming `auto_dvp_msg.trade_version` to `major_version`.
- Rule-field validation before rule execution.

## Control limitation

The source does not identify pipeline names, deployment dependencies, database migration steps, or story-specific rollback procedures. “All ADO pipelines” describes the intended mechanism but is not, by itself, evidence that database, schema, or retained-data state can be safely restored.
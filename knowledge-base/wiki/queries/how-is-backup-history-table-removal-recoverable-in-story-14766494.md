---
type: query
title: How Is Backup-History-Table Removal Recoverable in Story 14766494?
created: 2026-08-22
updated: 2026-08-22
tags: [data-archival, backup-table, recoverability, database-change, ado-story]
related: [chg1047654, 26-auto-netting-page-md-files--157-ratan-51358-ratan-51358-ratan-release-ratan-release-plan-2026-ratan-pre-cab-c--ozcpmu, data-archival-backup-table-retirement, where-is-chg1047654-uvt-regression-and-uat-evidence]
sources: ["RATAN - 51358/RATAN/RATAN -Release/Ratan Release Plan 2026/Ratan Pre-Cab Checklist 2026/2026_08_15_CHG1047654_Ratan BAU Release - 15th Aug.md"]
---
# How Is Backup-History-Table Removal Recoverable in Story 14766494?

Story 14766494 is described as an archival phase 1 change to drop a backup history table. CHG1047654 records rollback generically as “All ADO pipelines,” which does not document restoration capability for a destructive table-removal change.

## Evidence needed

- The precise table name, schema, and deployed DDL.
- Backup location, retention period, and data-owner approval.
- A tested table and data restoration procedure.
- Dependency analysis for archival retrieval, jobs, reports, and downstream consumers.
- Rollback trigger conditions and evidence from a rollback rehearsal.
- Post-deployment verification that required historical data remains accessible.

Until this evidence is available, the checklist supports only the intended change scope, not the recoverability or compliance of the table retirement.
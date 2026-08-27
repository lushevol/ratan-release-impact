---
type: query
title: Is the ratanone Camunda Purge Script Approved and Safe for Each Environment?
created: 2026-08-24
updated: 2026-08-24
tags: [camunda, ratanone, data-purge, environment-control, change-management]
related: [camunda, ratanone-schema, destructive-workflow-data-purge, camunda-persistence-schema]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Camunda ER diagram and purge script.md"]
---
# Is the ratanone Camunda Purge Script Approved and Safe for Each Environment?

The source provides an unrestricted `TRUNCATE ... CASCADE` script for Camunda tables in `ratanone`, but does not identify its approved environment, operator, owner, change-control status, or recovery procedure.

## Questions to resolve

- Is the script restricted to DEV or test environments, or can it be used in UAT, disaster-recovery, or production-like environments?
- Who owns the `ratanone` schema and who is authorized to execute destructive operations?
- Is application quiescing required before truncating active `ACT_RU_*` workflow state?
- Has the SQL been corrected, tested, peer-reviewed, and packaged with backup and post-purge validation steps?
- Is production execution explicitly prohibited?

The supplied SQL has duplicated `CASCADE` clauses and a missing semicolon after `act_hi_batch`; it should not be executed as supplied. See [[destructive-workflow-data-purge]].
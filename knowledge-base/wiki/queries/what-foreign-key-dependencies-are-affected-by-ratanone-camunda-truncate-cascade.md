---
type: query
title: What Foreign-Key Dependencies Are Affected by ratanone Camunda TRUNCATE CASCADE?
created: 2026-08-24
updated: 2026-08-24
tags: [postgresql, foreign-keys, truncate-cascade, camunda, ratanone]
related: [postgresql, ratanone-schema, camunda, camunda-persistence-schema, destructive-workflow-data-purge]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Camunda ER diagram and purge script.md"]
---
# What Foreign-Key Dependencies Are Affected by ratanone Camunda TRUNCATE CASCADE?

Every documented statement uses `CASCADE`, allowing PostgreSQL to truncate referencing tables where required by foreign-key dependencies. The source contains neither DDL nor catalog output, so the full effective table set is unknown.

## Evidence needed

- The `ratanone` schema DDL or PostgreSQL catalog output for all foreign keys referencing the listed tables.
- A dry-run or controlled-environment dependency assessment.
- Identification of tables outside the supplied list that PostgreSQL would truncate.
- Confirmation that all affected application data is in scope for the intended reset.
- A reviewed execution order and post-purge reconciliation procedure.

The unavailable ER-diagram details must not be used as evidence for dependencies until the original attachment is inspected.
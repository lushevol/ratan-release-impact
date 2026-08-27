---
type: query
title: What Camunda History Retention and Audit Requirements Apply to ratanone?
created: 2026-08-24
updated: 2026-08-24
tags: [camunda, audit-retention, workflow-history, ratanone, compliance]
related: [camunda, ratanone-schema, camunda-persistence-schema, destructive-workflow-data-purge, audit-trail, cash-settlement-audit-api-migration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Camunda ER diagram and purge script.md"]
---
# What Camunda History Retention and Audit Requirements Apply to ratanone?

The documented purge script truncates Camunda history tables, including operation logs, incidents, comments, attachments, task history, process history, and variables. The source does not state whether these records are operational logs only or are subject to audit, regulatory, legal-hold, or business-retention requirements.

## Evidence needed

- The data classification and retention policy for `ACT_HI_*` records in `ratanone`.
- Confirmation of whether `act_hi_op_log`, `act_hi_comment`, `act_hi_attachment`, and incident records support formal audit evidence.
- The authoritative retention owner and approved deletion schedule.
- Whether backups retain data that a purge removes and how restored records would be governed.
- The relationship, if any, between Camunda history and the existing [[audit-trail]] or [[cash-settlement-audit-api-migration]] scope.

Until resolved, a broad history-table truncation should be treated as potentially destructive to audit-relevant evidence.
---
type: concept
title: Destructive Workflow Data Purge
created: 2026-08-24
updated: 2026-08-24
tags: [data-purge, camunda, postgresql, truncate, workflow-state, audit]
related: [camunda, ratanone-schema, camunda-persistence-schema, postgresql, audit-trail]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Camunda ER diagram and purge script.md"]
---
# Destructive Workflow Data Purge

A destructive workflow data purge removes entire persistence-table contents rather than selecting records according to an approved retention policy. In the documented `ratanone` script, PostgreSQL `TRUNCATE ... CASCADE` is applied to Camunda history, runtime, and byte-array tables.

## Effects

Truncating `ACT_RU_*` tables can remove active process executions, assigned tasks, queued jobs, event subscriptions, and runtime variables. Applications using that state may be interrupted or left unable to resume in-progress workflows.

Truncating `ACT_HI_*` tables can remove process and task history, incidents, operation logs, comments, attachments, variables, and other historical evidence. Whether any such data has formal audit or regulatory-retention obligations remains unconfirmed.

`CASCADE` can widen the operation beyond the named table list by truncating tables that reference the target tables through foreign keys. The actual blast radius requires schema metadata.

## Required controls

A destructive workflow purge should have:

- an explicitly approved target environment and accountable operator;
- application quiescing and confirmation that active workflow processing can be discarded;
- backup, recovery, and rollback planning;
- reviewed and executable SQL;
- an assessment of `CASCADE` dependencies;
- a decision on whether identities or sequences must be reset;
- post-purge reconciliation and application-health validation; and
- documented retention and audit approval before history is removed.

The source script lacks these controls and contains apparent syntax defects. Its purpose and approved execution context are open in [[is-the-ratanone-camunda-purge-script-approved-and-safe-for-each-environment]].
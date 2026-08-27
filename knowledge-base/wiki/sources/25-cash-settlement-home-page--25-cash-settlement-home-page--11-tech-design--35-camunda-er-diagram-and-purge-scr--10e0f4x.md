---
type: source
title: Camunda ER Diagram and Purge Script
authors: []
year: 2025
url: ""
venue: Internal technical design document
created: 2026-08-24
updated: 2026-08-24
tags: [camunda, postgresql, ratanone, cash-settlement, data-purge]
related: [camunda, ratanone-schema, camunda-persistence-schema, destructive-workflow-data-purge, postgresql, audit-trail]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Camunda ER diagram and purge script.md"]
---
# Camunda ER Diagram and Purge Script

This technical-design document contains an ER-diagram attachment and a PostgreSQL `TRUNCATE` script for Camunda-prefixed tables in the `ratanone` schema.

The supplied text does not expose the ER diagram's table relationships, keys, or cardinalities. No relationship or dependency claims should be derived from the image until the attachment is inspected directly.

## Scope

The script targets:

- `ACT_HI_*` history tables, including process, task, variable, incident, decision, operation-log, attachment, and comment records.
- `ACT_RU_*` runtime tables, including active executions, tasks, jobs, subscriptions, variables, incidents, and authorizations.
- `act_ge_bytearray`, a general Camunda table that may contain binary or serialized data depending on the deployment configuration.

This is a full-table destructive reset, not a bounded retention cleanup. Truncating the runtime tables can invalidate active workflows and asynchronous work. Truncating history tables can remove operational and potentially audit-relevant records.

## Preserved purge script

```sql
TRUNCATE ratanone.act_hi_actinst CASCADE CASCADE;
TRUNCATE ratanone.act_hi_attachment CASCADE CASCADE;
TRUNCATE  ratanone.act_hi_batch CASCADE
TRUNCATE  ratanone.act_hi_caseactinst CASCADE;
TRUNCATE  ratanone.act_hi_caseinst CASCADE;
TRUNCATE  ratanone.act_hi_comment CASCADE;
TRUNCATE  ratanone.act_hi_dec_in CASCADE;
TRUNCATE  ratanone.act_hi_dec_out CASCADE;
TRUNCATE  ratanone.act_hi_decinst CASCADE;
TRUNCATE  ratanone.act_hi_detail CASCADE;
TRUNCATE  ratanone.act_hi_ext_task_log CASCADE;
TRUNCATE  ratanone.act_hi_identitylink CASCADE;
TRUNCATE  ratanone.act_hi_incident CASCADE;
TRUNCATE  ratanone.act_hi_job_log CASCADE;
TRUNCATE  ratanone.act_hi_op_log CASCADE;
TRUNCATE  ratanone.act_hi_procinst CASCADE;
TRUNCATE  ratanone.act_hi_taskinst CASCADE;
TRUNCATE  ratanone.act_hi_varinst CASCADE;

TRUNCATE  ratanone.act_ru_authorization CASCADE;
TRUNCATE  ratanone.act_ru_batch CASCADE;
TRUNCATE  ratanone.act_ru_case_execution CASCADE;
TRUNCATE  ratanone.act_ru_case_sentry_part CASCADE;
TRUNCATE  ratanone.act_ru_event_subscr CASCADE;
TRUNCATE  ratanone.act_ru_execution CASCADE;
TRUNCATE  ratanone.act_ru_ext_task CASCADE;
TRUNCATE  ratanone.act_ru_filter CASCADE;
TRUNCATE  ratanone.act_ru_identitylink CASCADE;
TRUNCATE  ratanone.act_ru_incident CASCADE;
TRUNCATE  ratanone.act_ru_job CASCADE;
TRUNCATE  ratanone.act_ru_jobdef CASCADE;
TRUNCATE  ratanone.act_ru_meter_log CASCADE;
TRUNCATE  ratanone.act_ru_task CASCADE;
TRUNCATE  ratanone.act_ru_variable CASCADE;
TRUNCATE  ratanone.act_ge_bytearray cascade;
```

## Execution concerns

The supplied script should not be treated as executable without correction and review:

- The first two statements include duplicated `CASCADE` clauses.
- The `act_hi_batch` statement lacks a terminating semicolon.
- No transaction boundary, backup procedure, application-quiescing step, approval requirement, or post-purge validation is included.
- `CASCADE` can truncate additional referencing tables; the effective scope cannot be established without the target schema's foreign-key metadata.
- The script does not request `RESTART IDENTITY`, so PostgreSQL sequence or identity positions would normally be retained.

See [[camunda-persistence-schema]] for the table-group interpretation and [[destructive-workflow-data-purge]] for operational controls. Open governance and dependency questions are tracked in [[is-the-ratanone-camunda-purge-script-approved-and-safe-for-each-environment]], [[what-camunda-history-retention-and-audit-requirements-apply-to-ratanone]], and [[what-foreign-key-dependencies-are-affected-by-ratanone-camunda-truncate-cascade]].
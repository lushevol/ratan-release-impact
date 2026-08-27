---
type: concept
title: Camunda Persistence Schema
created: 2026-08-24
updated: 2026-08-24
tags: [camunda, workflow-engine, persistence, postgresql, database-schema]
related: [camunda, ratanone-schema, destructive-workflow-data-purge, postgresql]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Camunda ER diagram and purge script.md"]
---
# Camunda Persistence Schema

A Camunda persistence schema conventionally uses table-prefix groups to distinguish workflow history, active runtime data, and general shared data.

## Table groups in the documented script

- `ACT_HI_*` denotes historical records. The supplied script includes process and task instances, variables, incidents, operation logs, comments, attachments, decision records, and job logs.
- `ACT_RU_*` denotes runtime records. The supplied script includes active executions, tasks, jobs, event subscriptions, variables, identity links, incidents, authorizations, and batch data.
- `ACT_GE_*` denotes general engine data. The source includes `act_ge_bytearray`.

The source identifies these table groups by name but does not provide DDL, primary keys, foreign keys, table ownership, or an interpretable ER-diagram model. Specific table relationships must not be inferred without inspecting the attachment or database metadata.

## Implication for purge activity

A purge that includes both `ACT_HI_*` and `ACT_RU_*` does more than remove completed-workflow history: it also removes active workflow state. Including `act_ge_bytearray` may further remove binary or serialized records whose exact use depends on the deployment configuration.

See [[destructive-workflow-data-purge]].
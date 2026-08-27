---
type: query
title: What Is the cashflow_user_operation_record Schema and Audit Policy?
tags: [audit, database-schema, maker-checker, cash-settlement]
related: [cashflow-user-operation-record, user-operation-audit-trail, nstp-maker-checker-processing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/NSTP Maker-Checker Separation From Code.md"]
created: 2026-08-24
updated: 2026-08-24
---
# What Is the cashflow_user_operation_record Schema and Audit Policy?

The design proposes `cashflow_user_operation_record` plus save and CRUD APIs, but provides no extractable schema definition.

Required confirmation includes:

- Authoritative DDL, column definitions, primary keys, foreign keys, constraints, and indexes.
- Record ownership and source-of-truth designation.
- Workflow, task, cashflow, and request correlation identifiers.
- Maker and checker identity, role, authorization, and timestamp fields.
- Immutability, update, deletion, retention, archival, and access-control policy.
- Idempotency and duplicate-record handling.

The User Operation Table appears only as an image in the source, so no structure should be inferred.
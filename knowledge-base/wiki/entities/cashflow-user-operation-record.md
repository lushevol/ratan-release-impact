---
type: entity
title: cashflow_user_operation_record
tags: [cash-settlement, audit, persistence, maker-checker]
related: [nstp-maker-checker-processing, user-operation-audit-trail, cashflow-user-operation-record-schema-and-audit-policy]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/NSTP Maker-Checker Separation From Code.md"]
created: 2026-08-24
updated: 2026-08-24
---
# cashflow_user_operation_record

`cashflow_user_operation_record` is a proposed persistence table or record store for maker-checker user-operation activity in Cash Settlement.

The implementation plan calls for an API to save this record, creation of the table, and CRUD functions. It assigns estimates of 1 for the save API and 2 for table and CRUD work.

The source includes a User Operation Table image but no extractable DDL or structured schema. Column names, types, keys, constraints, indexes, ownership, access controls, correlation identifiers, and retention requirements remain unspecified. See [[cashflow-user-operation-record-schema-and-audit-policy]].
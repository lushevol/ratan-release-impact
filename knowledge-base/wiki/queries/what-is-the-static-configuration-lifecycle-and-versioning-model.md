---
type: query
title: What Is the Static Configuration Lifecycle and Versioning Model?
created: 2026-08-24
updated: 2026-08-24
tags: [static-configuration, lifecycle, versioning, audit, maker-checker]
related: [schema-validated-static-configuration, static-configuration-auditability, shared-static-configuration-maker-checker-engine, pending-configuration-change-isolation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan Static Config Service Design (Draft).md"]
---
# What Is the Static Configuration Lifecycle and Versioning Model?

The draft defines separate state vocabularies but no lifecycle model:

- Definitions: `LIVE`, `DISABLED`
- Content: `LIVE`, `DISABLED`, `UPDATE_PENDING`, `DEAD`, `ADD_PENDING`
- Audit records: `UPDATE`, `ADDED`, `DELETED`, `PENDING_UPDATE`, `PENDING_ADDED`, `PENDING_DELETED`

The authoritative model must define legal transitions, actor permissions, approval roles, segregation of duties, rollback behavior, audit immutability, and whether pending changes are visible to normal readers.

It must also reconcile the definition-level `VARCHAR` version with `INT` versions on content and audit records, specify version scope, and establish optimistic-concurrency behavior.
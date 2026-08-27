---
type: entity
title: ratan_static_config_audit_log
created: 2026-08-24
updated: 2026-08-24
tags: [ratanone, cash-settlement, database-table, audit, maker-checker]
related: [static-configuration-auditability, shared-static-configuration-maker-checker-engine, ratan-static-config-maker-request, ratan-fxu-config]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Static configuration design.md"]
---
# ratan_static_config_audit_log

`ratan_static_config_audit_log` is the proposed shared audit-history table for static-configuration operations.

The proposed columns are `id`, `operator`, `role`, `operation_type`, `target_table`, `target_id`, `target_snapshot`, and `created_at`. The snapshot is stored as `TEXT`, and the target is identified through a table name and optional record ID.

The shared log is intended to avoid fragmented histories such as the BicNetting flow, where one logical configuration may have multiple related record IDs. The design does not state whether this table replaces or coexists with domain-specific tables such as `ratan_fxu_config_audit`.

The reproduced DDL has a trailing comma after `created_at` and is invalid as written in PostgreSQL. It also lacks indexes, immutability controls, retention rules, request IDs, and schema-version fields.
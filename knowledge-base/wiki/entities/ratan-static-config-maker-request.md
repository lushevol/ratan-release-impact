---
type: entity
title: ratan_static_config_maker_request
created: 2026-08-24
updated: 2026-08-24
tags: [ratanone, cash-settlement, database-table, maker-checker, configuration]
related: [shared-static-configuration-maker-checker-engine, pending-configuration-change-isolation, static-configuration-auditability, ratan-static-config-audit-log]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Static configuration design.md"]
---
# ratan_static_config_maker_request

`ratan_static_config_maker_request` is the proposed shared table for maker/checker requests across static-configuration domains.

The source proposes these fields:

- `id`: `bigserial` primary key.
- `maker_id` and optional `checker_id`.
- `target_table` and optional `target_id`.
- `operation_type`: insert, update, or delete.
- `data_status`: pending, confirmed, rejected, or cancelled.
- `payload`: configuration data serialized as text.
- `created_at` and `updated_at`.

The table is intended to keep pending changes separate from effective configuration records. However, the source does not define allowed transitions, request-to-record identity rules, uniqueness for concurrent requests, payload schema versions, or indexes for work queues.

`target_table` is a polymorphic textual reference and has no foreign-key relationship to a configuration table in the proposed DDL.
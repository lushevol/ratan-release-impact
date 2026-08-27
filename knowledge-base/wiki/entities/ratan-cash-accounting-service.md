---
type: entity
title: ratan_cash_accounting_service
tags: [RATAN, accounting, cashflow, data-migration, service]
related: [ratan-indonesia-entity-scoped-data-migration, cashflow-lineage-and-operational-visibility]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Data Migration - Indonesia.md"]
---
# ratan_cash_accounting_service

`ratan_cash_accounting_service` is a RATAN service schema containing accounting request tasks, request-task history, and accounting response information.

## Role in the Indonesia migration

The request-task tables are scoped by `cashflow_id` and `booking_entity_fmid`. The source proposes extracting dependent response records using `external_system_key`, joining `ratan_accounting_response_info.external_system_key` to `ratan_accounting_request_task.external_system_key`.

## Source-supplied query

```sql
SELECT DISTINCT "external_system_key"::text AS id
FROM "ratan_cash_accounting_service"."ratan_accounting_request_task"
WHERE "booking_entity_fmid"::text = '8'
  AND "external_system_key"::text != ''
```

## Limitation

The source supplies the extraction key but does not provide schema definitions or foreign-key validation for the proposed `external_system_key` relationship.
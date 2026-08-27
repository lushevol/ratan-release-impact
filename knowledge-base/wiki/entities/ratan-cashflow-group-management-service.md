---
type: entity
title: ratan_cashflow_group_management_service
tags: [RATAN, cashflow, group-management, data-migration, service]
related: [ratan-indonesia-entity-scoped-data-migration, trade-cashflow-correlation-by-trade-version, cashflow-lineage-and-operational-visibility]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Data Migration - Indonesia.md"]
---
# ratan_cashflow_group_management_service

`ratan_cashflow_group_management_service` is a RATAN service schema that manages relationships among cashflows, trades, groups, and group messages.

## Role in the Indonesia migration

The source proposes this service as a migration pivot. `ratan_cashflow_group_message` is filtered by `booking_entity_id = '8'` to derive:

- in-scope `cashflow_id` values;
- related `trade_id` values; and
- dependent SCBML history and message identifiers.

The inventory also includes group, group history, group-message history, mapping, mapping history, message I/O, inbound message, trade, and trade history tables.

## Source-supplied extraction queries

```sql
SELECT DISTINCT "cashflow_id"::text AS id
FROM "ratan_cashflow_group_management_service"."ratan_cashflow_group_message"
WHERE "booking_entity_id"::text = '8'
  AND "cashflow_id"::text != ''
```

```sql
SELECT DISTINCT "trade_id"::text AS id
FROM "ratan_cashflow_group_management_service"."ratan_cashflow_group_message"
WHERE "booking_entity_id"::text = '8'
  AND "trade_id"::text != ''
```

## Limitation

The source does not establish that every valid Indonesia cashflow appears in `ratan_cashflow_group_message`. The service therefore requires population-completeness testing before it can be used as the sole migration starting point.
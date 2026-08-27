---
type: entity
title: cash_settlement_lms_service
tags: [RATAN, LMS, cash-settlement, messages, data-migration]
related: [ratan-indonesia-entity-scoped-data-migration, source-stack-flow-name-propagation, lms-source-value-proposals]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Data Migration - Indonesia.md"]
---
# cash_settlement_lms_service

`cash_settlement_lms_service` is a RATAN service schema containing LMS messages and raw LMS messages.

## Role in the Indonesia migration

The proposed scope for `lms_message` uses `cashflow_id` and `party1_fm_id`. Dependent `lms_raw_message` records are proposed for extraction through `aggregate_root_id`, with a tentative relationship between `lms_raw_message.message_key` and `lms_message.aggregate_root_id`.

## Source-supplied query

```sql
SELECT DISTINCT "aggregate_root_id"::text AS id
FROM "cash_settlement_lms_service"."lms_message"
WHERE "party1_fm_id"::text = '8'
  AND "aggregate_root_id"::text != ''
```

## Limitation

The relationship between `lms_raw_message.message_key` and `lms_message.aggregate_root_id` is marked as uncertain in the source. Foreign-key metadata or sample-record validation is required before production migration.
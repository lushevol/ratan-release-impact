---
type: source
title: Cash Settlement Data Migration - Indonesia
tags: [cash-settlement, data-migration, Indonesia, RATAN, onshoring]
related: [ratan-indonesia-onshoring-2026, ratan-indonesia-isolated-deployment, indonesia-ratan-data-residency-isolation, ratan-indonesia-entity-scoped-data-migration, cashflow-lineage-and-operational-visibility, cashflow-sequence-and-count-completeness-control, cashflow-batch-control, cash-settlement-platform-architecture-indonesia]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Data Migration - Indonesia.md"]
authors: []
year: 2026
url: ""
venue: ""
---

# Cash Settlement Data Migration - Indonesia

## Summary

This document is a preliminary migration inventory for Cash Settlement Platform data associated with entity or FM ID `'8'`, likely representing the Indonesia deployment. It identifies candidate tables, relationship fields, migration keys, and selected SQL queries for deriving dependent records.

The document is an implementation worksheet rather than an approved production migration specification. Several relationships, inclusion decisions, and key strategies remain uncertain, as indicated by question marks, blank key fields, and unverified inferred joins.

## Migration scope

The proposed scope is primarily cashflow-rooted. Most tables use `cashflow_id` as the migration key, while related records are derived through entity-scoped parent tables. The document uses several service-specific scope fields:

- `party1_fm_id`
- `entity__booking_entity_sci_fmid`
- `booking_entity_fmid`
- `booking_entity_id`
- `entity_fmid`

The source does not establish that these fields share the same identifier domain or that `'8'` has identical semantics in every service.

## Migration inventory

The following inventory is preserved from the source, including blank fields, question marks, spelling, and inferred relationship notation.

| Table | Related Filed | Key | Key query |
| --- | --- | --- | --- |
| cash_netting_service.**ratan_auto_netting_cashflow** | Cashflow_id | Cashflow_id | |
| cash_netting_service.**ratan_auto_netting_cashflow_history** | Cashflow_id | Cashflow_id | |
| cash_netting_service.**splitting_cashflow** | Cashflow_id | Cashflow_id | |
| cash_settlement_lms_service.**lms_message** | Cashflow_id/party1_fm_id | Cashflow_id | |
| cash_settlement_lms_service.**lms_raw_message** | message_key <-> **lms_message****.**aggregate_root_id ? | aggregate_root_id | SELECT DISTINCT "aggregate_root_id"::text AS id FROM "cash_settlement_lms_service"."lms_message" WHERE "party1_fm_id"::text = '8' AND "aggregate_root_id"::text != '' |
| cash_settlement_query_cn.**cashflow_data** | Cashflow__cashflow_id and entity__booking_entity_sci_fmid = '8' | Cashflow_id | |
| cash_settlement_query_cn.**cashflow_data_history** | Cashflow__cashflow_id | Cashflow_id | |
| cash_settlement_query_cn**.****t_event** ? | | | |
| cash_settlement_ssi_cn.**cashflow_stamping** | Cashflow_id/party1_fm_id | Cashflow_id | |
| cash_settlement_ssi_cn.**cashflow_stamping_legacy_exception** | Cashflow_id | Cashflow_id | |
| cash_settlement_ssi_cn.**maker_checker_reques**t | Cashflow_id | Cashflow_id | |
| cash_settlement_ssi_cn.**raw_message** | message_key(cashflow_id) ？ | | |
| cash_settlement_ssi_cn.**stamped_nostro_account** | cashflow_stamping_id(cashflow_id) | cashflow_id | |
| cash_settlement_ssi_cn.**stamped_vostro_account** | cashflow_stamping_id(cashflow_id) | cashflow_id | |
| ratan_cash_accounting_service.**ratan_accounting_request_task** | cashflow_id/booking_entity_fmid | cashflow_id | |
| ratan_cash_accounting_service.**ratan_accounting_request_task_history** | cashflow_id/booking_entity_fmid | cashflow_id | |
| ratan_cash_accounting_service.**ratan_accounting_response_info** | external_system_key <-> **ratan_accounting_request_task****.**external_system_key | external_system_key | SELECT DISTINCT "external_system_key"::text AS id FROM "ratan_cash_accounting_service"."ratan_accounting_request_task" WHERE "booking_entity_fmid"::text = '8' AND "external_system_key"::text != '' |
| ratan_cash_settlement_batch_service.cash_mxg_batch_fix_notify | flow_id(cashflow_id) | | |
| ratan_cash_settlement_fx_utilization_service ? | | | |
| ratan_cashflow_group_management_service.**ratan_cashflow_group** | trade_id | trade_id | |
| ratan_cashflow_group_management_service**.****ratan_cashflow_group_history** | trade_id/**ratan_cashflow_group****.**group_id | trade_id | |
| ratan_cashflow_group_management_service**.****ratan_cashflow_group_message** | cashflow_id/booking_entity_id | cashflow_id | SELECT DISTINCT "cashflow_id"::text AS id FROM "ratan_cashflow_group_management_service"."ratan_cashflow_group_message" WHERE "booking_entity_id"::text = '8' AND "cashflow_id"::text != '' |
| ratan_cashflow_group_management_service.**ratan_cashflow_group_message_history** | cashflow_id/booking_entity_id | cashflow_id | |
| ratan_cashflow_group_management_service.**ratan_cashflow_mapping** | Original_cashflow_id | | |
| ratan_cashflow_group_management_service.**ratan_cashflow_mapping****_history** | Mapping_id/Original_cashflow_id | | |
| ratan_cashflow_group_management_service**.****ratan_cashflow_message_io**** ?** | | | |
| ratan_cashflow_group_management_service.**ratan_inbound_message****?** | | | |
| ratan_cashflow_group_management_service.**ratan_trade** | trade_id | trade_id | SELECT DISTINCT "trade_id"::text AS id FROM "ratan_cashflow_group_management_service"."ratan_cashflow_group_message" WHERE "booking_entity_id"::text = '8' AND "trade_id"::text != '' |
| ratan_cashflow_group_management_service.**ratan_trade_history** | trade_id | trade_id | |
| ratan_cashflow_lifecycle_service.**ratan_cashflow_affirmation_status** | cashflow_id | cashflow_id | |
| ratan_cashflow_lifecycle_service.**ratan_cashflow_holding_message** | cashflow_id | cashflow_id | |
| ratan_cashflow_lifecycle_service.**ratan_cashflow_scbml_history** | cashflow_id | cashflow_id | |
| ratan_cashflow_lifecycle_service.**ratan_cashflow_scbml_message** | Id <-> **ratan_cashflow_scbml_history****.**body_event_rowkey | body_event_rowkey | SELECT DISTINCT rcsh."body_event_rowkey"::text AS id FROM "ratan_cashflow_lifecycle_service"."ratan_cashflow_scbml_history" rcsh JOIN "ratan_cashflow_group_management_service"."ratan_cashflow_group_message" cd ON cd."cashflow_id"::text = rcsh."cashflow_id"::text WHERE cd."booking_entity_id"::text = '8' AND rcsh."body_event_rowkey"::text != '' |
| ratan_cashflow_lifecycle_service.**ratan_stella_message_event_source** | cashflow_id/entity_fmid | cashflow_id | |
| ratan_exception_platform.**rep_exception** | entity_id(cashflow_id) ？ | | |
| ratan_exception_platform.**rep_exception_history** | entity_id(cashflow_id) ？ | | |
| Rule sync ? | | | |
| ratanone_swift_service.**ratanone_swift_conversion_record** | cashflow_data(cashflow_id) | | |
| ratanone_swift_service**.****swift_message** | cashflow_id | cashflow_id | |
| ratanone_swift_service.**swift_raw_message** | cashflow_id | cashflow_id | |

## Source-supplied SQL

```sql
SELECT DISTINCT "aggregate_root_id"::text AS id
FROM "cash_settlement_lms_service"."lms_message"
WHERE "party1_fm_id"::text = '8'
  AND "aggregate_root_id"::text != ''
```

```sql
SELECT DISTINCT "external_system_key"::text AS id
FROM "ratan_cash_accounting_service"."ratan_accounting_request_task"
WHERE "booking_entity_fmid"::text = '8'
  AND "external_system_key"::text != ''
```

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

```sql
SELECT DISTINCT rcsh."body_event_rowkey"::text AS id
FROM "ratan_cashflow_lifecycle_service"."ratan_cashflow_scbml_history" rcsh
JOIN "ratan_cashflow_group_management_service"."ratan_cashflow_group_message" cd
  ON cd."cashflow_id"::text = rcsh."cashflow_id"::text
WHERE cd."booking_entity_id"::text = '8'
  AND rcsh."body_event_rowkey"::text != ''
```

## Key findings

1. The intended migration is primarily cashflow-scoped, with FM ID `'8'` as the apparent Indonesia scope predicate.
2. `ratan_cashflow_group_management_service` is the proposed migration pivot for group messages, trades, and selected lifecycle SCBML records.
3. LMS, accounting, and SCBML message records require non-cashflow lookup keys.
4. The inventory is incomplete and is not executable as a production migration specification.
5. `data_migration.sh` and `execute.sh` are referenced attachments, but their contents are unavailable in this source.

## Migration risks and unresolved areas

The source does not define migration ordering, transaction consistency, duplicate handling, identity or sequence handling, data masking, cutover timing, rollback, post-load validation, or reconciliation acceptance criteria.

Unresolved entries include `t_event`, SSI `raw_message`, FX utilization, message I/O, inbound messages, exception tables, batch notifications, mapping tables, rule synchronization, and the relationship between several raw-message and parent-message tables.

The inventory also does not establish whether all Indonesia cashflows are represented in `ratan_cashflow_group_message`. Using that table as the sole population source could omit valid netting, lifecycle, Swift, exception, or accounting records.

## Referenced implementation artifacts

- `attachments/data_migration.sh`
- `attachments/execute.sh`

The source does not provide the script bodies, so their scope parameterization, ordering, error handling, idempotency, credentials handling, and rollback behavior remain unassessed.

## Related context

This source supports [[projects/ratan-indonesia-onshoring-2026]] and [[projects/ratan-indonesia-isolated-deployment]]. It is also relevant to [[concepts/indonesia-ratan-data-residency-isolation]], [[concepts/cashflow-lineage-and-operational-visibility]], [[concepts/cashflow-sequence-and-count-completeness-control]], and [[concepts/cashflow-batch-control]].

It should be treated as a subordinate migration artifact to the Indonesia architecture source [[cash-settlement-platform-architecture-indonesia]], not as evidence that the migration design has been approved.
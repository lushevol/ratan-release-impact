---
type: source
title: "Cash Settlement Query Service: cashflow_data_history Purge Design"
authors: []
year: 2025
url: ""
venue: ""
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, postgresql, data-retention, jsonb, toast, database-maintenance]
related: [cashflow-data-history, cashflow, postgresql, postgresql-toast-storage, postgresql-jsonb-history-payload-slimming, replacement-table-purge-and-swap]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Cash Settlement Query Service - cashflow_data_history purge.md"]
---
# Cash Settlement Query Service: `cashflow_data_history` Purge Design

## Purpose

This technical-design note evaluates ways to reduce PostgreSQL storage consumption in `cash_settlement_query_cn.cashflow_data_history`. The table grows rapidly because historical records retain large `jsonb` payloads. The document compares in-place payload updates with a replacement-table migration.

The recommended approach is Option 2: create `cashflow_data_history_temp_slim_all_column`, retain selected historical fields, set nonessential columns to `null`, build the required indexes, and swap the replacement table into the `cashflow_data_history` name.

## Scope and test data

Testing was performed in DEV using approximately one million rows for the comparison tables. The production-like `cashflow_data_history` table was reported as approximately 54 million rows.

| Table | Description | Estimated rows | Indexes |
|---|---|---:|---|
| `cashflow_data_history` | Original table | ~1.69 million | Yes |
| `cashflow_data_history_temp_original` | Original structure with one million records | 1 million | No |
| `cashflow_data_history_temp_slim_key_column` | Only the JSON payload is slimmed | 1 million | No |
| `cashflow_data_history_temp_slim_all_column` | Key columns retained; other columns set to `null` | 1 million | No |
| `cashflow_data_history_temp_slim` | Only key columns retained | 1 million | No |

## Storage findings

The original production-like table was reported at 10 GB, including 1,648 MB of heap and 8,677 MB of combined TOAST/index-related storage. The separately reported indexes total 234 MB, while the associated TOAST table was 8,446 MB. This indicates that the large `jsonb` payload, rather than ordinary indexes, is the dominant storage contributor.

| table_name | relid | total_size | table_size | fsm_size | vm_size | toast_size_index_size |
|---|---:|---:|---:|---:|---:|---:|
| `cashflow_data_history` | 1500907339 | 10 GB | 1648 MB | 432 kB | 56 kB | 8677 MB |
| `cashflow_data_history_temp_original` | 4252381026 | 5535 MB | 1004 MB | 272 kB | 32 kB | 4530 MB |
| `cashflow_data_history_temp_slim_key_column` | 4252124751 | 1703 MB | 1412 MB | 376 kB | 48 kB | 291 MB |
| `cashflow_data_history_temp_slim_all_column` | 4251832532 | 537 MB | 537 MB | 152 kB | 24 kB | 8192 bytes |
| `cashflow_data_history_temp_slim` | 4251828143 | 519 MB | 519 MB | 152 kB | 24 kB | 8192 bytes |

The reported indexes on `cashflow_data_history` were:

| index_name | table_name | index_size |
|---|---|---:|
| `cashflow_data_history_pkey` | `cashflow_data_history` | 131 MB |
| `cashflow_data_history_cashflowa_id_idx` | `cashflow_data_history` | 30 MB |
| `cashflow_history_jsonb_nettingid_idx` | `cashflow_data_history` | 21 MB |
| `index_cashflow_history_jsonb_nettingid_btree` | `cashflow_data_history` | 21 MB |
| `cashflow_data_history_cashflowaction_idx` | `cashflow_data_history` | 20 MB |
| `cashflow_data_history_jsonb_splitting_id` | `cashflow_data_history` | 11 MB |

The reported TOAST tables were:

| table_name | toast_table_name | toast_table_size |
|---|---|---:|
| `cashflow_data_history` | `pg_toast_1500907339` | 8446 MB |
| `cashflow_data_history_temp_original` | `pg_toast_4252381026` | 4530 MB |
| `cashflow_data_history_temp_slim_key_column` | `pg_toast_4252124751` | 291 MB |
| `cashflow_data_history_temp_slim_all_column` | `pg_toast_4251832532` | 8192 bytes |
| `cashflow_data_history_temp_slim` | `pg_toast_4251828143` | 8192 bytes |

## Option 1: in-place JSON update

Option 1 replaces the large `cashflow` JSON object with a smaller object containing selected lifecycle, identity, payment-date, netting, splitting, and exception fields.

```sql
update
    cash_settlement_query_cn.cashflow_data_history
set
    cashflow = json_build_object('Cashflow',
        json_build_object(
            'Cashflow_Id', jsonb_extract_path_text(cashflow, 'Cashflow', 'Cashflow_Id'),
            'Cashflow_Minor_Version', jsonb_extract_path_text(cashflow, 'Cashflow', 'Cashflow_Minor_Version'),
            'Cashflow_Business_Version', jsonb_extract_path_text(cashflow, 'Cashflow', 'Cashflow_Business_Version'),
            'Cashflow_Version', jsonb_extract_path_text(cashflow, 'Cashflow', 'Cashflow_Version'),
            'Cashflow_Sub_State', jsonb_extract_path_text(cashflow, 'Cashflow', 'Cashflow_Sub_State'),
            'Cashflow_Event_Type', jsonb_extract_path_text(cashflow, 'Cashflow', 'Cashflow_Event_Type'),
            'Cashflow_State', jsonb_extract_path_text(cashflow, 'Cashflow', 'Cashflow_State'),
            'Status_Event_Type', jsonb_extract_path_text(cashflow, 'Cashflow', 'Status_Event_Type'),
            'Cashflow_Sub_State_Updater', jsonb_extract_path_text(cashflow, 'Cashflow', 'Cashflow_Sub_State_Updater'),
            'Payment_Date', jsonb_extract_path_text(cashflow, 'Cashflow', 'Payment_Date'),
            'Netting_Id', jsonb_extract_path_text(cashflow, 'Cashflow', 'Netting_Id'),
            'Splitting_Id', jsonb_extract_path_text(cashflow, 'Cashflow', 'Splitting_Id'),
            'NSTP_Exception', jsonb_extract_path_text(cashflow, 'Cashflow', 'NSTP_Exception')
        )
    )
where
    id in (
        select id
        from cash_settlement_query_cn.cashflow_data_history
        where cashflow__payment_date < (
            select current_timestamp - interval '3 months')
        limit 100000
    );
```

In the one-million-row DEV test, the original table grew from 5,535 MB to 6,933 MB after the update. After `VACUUM FULL`, it decreased to 1,692 MB.

```sql
vacuum full cash_settlement_query_cn.cashflow_data_history_temp_original;
```

The reported `VACUUM FULL` duration was 37.553 seconds for one million records. This demonstrates update-induced bloat and the need for a table rewrite, but it does not provide a reliable production duration estimate for approximately 54 million rows.

## Option 2: replacement-table slimming

The selected candidate is `cashflow_data_history_temp_slim_all_column`. It retains the apparent entity column set while preserving values only for selected columns. The `cashflow` JSON object retains:

- `Cashflow_Id`
- `Cashflow_Minor_Version`
- `Cashflow_Business_Version`
- `Cashflow_Version`
- `Cashflow_Sub_State`
- `Cashflow_Event_Type`
- `Cashflow_State`
- `Status_Event_Type`
- `Cashflow_Sub_State_Updater`
- `Payment_Date`
- `Netting_Id`
- `Splitting_Id`
- `NSTP_Exception`

The candidate also retains the extracted key columns and `created_at`/`updated_at`. Nonessential fields are projected as `null`.

```sql
create table cash_settlement_query_cn.cashflow_data_history_temp_slim_all_column as
select
    cdh.id,
    cdh.cashflow__cashflow_id,
    cdh.cashflow__cashflow_business_version,
    cdh.cashflow__cashflow_minor_version,
    cdh.cashflow__cashflow_event_type,
    cdh.cashflow__cashflow_state,
    cdh.cashflow__cashflow_sub_state,
    cdh.cashflow__status_event_type,
    cdh.cashflow__cashflow_sub_state_updater,
    cdh.cashflow__payment_date,
    cdh.cashflow__nstp_exception,
    cdh.cashflow__netting_id,
    cdh.cashflow__splitting_id,
    json_build_object(
        'Cashflow',
        json_build_object(
            'Cashflow_Id', jsonb_extract_path_text(cashflow, 'Cashflow', 'Cashflow_Id'),
            'Cashflow_Minor_Version', jsonb_extract_path_text(cashflow, 'Cashflow', 'Cashflow_Minor_Version'),
            'Cashflow_Business_Version', jsonb_extract_path_text(cashflow, 'Cashflow', 'Cashflow_Business_Version'),
            'Cashflow_Version', jsonb_extract_path_text(cashflow, 'Cashflow', 'Cashflow_Version'),
            'Cashflow_Sub_State', jsonb_extract_path_text(cashflow, 'Cashflow', 'Cashflow_Sub_State'),
            'Cashflow_Event_Type', jsonb_extract_path_text(cashflow, 'Cashflow', 'Cashflow_Event_Type'),
            'Cashflow_State', jsonb_extract_path_text(cashflow, 'Cashflow', 'Cashflow_State'),
            'Status_Event_Type', jsonb_extract_path_text(cashflow, 'Cashflow', 'Status_Event_Type'),
            'Cashflow_Sub_State_Updater', jsonb_extract_path_text(cashflow, 'Cashflow', 'Cashflow_Sub_State_Updater'),
            'Payment_Date', jsonb_extract_path_text(cashflow, 'Cashflow', 'Payment_Date'),
            'Netting_Id', jsonb_extract_path_text(cashflow, 'Cashflow', 'Netting_Id'),
            'Splitting_Id', jsonb_extract_path_text(cashflow, 'Cashflow', 'Splitting_Id'),
            'NSTP_Exception', jsonb_extract_path_text(cashflow, 'Cashflow', 'NSTP_Exception')
        )
    ) as cashflow,
    cdh.created_at,
    cdh.updated_at,
    null as cashflow_index,
    null as cashflow_status,
    null as cashflow_sub_status,
    null as cashflow_sub_status_type,
    null as cashflow_sub_status_updater,
    null as cashflow__cashflow_version,
    null as cashflow__cashflow_affirmation_status,
    null as data_flow__data_publication_date_time,
    null as data_flow__data_publication_id,
    null as data_flow__data_sender,
    null as data_flow__data_source_system,
    null as data_flow__data_source_system_country_code,
    null as data_flow__data_source_system_domain_name,
    null as data_flow__data_type,
    null as cashflow__event_date,
    null as cashflow__payment_payer_party_reference,
    null as cashflow__payment_receiver_party_reference,
    null as cashflow__payment_currency,
    null as cashflow__payment_amount,
    null as cashflow__payment_date_business_day_convention,
    null as instrument_common__cfi_code,
    null as instrument_common__isda_taxonomy,
    null as trade_state,
    null as trade_id,
    null as position_id,
    null as parent_trade_id,
    null as entity__booking_entity_sci_fmcode,
    null as entity__booking_entity_sci_fmid,
    null as entity__counterparty_sci_fmid,
    null as settlement_method,
    null as delivery_method,
    null as entity__counterparty_sci_fmcode,
    null as entity__counterparty_cif_code,
    null as entity__counterparty_source_system_entity_id,
    null as cashflow__pay_receive_indicator,
    null as cashflow__payer_name,
    null as cashflow__is_private_banking_cashflow,
    null as cashflow__is_amended_post_settlement,
    null as cashflow__payment_type,
    null as cashflow__is_cashflow_unnet,
    null as cashflow__transaction_details,
    null as data_flow__unique_identifier_message_id,
    null as cashflow__execution_date_time,
    null as entity__general_ledger_business_unit_name,
    null as entity__booking_entity_general_ledger_business_unit_id,
    null as trade__event_physical_status,
    null as cashflow__is_stp,
    null as cashflow__is_stp_ratan,
    null as cashflow__nstp_reason,
    null as cashflow__cashflow_sub_state_type,
    null as cashflow__prev_cashflow_id,
    null as cashflow__next_cashflow_id,
    null as cashflow__validation_status,
    null as cashflow__exception_reason,
    null as cashflow__fmo_comment,
    null as cashflow__fmo_comment_updater,
    null as cashflow__fmo_comment_timestamp,
    null as cashflow__netting_cuttoff_date,
    null as cashflow__booking_entity_sci_fmcode,
    null as cashflow__cashflow_audit_version,
    null as cashflow__payment_cutoff_time,
    null as cashflow__bypass_workflow_indicator,
    null as cashflow__is_netting_required,
    null as cashflow__accounting_reason,
    null as cashflow__accounting_status,
    null as cashflow__swift_status,
    null as cashflow__swift_reason,
    null as trade_date,
    null as linked_trade_id,
    null as cashflow__is_pending_fixing,
    null as cashflow__clearing_alpha,
    null as cashflow__pending_fixing_flag,
    null as cashflow__duplicate_nds_fxd
from cash_settlement_query_cn.cashflow_data_history cdh
limit 1000000;
```

The source reports a total size of 537 MB and a TOAST size of 8,192 bytes for the one-million-row `cashflow_data_history_temp_slim_all_column` test table. The smaller `cashflow_data_history_temp_slim` table was 519 MB, but it did not preserve the complete apparent entity shape.

## Indexes and proposed swap

The proposed indexes are:

```sql
ALTER TABLE cash_settlement_query_cn.cashflow_data_history
    ADD CONSTRAINT cashflow_data_history_pkey PRIMARY KEY (id);

CREATE INDEX cashflow_data_history_new_cashflowa_id_idx
    ON cash_settlement_query_cn.cashflow_data_history_temp_slim_all_column
    USING btree (cashflow__cashflow_id);

CREATE INDEX cashflow_data_history_new_cashflowaction_idx
    ON cash_settlement_query_cn.cashflow_data_history_temp_slim_all_column
    USING btree (cashflowaction);

CREATE INDEX cashflow_data_history_new_jsonb_nettingid_idx
    ON cash_settlement_query_cn.cashflow_data_history_temp_slim_all_column
    USING btree (
        jsonb_extract_path_text(
            cashflow::jsonb,
            VARIADIC ARRAY['Cashflow'::text, 'Netting_Id'::text]
        )
    );

CREATE INDEX cashflow_data_history_new_jsonb_splitting_id
    ON cash_settlement_query_cn.cashflow_data_history_temp_slim_all_column
    USING btree (
        jsonb_extract_path_text(
            cashflow::jsonb,
            VARIADIC ARRAY['Cashflow'::text, 'Splitting_Id'::text]
        )
    );
```

The source proposes:

```sql
alter table cash_settlement_query_cn.cashflow_data_history
    rename to cashflow_data_history_purge;

alter table cash_settlement_query_cn.cashflow_data_history_temp_slim_all_column
    rename to cashflow_data_history;
```

The primary-key statement appears to target the old table rather than the replacement table and must be corrected before execution.

## Risks and unresolved validation

The source does not establish an approved retention policy. The three-month cutoff appears in the Option 1 test only and must not be treated as an approved business or regulatory rule.

Before production execution, the following require validation:

1. The canonical production DDL, including types, defaults, constraints, ownership, grants, triggers, partitioning, replica identity, and publications.
2. Null safety for every downstream consumer, including UI, exports, reporting, and domain-event processing.
3. A strategy for writes arriving while the replacement table is being built.
4. Production runtime, WAL generation, disk headroom, replication impact, and lock duration.
5. Query-plan and latency equivalence for preserved access patterns.
6. Backup, rollback, reconciliation, and post-cutover monitoring procedures.
7. Disposition and retention of `cashflow_data_history_purge`.

The source demonstrates a promising storage reduction, but it is a proposal and DEV experiment rather than evidence of an approved production migration.

## Preserved size-inspection SQL

```sql
SELECT 
    st.relname AS table_name,
    relid,
    pg_size_pretty(pg_total_relation_size(relid)) AS total_size,
    pg_size_pretty(pg_relation_size(relid)) AS table_size,
    pg_size_pretty(pg_relation_size(relid, 'fsm')) AS fsm_size,
    pg_size_pretty(pg_relation_size(relid, 'vm')) AS vm_size
FROM pg_catalog.pg_statio_user_tables st
WHERE schemaname = 'cash_settlement_query_cn'
  AND st.relname LIKE 'cashflow_data_history%'
ORDER BY pg_total_relation_size(relid) DESC;
```

```sql
select
    n.nspname as schema_name,
    c.relname as index_name,
    t.relname as table_name,
    pg_size_pretty(pg_relation_size(c.oid)) as index_size
from pg_class c
join pg_namespace n on n.oid = c.relnamespace
join pg_index i on i.indexrelid = c.oid
join pg_class t on i.indrelid = t.oid
where nspname = 'cash_settlement_query_cn'
  and t.relname like 'cashflow_data_history%'
order by pg_relation_size(c.oid) desc;
```

```sql
select
    c.relname AS table_name,
    t.relname AS toast_table_name,
    pg_size_pretty(pg_total_relation_size(c.reltoastrelid)) AS toast_table_size
FROM pg_class c
JOIN pg_class t ON c.reltoastrelid = t.oid
WHERE c.relname like 'cashflow_data_history%'
ORDER BY c.relname, pg_total_relation_size(c.reltoastrelid) DESC;
```
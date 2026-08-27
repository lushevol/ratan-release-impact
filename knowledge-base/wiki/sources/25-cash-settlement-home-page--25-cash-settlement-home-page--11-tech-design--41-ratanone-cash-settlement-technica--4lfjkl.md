---
type: source
title: Cash Settlement Standardization Service
authors: []
year: 2026
url: ""
venue: ""
created: 2026-08-24
updated: 2026-08-24
tags: [ratanone, uber-integration, database-schema, cash-settlement, ddl]
related: [ratan-inbound-message, ratan-cashflow-rounding-config, ratan-fxu-config, currency-level-cashflow-rounding-configuration, schema-evolution-for-cash-settlement, what-is-the-ratan-inbound-message-idempotency-status-and-version-contract, what-is-the-authoritative-fxu-configuration-and-audit-integrity-contract, why-is-ratan-cashflow-rounding-config-indexed-twice-by-currency]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Cash Settlement Standardization Service.md"]
---
# Cash Settlement Standardization Service

This source is a database-schema change record associated with RATAN–Uber integration. Despite its filename, it does not describe a Cash Settlement Standardization Service architecture, processing flow, API contract, or logical diagram. Its substantive content is DDL for inbound-message persistence, currency rounding configuration, group-message changes, accounting metadata, and FXU configuration.

## Supplied DDL

```sql
--- group - ratan_inbound_message ---CREATE TABLE if not exists ratan_cashflow_group_management_service.ratan_inbound_message (
id bigserial NOT NULL,
correlation_id text NOT NULL,
trade_id text NOT NULL,
status text NOT NULL DEFAULT 'VALIDATED'::text,
message text NOT NULL,
message_type text NOT NULL,
created_at timestamp NOT NULL,
updated_at timestamp NOT NULL,
version int4 NOT NULL,
CONSTRAINT ratan_uber_message_pk PRIMARY KEY (id)
);
CREATE INDEX if not exists ratan_inbound_message_trade_id_idx ON ratan_cashflow_group_management_service.ratan_inbound_message (trade_id);
CREATE INDEX if not exists ratan_inbound_message_tracking_id_idx ON ratan_cashflow_group_management_service.ratan_inbound_message (correlation_id);

--- group - ratan_cashflow_rounding_config ---
CREATE TABLE IF NOT EXISTS ratan_cashflow_group_management_service.ratan_cashflow_rounding_config (
k_currency text NOT NULL,
v_precision int2 NULL,
v_type text NULL,
CONSTRAINT ratan_cashflow_rounding_config_pkey PRIMARY KEY (k_currency)
);
CREATE INDEX if not exists idx_ratan_cashflow_rounding_config ON ratan_cashflow_group_management_service.ratan_cashflow_rounding_config USING btree (k_currency);

--- static data - fxu config ---
CREATE TABLE IF NOT EXISTS ratanone.ratan_fxu_config (
id SERIAL PRIMARY KEY,
booking_entity_fmid TEXT NOT NULL,
counterparty_fmid TEXT NOT NULL,
booking_entity_fmcode TEXT NOT NULL,
counterparty_fmcode TEXT NOT NULL,
is_auto_utilize BOOLEAN NOT NULL,
settlement_means TEXT NOT NULL,
settlement_account TEXT NOT NULL,
data_status text NULL,
maker_id text NULL default 'System',
checker_id text NULL default 'System',
update_record_id int8 NULL,
created_at timestamp NOT NULL DEFAULT now(),
updated_at timestamp NOT NULL DEFAULT now()
);

--- static data - fxu config audit ---
CREATE TABLE IF NOT EXISTS ratanone.ratan_fxu_config_audit (
id SERIAL PRIMARY KEY,
ratan_fxu_config_id int8 NOT NULL,
snapshot text NOT NULL,
data_status text NULL,
user_id text NULL default 'System',
created_at timestamp NOT NULL
);

# Existing Table Updated (FXU related table not included）

--- group ---
ALTER TABLE ratan_cashflow_group_management_service.ratan_cashflow_group_message ADD COLUMN IF NOT EXISTS raw_message_type text NOT NULL DEFAULT 'XML';
ALTER TABLE ratan_cashflow_group_management_service.ratan_cashflow_group_message_history ALTER COLUMN raw_message DROP NOT NULL;
--- accounting ---
ALTER TABLE ratan_cash_accounting_service.ratan_accounting_request_task ADD COLUMN IF NOT EXISTS meta_data varchar NULL;
ALTER TABLE ratan_cash_accounting_service.ratan_accounting_request_task_history ADD COLUMN IF NOT EXISTS meta_data varchar NULL;
```

## Recorded Changes

The Group Management datastore gains [[ratan-inbound-message]] for durable inbound-message records and [[ratan-cashflow-rounding-config]] for currency-level cashflow rounding settings. The schema is likely associated with [[group-management-service]], although the source does not explicitly establish service ownership.

The source also adds `raw_message_type` with an `XML` default to `ratan_cashflow_group_message`, makes historical `raw_message` nullable, and adds nullable `meta_data` fields to live and historical accounting request tasks. The `XML` default is evidence of a storage default, not evidence that XML is the only supported format; see [[what-is-the-supported-xml-message-format-scope-for-cash-settlement]].

FXU configuration and audit DDL is supplied for [[ratan-fxu-config]], even though the surrounding headings state that FXU-related tables are not included. This scope inconsistency remains unresolved.

## Limits of the Evidence

The inbound table has traceability fields and indexes, but no declared unique key for `correlation_id`, `trade_id`, or `version`. Therefore, it does not by itself establish idempotency, replay behavior, duplicate suppression, or a status-transition lifecycle. See [[uber-inbound-message-idempotency-and-error-state]] and [[what-is-the-ratan-inbound-message-idempotency-status-and-version-contract]].

The FXU audit table requires `ratan_fxu_config_id`, but the supplied DDL declares no foreign key. It also does not declare a business-key uniqueness constraint for FXU configurations. See [[what-is-the-authoritative-fxu-configuration-and-audit-integrity-contract]].

The rounding configuration primary key and explicit B-tree index are both defined on `k_currency`; the source gives no reason for the additional index. See [[why-is-ratan-cashflow-rounding-config-indexed-twice-by-currency]].
---
type: concept
title: RATAN Indonesia Entity-Scoped Data Migration
tags: [RATAN, Indonesia, data-migration, entity-scope, referential-integrity]
related: [ratan-indonesia-onshoring-2026, ratan-indonesia-isolated-deployment, indonesia-ratan-data-residency-isolation, cashflow-lineage-and-operational-visibility, ratan-cashflow-group-management-service, what-is-the-approved-ratan-indonesia-data-migration-reconciliation-plan, what-are-the-authoritative-foreign-key-paths-for-indonesia-ratan-migration]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Data Migration - Indonesia.md"]
---
# RATAN Indonesia Entity-Scoped Data Migration

## Definition

RATAN Indonesia entity-scoped data migration is the proposed selection and transfer of Cash Settlement Platform records associated with entity or FM ID `'8'`. The approach is primarily cashflow-rooted, with dependent records derived through cashflow, trade, group, message, and external-system identifiers.

## Scope model

The source uses multiple service-specific fields to identify the Indonesia population:

- `party1_fm_id`
- `entity__booking_entity_sci_fmid`
- `booking_entity_fmid`
- `booking_entity_id`
- `entity_fmid`

Their semantic equivalence is assumed but not demonstrated. The canonical scope contract must confirm whether `'8'` identifies the same legal or booking entity in every service.

## Extraction model

The proposed extraction model has two layers:

1. Select directly scoped cashflow records using `cashflow_id` and an entity predicate.
2. Derive dependent identifiers for records that do not expose the cashflow key directly.

Important derived-key paths include:

- `lms_message.aggregate_root_id` to select `lms_raw_message`;
- `ratan_accounting_request_task.external_system_key` to select accounting responses;
- `ratan_cashflow_group_message.cashflow_id` to select group-related records;
- `ratan_cashflow_group_message.trade_id` to select trade and group history;
- `ratan_cashflow_scbml_history.body_event_rowkey` to select SCBML messages.

## Required controls

Before execution, the migration should establish:

- a complete starting population and de-duplication rule;
- authoritative foreign-key or business-key relationships;
- parent-before-dependent load ordering;
- treatment of current and history tables;
- handling for in-flight, held, affirmed, exceptioned, netted, split, and pending-accounting cashflows;
- source-to-target row counts and integrity checks;
- rollback and retry behavior;
- operational and business sign-off.

## Current maturity

The source is an inventory, not an approved migration design. Question-marked or incomplete items include `t_event`, SSI `raw_message`, FX utilization, group message I/O, inbound messages, exception records, batch fix notifications, mapping tables, and rule synchronization.

The referenced `data_migration.sh` and `execute.sh` scripts cannot be evaluated because their contents are not included.

## Related work

This concept extends the Indonesia onshoring and isolated-deployment work described in [[projects/ratan-indonesia-onshoring-2026]] and [[projects/ratan-indonesia-isolated-deployment]]. It also depends on the lineage and operational-visibility principles in [[concepts/cashflow-lineage-and-operational-visibility]].
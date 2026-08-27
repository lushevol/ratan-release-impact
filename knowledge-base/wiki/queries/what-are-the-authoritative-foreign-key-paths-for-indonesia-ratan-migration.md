---
type: query
title: What Are the Authoritative Foreign-Key Paths for Indonesia RATAN Migration?
tags: [RATAN, Indonesia, data-migration, foreign-keys, schema]
related: [ratan-indonesia-entity-scoped-data-migration, ratan-cashflow-group-management-service, cash-settlement-lms-service, ratan-cash-accounting-service, ratan-cashflow-lifecycle-service]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Data Migration - Indonesia.md"]
---
# What Are the Authoritative Foreign-Key Paths for Indonesia RATAN Migration?

## Question

Which proposed relationships are authoritative for selecting dependent migration records?

## Relationships requiring confirmation

The source leaves the following paths unresolved or incompletely specified:

- `lms_raw_message.message_key` to `lms_message.aggregate_root_id`;
- SSI `raw_message.message_key` to a cashflow identifier;
- `rep_exception.entity_id` to `cashflow_id`;
- `cash_mxg_batch_fix_notify.flow_id` to `cashflow_id`;
- `ratan_cashflow_mapping` and its history relationships;
- group message I/O and inbound-message relationships;
- `ratan_cashflow_scbml_message.id` to `body_event_rowkey`;
- FX-utilization and rule-synchronization dependencies.

## Resolution needed

Review service schemas, foreign-key metadata, application code, and representative production records. Mark each table as required, audit/history, operational-message, rebuildable, or explicitly excluded, with a deterministic extraction rule.
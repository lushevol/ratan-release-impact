---
type: entity
title: ratan_fxu_config and ratan_fxu_config_audit
created: 2026-08-24
updated: 2026-08-24
tags: [database-table, fxu, static-data, audit, maker-checker, ratanone]
related: [what-is-the-authoritative-fxu-configuration-and-audit-integrity-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Cash Settlement Standardization Service.md"]
---
# ratan_fxu_config and ratan_fxu_config_audit

`ratanone.ratan_fxu_config` stores FXU configuration, and `ratanone.ratan_fxu_config_audit` stores text snapshots associated with configuration records.

## Configuration Record

The configuration table has a serial primary key and requires booking-entity and counterparty FMID and FMCode values, `is_auto_utilize`, `settlement_means`, and `settlement_account`. It also provides nullable `data_status` and `update_record_id`, maker/checker identifiers defaulting to `System`, and timestamps defaulting to `now()`.

## Audit Record

The audit table has a serial primary key, requires `ratan_fxu_config_id`, `snapshot`, and `created_at`, and provides optional `data_status` and a `user_id` defaulting to `System`.

## Integrity Limits

The supplied DDL declares no foreign key from `ratan_fxu_config_audit.ratan_fxu_config_id` to the configuration table. It also provides no business-key uniqueness constraint across the booking-entity and counterparty identifiers.

The source contains the FXU DDL while labeling FXU-related tables as excluded. Ownership, maker-checker behavior, audit snapshot format, and integrity expectations remain open in [[what-is-the-authoritative-fxu-configuration-and-audit-integrity-contract]].
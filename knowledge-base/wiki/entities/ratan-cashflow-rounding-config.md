---
type: entity
title: ratan_cashflow_rounding_config
created: 2026-08-24
updated: 2026-08-24
tags: [database-table, rounding, currency, cashflow, group-management]
related: [group-management-service, currency-level-cashflow-rounding-configuration, why-is-ratan-cashflow-rounding-config-indexed-twice-by-currency]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Cash Settlement Standardization Service.md"]
---
# ratan_cashflow_rounding_config

`ratan_cashflow_group_management_service.ratan_cashflow_rounding_config` stores cashflow rounding configuration by currency.

## Physical Contract

`k_currency` is the primary key. `v_precision` is nullable `int2`, and `v_type` is nullable `text`.

The DDL also creates `idx_ratan_cashflow_rounding_config`, a B-tree index on `k_currency`, in addition to the access path normally created for the primary key.

## Limits

The source does not define the rounding modes represented by `v_type`, the meaning of `v_precision`, permitted null values, fallback behavior for an absent currency, or the owner and deployment process for configuration changes.

The separate index has no documented rationale and is tracked in [[why-is-ratan-cashflow-rounding-config-indexed-twice-by-currency]]. For the broader pattern, see [[currency-level-cashflow-rounding-configuration]].
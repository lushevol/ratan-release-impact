---
type: query
title: Why Is ratan_cashflow_rounding_config Indexed Twice by Currency?
created: 2026-08-24
updated: 2026-08-24
tags: [database-index, rounding, currency, performance]
related: [ratan-cashflow-rounding-config, currency-level-cashflow-rounding-configuration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Cash Settlement Standardization Service.md"]
---
# Why Is ratan_cashflow_rounding_config Indexed Twice by Currency?

`ratan_cashflow_rounding_config` declares `k_currency` as its primary key and separately creates a B-tree index on the same column.

## Questions

- Is the explicit `idx_ratan_cashflow_rounding_config` required for a documented access pattern?
- Does the production database implement the primary-key index differently from the expected B-tree access path?
- Should the separate index be retained, removed, or justified as part of the migration standard?
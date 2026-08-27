---
type: entity
title: splitting_cashflow
tags: [postgresql, ratan, cashflow-splitting, persistence]
related: [split-cashflow-persistence-and-lineage, cashflow-splitting, ratan-cash-settlement-netting-service]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting/Splitting Tech Design.md"]
---
# splitting_cashflow

`cash_netting_service.splitting_cashflow` is the RATAN persistence table for split-cashflow records.

It stores both `cashflow_id` and `splitting_id`, allowing a split record to be located by individual cashflow or split group. `business_version` and `minor_version` show that split operations are version-aware. The table indexes only `cashflow_id` and `splitting_id`.

The source stores `amount` as text and does not define controlled values for `cashflow_character`, `"action"`, `status`, or `split_type`. Consumers must not infer an authoritative state taxonomy from these columns.

See [[split-cashflow-persistence-and-lineage]] and [[what-is-the-canonical-splitting-id-and-rule-unique-id-contract]].
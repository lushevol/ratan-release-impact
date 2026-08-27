---
type: concept
title: Auto-Netting Persistence Model
created: 2026-08-22
updated: 2026-08-22
tags: [cashflow-auto-netting, persistence, database-design, optimistic-locking]
related: [cashflow-auto-netting, auto-netting-rule-management, netting-rule-change-cashflow-refresh, ccil-settlement-method-stamping, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Auto Netting Technical Design.md"]
---
# Auto-Netting Persistence Model

## Purpose

The proposed persistence model separates cashflow-level auto-netting records from netting-type configuration:

- `ratan_auto_netting_cashflow` tracks eligible cashflows, rule identity, grouping, trigger timing, processing status, failure information, and optimistic-locking state.
- `ratan_auto_netting_config` stores configurable grouping fields and resultant-cashflow mappings for each netting type.

## Design characteristics

The cashflow table stores both `rule_id` and `rule_uuid`. The source states that `rule_id` may change when a user updates a rule, while `rule_uuid` is intended to provide stable identity across that change.

`net_group_key` is a serialized grouping value. The source gives `400452428,2024-06-04,USD` as a CCIL example. The configuration table instead stores JSON describing grouping fields, including `entityFmid`, `valueDate`, and `settlementCurrency`.

`resultant_mapping_config` supports mappings such as a fixed CCIL counterparty and settlement method:

```json
{ "counterpartyFmId": "400021949", "counterpartyFmCode": "CLEARING CORP*MMB", "settlementMethod": "Cash" }
```

The proposed `version INT` column is identified as supporting optimistic locking.

## Proposed status and enum values

The source lists these `net_status` values:

`Waiting`, `Pending`, `Done`, `Disabled`, and `Failed`.

It lists these STP values in the table comment:

`MakerChecker`, `CheckerOnly`, and `FullStp`.

It lists these netting types:

`BilateralNetting`, `SwapAgentNetting`, `CcilNetting`, and `BicNetting`.

The Rule Engine request instead uses `FULL_STP` and `"Bilateral Netting"`. These differences are unresolved serialization inconsistencies, not canonical values.

## Integrity gaps

The document includes an `Index` heading without index definitions. It also omits uniqueness constraints, foreign keys, check constraints, retention rules, and explicit transition rules. Before implementation approval, the team should define uniqueness for cashflow records and rule versions, indexes for lookup and scheduling, status-transition enforcement, and retry behavior.

The source preserves the column spelling `bussiness_version`; this should be confirmed before a schema is finalized.
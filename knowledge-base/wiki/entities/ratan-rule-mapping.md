---
type: entity
title: ratan_rule_mapping
created: 2026-08-24
updated: 2026-08-24
tags: [database-table, rule-mapping, special-rules, lineage]
related: [ratan-rule-engine, rule-mapping-and-update-lineage, ratanone-rule-service, special-rule-processing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Ratan-rule-service reconstruction for rule-engine.md"]
---
# `ratan_rule_mapping`

`ratan_rule_mapping` associates rule-engine rules with exception metadata and update lineage.

## Proposed `is_special` field

The design adds `is_special` as a Boolean. Six rules generated from `ratan_special_rule_config` are expected to have `is_special = true`; other rules default to `false`.

The source does not identify the six rules, define how this classification is maintained, or specify migration and reconciliation procedures.

## Update lineage

`reference_rule_id` identifies the previous rule ID when a rule is updated. This supports historical association between a current rule and its predecessor.

The source does not establish whether this table is authoritative or a derived projection of Ratan Rule Engine data.
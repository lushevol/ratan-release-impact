---
type: entity
title: ratan_special_rule_config_v2
created: 2026-08-24
updated: 2026-08-24
tags: [database-table, special-rules, rule-configuration, schema-evolution]
related: [special-rule-processing, ratanone-rule-service, ratan-rule-mapping, rule-maintenance-and-validation-pipeline]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Ratan-rule-service reconstruction for rule-engine.md"]
---
# `ratan_special_rule_config_v2`

`ratan_special_rule_config_v2` stores configuration for special rules, including exception attributes and predefined rule expressions.

## Proposed changes

The design:

- Removes `fact_processor`
- Adds `rule_content`
- Removes or replaces the prior `active` field
- Adds `is_used`
- Adds `is_mapped_rule`

`rule_content` contains an expression such as:

```text
fmEntity__fmAccount__fmType matches "(?i)CORP"
```

This expression is passed to `ratanone-rule-service` for special-rule processing.

## Flag semantics

`is_used = true` means the rule is `save_confirmed` or `delete_pending`; `false` means it is neither status. `is_mapped_rule = true` means a mapped rule exists regardless of status; `false` means no rule exists.

The source does not define all permitted combinations, whether `active` is physically removed, or whether `processor` remains independently necessary.
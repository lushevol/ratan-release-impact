---
type: concept
title: Rule Mapping and Update Lineage
created: 2026-08-24
updated: 2026-08-24
tags: [rule-mapping, lineage, versioning, lifecycle]
related: [ratan-rule-mapping, ratan-rule-engine, ratan-special-rule-config-v2, ratanone-rule-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Ratan-rule-service reconstruction for rule-engine.md"]
---
# Rule Mapping and Update Lineage

Rule mapping links a rule-engine rule to exception metadata, operation level, special-rule classification, and its predecessor.

`referenceRuleId` in the rule response corresponds to `reference_rule_id` in `ratan_rule_mapping` and identifies the previous rule ID when a rule is updated. This provides a basis for version and historical traceability.

The design distinguishes two configuration flags:

- `is_used`: whether the rule is in the `save_confirmed` or `delete_pending` status set.
- `is_mapped_rule`: whether a mapped rule exists regardless of status.

These flags are not defined as equivalent to a generic active flag. The source does not specify all valid combinations, the relationship to statuses such as `ADD_PENDING`, or whether the mapping table is authoritative or derived.
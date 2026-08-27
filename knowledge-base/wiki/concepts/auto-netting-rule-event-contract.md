---
type: concept
title: Auto-Netting Rule Event Contract
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, auto-netting, event-contract, drools, metadata]
related: [auto-netting-rule-lifecycle, auto-netting-rule-version-replacement, drools, enhancedfact, matchedrule, what-is-the-authoritative-auto-netting-rule-action-contract, what-is-the-authoritative-auto-netting-rule-schema-and-metadata-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/rule engine rule_action_event：.md"]
---
# Auto-Netting Rule Event Contract

An auto-netting event transports both the lifecycle instruction and the rule that must be evaluated by the rule engine.

## Required Contract Areas

- `type` identifies the lifecycle event: `SAVE`, `CONFIRM`, or `REMOVE`.
- `ruleScript` contains Java-dialect [[drools|Drools]] code.
- `userRule` retains the user-facing expression represented in the generated script.
- `scriptHashKey` identifies the script using a hash-like value.
- `ruleAdditionalInfo` carries rule identity, status, replacement linkage, and metadata.
- `businessFlow` is `STRATEGIC_SETTLEMENT`.
- `ruleType` is `AUTO_NETTING`.
- `rule_action`, where present, distinguishes operations such as `update`, `enable`, `disable`, `reject`, and `confirm`.

The script is expected to match an [[enhancedfact|EnhancedFact]] and add a [[matchedrule|MatchedRule]] to `matchedRuleSet`.

## Configuration Metadata

The `metadata` field is double-encoded JSON. Its documented `autoNettingConfig` contains:

- `nettingDate`, shown as `VD`;
- `nettingTime`, shown as `00:00`;
- `stpLevel`, shown as `NSTP_MAKER_CHECKER`;
- `nettingType`, shown as `BIC Netting` or `SAL MTM Netting`.

The source does not define a schema version, field governance, validation rules, or the meaning of those coded values. These gaps are tracked in [[what-is-the-authoritative-auto-netting-rule-schema-and-metadata-contract]].

## Approval Action Ambiguity

The lifecycle matrix assigns `create_confirm` and `update_confirm` as approval actions. The supplied `CONFIRM` payloads instead contain `rule_action: "confirm"` for both creation and update approval. Consumers should not infer a canonical approval action value until [[what-is-the-authoritative-auto-netting-rule-action-contract]] is resolved.
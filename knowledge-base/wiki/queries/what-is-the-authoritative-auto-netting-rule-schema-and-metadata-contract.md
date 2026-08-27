---
type: query
title: What Is the Authoritative Auto-Netting Rule Schema and Metadata Contract?
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, auto-netting, metadata, schema, validation]
related: [auto-netting-rule-event-contract, drools, enhancedfact]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/rule engine rule_action_event：.md"]
---
# What Is the Authoritative Auto-Netting Rule Schema and Metadata Contract?

The source supplies example payloads but does not define a versioned schema or validation contract.

`ruleAdditionalInfo.metadata` is a JSON string containing JSON. The nested `autoNettingConfig` includes `nettingDate`, `nettingTime`, `stpLevel`, and `nettingType`, with observed values `VD`, `00:00`, `NSTP_MAKER_CHECKER`, `BIC Netting`, and `SAL MTM Netting`.

## Questions to Resolve

- What do `VD` and `NSTP_MAKER_CHECKER` mean operationally?
- What values are valid for every `autoNettingConfig` field?
- Is double-encoded metadata intentional, and which layer validates it?
- What is the canonical meaning and generation process for `scriptHashKey`?
- Which `EnhancedFact` fields, operators, and expressions are permitted in `userRule`?
- Is there a schema version, migration policy, or backward-compatibility contract?

Resolution would make [[auto-netting-rule-event-contract]] implementable without relying on examples alone.
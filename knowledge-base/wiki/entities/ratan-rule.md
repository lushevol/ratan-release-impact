---
type: entity
title: ratan_rule
created: 2026-08-24
updated: 2026-08-24
tags: [database-table, ratan, rule-engine, archived-design]
related: [ratan-drools-rule, ratan-drools-fact-processor, dynamic-drl-compilation, rule-governance-and-auditability, what-is-the-authoritative-ratan-rule-service-api-and-schema-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/Rule Service Tech Design.md"]/Rule Service Tech Design.md"]/Rule Service Tech Design.md"]
---
# ratan_rule

> [!warning]
> This table is a proposed historical schema from an archived Rule Service design. It is not evidence of the current production schema.

`ratan_rule` was intended to store user-manageable business rules, their lifecycle status, version, reason, and audit fields. The archived design proposes that rule changes generate corresponding DRL persisted in [[ratan-drools-rule]].

The nullable `rule` and `fact_processor` fields are documented with the requirement that at least one must be non-null, but no database `CHECK` constraint or application-validation mechanism is provided.

The design also proposes removal of `operation_level`, `exception_code`, and `exception_category`; this is historical evidence only and does not establish the current model.

See [[what-is-the-authoritative-ratan-rule-service-api-and-schema-contract]] for verification of the deployed schema and lifecycle contract.
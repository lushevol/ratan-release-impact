---
type: entity
title: ratan_drools_rule
created: 2026-08-24
updated: 2026-08-24
tags: [database-table, drools, drl, ratan, archived-design]
related: [ratan-rule, dynamic-drl-compilation, drools-rule-refresh, what-is-the-authoritative-ratan-rule-service-api-and-schema-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/Rule Service Tech Design.md"]/Rule Service Tech Design.md"]/Rule Service Tech Design.md"]
---
# ratan_drools_rule

> [!warning]
> This is a proposed historical schema from an archived Rule Service design, not a confirmed current table.

`ratan_drools_rule` was intended to persist executable DRL generated from business rules in [[ratan-rule]]. The design loads DRL using a business-flow and rule-type selection, then compiles and executes it through Drools.

The source describes a composite unique index on `business_workflow` and `rule_type`, while the documented schema column is `business_flow`. Because no DDL is supplied, the index field and actual uniqueness constraint are ambiguous.

The table's `version` was intended to start at `1` and increment when a rule is updated. See [[dynamic-drl-compilation]] and [[drools-rule-refresh]].
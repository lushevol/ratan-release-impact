---
type: concept
title: Database-Backed Rule Loading
created: 2026-08-24
updated: 2026-08-24
tags: [rule-engine, database, rule-loading, cash-settlement]
related: [ratanone-rule-service, ratanone-rule-service-ratan-rule, business-flow-and-rule-type-classification, drools]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/Rule Service Migration.md"]/Rule Service Migration.md"]/Rule Service Migration.md"]
---
# Database-Backed Rule Loading

Database-backed rule loading is the intended target pattern in which [[ratanone-rule-service]] retrieves rules from its database when validating a specified dataset.

The archived design identifies `business_flow` and `rule_type` as selection parameters for records in `ratanone_rule_service.ratan_rule`. During migration, supplied production CSV rules are intended to be imported and converted into corresponding [[drools]] rule records in the database.

The source does not define query semantics, precedence, evaluation ordering, cache behavior, rule compilation, failure behavior, or the Drools runtime configuration.
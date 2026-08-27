---
type: entity
title: ratanone_rule_service.ratan_rule
created: 2026-08-24
updated: 2026-08-24
tags: [database-table, rule-engine, migration, schema]
related: [ratanone-rule-service, rule-service-consolidation, business-flow-and-rule-type-classification, database-backed-rule-loading]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/Rule Service Migration.md"]/Rule Service Migration.md"]/Rule Service Migration.md"]
---
# ratanone_rule_service.ratan_rule

`ratanone_rule_service.ratan_rule` is the proposed common target table for migrated CN and BAU rules.

The archived design changes BAU identifiers from `bigserial` to `text`, maps `business_workflow` to `business_flow`, and renames audit columns. It removes BAU `hierarchy` and `value_date`, removes CN `operation_level`, `exception_code`, and `exception_category`, and adds `fact_processor` as a replacement for the CN special-rule processor.

The intended retrieval keys are `business_flow` and `rule_type`. Default values, canonical casing, uniqueness constraints, and collision semantics are unspecified. See [[canonical-business-flow-and-rule-type-taxonomy]].
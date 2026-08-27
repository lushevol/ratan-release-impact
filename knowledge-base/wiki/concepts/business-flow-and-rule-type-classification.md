---
type: concept
title: Business Flow and Rule Type Classification
created: 2026-08-24
updated: 2026-08-24
tags: [rule-engine, rule-classification, database-design, cash-settlement]
related: [ratanone-rule-service-ratan-rule, database-backed-rule-loading, canonical-business-flow-and-rule-type-taxonomy]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/Rule Service Migration.md"]/Rule Service Migration.md"]/Rule Service Migration.md"]
---
# Business Flow and Rule Type Classification

Business Flow and Rule Type Classification is the archived design's proposed way to distinguish CN and BAU rules in the shared `ratanone_rule_service.ratan_rule` table. The service would load rules using `business_flow` and `rule_type`.

The source approves a default `rule_type` but does not specify it. Its UAT inventories also expose unresolved normalization issues: BAU uses `business_workflow` before mapping to `business_flow`, contains `NULL` rule types, and uses values such as `nstp` and `netting`; CN uses `NSTP`, `NETTING`, `SUPPRESSION`, and `IRS`.

No canonical enumeration, null-handling rule, composite uniqueness constraint, or collision behavior is supplied. See [[canonical-business-flow-and-rule-type-taxonomy]].
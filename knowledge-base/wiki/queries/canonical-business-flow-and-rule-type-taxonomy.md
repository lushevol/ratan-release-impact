---
type: query
title: What Is the Canonical Business Flow and Rule Type Taxonomy?
created: 2026-08-24
updated: 2026-08-24
tags: [rule-engine, taxonomy, database-migration, cash-settlement]
related: [business-flow-and-rule-type-classification, ratanone-rule-service-ratan-rule, ratanone-rule-service, rule-service-consolidation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/Rule Service Migration.md"]/Rule Service Migration.md"]/Rule Service Migration.md"]
---
# What Is the Canonical Business Flow and Rule Type Taxonomy?

The archived design selects `business_flow` and `rule_type` as the discriminator for shared CN and BAU rule storage, but does not provide the canonical taxonomy.

## Questions to resolve

- What is the approved default value for `rule_type`?
- How must legacy `NULL` BAU values be represented?
- Are values case-sensitive, and how are `nstp`/`NSTP` and `netting`/`NETTING` normalized?
- Is `business_workflow` always mapped directly to `business_flow`?
- Which combinations are valid, and is a composite uniqueness constraint required?
- How are collisions, precedence, and rule selection handled for shared combinations?

The UAT inventory is insufficient to establish the full production taxonomy.
---
type: query
title: What Is the Authoritative Rule Service Migration and Reconciliation Plan?
created: 2026-08-24
updated: 2026-08-24
tags: [migration, reconciliation, drools, rule-engine, production-readiness]
related: [rule-service-consolidation, ratanone-rule-service, ratanone-rule-service-ratan-rule, lin-liang]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/Rule Service Migration.md"]/Rule Service Migration.md"]/Rule Service Migration.md"]
---
# What Is the Authoritative Rule Service Migration and Reconciliation Plan?

The archived design proposes that BAU and CN teams provide production rules as `sample.csv`, after which Lin Liang imports them and generates Drools rule records.

## Questions to resolve

- What is the authoritative production inventory and CSV contract?
- How are source columns transformed into the target schema, including removed fields and `fact_processor`?
- What source-to-target count, status, and semantic reconciliation thresholds apply?
- How are Drools records validated against legacy behavior?
- What is the idempotency, approval, rollback, and environment-promotion process?
- What are the service cutover, API deprecation, monitoring, and contingency plans?
- Is there evidence that this archived proposal was implemented or superseded?

No migration-control specification or completion evidence is contained in the source.
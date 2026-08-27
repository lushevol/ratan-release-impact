---
type: concept
title: Rule Service Migration
created: 2026-08-24
updated: 2026-08-24
tags: [rule-engine, migration, delivery-planning, archived, cash-settlement]
related: [rule-service, csv-to-drools-rule-generation, business-rule-engines, rule-engine-vs-workflow-orchestration, did-the-2023-rule-service-migration-and-uat-complete]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/Rule Service Migration/Rule Service Delivery Plan.md"]/Rule Service Migration/Rule Service Delivery Plan.md"]/Rule Service Migration/Rule Service Delivery Plan.md"]
---
# Rule Service Migration

Rule Service migration is the planned transfer and onboarding of existing rule portfolios into a [[rule-service]]. The archived 2023 plan covered a migration proposal, a detailed plan, FX replication rules, BAU suppression rules, CN rules, and an undefined “Detective rules” work item.

The only workstream recorded as complete in the plan is FX Replication Rules Development. UAT deployment was still in progress, while BAU and CN onboarding remained TBC. Target dates alone must not be read as completed migration milestones.

The plan also identifies a proposed division of responsibility: fields-service functionality and validation rules would move to [[static-data-service]]. It does not define the retained Rule Service scope or prove that the split was implemented.

Rule migration should include evidence of source-rule ownership, semantic equivalence, testing, approval, version control, release promotion, rollback, and auditability. Those controls are not specified by this delivery plan. See [[rule-governance-and-auditability]] and [[did-the-2023-rule-service-migration-and-uat-complete]].
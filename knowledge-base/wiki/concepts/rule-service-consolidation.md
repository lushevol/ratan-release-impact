---
type: concept
title: Rule Service Consolidation
created: 2026-08-24
updated: 2026-08-24
tags: [rule-engine, service-migration, cash-settlement, architecture]
related: [ratanone-rule-service, ratan-rule-service, ratan-suppression-service, business-rule-engines, rule-service-domain-boundaries, authoritative-rule-service-migration-and-reconciliation-plan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/Rule Service Migration.md"]/Rule Service Migration.md"]/Rule Service Migration.md"]
---
# Rule Service Consolidation

Rule-service consolidation is the proposed movement of CN rules from [[ratan-rule-service]] and BAU suppression and netting rules from [[ratan-suppression-service]] into [[ratanone-rule-service]].

In this archived design, consolidation covers common table storage, rule maintenance, and validation. It does not mean every adjacent capability moves to the target: Data Entitlement Rule is explicitly standalone, while Fields and frontend Validation Rules are intended to leave Rule Service.

The source is evidence of a proposed architecture only. It does not demonstrate a completed cutover, API compatibility, data reconciliation, or operational acceptance.
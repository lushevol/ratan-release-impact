---
type: entity
title: Rule Service
created: 2026-08-22
updated: 2026-08-23
tags: [RATAN, rule-engine, Drools, business-rules, rule-service, NSTP, cashflow-classification, CCIL, cash-settlement, rules, field-mapping, versioning, archived]
related: [ratan, drools, ratan-rule-lifecycle-management, business-rule-maintenance, ccil-netting, settlement-method-driven-netting, ratanone-rule-service, centralized-cashflow-field-mapping-governance, dynamic-cashflow-query-field-mapping, ratanone-foundation, query-service, what-is-the-authoritative-versioned-logical-field-to-xpath-contract, rule-service-migration, csv-to-drools-rule-generation, static-data-service, did-the-2023-rule-service-migration-and-uat-complete]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Ratan One Processing Guide (DOI)/Business Rules Maintenance.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/CCIL Netting Design.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cashflow Query Service - GraghQL schema and DB column mapping for dynamic query.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/Rule Service Migration/Rule Service Delivery Plan.md"]/Rule Service Migration/Rule Service Delivery Plan.md"]
---

# Rule Service

Rule Service is identified by the RATAN One processing guide as responsible for rule creation, maintenance, and execution following the 2023 Rule Service engine upgrade to Drools.

An archived 2023 Rule Service Delivery Plan separately identifies Rule Service as the target service for migration and onboarding of business-rule portfolios. That plan is historical context for [[rule-service-migration]] and does not establish the service's final implementation status, runtime design, current owner, deployment model, or continued role in the current RATAN architecture.

## Rule-engine role and documented capabilities

The RATAN One processing guide presents Rule Service as the common engine behind RATAN One rule blotters. It states that blotters share a common style and feature set while the engine supports customization.

The associated Rule Blotter documentation describes:

- Rule creation with field-value conditions.
- Logical `AND` evaluation across different selected fields.
- Grouped rules for complex scenarios.
- Dry-run configuration.
- Approval and rejection workflows.
- Rule updates, disabling, and activation.
- History viewing, export, and filtering.

The processing-guide source does not provide architecture diagrams, service interfaces, deployment details, migration criteria, or evidence that every described control is technically enforced by Rule Service.

## Archived 2023 migration and delivery-plan context

The archived delivery plan records:

- Completed FX Replication Rules Development against a target date of 10 November 2023.
- An in-progress target to deploy Rule Service with FX rules to UAT by 24 November 2023.
- BAU suppression-rule and CN-rule onboarding listed as TBC end-of-December work.

The plan does not confirm whether the migration or UAT deployment completed. See [[did-the-2023-rule-service-migration-and-uat-complete]].

For planned BAU onboarding, the delivery plan used [[csv-to-drools-rule-generation]]. Its proposed movement of fields-service functionality and validation rules to [[static-data-service]] suggests an intended responsibility boundary, but that boundary remains unconfirmed.

## Proposed field-mapping role

Separately, the **Cashflow Query Service - GraghQL schema and DB column mapping for dynamic query** design proposes Rule Service as the central system of record for cashflow logical fields and logical-model-to-XPath mapping metadata.

Under that proposed design, Rule Service would:

- Provide mappings selected by version and context.
- Version XPath mapping data.
- Optionally publish data-version-upgrade events.

This is proposed design intent, not evidence of an implemented production contract. The API shape, context semantics, ownership, compatibility guarantees, access control, and availability requirements are unspecified.

[[query-service]] and the UI are intended consumers of this proposed mapping role. See [[centralized-cashflow-field-mapping-governance]] and [[what-is-the-authoritative-versioned-logical-field-to-xpath-contract]].

## CCIL netting design usage

The **CCIL Netting Design** describes Rule Service as the **proposed** decision point for applying special straight-through-processing treatment to cashflows tagged with settlement method `CCIL`.

The design calls for an NSTP rule matching:

```text
Settlement_Method = "CCIL"
```

When the rule matches, the cashflow should receive:

```text
Waiting+IsNettingEligible
```

The CCIL Netting Design does not define:

- Rule priority.
- Interactions with existing rules.
- Persistence semantics.
- The mapping between `Waiting+IsNettingEligible` and the frontend status expression `waiting+pending netting`.

## Related pages

- [[ratan]]
- [[drools]]
- [[ratan-rule-lifecycle-management]]
- [[rule-service-migration]]

---
type: entity
title: RATAN Rule Engine
created: 2026-08-24
updated: 2026-08-24
tags: ["ratan", "rule-engine", "ratanone", "cash-settlement", "rules", "STRATEGIC_SETTLEMENT"]
related: ["drools", "domain-owned-rule-fact-enrichment", "json-based-rule-evaluation", "ratan-rule-engine-v2-migration", "ratanone-rule-service", "ratan-rule-mapping", "rule-maintenance-and-validation-pipeline", "special-rule-processing"]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Ratan-rule-service reconstruction for rule-engine.md"]/RATAN Rule Engine Overview.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Ratan-rule-service reconstruction for rule-engine.md"]
---
# RATAN Rule Engine

## Identity

The RATAN Rule Engine, also called the RatanOne Rule Service, is the central rule-evaluation service described in the archived overview. The archived source distinguishes an existing v1 from a proposed v2 architecture.

The reconstruction source describes the Ratan Rule Engine as the rule-evaluation component from which rule information is fetched and with which `ratanone-rule-service` interacts.

## Rule information

According to the reconstruction source, rule information includes:

- Rule identity
- Business scope
- Rule type
- User and running expressions
- Lifecycle status
- Execution settings
- Update lineage
- Category
- Exception metadata
- Audit fields

A representative business flow is `STRATEGIC_SETTLEMENT`. The example rule type is `NSTP`, and rule categories are `NORMAL` or `SPECIAL`.

## Relationship to `ratanone-rule-service`

The reconstruction source presents `ratanone-rule-service` as the direct interface for rule maintenance and validation. It identifies `ratan_rule_mapping.rule_id` as an ID from `ratanone_rule_service.ratan_rule_engine`.

The reconstruction source does not define whether the rule engine or `ratan_rule_mapping` is authoritative for mappings, nor does it specify the complete rule API.

## Proposed v2 direction

According to the archived overview, RatanOne Rule Service v2 is intended to:

- Consume JSON facts rather than perform SCBML conversion.
- Receive domain-enriched data from consuming services.
- Execute generic [[drools]] predicates.
- Return matching-rule results such as `MatchedRule`.
- Remove legacy and domain-specific processor responsibilities from the central service.

Rule maintenance is expected to include F2E support, logical-model alignment, maker/checker CRUD control, self-service user management, dry-run capability, and more complex rule authoring.

## v1 and migration posture

The archived overview states that v1 should remain unchanged temporarily, be decommissioned in the future, and not be maintained. BCS, CN, and Trade Review are identified as migration scope, but the current migration status is not documented.

This page should not be used as the authoritative API or production-support status for RATAN.
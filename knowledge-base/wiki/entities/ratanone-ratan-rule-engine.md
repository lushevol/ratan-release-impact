---
type: entity
title: ratanone.ratan_rule_engine
created: 2026-08-24
updated: 2026-08-24
tags: [database-table, rule-engine, validation, RATAN, cash-settlement]
related: [cash-settlement-entity-onboarding, entity-level-static-data-consolidation, cash-settlement-platform]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Entity level static.md"]
---
# ratanone.ratan_rule_engine

## Role

`ratanone.ratan_rule_engine` is identified as the existing database static-data location for the Bypass Validation Rule in the Rule Engine domain.

## Planned change

The source states that this configuration will be dropped by new MO validation. It is therefore part of the current onboarding inventory but is not listed as a continuing attribute in the proposed consolidated table.

The source does not define the new MO validation design, its ownership, or the migration and retirement procedure for this table's configuration.

## Onboarding significance

Removing bypass-validation configuration could reduce one onboarding touchpoint, provided that the replacement validation capability is available and covers the same business cases.

The relationship between this table and the broader [[concepts/cash-settlement-entity-onboarding]] process should be confirmed before decommissioning.
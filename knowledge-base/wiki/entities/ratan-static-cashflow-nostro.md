---
type: entity
title: ratanone.ratan_static__cashflow_nostro
created: 2026-08-24
updated: 2026-08-24
tags: [database-table, static-data, Nostro, cash-settlement, RATAN]
related: [cash-settlement-entity-onboarding, entity-level-static-data-consolidation, static-data-service, cash-settlement-platform]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Entity level static.md"]
---
# ratanone.ratan_static__cashflow_nostro

## Role

`ratanone.ratan_static__cashflow_nostro` stores Nostro Static setup for Cash Settlement entity processing. The source identifies it as a mandatory setup for each entity and explicitly excludes it from the proposed consolidated entity-level table.

## Key

The source gives the Nostro Static key as:

- Entity FMID
- Currency
- Settlement Means
- Settlement Method

This key is more specific than an entity-only key because Nostro configuration can vary by currency and settlement attributes.

## Operating characteristics

The source describes Nostro Static setup as self-serviced. It does not define the table schema, ownership, validation rules, effective-date behavior, approval controls, or propagation mechanism.

## Onboarding dependency

Nostro Static is the principal exception to the proposed entity-level consolidation. A complete onboarding workflow must ensure that the central entity configuration and this separate Nostro record are both valid and activated consistently.

This boundary is documented in [[concepts/cash-settlement-entity-onboarding]] and [[concepts/entity-level-static-data-consolidation]].
---
type: concept
title: Entity and Product Onboarding
tags: [onboarding, entity, product, cash-settlement]
related: [cash-settlement-home-page, ratan, onboarding-checklist, static-data-readiness]
created: 2026-08-22
updated: 2026-08-22
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List.md"]
---
# Entity and Product Onboarding

## Definition

Entity and product onboarding is the inferred process of enabling an entity, a product, or an entity-product combination for participation in a cash-settlement platform or operating model.

This concept is derived from the title of [[sources/25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--38-04-onboardingentity-pr--4ep9ae]]. The source body was unavailable, so no detailed lifecycle, prerequisite, ownership, or approval model is established.

## Possible scope

Depending on the terminology used in the original document, “entity product” may refer to:

1. Separate onboarding tracks for entities and products
2. A matrix defining which products are enabled for each entity
3. A named functional capability

The distinction remains unresolved.

## Information required to define the process

A complete operational definition would need to identify:

- In-scope entities, products, currencies, regions, and settlement flows
- Required reference and static data
- Configuration and integration dependencies
- Validation and testing requirements
- Requester, preparer, reviewer, and approver responsibilities
- Production activation and rollback procedures
- Evidence and completion criteria

Potential dependencies may include [[concepts/static-data-readiness]], but the source does not confirm any specific dependency.

## Current evidence boundary

No platform-specific behavior should be inferred from this page. In particular, the available metadata does not establish that onboarding is governed by [[entities/ratan]] or [[entities/cash-settlement-home-page]], nor that it forms part of [[projects/cashflow-migration]] or another migration workstream.

---
type: query
title: Did the 2023 Rule Service Migration and UAT Complete?
created: 2026-08-24
updated: 2026-08-24
tags: [rule-service, migration, uat, archived, open-question]
related: [rule-service, rule-service-migration, static-data-service, csv-to-drools-rule-generation, what-replaced-the-archived-ratan-rule-engine-design, which-drools-version-and-rule-deployment-model-should-be-adopted]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/Rule Service Migration/Rule Service Delivery Plan.md"]/Rule Service Migration/Rule Service Delivery Plan.md"]/Rule Service Migration/Rule Service Delivery Plan.md"]
---
# Did the 2023 Rule Service Migration and UAT Complete?

## Question

Did the planned 24 November 2023 UAT deployment of [[rule-service]] with FX rules occur, did Hawk integration testing pass, and did BAU suppression-rule onboarding, CN-rule onboarding, and the intended [[static-data-service]] migration complete?

## Evidence

The archived delivery plan records FX Replication Rules Development as done by 10 November 2023. It records UAT deployment with FX rules as in progress, not complete. BAU suppression-rule and CN-rule onboarding have end-of-December targets but are marked TBC.

The plan proposes a [[csv-to-drools-rule-generation]] process for BAU rules and states that fields-service functionality and validation rules would move to Static Data Service. It does not include delivery closure, test results, approval records, production deployment evidence, or successor-architecture confirmation.

## Needed evidence

- UAT deployment records, release notes, and environment configuration for the FX rules.
- Hawk integration-test results, defects, and acceptance evidence.
- BAU and CN onboarding completion records, imported-rule inventories, and business sign-off.
- Implementation evidence for the Static Data Service validation migration and a defined service-boundary contract.
- Documentation identifying the successor to the archived Rule Service approach.

This question supports [[what-replaced-the-archived-ratan-rule-engine-design]] and should not be resolved by treating planned dates as completion evidence.
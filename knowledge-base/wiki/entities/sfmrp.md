---
type: entity
title: SFMRP
created: 2026-08-22
updated: 2026-08-22
tags: [sfmrp, regression-suite, test-automation, ratanone]
related: [uber-integration, uber-regression-testing, regression-failure-triage, ratan-one]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Uber Development Testing/UBER regression - round 2.md"]
---
# SFMRP

## Role

SFMRP is the principal regression-test package namespace used in the UBER integration testing record. Most packages ran from the `main` branch and exercised RATANONE cash-settlement capabilities and connected systems.

## Coverage

SFMRP packages covered Murex fixing and trade confirmation, Stella confirmation and undo, SSI and rule-service behavior, bulk processing, auto-netting, Aspire accounting, EBBS, SWIFT, LMS, IMS, cashflow operations, auto jobs, comments, and data entitlement.

## Interpretation of results

SFMRP failure counts are reported as sequences such as `65→18→5`, rather than as a single normalized result. They include initial failures, reruns, stale assertions, test-data defects, environment blockers, and possible implementation defects. SFMRP results should therefore be interpreted using [[concepts/regression-failure-triage]] rather than treating every failed assertion as a product defect.
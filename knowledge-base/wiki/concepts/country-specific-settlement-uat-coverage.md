---
type: concept
title: Country-Specific Settlement UAT Coverage
created: 2026-08-23
updated: 2026-08-23
tags: [uat, settlement, country-coverage, ratan, fmsgw, risk-based-testing]
related: [manual-entity-settlement-onboarding, ratan, fmsgw, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requir--1u0fes]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing.md"]
---
# Country-Specific Settlement UAT Coverage

Country-specific settlement UAT coverage is a targeted testing model in which planned test scope varies by country or branch rather than applying a common test suite to all onboarding locations.

For manual-entity onboarding, the source records separate planned case counts for [[ratan]] and [[fmsgw]]. The stated focus is changes specific to onboarding, especially SWIFT generation and accounting generation, supplemented by generic cases for country operations confidence.

## Interpretation limits

Planned case counts do not demonstrate execution, quality, functional correctness, or operational readiness. The available source does not document the risk rationale for the varying country counts, individual scenarios, expected results, execution status, defects, or approvals.

A zero count can also be a scope exclusion rather than a successful test result. In the documented matrix, Slate One has zero RATAN and FMSGW cases because it is not configured for downstream handling. Colombo FCB has unresolved counts and therefore has incomplete coverage planning.
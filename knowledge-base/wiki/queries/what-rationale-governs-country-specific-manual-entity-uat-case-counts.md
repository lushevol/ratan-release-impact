---
type: query
title: What Rationale Governs Country-Specific Manual-Entity UAT Case Counts?
created: 2026-08-23
updated: 2026-08-23
tags: [uat, risk-based-testing, country-coverage, manual-entities, settlement]
related: [country-specific-settlement-uat-coverage, manual-entity-settlement-onboarding, ratan, fmsgw, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requir--1u0fes]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing.md"]
---
# What Rationale Governs Country-Specific Manual-Entity UAT Case Counts?

The UAT plan explicitly varies coverage across countries and branches, but it does not provide traceability from country risk to planned RATAN and FMSGW case counts.

Required evidence:

- Risk assessment or requirement traceability supporting each country and branch count.
- Minimum mandatory coverage for SWIFT generation and accounting generation.
- Treatment of static data, downstream routing, operational access, exceptions, reconciliation, cut-offs, and regulatory requirements.
- Justification for differences such as Zambia's 13 RATAN cases, Colombo's 36 cases, and the 11-case FMSGW plans for Tanzani and Bangladesh.
- Confirmation that GBS user familiarity does not substitute for jurisdiction-specific functional and configuration validation.

The source establishes planned variation, but not the governance basis or adequacy of that variation.
---
type: concept
title: Manual-Entity Settlement Onboarding
created: 2026-08-22
updated: 2026-08-23
tags: [settlement-day-2, onboarding, manual-entities, operational-readiness, settlement, ratan, uat]
related: [settlement-day-2, ratan, entity-routing-and-cashflow-suppression, swift-entity-configuration, ssi-stamping-hierarchy, nostro-static, business-rule-maintenance, fmrp, fmsgw, country-specific-settlement-uat-coverage, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requir--1u0fes]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/00 Manual Entities Onboarding Checklist.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing.md"]
---
# Manual-Entity Settlement Onboarding

Manual-entity settlement onboarding is the controlled preparation of a new entity for Settlement Day 2 processing in the Cash Settlement/[[ratan]] environment. It enables manually handled entities to use the established settlement-processing workflow in [[ratan]] that is already used in other markets.

## Scope and testing boundary

The UAT-testing source treats the existing core workflow as pre-established and concentrates validation on changes introduced by onboarding. Its named priority areas are:

- SWIFT generation.
- Accounting generation.

Separate planned coverage is recorded for [[ratan]] and [[fmsgw]].

This concept does not establish that the existing workflow is suitable or fully certified for every newly onboarded jurisdiction. It describes the intended onboarding and testing scope recorded in [[25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requir--1u0fes]]. Country-level test coverage is intentionally variable; see [[country-specific-settlement-uat-coverage]].

## Readiness domains

The onboarding checklist identifies the following domains for assessment before enablement:

- Entity routing, LMS feed participation, cashflow suppression, and downstream handling.
- Per-entity SWIFT identifiers and message-field mappings.
- Currency release times, currency mappings, and special-currency rounding where applicable.
- Bridge-account, EBBS, and other settlement-accounting configuration.
- Nostro and Vostro static setup, including branch-specific SSI for over-account clients.
- Business-rule and netting-static review.
- Network access, downstream analysis, UAT, regression testing, and a possible CPT stage.

## Ownership guidance

The onboarding checklist assigns:

- Lower-volume Nostro setup, Vostro static setup, and business-rule setup to [[data-ops]].
- High-volume Nostro work to the Dev Team through a Change Request.
- UAT ownership to [[settlement-ops]].
- Regression testing and firewall work to the Dev Team.

These assignments are operational guidance, not a complete RACI. The checklist gives no approval authority, readiness criteria, due dates, or definition of high volume.

## Historical exclusions

The onboarding checklist regards bypass validation and Murex-only H2 Adaptor batch-list configuration as retired under the New MO Validation Model and [[fmrp]]. They should not be reintroduced as active onboarding requirements without confirming the current process.
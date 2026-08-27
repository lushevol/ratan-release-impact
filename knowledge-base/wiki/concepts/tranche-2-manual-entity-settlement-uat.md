---
type: concept
title: Tranche 2 Manual-Entity Settlement UAT
created: 2026-08-23
updated: 2026-08-23
tags: [uat, settlement, manual-entities, tranche-2, test-coverage]
related: [manual-entity-settlement-enablement, manual-entity-settlement-onboarding, country-specific-settlement-uat-coverage, manual-entity-swift-mx-bifurcation, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requi--1kxkozl]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/UAT testing checking-Tranche2.md"]
---
# Tranche 2 Manual-Entity Settlement UAT

Tranche 2 Manual-Entity Settlement UAT is the country- and entity-specific validation of settlement-message scenarios for manually enabled entities. The tracking sheet covers BH, QA, NG, GH, and UG, with a related configuration question for QATAR SLATE ONE LLC*DOH.

## Coverage Dimensions

Coverage is organized around:

- SWIFT scenarios including MT103, MT202, MT202COV, and MT210.
- Internal MX and external MX routing variants.
- MT202Flip variants.
- Withdrawal and cancellation flows.
- DVP NSTP exception handling.
- Netting.
- Split cashflows and Withholding TAX/WHT NSTP behavior.

The presence of a scenario or cashflow ID indicates tracking scope, not verified execution or acceptance.

## Evidence Standard

A complete UAT record should identify the expected result, actual result, cashflow or message trace, test report, relevant queue or service evidence, and defect or approval reference where applicable. The source does not meet this standard consistently because its `Test Report` column is blank and many rows contain only scenario names and IDs.

## Current Risks

The tracker records repeated MT210 non-generation observations for BH, NG, and UG. It also records incomplete MX cancellation and MT202Flip-MX coverage for BH, QA, and NG, an unresolved BH-BH RTGS test, a questionable GH DVP-exception pass, an unresolved QATAR SLATE ONE LLC*DOH suppression-verification question, and an unclear UG WHT NSTP expectation.

These findings should be kept attached to their specific entity and scenario. They do not establish a general release status for all manual entities.
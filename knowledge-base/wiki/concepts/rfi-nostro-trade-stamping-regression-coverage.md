---
type: concept
title: RFI Nostro Trade Stamping Regression Coverage
created: 2026-08-23
updated: 2026-08-23
tags: [uat, regression-testing, rfi-nostro, trade-stamping, test-coverage]
related: [portfolio-based-rfi-nostro-stamping, nostro-stamping, rfi-nostro-account, what-is-the-authoritative-rfi-nostro-lookup-and-duplicate-rule, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requi--1w2mf91]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/RFI Nostro stamping based on Portfolio/RFI Nostro stamping based on Portfolio - UAT/RFI Nostro Trade Stamping Regression.md"]
---
# RFI Nostro Trade Stamping Regression Coverage

RFI Nostro trade stamping regression coverage tests whether [[portfolio-based-rfi-nostro-stamping]] is exercised for each in-scope product under normal, unresolved, and ambiguous matching conditions.

## Covered Dimensions

The UAT regression matrix covers four products:

- IRS
- fixing
- forward
- swap

Each product is paired with the following matching conditions:

- **Missing Nostro:** no eligible or returned Nostro match is available in the test setup.
- **Best-match Nostro:** one candidate is treated as the preferred match.
- **Multi-match Nostro:** more than one candidate satisfies the matching condition.

This produces 12 substantive test scenarios.

## Interpretation

The matrix demonstrates scenario execution coverage rather than confirmed behavior. Screenshot evidence alone must not be used to conclude that a Nostro was stamped, that the selected account was correct, or that all scenarios passed.

The required selection and duplicate-handling rules remain under investigation in [[what-is-the-authoritative-rfi-nostro-lookup-and-duplicate-rule]]. Any eventual validation should identify the expected and observed outcomes for all product-and-condition combinations.
---
type: concept
title: UAT Test Case
created: 2026-08-23
updated: 2026-08-23
tags: [uat, testing, test-data, settlement]
related: [cashflow-auto-netting, cashflow-identifier, settlement-day2-requirement]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Cashflow Auto Netting UAT testing sample.md"]
---
# UAT Test Case

A UAT test case is a concrete production-like record used by business testers to validate system behavior. In the Cashflow Auto Netting sample, each case is represented primarily by a booking-entity FMCODE, a counterparty FMCODE, and a cashflow identifier.

The source contains 184 test records grouped into six named cohorts. It is a test-data inventory, not a test execution report: no expected outcome, observed outcome, pass/fail status, or defect reference is included.

## Required execution context

To turn the inventory into executable UAT coverage, each identifier would need an expected netting result and the fields that determine eligibility and grouping. The sample does not provide currency, value date, amount, debit or credit direction, product, account, settlement status, or netting key.

The complete population is preserved in [[sources/25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requir--1p3a3x|Cashflow Auto Netting UAT Testing Sample]].
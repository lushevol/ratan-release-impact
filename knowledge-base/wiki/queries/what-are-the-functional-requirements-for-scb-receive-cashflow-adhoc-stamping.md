---
type: query
title: What Are the Functional Requirements for SCB Receive Cashflow Adhoc Stamping?
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, scb, receive-cashflow, adhoc-stamping, requirements]
related: [25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requi--1bvzw6b, cash-settlement-home-page, nostro-stamping, dedicated-nostro-stamping, ssi-stamping-behavior-differences]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/SCB Receive Cashflow Stamping/Cashflow Adhoc Stamping.md"]
---
# What Are the Functional Requirements for SCB Receive Cashflow Adhoc Stamping?

## Status

Open. The source file is available as a path reference, but its document body was not supplied for analysis.

## Question

What are the authoritative functional requirements for ad hoc stamping of SCB receive cashflows?

## Evidence currently available

Only the folder hierarchy and filename are known. They indicate a likely relationship to [[cash-settlement-home-page]] and Settlement Day 2 requirements, but they do not establish the exact stamping type, applicable SCB entity, eligible cashflow population, or downstream behavior.

## Information required

The original document should be obtained, including embedded images, tables, API examples, and acceptance criteria. The review should identify:

1. The precise SCB entity, branch, booking location, and product scope.
2. The exact fields or settlement attributes applied by stamping.
3. The authoritative trigger and eligible cashflow states.
4. The UI, API, or service responsible for the action.
5. Authorization, maker/checker, audit, override, and rollback controls.
6. Validation, error, idempotency, and re-stamping behavior.
7. Effects on SWIFT, LMS, reconciliation, settlement-accounting, and downstream settlement processing.
8. Differences between receive-side and payment-side behavior.

## Scope caution

Do not infer that this requirement is equivalent to [[nostro-stamping]], [[dedicated-nostro-stamping]], or [[ssi-stamping-behavior-differences]] until the source content confirms the relationship.
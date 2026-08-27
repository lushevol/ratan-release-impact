---
type: query
title: How Are Payment Dates Compared for Bulk Cashflow Validation?
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, bulk-processing, payment-date, timezone, validation, open-question]
related: [bulk-cashflow-selection-homogeneity, payment-date-override, what-is-the-authoritative-timezone-rule-for-cash-settlement-datetime-fields]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Multi Exceptions/Bulk Process for Multi Exceptions/Bulk UI Technical Design.md"]
---
# How Are Payment Dates Compared for Bulk Cashflow Validation?

## Question

What is the authoritative comparison rule for `Payment Date` when validating that all cashflows selected for a bulk action have the same date?

## Evidence

The design requires identical `Payment Date` values for both **Bulk Submit** and **Bulk Approve**. It does not specify whether comparison uses the stored timestamp, a normalized date, the displayed date, UTC, or a business-local timezone.

## Required Clarification

Specify:

- The canonical source field and data type.
- The timezone or business-calendar basis.
- Whether comparison is date-only or datetime-sensitive.
- How null, invalid, or overridden dates are handled.
- Whether the UI and backend use the same normalization rule.

This question should be resolved consistently with [[queries/what-is-the-authoritative-timezone-rule-for-cash-settlement-datetime-fields]].
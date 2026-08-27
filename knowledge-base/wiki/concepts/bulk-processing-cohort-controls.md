---
type: concept
title: Bulk Processing Cohort Controls
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, bulk-processing, operational-risk, validation, cohort]
related: [bulk-cashflow-exception-processing, cashflow-bulk-eligibility, cashflow-blotter]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Multi Exceptions/Bulk Processing for Multi Exception Demo.md"]
---
# Bulk Processing Cohort Controls

Bulk processing cohort controls restrict a bulk selection to cashflows that share the same Value Date, Booking Entity, and Counterparty. The source presents this three-attribute restriction as a safeguard against manual operational error.

## Expected Behavior

A user selects cashflows in the [[cashflow-blotter]] and invokes Bulk Submit. A cohort with matching Value Date, Booking Entity, and Counterparty is expected to expose the Bulk Submit action. If a cashflow with a different Booking Entity is added while the Counterparty and Value Date remain the same, the action remains visible but an alert is expected after it is clicked.

## Coverage Limitation

The planned demo tests only a different-entity selection. It does not independently test a different Counterparty or different Value Date, despite both being mandatory cohort attributes.

This is a processing-safety control, not a blotter filter or view-ordering rule. It operates alongside [[cashflow-bulk-eligibility]], which determines whether the exceptions on a selected item permit bulk processing.
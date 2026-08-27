---
type: concept
title: Pending Affirmation Bulk Processing
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, pending-affirmation, bulk-processing, maker-checker, data-capture]
related: [bulk-cashflow-exception-processing, cashflow-bulk-eligibility, what-are-the-required-affirmation-fields-and-validation-rules-for-pending-affirmation-cashflows]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Multi Exceptions/Bulk Processing for Multi Exception Demo.md"]
---
# Pending Affirmation Bulk Processing

`Pending Affirmation` is listed as bulk eligible for RATAN ONE exception processing. When a selected eligible cashflow carries this exception, the user must manually enter affirmation details before processing.

## Scope of Entered Data

Affirmation details are intended to apply only to selected cashflows with `Pending Affirmation`; they must not be applied indiscriminately to other cashflows in the bulk selection.

The planned approval demo further expects maker-entered affirmation data to remain associated only with the cashflows used in the earlier maker submission.

## Fallback

A remaining `Pending Affirmation` cashflow can be processed through single submit with different affirmation information. The source does not establish whether every bulk-ineligible exception has an equivalent single-processing path.

## Undefined Requirements

The requirement does not specify the affirmation fields, requiredness, validation, persistence model, audit trail, mixed-selection behavior, or whether a checker can amend maker-entered values. It also does not establish that `Pending Affirmation` is equivalent to [[pending-trade-validation-investigation]].
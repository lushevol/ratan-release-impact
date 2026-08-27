---
type: query
title: What Is the Authoritative Bulk Manual Fail Error and Validation Contract?
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, bulk-fail, validation, user-interface, open-question]
related: [bulk-cashflow-manual-fail, cashflow-manual-fail-maker-checker, cash-settlement-home-page]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Bulk Fail.md"]
---
# What Is the Authoritative Bulk Manual Fail Error and Validation Contract?

## Question

What exact validation and error behavior governs Bulk Fail in the Cash Settlement Home Page?

## Known rule

A user may select up to 1,000 cashflows. Selecting more than 1,000 must display an error message. The source references screenshots but does not include the exact message text in the document body.

## Additional gaps

The requirement does not define the behavior when:

- A selected cashflow changes status after selection.
- A selected cashflow becomes `Pending Manual Fail` before submission.
- A suppressed cashflow no longer satisfies `Current Date > Payment Date`.
- The maker comment is empty or invalid.
- The checker comment is empty or invalid.
- The request contains mixed eligible and ineligible cashflows.
- A bulk submission or approval partially fails.

## Required decision

The team should establish a canonical validation contract covering message text, validation timing, mixed-selection handling, stale selections, retry behavior, and user-visible partial failures.

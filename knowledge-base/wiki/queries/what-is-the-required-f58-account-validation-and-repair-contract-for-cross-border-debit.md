---
type: query
title: What Is the Required F58 Account Validation and Repair Contract for Cross-Border Debit?
created: 2026-08-23
updated: 2026-08-23
tags: [cross-border-debit, swift, f58, validation, exception-handling, payment-generation]
related: [cross-border-debit-settlement, cross-border-debit-message-mapping]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cross Border Debit/Cross Border Debit UAT.md"]
---
# What Is the Required F58 Account Validation and Repair Contract for Cross-Border Debit?

A EUR receive-side UAT case found that payment generation was not allowed when the F58 account number was missing, and the user was required to reprocess the cashflow.

The source does not define the required F58 format, validation point, error code, resulting cashflow status, repair permissions, or whether downstream message submission is fully suppressed.

## Evidence Needed

- The canonical field-58 validation rule and mandatory-account criteria.
- API or UI error messages and status-transition behavior.
- The approved repair and reprocessing procedure.
- Negative-path evidence for duplicate submissions, correction after release, and downstream delivery failures.
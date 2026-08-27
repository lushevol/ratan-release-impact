---
type: query
title: What Is the Authoritative Bulk Cashflow Eligibility Evaluation and Revalidation Rule?
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, bulk-processing, eligibility, revalidation, business-rules]
related: [cashflow-bulk-eligibility, bulk-cashflow-exception-processing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Multi Exceptions/Bulk Processing for Multi Exception Demo.md"]
---
# What Is the Authoritative Bulk Cashflow Eligibility Evaluation and Revalidation Rule?

The requirement says the bulk preview compares cashflow exceptions with the latest rule configuration. It does not say whether the system repeats that evaluation immediately before execution.

## Questions

- Is eligibility evaluated only when the preview opens, or again on submit, approve, and reject?
- Which configuration version and timestamp are recorded with the operation?
- What occurs if `FMO_BR_APR` or `FMO_BR_MKR` configuration changes after preview and before confirmation?
- Does the all-exceptions rule apply to a payment, a cashflow, or both?
- What user-visible result is produced when an item becomes ineligible after preview?

This question draws on [[cashflow-bulk-eligibility]] and the source requirement.
---
type: concept
title: Cashflow Bulk Eligibility
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, bulk-processing, eligibility, nstp, business-rules]
related: [bulk-cashflow-exception-processing, pending-affirmation-bulk-processing, is-the-bulk-exception-eligibility-catalogue-case-sensitive-and-deduplicated, what-is-the-authoritative-bulk-cashflow-eligibility-evaluation-and-revalidation-rule]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Multi Exceptions/Bulk Processing for Multi Exception Demo.md"]
---
# Cashflow Bulk Eligibility

Cashflow bulk eligibility is the configurable decision that determines whether a cashflow can participate in a RATAN ONE bulk exception operation.

## Rule

The source defines an all-exceptions rule: if a payment contains any exception configured as not bulk eligible, that payment is not eligible for bulk processing. The source uses both “payment” and “cashflow” without defining whether they are the same processing object or how they relate.

Eligibility configuration is maintained through business-rule profiles `FMO_BR_APR` and `FMO_BR_MKR`. At preview time, the system is intended to compare cashflow exceptions with the latest rule configuration and divide results into eligible and not eligible sections.

## Exception Catalogue

The authoritative catalogue currently available in this source is preserved in [[sources/25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--16-multi-exceptions--40--1fhoub0]]. It explicitly permits `Pending Affirmation` and excludes, among other labels, `DVP`, `Manual Deliver`, `Reversal`, `reversal`, `Murex STP_HOLD`, and `Multi SSI`.

Until the reference-data contract is confirmed, exception labels should be treated as source-provided values rather than normalized names.

## Open Control Gap

The requirement specifies use of the latest rule configuration when the preview opens, but it does not establish whether eligibility is validated again when the user confirms submit or approve. The unresolved execution-time control is tracked in [[what-is-the-authoritative-bulk-cashflow-eligibility-evaluation-and-revalidation-rule]].
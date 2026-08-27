---
type: query
title: Is the Bulk Exception Eligibility Catalogue Case-Sensitive and Deduplicated?
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, bulk-processing, eligibility, reference-data, exception-catalogue]
related: [cashflow-bulk-eligibility]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Multi Exceptions/Bulk Processing for Multi Exception Demo.md"]
---
# Is the Bulk Exception Eligibility Catalogue Case-Sensitive and Deduplicated?

The source's not-allowed catalogue contains both `Reversal` and `reversal`, as well as two entries for `Rebook`. It is unclear whether these are distinct case-sensitive exception identifiers, duplicate configuration values, or inconsistent display labels.

## Questions

- Are exception values evaluated as exact case-sensitive codes or normalized display names?
- Do `Reversal` and `reversal` represent different exceptions?
- Why does `Rebook` appear twice?
- What system owns the canonical exception catalogue?
- How are duplicate, retired, renamed, or unmapped exceptions governed in `FMO_BR_APR` and `FMO_BR_MKR`?

Until resolved, the catalogue should be preserved exactly as recorded in [[cashflow-bulk-eligibility]].
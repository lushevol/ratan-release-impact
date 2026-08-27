---
type: query
title: What Request Info Is Required for Split Cashflow Accounting Tasks?
tags: [accounting, request-info, ratan, cashflow-splitting, validation]
related: [accounting-request-info-attachment, cashflow-splitting, ratan]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting/Cashflow Splitting UAT/Cashflow Splitting UAT For ASPIRE.md"]
---
# What Request Info Is Required for Split Cashflow Accounting Tasks?

The UAT record supplies an SQL query that selects `request_info` from `ratan_cash_accounting_service.ratan_accounting_request_task`. It supplies neither returned data nor an acceptance rule.

## Questions to resolve

- Is `request_info` mandatory for every split-child accounting task?
- What schema, format, and required fields does it have?
- Which service creates and owns the payload?
- Is the attachment produced per child event, parent event, or accounting-task batch?
- How are business version and minor version represented in the attachment?
- Why does the query use a separate `S00000049998`–`S00000050023` data set rather than the UAT matrix IDs?
- What validation and audit evidence establishes that the attachment is correct?

## Evidence

[[25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requir--6za5lq]] establishes only that this table and field were intended for inspection during or alongside UAT.
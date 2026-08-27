---
type: concept
title: Accounting Request Info Attachment
tags: [accounting, request-info, ratan, cashflow, database]
related: [ratan, cashflow-splitting, what-request-info-is-required-for-split-cashflow-accounting-tasks]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting/Cashflow Splitting UAT/Cashflow Splitting UAT For ASPIRE.md"]
---
# Accounting Request Info Attachment

`request_info` is a field selected from the RATAN accounting-request task table in an ASPIRE cashflow-splitting UAT inspection query.

## Observed inspection target

The source queries:

```text
ratan_cash_accounting_service.ratan_accounting_request_task
```

alongside cashflow identity, version, payment, trade, country, entity, counterparty, external-system-key, and currency fields.

The query targets eight `S...` cashflow IDs in the `S00000049998`–`S00000050023` range. These IDs differ from the `S000000516xx` child cashflows in the documented UAT scenario matrix.

## Evidence boundary

No returned records, schema definition, API contract, or expected `request_info` payload is provided. The source therefore does not establish that an attachment was present, valid, complete, or linked to a particular split-child action.

Required payload content, producer, validation, and per-event versus per-task behavior remain open in [[what-request-info-is-required-for-split-cashflow-accounting-tasks]].
---
type: concept
title: RATAN Accounting Reconciliation API
created: 2026-08-23
updated: 2026-08-23
tags: [RATAN, API, accounting, reconciliation, korea, query, task-history]
related: [ratan, tlm, korea-accounting-reconciliation, accounting-posting-statuses, ebbs-accounting-message-mapping]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Payment Accounting/Cash Settlement - Korea Accounting Recon - RATAN- TLM.md"]
---
# RATAN Accounting Reconciliation API

The RATAN Accounting Reconciliation API is a proposed GET interface for retrieving Korea accounting records for [[tlm]].

## Endpoint and constraints

The example endpoint is:

```text
GET /v1/accounting/queryReconRecords/
```

The API is intended to accept `startReleaseTime`, `endReleaseTime`, and `fmidList`. Only FMID `10036645` is supported by the stated Korea business agreement. The longest permitted interval is three days.

The intended selection predicates are:

```sql
ratan_accounting_request_task_history.task_status = 'SENT'
ratan_accounting_request_task_history.created_at > startReleaseTime
ratan_accounting_request_task_history.booking_entity_fmid in fmidList
ratan_accounting_request_task_history.created_at <= endReleaseTime
```

The source calls the parameters release times but applies predicates to task-history `created_at`. It also says that date-times must be converted to GMT.

## Response

The response contains `totalNumberOfRecords` and `accountingRecords`. Each record includes a `publishTimestamp` and a posting message with source system `RATAN`, posting type `FundsTransfer`, and transaction type `RTN`.

The message is populated using [[ebbs-accounting-message-mapping]]. It includes a cashflow-derived external-system key, transaction currency and amount, value date, account information, transaction code, debit/credit direction, and narratives.

## Operational limitations

The requirement does not resolve:

- whether task status and accounting response status are separate fields;
- whether the time boundary represents release time or task creation time;
- whether input uses a space or `T` separator;
- whether timestamps are local, GMT, or UTC with an explicit offset;
- whether `casa-currency-code` should be `USD`, the transaction currency, or another value;
- which transaction entry is the Nostro leg and which is the bridge leg; or
- how pagination, retries, authentication, and error responses work.

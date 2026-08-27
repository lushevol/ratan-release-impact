---
type: concept
title: Accounting Posting Statuses
created: 2026-08-23
updated: 2026-08-23
tags: [accounting, status, OLTP, RATAN, acknowledgement, reconciliation]
related: [ratan, oltp, tlm, korea-accounting-reconciliation, ratan-accounting-reconciliation-api]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Payment Accounting/Cash Settlement - Korea Accounting Recon - RATAN- TLM.md"]
---
# Accounting Posting Statuses

The source defines six accounting statuses for RATAN-generated postings.

| Status | Meaning |
|---|---|
| `HOLD` | The accounting entry is generated before the cashflow reaches value date and remains held. |
| `MISSING_INFO` | Mandatory information is unavailable. The source includes `SWIFT_SUPPRESSED` with no available Nostro as an example. RATAN may not generate the entry. |
| `DISABLED` | The entry is generated but is not sent to OLTP, including settlement account `UIDD/UISUS` with settlement method `NOX`. |
| `SUCCESS` | The entry is sent to OLTP and receives a `SUCCESS` response. |
| `SENT` | The entry is sent to OLTP and has not received a response. |
| `REJECTED` | The entry is sent to OLTP and receives a `REJECTED` response. |

## API exposure

The Korea reconciliation requirement explicitly states that `SUCCESS`, `SENT`, and `REJECTED` accounting statuses respond to TLM. It does not state that `HOLD`, `MISSING_INFO`, or `DISABLED` are returned by the API.

There is an unresolved distinction between the API's stated response statuses and the implicit filter:

```sql
ratan_accounting_request_task_history.task_status = 'SENT'
```

A separate task status and accounting response status may be intended, but the source does not define that relationship.
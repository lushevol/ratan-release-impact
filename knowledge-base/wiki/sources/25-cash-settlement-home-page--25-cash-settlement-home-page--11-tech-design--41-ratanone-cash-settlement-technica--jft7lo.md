---
type: source
title: Settlement Accounting for Aspire Tech Design
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, accounting, aspire, ebbs, file-delivery, technical-design, proposal]
related: [aspire, ebbs, fileit, control-m, accounting-aspire-execution, value-date-accounting-feed-cutoff, accounting-feed-file-generation-idempotency, accounting-feed-withdrawal-as-reversal, accounting-file-delivery-acknowledgement, country-local-time-accounting-batch-scheduling]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Settlement Accounting for Aspire Tech design.md"]
authors: []
year: 2026
url: ""
venue: "Internal technical design"
---
# Settlement Accounting for Aspire Tech Design

## Summary

This design proposal describes an intended RATANONE Cash Settlement accounting-feed process for Aspire and/or EBBS. Feed work is proposed to be event-driven, while file publication is deferred until cashflow value-date eligibility and executed by country-local scheduled jobs.

The document is design-level evidence only. It provides no approved DDL, API definitions, event contracts, test evidence, or production confirmation.

## Proposed principles

1. Generate EBBS feeds event-driven.
2. Use value date as the publication cutoff:
   - Hold work when the value date has not arrived.
   - Publish eligible work in a batch file when the value date has arrived by 22:05 local time.
3. Represent withdrawal as a reversal-direction transaction of the original `New` record rather than as a wholly new feed type.

## Proposed Control-M operation

The proposal assigns [[control-m]] a 30-minute job schedule from 22:05 to 02:05 local time. The job selects tasks where payment date is no later than the current date and `create_time` is before 22:00 on the current date. It is intended to generate one file per workday job.

An empty-file job is proposed for 03:30 local time.

## HK scenario walkthrough

The source provides this proposed sequence for HK:

```text
1. current GMT time (2022-02-2014:05:00 GMT)→ 2025-02-2022:05:00 (Local)
2. find latest asOfDate by HK from accounting_aspire_execution table 1. exist 2025-02-19record
3. then get the task list and generate 2 transaction records for each task 1. country = HK and systemDate = 2025-02-20
4. create HK_20250220_01.csv and write above transaction records in this file
5. call lifecycle for each cashflow status update
6. call FileIT to copy the file 1. insert execution table : HK; 2025-02-20; SENT; and update task table filename = HK_20250220_01.csv in above task id
7. receive response from fileIT 1. update execution table response_code = 2000 , response_desc = SUCCESS which record is country = HK and asOfDate = 2025-02-20 and file_sent = SENT
8. job complete
```

The illustrated timestamps are malformed and must not be treated as an authoritative time-zone conversion contract. The generic lifecycle call does not establish that [[ratan-cashflow-lifecycle-service]] owns the endpoint.

## Business scenarios

| Scenario | Cashflow info | Current Time | external_system_key | action | task_status | Filename / job behavior | execution id | country | as_of_date | file_sent | reason |
|---:|---|---|---|---|---|---|---:|---|---|---|---|
| 1 | cf1 - 20250220 | 20250220 09:00 (local) 20250220 01:00 (GMT) | cf1.0.3 | Fail/SwiftSuppress | HOLD/MISSING_INFO |  | 1 | HK | 20250219 | ACKED | SUCCESS |
| 1 | cf1 - 20250220 | 20250220 11:00 (local) 20250220 03:00 (GMT) | cf1.0.3 | Reinstate/UnSwiftSuppress | DISABLED |  | 1 | HK | 20250219 | ACKED | SUCCESS |
| 1 | cf1 - 20250220 | 20250220 22:00 (local) 20250220 14:00 (GMT) |  |  |  | RATAN_PAYMENT_TRANSACTION_HK_20250220_01.csv | 2 | HK | 20250220 | SENT |  |
| 1 | cf1 - 20250220 | 20250220 22:02 (local) 20250220 14:02 (GMT) |  |  |  |  | 2 | HK | 20250220 | ACKED | SUCCESS |
| 1 | cf1 - 20250220 | 20250220 22:30 (local) 20250220 14:30 (GMT) |  |  |  | RATAN_PAYMENT_TRANSACTION_HK_20250220_01.csv existed , so this job will skip | 2 | HK | 20250220 | ACKED | SUCCESS |
| 2 | cf2 - 20250220 | 20250220 09:00 (local) 20250220 01:00 (GMT) | cf2.0.3 | Release/Fail/SwiftSuppress | HOLD |  | 1 | HK | 20250219 | ACKED | SUCCESS |
| 2 | cf2 - 20250220 | 20250220 22:00 (local) 20250220 14:00 (GMT) | cf2.0.3 |  | SUCCESS | RATAN_PAYMENT_TRANSACTION_HK_20250220_01.csv | 2 | HK | 20250220 | SENT |  |
| 2 | cf2 - 20250220 | 20250220 22:02 (local) 20250220 14:02 (GMT) |  |  |  |  | 2 | HK | 20250220 | ACKED/NACK | SUCCESS/Invalid Request |
| 3 | cf3 - 20250220 | 20250220 22:05 (local) 20250220 14:05(GMT) | cf3.0.3 | Release/Fail/SwiftSuppress | HOLD |  | 2 | HK | 20250220 | ACKED | SUCCESS |
| 3 | cf3 - 20250220 | 20250221 22:00 (local) 20250221 14:00 (GMT) | cf3.0.3 |  | SUCCESS | RATAN_PAYMENT_TRANSACTION_HK_20250221_01.csv | 3 | HK | 20250221 | SENT |  |
| 3 | cf3 - 20250220 | 20250221 22:02 (local) 20250221 14:02 (GMT) |  |  |  |  | 3 | HK | 20250221 | ACKED/NACK | SUCCESS/Invalid Request |
| 4 | cf4 - 20250220 | 20250220 09:00 (local) 20250220 01:00 (GMT) | cf4.0.3 | Release/Fail/SwiftSuppress | MISS_INFO |  | 1 | HK | 20250219 | ACKED | SUCCESS |
| 4 | cf4 - 20250220 | 20250220 11:00 (local) 20250220 03:00 (GMT) | cf4.0.3 | NostroStamped | DISABLED |  | 1 | HK | 20250219 | ACKED | SUCCESS |
| 4 | cf4 - 20250220 | 20250220 11:01 (local) 20250220 03:01 (GMT) | cf4.0.4 | NostroStamped | HOLD |  | 1 | HK | 20250219 | ACKED | SUCCESS |
| 4 | cf4 - 20250220 | 20250220 22:00 (local) 20250220 14:00 (GMT) | cf4.0.4 |  | SUCCESS | RATAN_PAYMENT_TRANSACTION_HK_20250220_01.csv | 2 | HK | 20250220 | SENT |  |
| 4 | cf4 - 20250220 | 20250220 22:02 (local) 20250220 14:02 (GMT) |  |  |  |  | 2 | HK | 20250220 | ACKED/NACK | SUCCESS/Invalid Request |
| 5 | cf5 - 20250220 | 20250220 09:00 (local) 20250220 01:00 (GMT) | cf5.0.3 | Release/Fail/SwiftSuppress | HOLD |  | 1 | HK | 20250219 | ACKED | SUCCESS |
| 5 | cf5 - 20250220 | 20250220 22:00 (local) 20250220 14:00 (GMT) |  |  | HOLD | RATAN_PAYMENT_TRANSACTION_HK_20250220_01.csv generate fail | 1 | HK | 20250219 | ACKED | SUCCESS |
| 5 | cf5 - 20250220 | 20250220 22:30(local) 20250220 14:30(GMT) |  |  | SUCCESS | RATAN_PAYMENT_TRANSACTION_HK_20250220_01.csv regenerate | 2 | HK | 20250220 | SENT |  |
| 5 | cf5 - 20250220 | 20250220 22:32(local) 20250220 14:32(GMT) |  |  |  |  | 2 | HK | 20250220 | ACKED | SUCCESS |

## Open design issues

- The document does not resolve whether [[aspire]] and [[ebbs]] are distinct targets, labels for one integration, or a system and channel respectively.
- It explicitly leaves open whether Aspire and EBBS feed data need two database columns or one shared column.
- No task-table name, DDL, uniqueness constraint, or formal task transition matrix is supplied.
- `MISSING_INFO` and `MISS_INFO` are both used without clarification.
- The source uses both `RATAN_PAYMENT_TRANSACTION_HK_20250220_01.csv` and `HK_20250220_01.csv`; no canonical filename is established.
- “Two transaction records for each task” is not defined.
- The FileIT submission, acknowledgement, NACK, timeout, and retry contract is absent.
- Lifecycle status is updated before FileIT acknowledgement in the proposed sequence, without a compensating procedure for transfer failure.
- Only HK is illustrated; business calendars, holidays, weekends, and other time zones are unspecified.

See [[are-aspire-and-ebbs-distinct-accounting-targets-or-names-for-one-feed]], [[what-is-the-authoritative-aspire-ebbs-feed-task-and-execution-schema]], and [[what-is-the-canonical-aspire-accounting-file-naming-and-uniqueness-key]].
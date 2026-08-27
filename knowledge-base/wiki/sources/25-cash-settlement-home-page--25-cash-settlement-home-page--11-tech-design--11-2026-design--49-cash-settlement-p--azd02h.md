---
type: source
title: Time Fields Summary — Indonesia
authors: []
year: 2026
url: ""
venue: Internal technical design
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, indonesia, cash-settlement, timestamps, utc, audit]
related: [ratan-indonesia-time-zone-contract, timestamp-semantic-and-format-consistency, does-idns-time-to-utc-incorrectly-reinterpret-z-suffixed-utc-timestamps, what-is-the-canonical-indonesia-cash-settlement-timestamp-contract, how-should-gdc-bic-netting-history-timestamps-be-interpreted-in-indonesia]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/UTC Time zone impact - Indonesia/Time Fields Summary.md"]
---
# Time Fields Summary — Indonesia

This technical-design inventory records time-bearing fields across the Indonesia Cash Settlement Platform. It labels fields as either UTC Time or Local Time, identifies UI and backend-audit use, and documents the UI's `IdnsTimeToUtc` behavior.

The inventory establishes a mixed time model. In particular, several values classified as Local Time are serialized with `Z` or `+00:00`, while the documented UI conversion treats a trailing `Z` as an Indonesia-local clock value and subtracts seven hours.

## Time-field inventory

| Service | Field Name | Display in UI | Audit fields in Backend | Upstream Field | Time Zone | Comments | API Response Value | UI Snapshot |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ratan-exception-platform | ExceptionTime |  | Y |  | Local Time |  |  |  |
| ratan-cash-settlement-accounting-service |  |  |  |  |  |  |  |  |
| ratan-cashflow-lifecycle-service |  |  |  |  |  |  |  |  |
| ratan-cash-settlement-group-management-service | EventTime |  | Y |  | Local Time | Exception Fields |  |  |
|  | ExceptionTime |  | Y |  | Local Time | Exception Fields |  |  |
| ratan-cash-settlement-netting-service |  |  |  |  |  |  |  |  |
| ratan-cash-settlement-ssi-stamping-service | EventTime |  | Y |  | Local Time |  |  |  |
|  | ExceptionTime |  | Y |  | Local Time |  |  |  |
| ratanone-swift-service | MT `<scb:messageTimestamp>${timestamp!''}</scb:messageTimestamp>` `<scb:initiatedTimestamp>${timestamp!''}</scb:initiatedTimestamp>` |  | Y |  | Local Time |  |  |  |
|  | occurTime |  | Y |  | Local Time |  |  |  |
| swift message | CreDt/CreDtTm | Y | Y |  | Local time |  | 2026-07-16T04:12:47+00:00 xml body |  |
| ratan-rule-service | affirmedAt |  | Y |  | Local Time |  |  |  |
|  | eventTime |  | Y |  | Local Time |  |  |  |
| ratan-cashflow-settlement-query-service Cashflow History | effective_Date_Time | Y |  | Y | UTC Time |  | 2024-01-03T00:00:00Z |  |
|  | ~~trade.execution_Date_Time~~ | Y |  | Y | UTC Time |  |  |  |
|  | cashflow.execution_Date_Time | Y |  | Y | UTC Time |  |  |  |
|  | cashflow.payment_Cutoff_Time ReleaseDateTime | Y |  |  | Local Time | backend will convert static data to local time | "2026-06-17T05:00Z" |  |
|  | data_Flow.data_Publication_Date_Time | Y |  | Y | UTC Time |  | "2026-06-08T00:54:26Z" |  |
|  | FMO_Comments.FMO_Comment_Timestamp | Y |  |  | Local Time |  | "Mon Jul 20 01:15:07 WIB 2026" |  |
|  | actionTime | Y | Y |  | Local Time |  | "2026-07-16T04:12:35.266680" |  |
|  | Trade_Lake_Latest_Event_Date_Time |  |  | Y | UTC Time |  |  |  |
|  | Trade_Lake_Raw_Event_Date_Time |  |  | Y | UTC Time |  |  |  |
|  | Trade_Lake_Transaction_From_Date_Time |  |  | Y | UTC Time |  |  |  |
|  | Trade_Lake_Transaction_To_Date_Time |  |  | Y | UTC Time |  |  |  |
|  | Trade_Lake_Valid_From_Date_Time |  |  | Y | UTC Time |  |  |  |
|  | Trade_Lake_Valid_To_Date_Time |  |  | Y | UTC Time |  |  |  |
|  | esDoc_Timestamp |  |  | Y | UTC Time |  |  |  |
|  | Message_Audit_Date_Time |  |  | Y | UTC Time |  |  |  |
| netting preview | EntryTime | Y | Y |  | Local Time |  | "2026-07-27T10:10:29.236599555" "2026-06-24T17:16:43" |  |
| Accounting detail | createdAt | Y | Y |  | Local Time |  | "2026-07-20T01:15:14.395524" |  |
|  | updatedAt | Y | Y |  | Local Time |  | "2026-07-20T01:24:00.011153" |  |
| Nstp/Suppression Swift/Suppression Cashflow rule | last modified | Y | Y |  | Local Time |  | "2026-07-16T04:12:14.602312Z" |  |
| Netting static | last modified | Y | Y |  | Local Time |  | "2026-07-07T08:53:09.098005Z" |  |
| Bic netting static/history | updated at | Y | Y |  | Local Time | gdc not use utc/local time function | "2025-11-21T11:06:25Z" | attachments recorded in source |
|  | created at | Y | Y |  | Local Time |  | "2025-11-21T10:54:53Z" | attachments recorded in source |
| Affirmation details | affirm - date time input | Y |  |  | Local Time |  | "2026-07-27T09:59:51.740Z" |  |
|  | ~~auto affirm - local date time~~ | Y |  |  | Local Time |  |  |  |
| Nostro static/history | created at | Y | Y |  | Local Time |  | "2026-04-01T11:34:52.38Z" |  |
|  | updated at | Y | Y |  | Local Time |  | "2026-04-01T12:17:44.959Z" |  |
| Rule history | updated at | Y | Y |  | Local Time |  | "2026-06-24T10:34:26.086282Z" |  |
| Group blotter | update at | Y | Y |  | Local Time |  | "2026-07-23T14:03:53.85515" |  |
| Utilization static/history | updated at | Y | Y |  | Local Time |  | "2026-04-25T09:34:22Z" |  |
|  | created at | Y | Y |  | Local Time |  | "2026-04-25T09:34:22Z" |  |

## UI parsing expression

```javascript
const idnsTimeRegex =
    /^(\d{4})-(\d{2})-(\d{2})(?:[T\s](\d{2}):(\d{2}):(\d{2})(?:\.(\d{1,10}))?)?Z?$/;
```

## Documented `IdnsTimeToUtc` conversion behavior

| Idns Local Time | IdnsTimeToUtc | UTC | Local(region utc+7) |
| --- | --- | --- | --- |
| 2026-08-20 07:00:00 | 2026-08-20T00:00:00Z | 2026-08-20T00:00:00Z | 2026-08-20 07:00:00 |
| 2026-08-20T05:00:00 | 2026-08-19T22:00:00Z | 2026-08-19T22:00:00Z | 2026-08-20 05:00:00 |
| 2026-08-20T10:00:00.395524 | 2026-08-20T03:00:00.395524Z | 2026-08-20T03:00:00Z | 2026-08-20 10:00:00 |
| 2026-08-20T10:00:00Z | 2026-08-20T03:00:00Z | 2026-08-20T03:00:00Z | 2026-08-20 10:00:00 |
| 2026-08-20T10:00:00.740Z | 2026-08-20T03:00:00.740Z | 2026-08-20T03:00:00Z | 2026-08-20 10:00:00 |
| 2026-08-20T10:00:00.098005Z | 2026-08-20T03:00:00.098005Z | 2026-08-20T03:00:00Z | 2026-08-20 10:00:00 |

## Implications

The source is direct evidence that `IdnsTimeToUtc` does not preserve the conventional UTC semantics of a `Z` suffix. It also records API timestamp forms ranging from naive ISO-like values to UTC values, offset-aware values, textual WIB values, and nine-digit fractional values.

The field classifications require an explicit cross-service contract before they can safely drive generic UI conversion. This affects [[ratan-indonesia]], [[51358-ratan-cash-settlement-query-service]], [[audit-trail]], and the [[ratan-indonesia-onshoring-2026]] project.
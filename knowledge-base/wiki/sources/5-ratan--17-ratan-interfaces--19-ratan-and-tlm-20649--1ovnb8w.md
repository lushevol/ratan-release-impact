---
type: source
title: RATAN and TLM 20649
authors: [Chongxuan Li, Yunzhe Ta]
year: 2026
url: ""
venue: "Internal interface documentation"
tags: [RATAN, TLM, interface-20649, reconciliation, accounting, Korea]
related: [tlm, ratan-tlm-reconciliation-query, what-is-the-authoritative-ratan-tlm-20649-interface-contract, ratan-accounting-status-lifecycle, oltp, aspire, ratan-interface-architecture, ratan-interface-inventory]
created: 2026-08-25
updated: 2026-08-25
sources: ["RATAN/RATAN -Interfaces/Ratan and TLM 20649.md"]
---

# RATAN and TLM 20649

## Summary

Interface 20649 documents a TLM-to-RATAN reconciliation query. TLM uses a RESTful API exposed through the RATAN/RATANONE flow to retrieve accounting information for the Korea entity and reconcile accounting requests sent to [[entities/oltp]]. The requested population is described as including acknowledged, negatively acknowledged, and unanswered records.

The business context states that [[entities/aspire]] cannot meet the Korea release timeline, creating a requirement for TLM to query RATAN accounting information directly.

## Source metadata

| Field | Value |
| --- | --- |
| Updated by | `@Chongxuan Li @Yunzhe Ta` |
| Update date | `2026-07-29` |
| Reviewed by | Not provided |
| Review date | Not provided |
| Status | Not provided; the document says status should become `Published` after review |

## End-to-end flow

```text
TLM <> RESTFUL API <> RATANONE
```

The documented API path is:

```text
/api/ratan/v1/accounting/queryReconRecords
```

This is a read/query interface for reconciliation, not an accounting submission or acknowledgement interface.

## Business agreement

- The current supported `fmidList` value is the Korea entity `10036645`.
- The effective implicit condition is:

```text
ratan_accounting_request_task_history.task_status = 'SENT'
```

- The longest permitted query time span is three days.
- `startReleaseTime` and `endReleaseTime` must be converted to GMT.

The Korea-only restriction applies to this interface and should not be generalized to other RATAN integrations without corroborating documentation.

## Interface specification

The source presents two URLs in a concatenated or malformed “PROD URL” field. Their deployment status requires confirmation.

Apparent production-like example:

```text
https://fmo-mfe.gdc.standardchartered.com:8453/api/ratan/v1/accounting/queryReconRecords?fmidList=10036645&startReleaseTime=2026-03-30T00:00:00&endReleaseTime=2026-04-01T00:00:00
```

Development-looking example:

```text
https://uklvadapp1344.uk.dev.net:8453/api/ratan/v1/accounting/queryReconRecords?fmidList=10036645&startReleaseTime=2026-05-28T09:00:00&endReleaseTime=2026-05-29T09:00:00
```

### Parameters

| parameters | type | M/O | sample | comment |
| --- | --- | --- | --- | --- |
| fmidList | String | M | `10036645`, with an example using repeated parameters | `ratan_accounting_request_task_history.booking_entity_fmid in fmidList`; only `10036645` is currently supported |
| startReleaseTime | `DateTime(yyyy-mm-dd'T'HH24:MM:SS)`; convert to GMT | M | `2026-04-30T00:00:00` | `ratan_accounting_request_task_history.created_at >= startReleaseTime` |
| endReleaseTime | `DateTime(yyyy-mm-dd'T'HH24:MM:SS)`; convert to GMT | M | `2026-05-01T00:00:00` | `ratan_accounting_request_task_history.created_at < endReleaseTime` |

The source also includes this local example:

```text
http://localhost:8080/v1/accounting/queryReconRecords/?fmidList=10075222&fmidList=10075223&startReleaseTime=2026-04-04T00:00:00&endReleaseTime=2026-04-05T00:00:00
```

The `fmidList` serialization contract is unresolved: the field is typed as `String`, while the examples show both a scalar value and repeated query parameters.

## Effective filtering semantics

The query applies the following conditions:

```text
ratan_accounting_request_task_history.booking_entity_fmid in fmidList
ratan_accounting_request_task_history.created_at >= startReleaseTime
ratan_accounting_request_task_history.created_at < endReleaseTime
ratan_accounting_request_task_history.task_status = 'SENT'
```

The time range is therefore half-open:

```text
[startReleaseTime, endReleaseTime)
```

The parameter names refer to release time, while the documented database predicate uses `created_at`. The source does not establish whether these are direct aliases or whether a separate release-time field exists.

## Performance-test evidence

```text
response total accounting feeds: 20286

Sent time scope: 22-July-2026T00:00:00 to 25-July-2026T00:00:00
```

The source links to an [[Apache JMeter]] dashboard:

<https://uklvadrtn006a.pi.dev.net:8081/performance-test/1785131956910/report/index.html>

The document provides no latency, throughput, concurrency, error-rate, pagination, or pass/fail metrics. The reported three-day test interval is consistent with the stated maximum range.

## Missing contract details

The source does not specify:

- Response JSON and field definitions.
- How ACK, NACK, and no-response outcomes are represented.
- HTTP status codes and error responses.
- Pagination behavior.
- Authentication requirements.
- Rate limits.
- Interface ownership, team contact, or OLA.
- Troubleshooting procedures.
- Whether the three-day limit is enforced or is operational guidance.

## Relationship to the existing wiki

This source extends [[concepts/ratan-interface-inventory]] and [[concepts/ratan-interface-architecture]] with a TLM-specific reconciliation query. Its accounting status semantics should be considered alongside [[concepts/ratan-accounting-status-lifecycle]] and [[queries/how-does-ratan-oltp-handle-eod-nacks]]. The relationship between `RATANONE` in this flow and [[entities/ratanone-message-bridge]] remains unconfirmed.
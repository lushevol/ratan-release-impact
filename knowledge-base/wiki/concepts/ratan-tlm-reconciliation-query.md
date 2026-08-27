---
type: concept
title: RATAN-TLM Reconciliation Query
tags: [RATAN, TLM, RESTful-API, reconciliation, accounting, Korea]
related: [tlm, ratan-and-tlm-20649--1ovnb8w, ratan-accounting-status-lifecycle, ratan-rest-cashflow-query-integration, ratan-interface-architecture, ratan-interface-inventory, oltp]
created: 2026-08-25
updated: 2026-08-25
sources: ["RATAN/RATAN -Interfaces/Ratan and TLM 20649.md"]
---

# RATAN-TLM Reconciliation Query

## Definition

The RATAN-TLM reconciliation query is interface 20649, a RESTful read API that allows [[entities/tlm]] to retrieve RATAN accounting records for reconciliation. The documented integration path is TLM to RESTful API to RATANONE.

## Query contract

The endpoint path is:

```text
/api/ratan/v1/accounting/queryReconRecords
```

The query requires:

- `fmidList`
- `startReleaseTime`
- `endReleaseTime`

The current documented business scope is limited to the Korea entity `10036645`.

## Filtering rules

The effective database predicates are:

```text
ratan_accounting_request_task_history.booking_entity_fmid in fmidList
ratan_accounting_request_task_history.created_at >= startReleaseTime
ratan_accounting_request_task_history.created_at < endReleaseTime
ratan_accounting_request_task_history.task_status = 'SENT'
```

The time interval is half-open, so records at the start boundary are included and records at the end boundary are excluded:

```text
[startReleaseTime, endReleaseTime)
```

The input timestamps must be converted to GMT. The mapping between the API names `startReleaseTime` and `endReleaseTime` and the database field `created_at` is not fully explained.

## Operational constraints

The longest documented query span is three days. A performance-test example reports:

```text
response total accounting feeds: 20286
Sent time scope: 22-July-2026T00:00:00 to 25-July-2026T00:00:00
```

This result does not establish latency, throughput, error-rate, pagination, or capacity thresholds.

## Accounting outcomes

The business description says the result should support reconciliation of accounting requests sent to [[entities/oltp]], including ACKed, NACKed, and unanswered records. The source does not identify the response fields or explain how these outcomes relate to the implicit `task_status = 'SENT'` predicate. This should be reconciled with [[concepts/ratan-accounting-status-lifecycle]].

## Boundaries

This concept describes interface 20649 only. Its Korea restriction, three-day limit, timestamp semantics, and `SENT` filter must not be generalized to other RATAN interfaces without separate evidence. The production endpoint, `fmidList` encoding, response schema, and ownership remain open questions tracked in [[queries/what-is-the-authoritative-ratan-tlm-20649-interface-contract]].
---
type: source
title: Ratan Query Service Message Consuming Control
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, ratan, query-service, event-consumption, event-store, scbml, capacity-planning]
related: [ratan-query-service, ratanone-cashflow-service-cqrs-cashflow-events, scbml-event-payload-storage-impact, what-version-ordering-policy-governs-ratan-query-service-event-consumption, what-retry-backoff-and-terminal-failure-policy-governs-ratan-query-service-consumption, cashflow-version-tuple-comparison, cashflow-locking-and-retry-policy, cash-settlement-capacity-planning-baseline]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Ratan query service message consuming control.md"]
authors: []
year: 2026
url: ""
venue: ""
---
# Ratan Query Service Message Consuming Control

This incomplete design note records open control questions for the [[ratan-query-service]] message consumer and a point-in-time storage snapshot for [[ratanone-cashflow-service-cqrs-cashflow-events]].

## Design status

The source leaves both the current process and proposal process blank. It does not define an approved ordering algorithm, retry policy, terminal-failure action, consumer acknowledgement boundary, or replay procedure.

The unresolved questions are:

1. How to check the order of `businessVersion + minorVersion`?
2. If `retryNum > 3`, throw exception or?
3. Delay time?

The notation `businessVersion + minorVersion` is ambiguous. This source does not establish whether versions are compared as a lexicographic tuple, serialized composite value, arithmetic sum, or another ordering key. It therefore supports the open investigation in [[what-version-ordering-policy-governs-ratan-query-service-event-consumption]], not a settled ordering policy.

## Event-store statistics

The source reports statistics for `ratanone_cashflow_service__cqrs_cashflow_events`:

- Records count: `811340`
- Total DB size: `2301 MB`

### Event-type distribution

| Event type | Each event size (kB) | Contains SCBML | Records count | Records percent |
| --- | --- | --- | --- | --- |
| CashflowCreationEvent | 5.36 | Yes | 139540 | 17.20% |
| CashflowAmendEvent | 5.76 | Yes | 276965 | 34.13% |
| CashflowHoldInRatan | 1.14 | No | 34005 | 4.19% |
| CashflowSkipped | 1.14 | No | 50264 | 6.19% |
| CashflowStatusUpdateEvent | 1.14 | No | 310566 | 38.28% |

The listed event counts reconcile to `811,340`. The reported percentages total `99.99%`, consistent with rounding.

## SCBML expansion scenario

The source models a scenario in which `CashflowHoldInRatan`, `CashflowSkipped`, and `CashflowStatusUpdateEvent` include SCBML and each has the same size as `CashflowAmendEvent` (`5.76 kB`).

Under that assumption:

- Database-size increase: **59%**
- Projected DB size: **3658.6 MB**

This is a scenario estimate captured in [[scbml-event-payload-storage-impact]], not a validated physical-storage forecast. The source does not state whether the total includes indexes, TOAST storage, WAL, backup storage, replication traffic, retention, or archival effects.
---
type: entity
title: ratanone_cashflow_service__cqrs_cashflow_events
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, ratan, cqrs, event-store, database]
related: [ratan-query-service, scbml-event-payload-storage-impact, cash-settlement-capacity-planning-baseline]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Ratan query service message consuming control.md"]
---
# ratanone_cashflow_service__cqrs_cashflow_events

`ratanone_cashflow_service__cqrs_cashflow_events` is the event table measured in the Ratan query-service consuming-control note.

## Reported snapshot

The source reports:

- `811,340` records;
- `2,301 MB` total DB size;
- five event types whose counts reconcile to the reported record count.

`CashflowStatusUpdateEvent` is the largest event group by count (`310,566`, `38.28%`), while `CashflowAmendEvent` has the largest stated per-event size (`5.76 kB`).

## Limits of the measurement

The measurement date, database version, table schema, indexes, retention policy, and definition of “Total DB size” are not provided. In particular, the source does not clarify inclusion of indexes, TOAST data, WAL, or other database overhead.

The SCBML payload-growth scenario is documented in [[scbml-event-payload-storage-impact]]. It applies only to this table and its stated assumptions; it must not be generalized to [[cashflow-data]] or other Cash Settlement stores.
---
type: concept
title: RATAN CQRS Cashflow Read Model
created: 2026-08-22
updated: 2026-08-22
tags: [ratan, cqrs, cashflow, read-model, graphql, event-driven]
related: [ratan-cashflow-lifecycle-service, ratan-cash-settlement-query-service, ratan, what-is-the-authoritative-ratan-cashflow-data-ownership-model]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design.md"]
---
# RATAN CQRS Cashflow Read Model

The technical design describes a CQRS-like separation between the Lifecycle Service write database and the Query Service read database.

The [[ratan-cashflow-lifecycle-service]] persists processing cashflow data and status movement. [[ratan-cash-settlement-query-service]] consumes events and stores data for UI and external queries, including GraphQL aggregation of cashflow, trade, exception, exception-stashing, and SSI-candidate information.

This architecture implies that query data may be separately materialized from processing data. The source does not specify replication latency, ordering, replay, recovery, retention, or which store prevails when statuses conflict. RATAN's “golden source” claim therefore needs a defined ownership boundary.
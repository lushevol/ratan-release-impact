---
type: query
title: Which Service Consumes and Persists Razor Cashflow Status Change Events?
tags: [cashflow, razor, consumer, persistence, integration]
related: [razor, scbml, fx-cashflow-status-write-back, cashflow-status-change-event-contract, cash-settlement-platform, ratan-query-service]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/FX Replication Status Write Back.md"]
---
# Which Service Consumes and Persists Razor Cashflow Status Change Events?

The sampled Razor message does not name a broker topic, queue, HTTP endpoint, consuming service, persistence table, or operational owner.

Determine the transport and receiver for `CashflowStatusChange`, then establish whether the receiver writes an event store, cashflow status history, a current-state record, a query projection, or multiple destinations. Existing [[ratan-query-service]] material must not be treated as evidence of consumption without a source that explicitly connects it to this message.
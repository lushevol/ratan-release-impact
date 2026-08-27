---
type: query
title: What Is the ratan_inbound_message Idempotency, Status, and Version Contract?
created: 2026-08-24
updated: 2026-08-24
tags: [uber, inbound-message, idempotency, status, version, database]
related: [ratan-inbound-message, tdsx-uber-message-listener, uber-inbound-message-idempotency-and-error-state, what-causes-duplicate-cashflow-ids-and-major-versions-in-uber-trades]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Cash Settlement Standardization Service.md"]
---
# What Is the ratan_inbound_message Idempotency, Status, and Version Contract?

The documented table stores `correlation_id`, `trade_id`, `status`, and `version`, but declares no uniqueness constraint beyond its surrogate `id` primary key.

## Questions

- Which field or field combination is the business identity of an inbound Uber message?
- Where is duplicate suppression enforced if it is not enforced by this DDL?
- What values and transitions are valid for `status`, and why does it default to `VALIDATED`?
- Does `version` represent message format, trade major version, optimistic locking, or another lifecycle version?
- What replay, retry, and terminal-error behavior applies to persisted messages?

The table is relevant evidence for traceability but does not establish the idempotency assumptions discussed in [[uber-inbound-message-idempotency-and-error-state]].
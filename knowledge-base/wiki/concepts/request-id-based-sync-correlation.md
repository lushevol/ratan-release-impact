---
type: concept
title: Request-ID-Based Sync Correlation
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, synchronization, correlation, request-id, reliability]
related: [data-synchronizer-manager, ratan-data-synchronizer, static-data-synchronization, per-destination-sync-status-tracking]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Common Module For Data Transfer.md"]
---
# Request-ID-Based Sync Correlation

Request-ID-based sync correlation is the rule that every static-data synchronization event receives a unique `request_id`, and that a response with a non-matching `request_id` is ignored.

This rule protects the current synchronization state from a response associated with a different event. It is implemented conceptually by [[data-synchronizer-manager]] and persisted in [[ratan-data-synchronizer]].

## Intended protection

When a data object is synchronized again, a new event should have a new `request_id`. A response from an earlier or unrelated event must not update the record for the current event if its identifier does not match.

## Undefined cases

The source does not define:

- whether matching is checked only against the newest record;
- duplicate-response handling;
- request-ID retention or expiry;
- logging and alerting for ignored responses;
- treatment of late `ACK` or `NACK` after a timeout;
- idempotency guarantees during retries or duplicate delivery.

These issues are tracked in [[what-is-the-ratan-static-data-sync-nack-retry-and-late-ack-policy]] and [[what-is-the-authoritative-ratan-static-data-sync-record-key-and-history-model]].
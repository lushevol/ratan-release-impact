---
type: concept
title: Per-Destination Sync Status Tracking
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, synchronization, status, acknowledgement, timeout]
related: [data-synchronizer-manager, ratan-data-synchronizer, static-data-synchronization, request-id-based-sync-correlation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Common Module For Data Transfer.md"]
---
# Per-Destination Sync Status Tracking

Per-destination sync status tracking records a synchronization outcome separately for each downstream data centre. The source illustrates the representation as `{"ID": "ACK"}` and shows status values stored in `sync_status`.

## Status vocabulary

- `SENT`: the Data Producer successfully produced the data.
- `FAILED`: the Data Producer failed to produce the data.
- `ACK`: the Data Consumer successfully consumed the data.
- `NACK`: the Data Consumer failed to consume the data.
- `TIMEOUT`: no response was received within five minutes.

This enables one data object to have different recorded outcomes across downstream destinations.

## Retry and reconciliation boundary

The documented `SyncFailedRetryer` retries `FAILED` and `TIMEOUT` records by setting their status to `SENT`. `NACK` is not included in this retry rule.

Consumers periodically reconcile through an unspecified REST API. The source does not define whether reconciliation changes status, how it resolves conflicts, or whether it can repair missing acknowledgements.

## Limitations to resolve

The source does not specify destination-level state transitions, terminal states, concurrent status-map updates, retry isolation between destinations, or the treatment of a late response after timeout or a newer event.
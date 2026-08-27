---
type: query
title: What Is the Ratan Static-Data Sync NACK, Retry, and Late-ACK Policy?
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, static-data, synchronization, retry, nack, timeout]
related: [data-synchronizer-manager, static-data-synchronization, per-destination-sync-status-tracking, request-id-based-sync-correlation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Common Module For Data Transfer.md"]
---
# What Is the Ratan Static-Data Sync NACK, Retry, and Late-ACK Policy?

## Question

What operational policy governs `NACK`, retries, duplicate delivery, and late acknowledgements for static-data synchronization events?

## Evidence

The source specifies that `SyncFailedRetryer` retries `FAILED` and `TIMEOUT` records, resetting their state to `SENT`. It does not include `NACK` in automatic retry. It also specifies a five-minute response timeout and requires mismatched `request_id` responses to be ignored.

## Decisions needed

- Determine whether `NACK` is terminal, manually remediated, or eligible for a separate retry path.
- Define retry interval, maximum attempts, backoff, retry ownership, and escalation.
- Define whether retries use a new `request_id` and how stale responses are handled.
- Define whether late `ACK` or `NACK` after `TIMEOUT` is ignored, recorded, or reconciled.
- Define idempotency and duplicate-delivery semantics.
- Define whether a retry for one destination can affect acknowledged status for another destination.

## Related pages

See [[per-destination-sync-status-tracking]] and [[request-id-based-sync-correlation]].
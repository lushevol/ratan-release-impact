---
type: source
title: Common Module For Data Transfer
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, static-data, synchronization, indonesia, architecture]
related: [ratan, ratan-indonesia-onshoring-2026, data-synchronizer-manager, ratan-data-synchronizer, static-data-synchronization, request-id-based-sync-correlation, per-destination-sync-status-tracking]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Common Module For Data Transfer.md"]
authors: []
year: 2026
url: ""
venue: ""
---
# Common Module For Data Transfer

## Summary

This design proposes a reusable synchronization capability for static data and rules from Ratan GDC to downstream XDC instances. The GDC-to-IDDC flow is the example used for Indonesia.

The proposed implementation is an embedded common module within a domain service. It is intended to remain independent of domain business logic: domain services produce and consume the business data, while the common module tracks synchronization events, delivery status, correlation, timeout, and retry state.

The source describes an alternative deployment as an independent service, but designs only the embedded-module approach. It does not establish that this approach is approved, implemented, or preferable to an independent service.

## Synchronization responsibilities

[[data-synchronizer-manager]] manages data-transfer records without interpreting business content. Its stated responsibilities and invariants are:

- Each data object retains one synchronization record for its newest synchronization event.
- Every synchronization event has a unique `request_id`.
- Delivery status is maintained separately for each downstream DC.
- A consumer response with a mismatched `request_id` is ignored.

[[data-synchronizer-manager]] is therefore a latest-state synchronization ledger rather than an append-only historical event log. The source does not define the exact object key, historical retention, concurrency behaviour, or handling of out-of-order events.

## Status model

The documented status vocabulary is:

| Status | Meaning |
|---|---|
| `SENT` | The Data Producer successfully produced the data. |
| `FAILED` | The Data Producer failed to produce the data. |
| `ACK` | The Data Consumer successfully consumed the data. |
| `NACK` | The Data Consumer failed to consume the data. |
| `TIMEOUT` | No response was received within five minutes. |

A status value is stored by destination DC, for example `{"ID": "ACK"}`. See [[per-destination-sync-status-tracking]].

## Retry and reconciliation

A `SyncFailedRetryer` in the Data Producer resynchronizes records in `FAILED` or `TIMEOUT` state and resets their status to `SENT`.

The Data Consumer periodically performs reconciliation using a REST API. The source does not provide API endpoints, payloads, authentication, reconciliation schedule, authority rules, or remediation semantics.

`NACK` is not included in the documented automatic retry scope. Retry cadence, maximum attempts, backoff, idempotency, late-response treatment, and escalation are unspecified.

## Preserved synchronization table

The source labels the following table as `ratan_data_synchronizer`. It supplies no SQL DDL, explicit primary key, uniqueness constraint, foreign key, index, or headers defining the unnamed `Y` columns.

| Field | Type | Source column 3 | Source column 4 | Default / example | Source column 6 |
|---|---|---|---|---|---|
| id | bigserial | Y |  |  | Y |
| object_id | text | Y | Y |  |  |
| object_type | text | Y |  |  |  |
| request_id | text | Y | Y |  |  |
| sync_content | text | Y |  | {} |  |
| sync_status | text | Y |  | `{ "ID": "ACK", "XX": "NACK", "...": "SENT", "...": "FAILED", "...": "TIMEOUT" }` |  |
| create_at | timestamp | Y |  |  |  |
| update_at | timestamp | Y |  |  |  |

## Relationship to existing architecture

This design concerns static data and rule propagation, not Murex cashflow publication, settlement processing, or FMRP workflows. It extends the Indonesia platform context documented in [[25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--11-2026-design--49-cash-settlement--1drygfb]] and is relevant to [[ratan-indonesia-onshoring-2026]] as a proposed GDC-to-IDDC dependency.

## Unresolved design points

- The authoritative key for one data object is not specified.
- The database constraints and serialization contract for `sync_content` and `sync_status` are not specified.
- The owner and mechanism that transition a record to `TIMEOUT` are not specified.
- The treatment of `NACK`, duplicate responses, late acknowledgements, and superseded requests is not specified.
- The manual resynchronization and refresh section has no defined behaviour.
- The REST reconciliation contract is absent.

See [[what-is-the-authoritative-ratan-static-data-sync-record-key-and-history-model]], [[what-is-the-ratan-static-data-sync-nack-retry-and-late-ack-policy]], and [[what-is-the-ratan-static-data-consumer-reconciliation-api-contract]].
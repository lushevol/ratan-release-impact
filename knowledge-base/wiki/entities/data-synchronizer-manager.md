---
type: entity
title: Data Synchronizer Manager
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, synchronization, static-data, common-module]
related: [ratan, ratan-data-synchronizer, static-data-synchronization, request-id-based-sync-correlation, per-destination-sync-status-tracking]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Common Module For Data Transfer.md"]
---
# Data Synchronizer Manager

Data Synchronizer Manager is a proposed Ratan common module for transferring static data and rules from GDC to downstream XDC deployments, including IDDC as the Indonesia example.

It manages synchronization records and delivery outcomes without interpreting domain business data. The documented design embeds the module in a domain service, while recognizing an independent-service deployment as an alternative that is not designed further in the source.

## Documented behaviour

- Maintains one record for the newest synchronization event of each data object.
- Assigns a unique `request_id` to every synchronization event.
- Tracks status independently by downstream DC.
- Ignores responses whose `request_id` does not match the current synchronization event.
- Supports producer-side retry of `FAILED` and `TIMEOUT` events through `SyncFailedRetryer`.
- Supports periodic consumer-side reconciliation through an unspecified REST API.

The persistent ledger is [[ratan-data-synchronizer]]. The status and correlation rules are described in [[per-destination-sync-status-tracking]] and [[request-id-based-sync-correlation]].

## Scope boundary

This component is for static data and rule synchronization. It is not described as a cashflow publication interface and should not be conflated with Ratan's Murex, FMRP, or settlement-message workflows.

## Open implementation questions

The source does not define object identity, historical retention, concurrency controls, destination-level retry isolation, timeout ownership, or independent-service operational characteristics.
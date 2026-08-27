---
type: query
title: What Is the Authoritative Ratan Static-Data Sync Record Key and History Model?
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, static-data, synchronization, database, audit]
related: [ratan-data-synchronizer, data-synchronizer-manager, static-data-synchronization, request-id-based-sync-correlation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Common Module For Data Transfer.md"]
---
# What Is the Authoritative Ratan Static-Data Sync Record Key and History Model?

## Question

What uniquely identifies a synchronized data object, and how are historical synchronization events retained after the latest event overwrites the object's only synchronization record?

## Evidence

The source states that each data object has one record for its newest synchronization event. The supplied `ratan_data_synchronizer` structure includes `object_id`, `object_type`, and `request_id`, but documents no primary key, unique constraint, or event-history mechanism.

## Decisions needed

- Confirm whether object identity is `object_id`, `(object_id, object_type)`, or another key.
- Confirm whether `request_id` is unique at database level.
- Define update and concurrency behaviour when a newer event arrives during a retry or while awaiting a response.
- Define audit, diagnostic, and regulatory retention for superseded events and responses.
- Define stale-response handling after an event record has been replaced.

## Related pages

See [[ratan-data-synchronizer]] and [[request-id-based-sync-correlation]].
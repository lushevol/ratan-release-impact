---
type: entity
title: ratan_data_synchronizer
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, database, synchronization, static-data]
related: [data-synchronizer-manager, static-data-synchronization, request-id-based-sync-correlation, per-destination-sync-status-tracking]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Common Module For Data Transfer.md"]
---
# ratan_data_synchronizer

`ratan_data_synchronizer` is the proposed persistent synchronization ledger used by [[data-synchronizer-manager]]. It stores the newest event for each synchronized data object and holds destination-specific delivery state.

The source does not provide SQL DDL or document primary keys, unique keys, foreign keys, indexes, or the meaning of the source table's unnamed indicator columns.

## Preserved source structure

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

## Design interpretation limits

`sync_content` and `sync_status` are both typed as `text` in the supplied table. Although the examples are JSON-like, the source does not specify serialization, validation, or database JSON support.

The statement that each data object has one newest-event record does not define whether the object identity is `object_id`, `object_type`, or `(object_id, object_type)`. It also does not state whether `request_id` has a uniqueness constraint or how historical synchronization events are retained.

See [[what-is-the-authoritative-ratan-static-data-sync-record-key-and-history-model]].
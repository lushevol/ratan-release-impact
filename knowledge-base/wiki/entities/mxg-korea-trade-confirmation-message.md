---
type: entity
title: Mxg_Korea_Trade_Confirmation_Message
created: 2026-08-24
updated: 2026-08-24
tags: [database-table, korea, murex, trade-confirmation, message-persistence]
related: [murex, murex-comp-status-driven-stp, how-does-korea-murex-comp-status-drive-stp, what-are-the-idempotency-ordering-and-retention-rules-for-korea-trade-confirmation-messages]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Korea Murex Trade COMP Design.md"]
---
# Mxg_Korea_Trade_Confirmation_Message

`Mxg_Korea_Trade_Confirmation_Message` is a proposed database table for persisting Korea-related Murex trade-confirmation messages. The design records both selected message data and the original message payload.

The source identifies [[murex]] as the source of trade XML/messages. It does not confirm that this table has been implemented.

## Proposed Fields

| Column | Comment | Type |
| --- | --- | --- |
| `id` | unique id | `id (seq)` |
| `trade_id` | Trade Id | `text` |
| `action` | action in trade xml `/events/mainEvent/action` | `text` |
| `raw_message` | original message | `text` |
| `created_at` | create timestamp | `timestamp` |
| `updated_at` | update timestamp | `timestamp` |

## Undocumented Semantics

The proposal does not specify a primary-key declaration, sequence name, nullability, default values, foreign keys, unique constraints, indexes, or database platform.

It also leaves the message lifecycle unresolved: a `trade_id` may or may not have multiple messages; no message identifier, event timestamp, version, ordering rule, or deduplication rule is defined. The purpose of `updated_at` is likewise unspecified.

Because `raw_message` stores the original message as unrestricted text, retention, access control, sensitive-data classification, and storage-volume controls require definition.
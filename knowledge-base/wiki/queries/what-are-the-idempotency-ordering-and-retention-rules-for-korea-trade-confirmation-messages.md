---
type: query
title: What Are the Idempotency, Ordering, and Retention Rules for Korea Trade-Confirmation Messages?
created: 2026-08-24
updated: 2026-08-24
tags: [korea, murex, trade-confirmation, idempotency, retention, database-design, open-question]
related: [murex, mxg-korea-trade-confirmation-message, murex-comp-status-driven-stp]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Korea Murex Trade COMP Design.md"]
---
# What Are the Idempotency, Ordering, and Retention Rules for Korea Trade-Confirmation Messages?

## Question

What persistence and operational rules govern messages stored in [[mxg-korea-trade-confirmation-message]]?

## Current Evidence

The proposed table contains `id`, `trade_id`, `action`, `raw_message`, `created_at`, and `updated_at`. It does not define constraints or message-processing semantics.

## Information Needed

- Primary-key, sequence, nullability, default-value, and indexing requirements.
- Whether `trade_id` is unique or may have multiple confirmation messages.
- A message identifier, version, event timestamp, or equivalent ordering key.
- Deduplication and idempotent-write behavior.
- The reason for `updated_at` and any permitted update or upsert rule.
- `raw_message` retention, archival, access-control, data-classification, and volume-management policies.
- Error handling and audit requirements for invalid or unparseable Murex messages.
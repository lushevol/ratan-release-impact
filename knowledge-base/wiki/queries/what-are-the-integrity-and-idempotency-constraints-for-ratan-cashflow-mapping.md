---
type: query
title: What Are the Integrity and Idempotency Constraints for ratan_cashflow_mapping?
created: 2026-08-24
updated: 2026-08-24
tags: [database, cashflow-mapping, idempotency, integrity, concurrency]
related: [ratan-cashflow-mapping, ratan-cashflow-mapping-history, cashflow-replacement-mapping]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Ratan processing on cashflow events/Group Management Service - Non-Eco Amendment Technical Design.md"]
---
# What Are the Integrity and Idempotency Constraints for ratan_cashflow_mapping?

The logical schema identifies only `id` as a primary key and implies a history relationship through `mapping_id`. It does not define data types, foreign keys, unique constraints, indexes, optimistic-lock semantics, write ownership, or concurrent-delivery behaviour.

An authoritative persistence contract is needed to prevent duplicate and conflicting mappings, determine whether replacement chains are supported, and establish how mapping-history records are created and retained.
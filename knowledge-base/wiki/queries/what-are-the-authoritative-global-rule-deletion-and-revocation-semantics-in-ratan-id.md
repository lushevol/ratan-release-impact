---
type: query
title: What Are the Authoritative Global Rule Deletion and Revocation Semantics in RATAN ID?
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, deletion, revocation, rule-history, indonesia]
related: [ratan-global-rule-synchronization, rule-sync-idempotency-and-version-ordering, ratan-gdc, ratan-indonesia]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Global Rule Sync From Ratan GDC to Ratan ID.md"]
---
# What Are the Authoritative Global Rule Deletion and Revocation Semantics in RATAN ID?

The source requires source-side amendments and deletions to feed Indonesia, while stating that a Global rule cannot be changed to non-Global because prior histories become `DEAD` and revoke synchronization status cannot be handled properly.

The authoritative behavior is needed for deletion, disablement, re-enablement, amendment, parent-history `DEAD` records, ID-side audit retention, and any transition that would otherwise make a Global rule non-Global.
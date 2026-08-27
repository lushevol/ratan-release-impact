---
type: concept
title: RATAN Global Rule Synchronization
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, global-rules, indonesia, solace, replication]
related: [ratan-gdc, ratan-indonesia, ratanone-rule-service, solace, rule-sync-idempotency-and-version-ordering, central-global-and-local-indonesia-rule-governance, deployment-profile]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Global Rule Sync From Ratan GDC to Ratan ID.md"]
---
# RATAN Global Rule Synchronization

RATAN Global Rule Synchronization is the proposed process for replicating eligible Global rules from [[ratan-gdc]] to [[ratan-indonesia]].

## Eligibility

A rule is automatically classified as Global if its expression includes neither:

- `Entity__Booking_Entity_SCI_FMID`
- `Entity__Booking_Entity_SCI_FMCODE`

Automatic incremental synchronization is limited to Global rules where:

- `businessFlow = STRATEGIC_SETTLEMENT`; and
- `ruleType` is `NSTP`, `SUPPRESSION`, `SWIFT_SUPPRESSION`, `NETTING`, or `AUTO_NETTING`.

## Direction and ownership

The proposed direction is GDC to Indonesia only. Replicated Global rules are read-only in Indonesia, while Indonesia-specific rules remain locally authored.

## Lifecycle

The design describes creation, update, enable/disable control, retry, and manual resend. A producer record tracks downstream states such as `SENT`, `ACK`, `NACK`, `FAILED`, `TIMEOUT`, and `IGNORE`.

Deletion and revocation behavior is incomplete, particularly where a previous rule history becomes `DEAD`. See [[what-are-the-authoritative-global-rule-deletion-and-revocation-semantics-in-ratan-id]].
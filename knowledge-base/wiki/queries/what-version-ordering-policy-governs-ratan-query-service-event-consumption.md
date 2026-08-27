---
type: query
title: What Version Ordering Policy Governs Ratan Query Service Event Consumption?
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, message-consumption, ordering, business-version, minor-version, idempotency]
related: [ratan-query-service, cashflow-version-tuple-comparison, ratanone-cashflow-service-cqrs-cashflow-events]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Ratan query service message consuming control.md"]
---
# What Version Ordering Policy Governs Ratan Query Service Event Consumption?

The source asks how the Ratan query-service consumer should check the order of `businessVersion + minorVersion`, but does not provide a policy or implementation.

## Questions to resolve

- Is the authoritative ordering a lexicographic `(businessVersion, minorVersion)` tuple, a serialized composite version, a broker sequence, or another identifier?
- Does the plus sign mean tuple composition or arithmetic addition?
- What constitutes a duplicate, stale, missing, or out-of-order event?
- Is a version gap rejected, buffered, retried, or accepted with compensating reconciliation?
- Which persistent state records the last successfully applied version?
- How does consumer acknowledgement coordinate with durable event processing and idempotency?

## Scope

This query is specific to [[ratan-query-service]]. The source is evidence that the question is open; it does not replace or establish the wider semantics documented in [[cashflow-version-tuple-comparison]].
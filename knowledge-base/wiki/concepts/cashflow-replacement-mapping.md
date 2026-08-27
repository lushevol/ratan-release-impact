---
type: concept
title: Cashflow Replacement Mapping
created: 2026-08-24
updated: 2026-08-24
tags: [cashflow, mapping, versioning, non-economic-amendment, traceability]
related: [cashflow, non-economic-cashflow-amendment, ratan-cashflow-mapping, ratan-cashflow-mapping-history, stella]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Ratan processing on cashflow events/Group Management Service - Non-Eco Amendment Technical Design.md"]
---
# Cashflow Replacement Mapping

Cashflow replacement mapping preserves the relationship between an original `New` cashflow and the replacement `New` cashflow created by a non-economic amendment. The proposed mapping records cashflow IDs together with business, cashflow, and major version values, making identity version-aware rather than ID-only.

The source's POC expects this mapping to support two continuity requirements:

- Netting status synchronisation should reference the replacement cashflow ID in the blocking queue.
- A Pending Affirmation exception for an original cashflow should close when the matching trade event arrives after its non-economic replacement has been mapped.

The source does not specify mapping cardinality, selection of an original across major versions, chaining of successive replacements, idempotency, conflict resolution, or database constraints. The example links an original at major version `1` with a replacement at major version `2`, despite inbound grouping being described as per trade ID and major version.
---
type: concept
title: Static Reference Data Synchronization
created: 2026-08-24
updated: 2026-08-24
tags: [reference-data, synchronization, golden-source, EDMI, reconciliation, cash-settlement]
related: [database-first-static-data-caching, ssi-stamping-reference-data, redis, what-is-the-authoritative-static-reference-data-freshness-and-reconciliation-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/The Cache Data Layer Design.md"]
---

# Static Reference Data Synchronization

Static reference data synchronization is the proposed process for maintaining local RatanOne copies of data mastered by surrounding systems.

## Proposed flow

1. Bootstrap the local database from a golden-source database dump.
2. Consume update notifications through EDMI, including FM-EDMI or Enterprise-EDMI.
3. Receive daily change files through FileIT or another suitable transfer channel.
4. Reconcile RatanOne data with the golden source.
5. Parse the golden-source file and refresh discrepancies by end of day.

The pattern is intended to improve STP stability and reduce access pressure on SSI+ and SCI.

## Unspecified contract

The design does not define event ordering, idempotency keys, version checks, replay, late or missing notification handling, file and event precedence, acceptable staleness, reconciliation thresholds, or recovery procedures. These requirements are tracked in [[queries/what-is-the-authoritative-static-reference-data-freshness-and-reconciliation-contract]].

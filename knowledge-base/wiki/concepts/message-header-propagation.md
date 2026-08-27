---
type: concept
title: Message Header Propagation
tags: [messaging, headers, routing, integration, contracts]
related: [message-bridge, domain-owned-message-filtering, message-topic-consolidation, what-is-the-canonical-message-filter-sdk-and-configuration-contract, cashflow-status-change-event-contract, ssi-stamping-message-contract]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Message Bridge Filters.md"]
---
# Message Header Propagation

Message header propagation is the requirement for [[message-bridge|Message Bridge]] to carry message headers unchanged when passing consumed messages onward.

## Role in the Proposed Design

The proposed removal of MB business filters depends partly on downstream services being able to filter using headers. The contemplated reusable SDK is expected to support filters over:

- [[scbml|SCBML]];
- UBER/JSON;
- headers.

## Unspecified Contract

The source does not identify which headers must be preserved or define header mutability, encoding, versioning, provenance, security classification, propagation failure behavior, or compatibility requirements.

These omissions are material because downstream filtering can only reproduce MB behavior if needed header values are consistently available and semantically stable. Header requirements should be reconciled with service-specific event contracts such as [[cashflow-status-change-event-contract]] and [[ssi-stamping-message-contract]].
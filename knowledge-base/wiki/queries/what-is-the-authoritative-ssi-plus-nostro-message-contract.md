---
type: query
title: What Is the Authoritative SSI+ Nostro Message Contract?
created: 2026-08-23
updated: 2026-08-23
tags: [ssi-plus, nostro, api, events, integration, open-question]
related: [ssi-plus, nams, nostro-stamping, nostro-notification-and-refresh, ratan, razor]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Nostro Centralization.md"]
---
# What Is the Authoritative SSI+ Nostro Message Contract?

## Question

What query and notification contracts must TP systems implement to consume centralized Nostro static data from `SSI+`?

## Current evidence

The requirement calls for:

- A new `SSI+` connection for Nostro queries.
- Queries supporting `Ratan` cashflow or trade stamping and accounting.
- Consumption of `New`, `Update`, and `Delete` static-data events.
- A refresh triggered by Nostro notifications.

Message formats and mappings are explicitly marked as requiring confirmation.

## Contract areas to resolve

- Query request and response schemas.
- Event payload schema and event-type vocabulary.
- Canonical and legacy Nostro identifiers.
- Portfolio-to-Nostro mapping for `RFI stamping`.
- Transport and authentication.
- Ordering, durability, replay, and idempotency.
- Delete and tombstone semantics.
- Error, timeout, retry, and fallback behavior.
- Cache invalidation and refresh completion.
- NFR targets for latency, availability, and recovery.

Until these items are confirmed, the requirement should be treated as scope guidance rather than an implementation-ready interface specification.

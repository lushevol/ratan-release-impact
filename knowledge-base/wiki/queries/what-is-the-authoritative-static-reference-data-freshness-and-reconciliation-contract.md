---
type: query
title: What Is the Authoritative Static Reference Data Freshness and Reconciliation Contract?
created: 2026-08-24
updated: 2026-08-24
tags: [open-question, reference-data, freshness, reconciliation, EDMI, golden-source]
related: [static-reference-data-synchronization, ssi-stamping-reference-data, database-first-static-data-caching]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/The Cache Data Layer Design.md"]
---

# What Is the Authoritative Static Reference Data Freshness and Reconciliation Contract?

## Question

What freshness, ordering, replay, idempotency, and reconciliation rules govern reference data synchronized from SSI+ and SCI into RatanOne?

## Evidence

The design proposes database-dump initialization, EDMI notifications with payloads, daily golden-source change files, and EOD reconciliation. It does not define:

- Which channel is authoritative when events and files disagree
- Event ordering, version checks, deduplication, or replay
- Handling for late, missing, malformed, or duplicate notifications
- Cache invalidation propagation
- Maximum acceptable staleness
- Reconciliation completion deadlines and discrepancy thresholds
- Repair, quarantine, and escalation procedures

## Required resolution

Define a contract for each dataset, including freshness SLO, event and file precedence, idempotency key, version semantics, reconciliation evidence, retry behavior, and operational ownership.

---
type: concept
title: OpenSearch Business Live
created: 2026-08-24
updated: 2026-08-24
tags: [opensearch, business-go-live, technical-go-live, cash-settlement]
related: [opensearch, ratanone, double-writing, three-way-data-reconciliation, idempotent-historical-data-migration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/OpenSearch Business Live Plan.md"]
---
# OpenSearch Business Live

## Definition

OpenSearch business live is the transition from using OpenSearch as a technically operational persistence platform to using it as the default business query source for RatanOne Cash Settlement.

## Technical go-live versus business go-live

Technical go-live establishes that OpenSearch can receive and persist supported data. Business go-live additionally requires:

- Complete required domain coverage.
- Historical data migration.
- Real-time synchronization.
- Query-model alignment.
- Behavioral equivalence with PG fallback.
- Reconciliation and operational recovery.
- Cutover and rollback controls.

## Staged adoption

The proposed adoption has two stages:

1. **Internal flow:** OpenSearch becomes the default for cashflow blotter, detail, and dashboard queries while PG remains available.
2. **External flow:** External consumers move to OpenSearch-backed querying through a v2 API after data-model and firewall changes.

The plan is not yet a complete go-live decision because acceptance criteria, performance targets, and PG retirement conditions are unspecified.

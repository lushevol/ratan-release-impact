---
type: concept
title: Double Writing
created: 2026-08-24
updated: 2026-08-24
tags: [double-writing, dual-write, opensearch, postgresql, migration]
related: [opensearch, postgresql, ratanone-opensearch-agent, opensearch-business-live, three-way-data-reconciliation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/OpenSearch Business Live Plan.md"]
---
# Double Writing

## Definition

Double writing is the transitional persistence pattern in which the same business change is written to both PostgreSQL and OpenSearch.

## Use in RatanOne

The source states that Cash Settlement already uses double writing after OpenSearch technical go-live and proposes extending the strategy to other required domain data.

Double writing supports PG fallback while OpenSearch becomes the default query source. It also introduces consistency risks between the two stores.

## Controls required

A production-ready double-writing contract should define:

- Write ordering and acknowledgement semantics.
- Retry and failure persistence.
- Idempotency key and document identity.
- Event or record versioning.
- Handling of partial success.
- Reconciliation and repair.
- Criteria for stopping PG writes.

Double writing should not be treated as proof that the two query sources are behaviorally equivalent.

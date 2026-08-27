---
type: entity
title: RatanOne OpenSearch Agent
created: 2026-08-24
updated: 2026-08-24
tags: [ratanone, opensearch, kafka, integration, dlt]
related: [opensearch, double-writing, kafka-persistent-retry-and-dlt-recovery, retry-and-failure-persistence-semantics, three-way-data-reconciliation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/OpenSearch Business Live Plan.md"]
---
# RatanOne OpenSearch Agent

## Role

The RatanOne OpenSearch Agent is the integration component responsible for OpenSearch persistence in the RatanOne Cash Settlement flow. Its implementation is associated with the `51358-ratanone-opensearch-agent` repository.

## Current behavior

The source states that Cash Settlement uses a double-writing model after technical go-live. The agent currently uses Kafka non-blocking retry for processing failures.

Messages that exhaust the retry path reach a DLT, but the current design provides no further operational process for those messages.

## Proposed enhancement

The plan proposes recording DLT messages in an index and supporting:

- Manual replay
- Potential automatic replay
- Identification of missing or mismatched cashflows through reconciliation

The replay design must define idempotency keys, document versioning, retry limits, ordering behavior, authorization, audit history, and poison-message handling.

## Reliability concerns

DLT replay and double writing can produce duplicate or stale OpenSearch documents unless event identity and version semantics are explicit. Reconciliation should identify the affected cashflow and distinguish missing, delayed, duplicated, stale, and semantically divergent records.

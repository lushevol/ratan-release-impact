---
type: concept
title: DLT Management for the OpenSearch Agent
created: 2026-08-24
updated: 2026-08-24
tags: [dlt, kafka, retry, replay, opensearch, operations]
related: [ratanone-opensearch-agent, kafka-persistent-retry-and-dlt-recovery, retry-and-failure-persistence-semantics, opensearch, three-way-data-reconciliation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/OpenSearch Business Live Plan.md"]
---
# DLT Management for the OpenSearch Agent

## Definition

DLT management is the operational process for retaining, inspecting, replaying, and resolving Kafka messages that the OpenSearch agent cannot process through the normal retry path.

## Proposed design

The source proposes an OpenSearch index for recording DLT messages, together with manual replay and potentially automatic replay.

## Safety requirements

The design must specify:

- DLT record identity and correlation to the business cashflow.
- Original payload and failure metadata.
- Retry count and terminal-failure state.
- Manual replay authorization and audit trail.
- Automatic replay policy and backoff.
- Idempotency and document-version checks.
- Ordering and stale-event handling.
- Poison-message quarantine.
- Success, exhaustion, and operator-resolution states.

DLT persistence and replay should be integrated with reconciliation so that operators can verify whether a replay repaired the missing or divergent record.

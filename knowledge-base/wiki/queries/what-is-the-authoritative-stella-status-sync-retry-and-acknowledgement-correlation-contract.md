---
type: query
title: What Is the Authoritative Stella Status-Sync Retry and Acknowledgement Correlation Contract?
created: 2026-08-24
updated: 2026-08-24
tags: [stella, status-synchronisation, retry, acknowledgement, blocking-queue]
related: [stella, cashflow-replacement-mapping, netting-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Ratan processing on cashflow events/Group Management Service - Non-Eco Amendment Technical Design.md"]
---
# What Is the Authoritative Stella Status-Sync Retry and Acknowledgement Correlation Contract?

The POC expects a failed Stella acknowledgement to move a blocking-queue record to `FAILED`, create an exception, and later permit replay. A successful Netting acknowledgement is expected to move the record to `SUCCESS` and automatically trigger Unnet status synchronisation.

The design does not identify the queue owner, acknowledgement correlation key, retry schedule, timeout policy, idempotency key, duplicate-acknowledgement behaviour, exception-to-queue linkage, or precise condition for automatically triggering Unnet status synchronisation.
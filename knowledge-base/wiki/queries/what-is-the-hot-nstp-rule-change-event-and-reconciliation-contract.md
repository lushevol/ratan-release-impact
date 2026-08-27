---
type: query
title: What Is the Hot NSTP Rule Change Event and Reconciliation Contract?
created: 2026-08-24
updated: 2026-08-24
tags: [NSTP, Rule Service, orchestration, events, reconciliation, query]
related: [nstp-rules, orchestration, rule-service, hot-nstp-rule-exception-reconciliation, rule-sync-idempotency-and-version-ordering]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Hot NSTP Rule Exception Generation.md"]
---
# What Is the Hot NSTP Rule Change Event and Reconciliation Contract?

## Question

How do GUI rule changes reach Rule Service and Orchestration, and how is the affected cashflow population reevaluated?

## Why It Matters

The source names GUI, Rule Service, and Orchestration as development areas but leaves all three sections empty. It therefore does not establish whether propagation uses direct APIs, events, polling, or another mechanism.

## Required Resolution

Define:

- Create, update, remove, activation, and effective-date semantics.
- The authoritative rule store and evaluation API.
- The change event or command payload.
- Rule versioning, ordering, and idempotency.
- Cashflow selection, pagination, batching, and throughput limits.
- Retry and dead-letter behavior.
- Partial-failure recovery and reconciliation.
- Metrics, audit records, alerts, and operator controls.
---
type: query
title: Is Minor-Version Validation Enforced at Every RATAN Status Transition?
created: 2026-08-22
updated: 2026-08-22
tags: [query, RATAN, concurrency, versioning, lifecycle]
related: [payment-release-concurrency-control, cashflow-netting-renetting, event-driven-component-cashflow-status-management, resultant-cashflow-status-consistency]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Auto Release Process.md"]
---
# Is Minor-Version Validation Enforced at Every RATAN Status Transition?

## Question

Is minor-version validation enforced consistently at the workflow, Lifecycle Service, status-movement API, persistence, Netting Service, SWIFT service, and outbound publication layers?

## Evidence

The source describes Camunda duplicate filtering using cashflow ID, business version, and minor version. However, the reported netting incident states that the status-movement API no longer validates minor version.

These statements may concern different layers, but the source does not define the authoritative validation boundary or confirm whether status updates are atomic and conditional on the expected version.

## Required Evidence

- Current status-movement API contract and implementation.
- Workflow and persistence version-check behaviour.
- Netting Service commit-time validation.
- SWIFT-service publication checks.
- Tests covering stale minor versions, reordered events, and concurrent operations.
- Production deployment and monitoring evidence.

See [[payment-release-concurrency-control]] and [[cashflow-netting-renetting]].
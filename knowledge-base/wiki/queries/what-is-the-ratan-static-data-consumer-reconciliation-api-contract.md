---
type: query
title: What Is the Ratan Static-Data Consumer Reconciliation API Contract?
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, static-data, synchronization, reconciliation, rest-api]
related: [data-synchronizer-manager, static-data-synchronization, per-destination-sync-status-tracking, ratan-indonesia-onshoring-2026]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Common Module For Data Transfer.md"]
---
# What Is the Ratan Static-Data Consumer Reconciliation API Contract?

## Question

What is the authoritative REST API contract and operating model for periodic Data Consumer reconciliation of static-data synchronization?

## Evidence

The source states only that a REST API exists for the Data Consumer to perform periodic reconciliation. It provides no endpoint, schema, timing, ownership, authorization, or outcome rules.

## Decisions needed

- Define endpoint paths, request and response schemas, and error semantics.
- Define reconciliation schedule, triggering, and ownership.
- Define the authoritative data source when producer and consumer state differ.
- Define authentication, authorization, audit logging, and operational observability.
- Define mismatch remediation and whether reconciliation may create a new synchronization event.
- Define how reconciliation handles deleted objects, removed rules, version incompatibility, and stale `request_id` values.

## Related pages

See [[data-synchronizer-manager]] and [[static-data-synchronization]].
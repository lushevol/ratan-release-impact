---
type: entity
title: Workflow
created: 2026-08-22
updated: 2026-08-22
tags: [workflow, payment-release, Camunda, RATAN]
related: [ratan, swift-service, payment-release-concurrency-control, event-driven-component-cashflow-status-management]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Auto Release Process.md"]
---
# Workflow

## Role in Auto Release

Workflow controls publication from the auto-release process to the SWIFT service. The design discussion proposes that it publish a cashflow only after confirming the current state is `READY + NA + NA`.

This check is intended to prevent a stale workflow decision from publishing a cashflow after a competing process has changed its state.

## Duplicate Filtering

The source states that Camunda workflow can filter duplicates using a cache-level lock keyed by cashflow ID, business version, and minor version. This is source-stated design information and is not independently confirmed here as an implementation guarantee.

## Relationship to Lifecycle Processing

Workflow operates alongside the [[entities/lifecycle-service|Lifecycle Service]] and [[entities/netting-service|Netting Service]]. The source stresses that workflow publication checks should be paired with current-state and version-aware validation at lifecycle and persistence boundaries.
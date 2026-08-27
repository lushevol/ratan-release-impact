---
type: concept
title: Lifecycle Compatibility API
created: 2026-08-22
updated: 2026-08-22
tags: [lifecycle, api, compatibility, routing, migration, rat an]
related: [ratan, uber, uber-legacy-workflow-isolation, ratan-strategic-json-data-model, ratan-uber-migration-options]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/RATAN - Uber Integration - Proposals.md"]
---
# Lifecycle Compatibility API

## Definition

The Lifecycle Compatibility API is a proposed tactical API that presents one stable external status-update contract while Lifecycle determines whether to invoke the old or new internal API.

## Motivation

Rule services, UI clients, netting clients, orchestration, scheduled jobs, and other domain services should not each determine which API version to call. A single lifecycle boundary is intended to centralize workflow and message-type routing and reduce duplicated caller logic.

The design also considers returning a message-type or workflow indicator so that downstream services can select the appropriate flow when Lifecycle cannot complete the routing transparently.

## Behavioral constraint

The old and new APIs are not behaviorally identical. In the new API, `NetNew` and `RevertToQueued` no longer cause Lifecycle to publish to the `process_in` topic; domain services must publish instead. Any compatibility layer must therefore define event ownership, retry behavior, failure handling, and idempotency.

## Lifecycle

The source explicitly treats this API as temporary. It is a proxy for coexistence and should eventually be removed after migration to the strategic model. No final contract or approval is recorded.
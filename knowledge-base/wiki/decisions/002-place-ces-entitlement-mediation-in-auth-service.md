---
type: decision
title: Place CES Entitlement Mediation in auth-service
created: 2026-08-24
updated: 2026-08-24
tags: [ces, data-entitlement, auth-service, architecture]
related: [ces, auth-service, query-service, static-data-service, api-gateway, cash-settlement-data-entitlement, ces-data-entitlement-integration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Data entitlement solution/FM CES Integration Technical Design.md"]
status: proposed
deciders: []
date: 2026-08-24
supersedes: ""
---
# Place CES Entitlement Mediation in auth-service

## Context

RATANONE requires CES-derived data-entitlement conditions for selected cashflow access paths. The design considered placing the integration in Static Data Service or having API gateway obtain entitlement results and forward them in request headers.

Static Data Service work was cancelled after the responsibility was moved to auth-service. Gateway forwarding would require structured entitlement payloads in headers, increase request size, affect interfaces that do not need filtering, constrain error handling, and would not serve direct service calls or WebSocket event delivery.

## Decision

Use [[auth-service|auth-service]] as the CES entitlement-mediation boundary. Query Service and other in-scope consumers retrieve entitlement results from auth-service on demand rather than relying on API-gateway entitlement headers.

auth-service is responsible for CES access, FMAA token use, Redis caching, entitlement-result exposure, and cache invalidation. [[query-service|Query Service]] remains responsible for translating and applying the result to its GraphQL, SQL, and WebSocket enforcement paths.

## Consequences

- The design aligns CES mediation with the existing EMS2 authorization-adjacent flow.
- WebSocket and direct service-to-service invocation paths can use the same entitlement source.
- Only in-scope interfaces incur entitlement integration impact.
- Consumers retain interface-specific error presentation and enforcement logic.
- auth-service becomes a critical dependency and must provide clear availability, cache, authorization, and operational contracts.
- Each consumer must integrate with auth-service rather than receiving an already-materialized gateway header.

## Status note

The source records this as a selected implementation direction, but this page is marked proposed until its current production status and governance approval are confirmed.
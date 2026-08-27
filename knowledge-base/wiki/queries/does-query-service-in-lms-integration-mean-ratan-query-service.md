---
type: query
title: Does Query Service in LMS Integration Mean Ratan Query Service?
created: 2026-08-24
updated: 2026-08-24
tags: [lms, query-service, ratan, cashflow-events, identity-resolution]
related: [lifecycle-service, ratan-query-service, cash-settlement-orchestration-process-in, lms-business-event-tracking, what-is-the-lms-integration-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/LMS Integration.md"]
---
# Does Query Service in LMS Integration Mean Ratan Query Service?

## Question

Does the generic “query service” named as the destination of a Lifecycle Service cashflow event refer to [[ratan-query-service]]?

## Evidence

The source states “Lifecycle service publish cashflow event to query service” and associates it with [[cash-settlement-orchestration-process-in]]. It does not use the name “Ratan Query Service,” identify a consumer, or describe any implementation behavior.

## Resolution criteria

Confirm the identity from an authoritative interface definition, service configuration, topic subscription, deployment record, or source code. Until then, the source must not be treated as evidence that [[ratan-query-service]] consumes this topic or follows its event-ordering and retry policies.
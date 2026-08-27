---
type: entity
title: Ratan Query Service
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, query-service, message-consumer, cqrs]
related: [ratanone-cashflow-service-cqrs-cashflow-events, what-version-ordering-policy-governs-ratan-query-service-event-consumption, what-retry-backoff-and-terminal-failure-policy-governs-ratan-query-service-consumption, query-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Ratan query service message consuming control.md"]
---
# Ratan Query Service

Ratan Query Service is the service implied by the source document’s message-consumption control questions. It is associated with the CQRS event table [[ratanone-cashflow-service-cqrs-cashflow-events]].

## Known concerns

The source identifies unresolved requirements for this consumer:

- ordering events using `businessVersion` and `minorVersion`;
- retry handling when `retryNum > 3`; and
- retry delay.

No consumer algorithm, retry configuration, dead-letter mechanism, or idempotency contract is supplied. The source does not establish that this component is identical to the existing [[query-service]] entity or its GraphQL read model.
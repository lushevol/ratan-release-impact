---
type: comparison
title: Message Bridge Filtering vs Domain Service Filtering
tags: [messaging, filtering, architecture, integration, capacity]
related: [message-bridge, domain-owned-message-filtering, message-topic-consolidation, message-header-propagation, should-message-bridge-own-business-filters, can-domain-services-handle-pass-through-message-volume]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Message Bridge Filters.md"]
---
# Message Bridge Filtering vs Domain Service Filtering

The source contrasts retaining first-level business filters in [[message-bridge|Message Bridge]] with moving filtering to domain services.

## Message Bridge Filtering

MB consumes messages from Solace queues, applies configured first-level filters, and routes selected messages onward.

Benefits stated by the source:

- centralized filter management;
- lower downstream-service processing demand;
- less log storage;
- less Kafka storage.

The stated drawback is that MB maintains business logic.

## Domain Service Filtering

MB passes messages and headers through, while each domain service applies business-specific consumption or publishing filters.

The stated benefit is a clearer domain-service boundary. The stated costs are greater downstream processing, log volume, and Kafka storage use.

The source highlights BCS settlement flow as a potential high-volume case, claiming that 99% of messages would be filtered. This is an unvalidated flow-specific claim.

## Decision Status

Neither approach is selected by the source. The conclusion field is blank, and no capacity benchmark, exception policy, filter contract, or rollback plan is supplied.

A decision should establish:

- the boundary between business filters and permissible technical or security filters;
- ownership of each filter;
- topic-consolidation compatibility;
- header propagation requirements;
- capacity and latency acceptance thresholds;
- replay, dead-letter, observability, and rollback behavior.
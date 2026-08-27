---
type: concept
title: Domain-Owned Message Filtering
tags: [messaging, filtering, domain-ownership, integration-architecture, kafka]
related: [message-bridge, message-header-propagation, message-topic-consolidation, message-bridge-filtering-vs-domain-service-filtering, should-message-bridge-own-business-filters, can-domain-services-handle-pass-through-message-volume, what-is-the-canonical-message-filter-sdk-and-configuration-contract, ratan, scbml]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Message Bridge Filters.md"]
---
# Domain-Owned Message Filtering

Domain-owned message filtering is an architectural model in which domain services evaluate business criteria for messages they consume or publish, while an integration component such as [[message-bridge|Message Bridge]] performs technical transport and routing.

## Proposed Application

The source proposes that MB pass messages through from Solace queues and preserve headers. Domain services would then apply filters appropriate to their business boundary, including:

- Group Service filtering BCS Cashflow messages;
- Trade service and Trade control service filtering by capture system;
- LMS Service filtering publication by BIC;
- BCS Cashflow Service filtering consumed Cashflow SCBML and LMS publication by BIC.

The source does not establish filter semantics, capture-system values, BIC rules, or ownership of individual filters.

## Trade-Off

This model improves separation between integration and business responsibilities, but transfers message inspection, processing, logging, and Kafka storage demand to domain services. The document explicitly identifies the BCS settlement flow as a high-risk case, stating that 99% of volume would be filtered. That figure is unvalidated and must not be generalized to other flows.

A transition requires capacity measurements, filter-outcome observability, failure handling, replay behavior, and rollback procedures. It also requires a canonical [[message-header-propagation|header contract]] and a defined filter SDK/configuration contract.

See [[message-bridge-filtering-vs-domain-service-filtering]] for the documented alternatives.
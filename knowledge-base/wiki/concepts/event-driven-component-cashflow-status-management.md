---
type: concept
title: Event-Driven Component Cashflow Status Management
created: 2026-08-22
updated: 2026-08-22
tags: [domain-events, cashflow-status, component-cashflow, eventual-consistency, netting, cashflow, event-driven-architecture, lifecycle]
related: [netting-and-lifecycle-service-separation, netting-service, netting-resultant-cashflow, ratan-external-and-internal-lifecycle-requests, cashflow-auto-netting, lifecycle-service, lifecycle-netting-responsibility-separation, resultant-cashflow-status-consistency]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Refactor Netting & Status Move Process.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Refactor Netting Process.md"]
---
# Event-Driven Component Cashflow Status Management

## Definition

Event-driven component cashflow status management is the proposed mechanism by which [[netting-service]] updates component cashflows in response to resultant-cashflow lifecycle changes.

The proposed implementation is the Netting Service function `manageComponentCashflowStatus`, which consumes a domain event from the `cash_settlement_cashflow_domain_events` topic.

## Proposed Behavior

Component-cashflow status management is required when the resultant cashflow status changes to:

- `released`
- `settled`

The operation performs the component-cashflow update after the resultant cashflow reaches the relevant lifecycle state. This isolates the reaction from the primary lifecycle status-update operation and supports a smaller direct transaction for a status change.

Moving component-status management to domain-event processing may also:

- Reduce work performed synchronously by the cashflow status-update API.
- Decouple resultant-cashflow lifecycle processing from component-cashflow side effects.
- Allow the primary status transition and downstream status synchronization to evolve independently.

These are design objectives, not measured results.

## Required Design Decisions

The source material does not specify the complete event contract or its operational guarantees. A production implementation needs to define:

- Event schema, versioning, and whether the event contains component identifiers.
- Producer and consumer ownership.
- Idempotent handling of duplicate deliveries.
- Ordering behavior, including late or out-of-order events and stale-event detection.
- Retry and dead-letter behavior.
- Replay and recovery after consumer failure.
- Monitoring, observability, and processing-lag measurement.
- Correlation between resultant and component cashflows.
- Reconciliation controls when a component update is unsuccessful.
- The recovery path when a resultant status change succeeds but component updates fail.
- Whether resultant statuses other than `released` and `settled` trigger processing.

The source does not define these controls or behaviors.

## Consistency Considerations

This design appears to move at least part of component-cashflow status management outside the primary transaction. It may therefore introduce temporary divergence between a resultant cashflow and its components.

Whether that divergence is acceptable depends on settlement, reporting, downstream messaging, and operational controls. The source material does not resolve whether the required model is:

- Atomic consistency.
- Eventual consistency.
- An explicit intermediate state.

These unresolved consistency concerns are tracked in [[resultant-cashflow-status-consistency]].

## Related Concepts

- [[netting-and-lifecycle-service-separation]]
- [[netting-resultant-cashflow]]
- [[ratan-external-and-internal-lifecycle-requests]]
- [[cashflow-auto-netting]]
- [[lifecycle-service]]
- [[lifecycle-netting-responsibility-separation]]
- [[resultant-cashflow-status-consistency]]
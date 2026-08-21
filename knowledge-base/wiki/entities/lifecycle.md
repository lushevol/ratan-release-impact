---
sources: ["summaries/service-catalog.md", "summaries/operations-runbook.md", "summaries/release-overview.md"]
type: "Product"
description: "Service in the Ratan platform that serves as system of record for case status and state transitions."
---

# Lifecycle

Lifecycle is a service in the [[entities/ratan]] platform that acts as the system of record for case status. It exposes REST endpoints for opening, pausing, resuming, and completing a case, and it emits a `case.completed` event only after persistence succeeds. This event is consumed by [[entities/orchestration]] to schedule downstream work.

## Role in Release 2026.08

In the [[summaries/release-overview]] release, Lifecycle works alongside [[entities/netting]] and [[entities/ssi-stamping]]. The release introduces [[concepts/correlation-ids]] across all services and a [[concepts/retry-budget]] for transient failures. Lifecycle's events are delivered asynchronously, supporting [[concepts/at-least-once-delivery]] semantics.

## Operational Considerations

The [[summaries/operations-runbook]] describes how operators handle settlement delays. Lifecycle's completion events can be replayed from the [[concepts/durable-log]] after a validation error is corrected. To avoid duplicate processing, consumers check the event ID against the [[concepts/idempotency]] record. When queue age exceeds ten minutes, operators inspect correlation IDs to determine whether work is waiting on Netting or SSI Stamping before retrying.

## Key Facts

- Owns case state transitions and is the system of record for case status.
- Exposes REST endpoints for lifecycle operations (open, pause, resume, complete).
- Publishes `case.completed` only after persistence succeeds.
- Emits events consumed by downstream services via [[concepts/event-driven-architecture]].
- Coordinates with other services as described in the [[summaries/service-catalog]].
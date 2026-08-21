---
sources: ["summaries/service-catalog.md", "summaries/operations-runbook.md", "summaries/release-overview.md"]
type: "Product"
description: "Workflow coordinator that orchestrates Netting and SSI Stamping in the settlement pipeline."
---

# Orchestration

Orchestration is one of the four services coordinated in the [[summaries/release-overview]] (Ratan Release 2026.08). It acts as the workflow coordinator in the settlement pipeline, turning lifecycle events into a dependency-aware work plan.

## Role in the Release

- Consumes the `case.completed` event emitted by [[entities/lifecycle]].
- Schedules downstream work after a case completes, following a fixed order: it calls [[entities/netting]] first, then [[entities/ssi-stamping]].
- Participates in the release-wide introduction of [[concepts/correlation-ids]] for end-to-end tracing, recording every attempt with the shared correlation ID.
- Uses the shared [[concepts/retry-budget]] of three attempts for transient downstream failures.
- Must tolerate [[concepts/at-least-once-delivery]], so duplicate events are handled via idempotent processing.
- Its interactions follow the [[concepts/event-driven-architecture]] used across the services, using JSON over HTTPS for synchronous calls and CloudEvents-compatible envelopes for asynchronous events.

## Operational Behavior

- For transient timeouts, Orchestration retries up to three times with exponential backoff, following the shared [[concepts/retry-budget]].
- Because delivery is at-least-once, duplicate `case.completed` events can arrive; operators verify the event ID and the consumer [[concepts/idempotency]] record. The expected result is one released settlement batch. If the idempotency record is missing, the affected workflow is paused and escalated to the platform owner.
- Validation errors are **not** retried blindly: an operator must first correct the case or settlement instruction, then replay the event from the [[concepts/durable-log]].
- During rollback, new releases are stopped, the durable event log is preserved, and a replay drill runs against a single test case before resuming production traffic.

## Related Entities

- [[entities/lifecycle]] — upstream service that emits the event Orchestration consumes.
- [[entities/netting]] — first downstream service called by Orchestration in the work plan.
- [[entities/ssi-stamping]] — second downstream service called in the settlement flow.
- [[entities/ratan]] — the product release that includes Orchestration.

## Risk Context

Orchestration is involved in the release risk around a potential mismatch between the [[entities/netting]] batch schema and the Orchestration consumer. The release checklist therefore includes contract tests to verify compatibility. Because the service must handle at-least-once delivery, runbooks emphasize validating idempotency records and replaying from the durable log to keep the workflow consistent during incidents.

## Related Documents
- [[summaries/operations-runbook]]
- [[summaries/service-catalog]]
---
sources: ["summaries/service-catalog.md", "summaries/operations-runbook.md", "summaries/release-overview.md"]
type: "Product"
description: "Ratan is the product delivering the 2026.08 release, coordinating four settlement services."
---

# Ratan

**Ratan** is the product that delivers the 2026.08 release, which coordinates four services: [[entities/lifecycle]], [[entities/netting]], [[entities/orchestration]], and [[entities/ssi-stamping]]. The release aims to make settlement workflows observable from intake through completion while preserving existing API contracts.

## Key Facts from [[summaries/release-overview]]

- Introduces [[concepts/correlation-ids]] across every service.
- Implements a [[concepts/retry-budget]] of three attempts for transient downstream failures.
- Supports rollback by redeploying the previous image and replaying events from a durable event log.
- Relies on [[concepts/event-driven-architecture]], with Lifecycle emitting the `case.completed` event that Orchestration consumes.
- Tracks queue age and failed batches on a dashboard for observability.

## Operational Facts from [[summaries/operations-runbook]]

- Operators use [[concepts/correlation-ids]] to determine whether delayed work is waiting on [[entities/netting]] or [[entities/ssi-stamping]] before retrying.
- Transient timeouts are retried by [[entities/orchestration]] up to three times with exponential backoff, matching the [[concepts/retry-budget]]; validation errors require correcting the instruction and replaying from the durable log.
- Duplicate completion events are resolved by checking the event ID and the consumer [[concepts/idempotency]] record, expecting one released settlement batch; a missing idempotency record pauses the workflow and escalates to the platform owner.
- Rollback preserves the durable event log, deploys the previous image, and runs a replay drill on a single test case before resuming production traffic, using [[concepts/durable-log]] to guarantee event recovery.

## Related Pages

- [[entities/lifecycle]]
- [[entities/netting]]
- [[entities/orchestration]]
- [[entities/ssi-stamping]]
- [[concepts/correlation-ids]]
- [[concepts/durable-log]]
- [[concepts/event-driven-architecture]]
- [[concepts/idempotency]]
- [[concepts/retry-budget]]
- [[summaries/operations-runbook]]
- [[summaries/release-overview]]

See also: [[summaries/service-catalog]]
---
type: "Concept"
sources: ["summaries/service-catalog.md", "summaries/operations-runbook.md", "summaries/release-overview.md"]
description: "Event-driven architecture coordinates settlement services through events, with retries, idempotency, and replay."
---

# Event-Driven Architecture

Event-driven architecture is a software design pattern in which services communicate by producing and consuming events rather than through direct synchronous calls. This approach decouples producers from consumers, allowing each service to evolve independently while still participating in a coherent workflow.

## Role in the Ratan Release

The Ratan Release 2026.08 (see [[summaries/release-overview]]) relies heavily on event-driven architecture to coordinate four services:

- **Lifecycle** ([[entities/lifecycle]]) owns case state transitions and emits a `case.completed` event.
- **Orchestration** ([[entities/orchestration]]) consumes that event and schedules downstream work.
- **Netting** ([[entities/netting]]) groups eligible obligations into settlement batches.
- **SSI Stamping** ([[entities/ssi-stamping]]) validates and records settlement instructions before a batch is released.

The event flow makes settlement workflows observable from intake through completion while preserving existing API contracts.

## Supporting Patterns

Event-driven systems typically rely on supporting mechanisms to ensure reliability and traceability:

- **Correlation IDs** ([[concepts/correlation-ids]]) are introduced across every service to trace a single case through the entire event chain. Operators use the correlation ID in the dashboard to determine whether work is waiting on Netting or SSI Stamping.
- **Retry budgets** ([[concepts/retry-budget]]) limit retry attempts for transient downstream failures. In the runbook, Orchestration may retry up to three times with exponential backoff for transient timeouts; validation errors are never retried blindly — the instruction is corrected and the event is replayed from the durable log.
- **Durable event logs** ([[concepts/durable-log]]) store events so rollback can be achieved by redeploying the previous image and replaying events. The runbook specifies preserving the durable log during rollback and running a replay drill against a single test case before resuming production traffic.
- **Idempotency** ([[concepts/idempotency]]) protects consumers from duplicate completion events. Operators check the event ID and the consumer idempotency record; if the record is missing, the workflow is paused and escalated to the platform owner. The expected result is exactly one released settlement batch.

These patterns are operationalized in [[summaries/operations-runbook]].

## Benefits and Risks

Benefits include loose coupling, scalability, and observability. Key risks are duplicate event delivery, stale settlement instructions, and schema mismatches between event producers and consumers. Proper contract testing, idempotency checks, and replay drills help mitigate these risks. When queue age exceeds ten minutes, operators compare event timestamps with service logs before retrying, avoiding unnecessary reprocessing.

## Related Pages

- [[summaries/release-overview]]
- [[summaries/operations-runbook]]
- [[concepts/correlation-ids]]
- [[concepts/retry-budget]]
- [[concepts/durable-log]]
- [[concepts/idempotency]]
- [[entities/lifecycle]]
- [[entities/orchestration]]
- [[entities/netting]]
- [[entities/ssi-stamping]]


See also: [[summaries/service-catalog]]
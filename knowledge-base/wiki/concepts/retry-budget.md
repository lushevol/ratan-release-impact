---
type: "Concept"
sources: ["summaries/service-catalog.md", "summaries/operations-runbook.md", "summaries/release-overview.md"]
description: "A policy capping retry attempts after transient failures, with exponential backoff and escalation paths."
---

# Retry Budget

A retry budget is a policy that caps the number of times an operation is retried after a transient failure. In the [[summaries/release-overview]], each service applies a retry budget of three attempts for transient downstream failures. The [[summaries/operations-runbook]] reinforces this: Orchestration may retry up to three times with exponential backoff. This means that if a downstream call fails, the system will retry up to three times before giving up and marking the operation as failed or routing it to a dead-letter queue.

## Why It Matters

Without a retry budget, systems can enter retry storms, overwhelming downstream services and delaying recovery. A small, explicit budget balances resilience with load control. It makes failure behavior predictable and observable, especially when combined with [[concepts/correlation-ids]] that trace each attempt across services.

## Relationship to Event-Driven Design

In an [[concepts/event-driven-architecture]], retries are often handled at the consumer level. The release's retry budget applies to transient downstream failures, while the durable event log provides a replay mechanism for more persistent issues. The budget complements the [[concepts/durable-log]] by limiting immediate retries and leaving a record for later replay.

The operations runbook adds an important distinction: retries are only appropriate for transient timeouts. Validation errors must not be blindly retried — instead, the case or settlement instruction should be corrected, then the event replayed from the durable log. This ties the retry budget to [[concepts/idempotency]]: duplicate completion events are checked against the consumer idempotency record, and if that record is missing, the workflow is paused and escalated.

## Operational Considerations

A retry budget should be paired with monitoring. The release's dashboard shows queue age and failed batches, helping operators see when retries are exhausted. The runbook instructs operators to inspect correlation IDs and compare timestamps before retrying, ensuring that retries are not wasted on issues that require manual correction. If a retry budget is exhausted, the escalation path may involve pausing the workflow and preserving the durable log, as done during rollback procedures.

Related: [[concepts/correlation-ids]], [[concepts/durable-log]], [[concepts/event-driven-architecture]], [[concepts/idempotency]], [[summaries/operations-runbook]], [[summaries/release-overview]]

See also: [[summaries/service-catalog]]
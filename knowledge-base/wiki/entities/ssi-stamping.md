---
sources: ["summaries/service-catalog.md", "summaries/operations-runbook.md", "summaries/release-overview.md"]
type: "Product"
description: "SSI Stamping is a service that validates and records settlement instructions for safe batch release."
---

# SSI Stamping

SSI Stamping is a service in the [[entities/ratan]] Ratan 2026.08 release. It validates settlement instructions against the approved counterparty profile and stores the stamped instruction version before a settlement batch is released for processing. It blocks release when an instruction is expired or has been superseded.

## Role in the workflow
SSI Stamping works alongside [[entities/lifecycle]], [[entities/netting]], and [[entities/orchestration]]. After Netting groups eligible obligations into batches, Orchestration calls SSI Stamping to verify settlement instructions and record the stamped version. This validation is the final gate before a batch is released, ensuring only current, approved instructions are used.

## Operational handling (from [[summaries/operations-runbook]])
The operations runbook defines how SSI Stamping participates in incident response. When queue age exceeds ten minutes, operators inspect the correlation ID in the dashboard to determine whether work is waiting on Netting or SSI Stamping. They compare event timestamps with service log timestamps before retrying.

For transient timeouts, Orchestration may retry up to three times with exponential backoff. However, for validation errors — a key SSI Stamping concern — operators must not retry blindly. Instead, they correct the case or settlement instruction, then replay the event from the [[concepts/durable-log]]. If duplicate completion events appear, operators check the event ID and the consumer's [[concepts/idempotency]] record; the expected result is one released settlement batch. If the idempotency record is missing, the workflow is paused and escalated to the platform owner.

These procedures rely on the [[concepts/correlation-ids]] introduced across the release, and complement the [[concepts/event-driven-architecture]] and [[concepts/retry-budget]] already noted in [[summaries/release-overview]].

## Shared contracts (from [[summaries/service-catalog]])
Like all services in the catalog, SSI Stamping uses JSON over HTTPS for synchronous calls and CloudEvents-compatible envelopes for asynchronous events. Every request includes `X-Correlation-Id`; every error includes a stable `code` and a human-readable `message`. This consistent contract supports troubleshooting and automation across the platform.

## Key facts from [[summaries/release-overview]]
- It is one of the four services coordinated in the release.
- The release introduces [[concepts/correlation-ids]] across every service, including SSI Stamping.
- Stale settlement instructions are a key risk, so SSI Stamping's validation is critical to settlement correctness.
- It participates in the release's [[concepts/event-driven-architecture]] and uses the [[concepts/retry-budget]] for transient downstream failures.

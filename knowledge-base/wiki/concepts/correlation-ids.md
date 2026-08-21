---
type: "Concept"
sources: ["summaries/service-catalog.md", "summaries/operations-runbook.md", "summaries/release-overview.md"]
description: "Unique IDs tracing settlement workflows across services, enabling observability and retry diagnosis."
---

## Correlation IDs

Correlation IDs are unique identifiers attached to every request or event, allowing a workflow to be traced end-to-end across multiple services. In the [[entities/ratan]] 2026.08 release, correlation IDs are introduced across every service — [[entities/lifecycle]], [[entities/netting]], [[entities/orchestration]], and [[entities/ssi-stamping]] — to make settlement workflows observable from intake through completion.

These IDs power the dashboard that shows queue age and failed batches. When queue age exceeds ten minutes, operators use the correlation ID to identify whether work is waiting on Netting or SSI Stamping, and compare the latest event timestamp with the service log timestamp before retrying. Correlation IDs also help diagnose duplicate event delivery, a key risk in [[concepts/event-driven-architecture]]. When duplicate completion events appear, operators check the event ID and the consumer idempotency record — the correlation ID ties these together so the expected result (one released settlement batch) can be verified.

Correlation IDs complement [[concepts/retry-budget]] by ensuring that retries can be tied back to the original workflow and its history. During rollback and replay drills, the final correlation IDs are recorded in the release report, supporting traceability.

See [[summaries/release-overview]] and [[summaries/operations-runbook]].

See also: [[summaries/service-catalog]]
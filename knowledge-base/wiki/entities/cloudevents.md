---
sources: ["summaries/service-catalog.md"]
type: "Work"
description: "CloudEvents is a standardized specification for describing event data in a common format."
---

CloudEvents is a specification that standardizes the envelope for asynchronous event data, allowing services to produce and consume events in a uniform way. In the context of the service catalog, all asynchronous events between services use CloudEvents-compatible envelopes, ensuring interoperability and consistent handling across the platform.

Key facts from the service catalog:
- It is used for all asynchronous communication, while synchronous calls use JSON over HTTPS.
- CloudEvents-compatible envelopes travel alongside the shared `X-Correlation-Id` header, enabling end-to-end tracing.
- The envelope format supports reliable eventing by providing a common structure for event metadata.

Related pages:
- [[concepts/event-driven-architecture]] – CloudEvents is a building block for event-driven systems.
- [[concepts/correlation-ids]] – Events carry correlation IDs for traceability.
- [[concepts/at-least-once-delivery]] – The eventing model must tolerate redelivery.
- [[entities/orchestration]] – Orchestration consumes lifecycle events to drive workflows.
- [[summaries/service-catalog]] – The source document describing this entity.
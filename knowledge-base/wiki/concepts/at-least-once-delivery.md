---
type: "Concept"
sources: ["summaries/service-catalog.md"]
description: "Delivery guarantee where a message may be delivered more than once, requiring idempotent consumers."
---

# At-Least-Once Delivery

At-least-once delivery is a messaging guarantee that ensures a message or event is never lost, but it may be delivered to a consumer more than once. This is a common trade-off in distributed systems: accepting duplicate deliveries in exchange for stronger reliability.

## Characteristics

- **No message loss**: The sender retries until it receives an acknowledgment, so the message is eventually delivered.
- **Possible duplicates**: Because retries can occur after the consumer processed the message but before the acknowledgment reached the sender, the consumer may see the same message multiple times.
- **Requires idempotent consumers**: Systems that rely on at-least-once delivery must be designed to handle duplicate events safely. [[concepts/idempotency]] is the key property that makes this possible.

## Role in the Service Catalog

The [[summaries/service-catalog]] explicitly states that the Orchestration service "must tolerate at-least-once delivery." This is a core requirement for the event-driven workflow that coordinates Netting and SSI Stamping.

When a `case.completed` event is published by the Lifecycle entity, Orchestration may receive it more than once. To handle this gracefully:

- Each attempt is recorded with a shared correlation ID (see [[concepts/correlation-ids]]).
- Operations such as Netting reject batches that cannot settle together, and those rejected batches are safe to retry after correction — meaning retries do not cause incorrect state.
- Consumers of events must treat duplicate deliveries as expected, not exceptional.

## Related Patterns

At-least-once delivery is often paired with:

- [[concepts/idempotency]] — duplicating an operation must not change the final result.
- [[concepts/retry-budget]] — retries are bounded and controlled to avoid infinite loops and excessive load.
- [[concepts/durable-log]] — a persistent record of events ensures that messages survive crashes and can be replayed.
- [[concepts/event-driven-architecture]] — asynchronous communication where delivery semantics like this are defined at the transport level.

In summary, at-least-once delivery is a pragmatic choice for systems that cannot afford to lose events, and it places a design burden on consumers to be idempotent and traceable.
---
type: query
title: What Is the Message Bridge Authoritative Retry and Terminal Failure Contract?
created: 2026-08-24
updated: 2026-08-24
tags: [message-bridge, kafka, retries, error-handling, failure-persistence]
related: [message-bridge, ratan-bridge-fail-message, retry-and-failure-persistence-semantics]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/[MB", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/[MB]An error occurs which cause the message to be lost.md"]An error occurs which cause the message to be lost.md"]An error occurs which cause the message to be lost.md"]
---
# What Is the Message Bridge Authoritative Retry and Terminal Failure Contract?

The incident source presents potentially overlapping retry mechanisms:

- `DispatchProducerRoute.onException` is described as performing six retries.
- Kafka is described as automatically retrying up to six times.
- The Kafka endpoint configuration contains `retries=10` and `retryBackoffMs=1000`.

The authoritative behavior is unresolved.

## Questions to resolve

- Which component owns retries: Kafka producer, Apache Camel error handler, `DispatchProducerRoute`, or multiple layers?
- What are the effective attempt count and backoff for a Kafka publication failure?
- Under what exact condition does processing enter `ExceptionProducerRoute`?
- When is [[ratan-bridge-fail-message]] written?
- Can a retry after ambiguous Kafka publication create a duplicate downstream message?
- Is `raw_message` the same store as `ratan_bridge_fail_message`?

Required evidence includes route error-handler configuration, Kafka producer configuration, retry metrics, exception-route traces, and database persistence logs.
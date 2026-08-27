---
type: query
title: How Should Message Bridge Clean Up Source and Target Deduplication Keys on Failure?
created: 2026-08-24
updated: 2026-08-24
tags: [message-bridge, redis, deduplication, idempotency, failure-recovery]
related: [message-bridge, message-bridge-deduplication-key-lifecycle, retry-and-failure-persistence-semantics]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/[MB", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/[MB]An error occurs which cause the message to be lost.md"]An error occurs which cause the message to be lost.md"]An error occurs which cause the message to be lost.md"]
---
# How Should Message Bridge Clean Up Source and Target Deduplication Keys on Failure?

The incident shows that a single mutable `DUPLICATION_CHECK_KEY` cannot safely represent both the source Solace delivery key and target Kafka publication key. When target processing overwrote the property, error cleanup removed only the target key and left the source key active for its 120-second TTL.

This stale source key suppressed a Solace redelivery after approximately 82 seconds.

## Questions to resolve

- Should source and target identities be stored in separate exchange properties or a structured key collection?
- Which key must be removed on successful publication, retryable failure, terminal failure, and failed persistence?
- Should a source key be committed only after durable downstream success?
- Should a terminal-failure record reserve the source identity, permit redelivery, or support a controlled replay process?
- Is TTL-only recovery acceptable for a delivery path requiring at-least-once behavior?
- What observability is required for key creation, deletion, expiry, and duplicate decisions?

The target state is a policy under which an unsuccessful delivery cannot suppress a valid recovery attempt.
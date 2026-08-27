---
type: concept
title: Message Bridge Deduplication Key Lifecycle
created: 2026-08-24
updated: 2026-08-24
tags: [message-bridge, deduplication, redis, idempotency, solace-redelivery]
related: [message-bridge, retry-and-failure-persistence-semantics, how-should-message-bridge-clean-up-source-and-target-deduplication-keys-on-failure]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/[MB", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/[MB]An error occurs which cause the message to be lost.md"]An error occurs which cause the message to be lost.md"]An error occurs which cause the message to be lost.md"]
---
# Message Bridge Deduplication Key Lifecycle

Message Bridge uses Redis keys to suppress duplicate processing. The incident demonstrates that source-delivery and target-publication identities require independent lifecycle management.

## Documented failure

`TargetSplittingRoute` stores a source Solace key in the mutable exchange property `DUPLICATION_CHECK_KEY`. `DispatchProducerRoute` later replaces that property with a target Kafka key. When send processing fails, `DuplicationCheckHelper.removeDuplicationKey(exchange)` removes only the current target key.

As a result, the source key remains active after the failed Kafka send.

For trace ID `7a756a7f83018dda1316ec41bcc9c661`, the source records:

- source key written at `09:51:12.922`;
- source-key TTL of 120 seconds;
- Solace redelivery at `09:52:34.696`, approximately 82 seconds later;
- redelivery evaluated as `is_duplicated = true` and filtered.

## Reliability requirement

A failed delivery must not cause an active deduplication marker to suppress a valid retry or transport redelivery. Source and target keys should therefore be independently retained, removed, expired, and observable.

The source does not determine the correct policy for key creation timing, successful-send cleanup, terminal-failure cleanup, or retention after durable failure persistence. These rules remain open in [[how-should-message-bridge-clean-up-source-and-target-deduplication-keys-on-failure]].
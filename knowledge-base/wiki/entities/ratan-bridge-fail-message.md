---
type: entity
title: ratan_bridge_fail_message
created: 2026-08-24
updated: 2026-08-24
tags: [database-table, message-bridge, failure-recovery, persistence]
related: [message-bridge, retry-and-failure-persistence-semantics, what-is-the-message-bridge-authoritative-retry-and-terminal-failure-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/[MB", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/[MB]An error occurs which cause the message to be lost.md"]An error occurs which cause the message to be lost.md"]An error occurs which cause the message to be lost.md"]
---
# ratan_bridge_fail_message

`ratan_bridge_fail_message` is the documented persistence target for Message Bridge messages that reach terminal exception handling.

The intended route is:

```text
ExceptionProducerRoute.process()
→ DIRECT_RAW_MESSAGE_PERSISTENCE_ROUTE
→ RawMessagePersistenceProducerRoute.saveRawMessage()
→ ratan_bridge_fail_message
```

In the reported `workerPool` incident, no corresponding record was observed. The source infers that retries were still active and `ExceptionProducerRoute` had not reached terminal processing, but this has not been verified with route metrics, error-handler configuration, or database write logs.

## Naming ambiguity

The source also refers to a `raw_message` table. It does not establish whether `raw_message` is another name for `ratan_bridge_fail_message`, a logical failure-message category, or a distinct physical store.

See [[what-is-the-message-bridge-authoritative-retry-and-terminal-failure-contract]].
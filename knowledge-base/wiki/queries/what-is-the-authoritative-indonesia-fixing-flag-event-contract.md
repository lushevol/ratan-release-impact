---
type: query
title: What Is the Authoritative Indonesia Fixing-Flag Event Contract?
created: 2026-08-24
updated: 2026-08-24
tags: [open-question, indonesia, fixing-flag, event-contract, kafka, solace]
related: [indonesia-pending-fixing-flag-relay, batch-service, message-bridge, kafka, solace]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Fixing Flag Process in Indonesia.md"]
---
# What Is the Authoritative Indonesia Fixing-Flag Event Contract?

The draft requires GDC to publish Indonesia pending-fixing-flag messages and Indonesia to consume them, but supplies no event definition.

The approved contract should define the payload, schema versioning, producer and consumer ownership, message key, cashflow and trade correlation identifiers, source-file lineage, timestamps, FMID/classification evidence, idempotency and deduplication behaviour, ordering, retry, dead-letter, replay, audit, and reconciliation requirements.

Until this is defined, the [[indonesia-pending-fixing-flag-relay]] is not implementation-ready.
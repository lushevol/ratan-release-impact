---
type: query
title: What Is the Canonical RATAN-to-eBBS Interface Contract?
tags: [ratan, ebbs, interface-contract, accounting, solace, json]
related: [ratan, ebbs, solace, ratan-ebbs-accounting-feed, ratan-interface-architecture, operational-level-agreement]
sources: ["RATAN/RATAN -Interfaces/Ratan and EBBS 14147.md"]
created: 2026-08-24
updated: 2026-08-24
---
# What Is the Canonical RATAN-to-eBBS Interface Contract?

The available interface overview states an intended JSON accounting feed from [[ratan]] to [[ebbs]] through [[solace]], but it does not provide an implementable or operationally complete contract.

## Evidence available

- RATAN is intended to generate payment-accounting entries.
- eBBS is the stated downstream recipient.
- Solace is the stated real-time transport.
- JSON is the stated message representation.
- The existing BPMS OLA is said to require no change.

## Information required

Establish or locate the authoritative specification for:

- Event triggers and applicable accounting-entry types
- JSON schema, required fields, optional fields, examples, and versioning
- Message, transaction, and correlation identifiers
- Solace topics, queues, subscriptions, environments, and producer/consumer ownership
- Authentication, authorization, and encryption
- Ordering, delivery guarantee, retries, idempotency, duplicate handling, and dead-letter processing
- Latency objective and the operational definition of “real time”
- Monitoring, alerting, reconciliation, incident handling, and escalation
- Interface-team contact and change-management process

## Related uncertainty

The referenced Interface Specification is an unavailable image attachment, and the source's publication status is blank. Any recovered contract should also confirm whether the consumer's canonical name is `eBBS` or `EBBS`.
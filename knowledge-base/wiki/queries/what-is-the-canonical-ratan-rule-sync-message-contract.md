---
type: query
title: What Is the Canonical RATAN Rule Sync Message Contract?
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, message-contract, solace, api, schema]
related: [ratan-global-rule-synchronization, rule-sync-idempotency-and-version-ordering, ratanone-rule-service, solace]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Global Rule Sync From Ratan GDC to Ratan ID.md"]
---
# What Is the Canonical RATAN Rule Sync Message Contract?

The source provides illustrative request and response examples but not a valid, versioned canonical contract. It varies field casing and spelling, including `requestId`, `request_id`, and `requestd`, and contains inconsistent response identifiers.

The contract must define:

- canonical field names and JSON schema;
- event types for create, update, deletion, enable, disable, retry, and manual resend;
- Solace topic, subscription, acknowledgment, replay, and dead-letter behavior;
- producer and consumer transaction boundaries;
- request-ID and version-based idempotency rules;
- response correlation and error semantics; and
- compatibility and schema-versioning policy.
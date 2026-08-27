---
type: query
title: What Is the LMS Integration Contract?
created: 2026-08-24
updated: 2026-08-24
tags: [lms, integration-contract, cash-settlement, event-driven]
related: [lms, lms-business-event-tracking, cash-settlement-orchestration-process-in, cash-settlement-cashflow-domain-events, trade-service-trade-events]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/LMS Integration.md"]
---
# What Is the LMS Integration Contract?

## Question

What does LMS represent, and what are its system role and contractual responsibilities for the documented cash-settlement events?

## Known evidence

The source names LMS only in its title and lists three business-event-to-topic associations. It does not define LMS or state whether it publishes, consumes, transforms, tracks, or reconciles those events.

## Information needed

- LMS expanded name, owner, service boundary, and business purpose.
- Publisher and consumer assignment for each topic.
- Messaging transport, topic ownership, ACLs, retention, consumer groups, and replay policy.
- Payload schemas, event types, keys, versioning, and compatibility rules.
- Processing outcomes, retries, DLQ behavior, reconciliation, monitoring, and alerting.
- BAU test cases, test ownership, environments, execution evidence, and acceptance criteria.
- Content of `attachments/image2023-4-19_15-31-41.png`.
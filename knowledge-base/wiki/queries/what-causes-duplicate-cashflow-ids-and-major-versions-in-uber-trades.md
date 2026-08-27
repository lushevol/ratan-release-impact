---
type: query
title: What Causes Duplicate Cashflow IDs and Major Versions in Uber Trades?
created: 2026-08-24
updated: 2026-08-24
tags: [uber, duplicate-key, cashflow, data-quality, idempotency]
related: [uber-inbound-message-idempotency-and-error-state, tdsx-uber-message-listener, kafka-persistent-retry-and-dlt-recovery]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/[group", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/[group]Analyzing uber msg would be deleted by wrongly in inbound table if any exception happen while Kafka topic consuming Uber msg.md"]Analyzing uber msg would be deleted by wrongly in inbound table if any exception happen while Kafka topic consuming Uber msg.md"]Analyzing uber msg would be deleted by wrongly in inbound table if any exception happen while Kafka topic consuming Uber msg.md"]
---
# What Causes Duplicate Cashflow IDs and Major Versions in Uber Trades?

The source records a separate non-consumption case for trade `7151397157`, correlation ID `f62f462588a404a5cf204757bb3231c3_7151397157`. A duplicate-key exception reportedly occurred because three cashflows had the same cashflow ID, `007390420129`, and the same major version.

## Scope

This data-integrity case should be investigated separately from the listener cleanup and retry defect. Both can result in incomplete consumption, but the source does not establish that the duplicate-key condition is caused by the same mechanism.

## Questions

- Which upstream system generated the duplicate cashflow records?
- What is the intended uniqueness key for cashflow identity and major version?
- Which database constraint raised the duplicate-key exception?
- Is the duplication valid under any event or amendment scenario?
- Can inbound reconciliation detect and quarantine this condition before group persistence fails?
- What correction and replay procedure is safe after upstream data is repaired?

The answer should inform the idempotency contract in [[uber-inbound-message-idempotency-and-error-state]].
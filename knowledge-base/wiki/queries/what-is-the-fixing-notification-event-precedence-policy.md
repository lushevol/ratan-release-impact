---
type: query
title: What Is the Fixing Notification Event Precedence Policy?
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, event-ordering, concurrency, idempotency, fixing-flag]
related: [fixing-notification-event-ordering, fixing-flag-notification-processing, lifecycle-service, cashflow-reinstatement-and-replay]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Fixing flag notification.md"]
---
# What Is the Fixing Notification Event Precedence Policy?

The fixing-flag design specifies outcomes for out-of-order and concurrent events but does not define how the system determines which event is authoritative.

## Questions

- Is precedence based on a source sequence number, event version, source timestamp, processing timestamp, or last-write-wins?
- What idempotency key identifies a notification?
- How are duplicate notifications prevented from repeatedly re-queueing or reinstating a cashflow?
- Are fixing-flag persistence and cashflow re-queueing atomic?
- How are notification-before-cashflow events correlated?
- What happens when a late notification carries an older fixing value?
- Which states are eligible for re-queueing or reinstatement?
- Do `failed` and `techfailed` follow the same recovery path?
- Does cancellation suppress only reprocessing, or all fixing-flag updates?

A decision is needed before the five scenarios can be implemented consistently.

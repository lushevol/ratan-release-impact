---
type: query
title: What Is the Canonical Cash Settlement Exception State Machine?
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, exception-handling, lifecycle, status-model]
related: [cash-settlement-exception-handling, cashflow-reinstatement-and-replay, cash-settlement-dependent-service-failure, adhoc-ssi-exception-lifecycle]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Exception Handling.md"]
---
# What Is the Canonical Cash Settlement Exception State Machine?

The exception-handling source uses `ERROR`, `FAILED`, `WAITING`, `READY+Pending Ack`, `RELEASED SETTLED`, `QUEUED+Pending Exception`, `TechFail`, and `TechFailed`, but does not define a canonical state machine or transition authority.

Questions to resolve:

- Are `TechFail` and `TechFailed` distinct persisted states, log labels, or alternate names for the same outcome?
- What exact relationship exists between `QUEUED+Pending Exception` and a technical failure?
- Which states support `ReInstate`, replay, amendment, or manual booking?
- Which actor is authorized to trigger each state transition?

A formal lifecycle contract is needed to prevent inappropriate recovery actions across different exception classes.
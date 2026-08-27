---
type: concept
title: Settlement Email Dispatch Audit
created: 2026-08-23
updated: 2026-08-23
tags: [audit, email-dispatch, exception-handling, settlement-affirmation]
related: [ratan, cdups, mdis, settlement-affirmation-email-automation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Derivative Settlement Affirmation - Email Automation.md"]
---
# Settlement Email Dispatch Audit

Settlement email dispatch audit records the lifecycle of an affirmation message from generation through client dispatch and failure handling.

CDUPS must return dispatch results to RATAN. RATAN records the dispatch date and time and supports filtering for successfully sent, failed, and pending-response cashflows. Delivery failures, including partial failures such as one NACK among multiple client IDs, must be reported to configured SCB contacts. Missing recipient configuration and other CDUPS dispatch issues must be visible to users.

The source does not yet define the precise meanings of acknowledgement, dispatch, delivery, NACK, retry, and client response.
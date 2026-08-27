---
type: query
title: What Is the CDUPS Affirmation Email Acknowledgement Contract?
tags: [cdups, acknowledgement, nack, solace, email-integration]
related: [cdups, solace, email-distribution-audit, outbound-affirmation-email]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Email Affirmation Automation/Email Affirmation Automation Tech Design.md"]
---
# What Is the CDUPS Affirmation Email Acknowledgement Contract?

The source requires distribution ack/nack for the proposed Solace-based CDUPS integration but does not define the contract.

The required specification includes the message schema, identifiers, acknowledgement states, failure taxonomy, timing guarantees, timeout behavior, retry policy, duplicate handling, idempotency, and distinction between CDUPS acceptance, dispatch, client delivery, and bounce.
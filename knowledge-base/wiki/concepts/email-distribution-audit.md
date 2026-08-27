---
type: concept
title: Email Distribution Audit
tags: [email, audit, cdups, acknowledgement, settlement]
related: [outbound-affirmation-email, cdups, solace, cashflow-affirmation-automation]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Email Affirmation Automation/Email Affirmation Automation Tech Design.md"]
---
# Email Distribution Audit

Email distribution audit records the lifecycle of an automated affirmation email between [[ratan]], [[cdups]], and the client.

The source identifies two separate timestamps:

1. The time the request is sent to CDUPS.
2. The time CDUPS sends the email to the client.

These events must not be conflated with client delivery, receipt, or affirmation. The source also requires distribution ack/nack but does not define its semantics.

## Required Audit Contract

The integration contract should distinguish, where supported:

- Submission from RATAN.
- Acceptance or rejection by CDUPS.
- Dispatch by CDUPS.
- Client delivery or bounce.
- Retry and resend attempts.
- Correlation identifiers and idempotency keys.
- Ack/nack payloads, status values, and failure reasons.
- Authoritative timestamps, timezones, and retention periods.

See [[what-is-the-cdups-affirmation-email-acknowledgement-contract]].
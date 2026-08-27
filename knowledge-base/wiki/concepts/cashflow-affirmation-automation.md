---
type: concept
title: Cashflow Affirmation Automation
tags: [cashflow, affirmation, email, settlement, stp, automation]
related: [outbound-affirmation-email, affirmation-response-processing, email-distribution-audit, ratan, cdups, ai-factory]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Email Affirmation Automation/Email Affirmation Automation Tech Design.md"]
---
# Cashflow Affirmation Automation

Cashflow affirmation automation is the proposed capability to obtain client confirmation of settlement cashflows through email and use the processed response to support automated settlement.

## Intended Flow

1. [[ratan]] assembles the cashflow details for an affirmation request.
2. An [[outbound-affirmation-email]] is submitted to [[cdups]].
3. CDUPS distributes the email to the client.
4. The client sends an affirmation response.
5. [[ai-factory]] processes the response.
6. RATAN uses a valid affirmative result to drive settlement.

## Preconditions for Automated Settlement

A complete design must define:

- An authoritative cashflow correlation key, likely including `FlowID`.
- The positive, negative, partial, ambiguous, duplicate, and late-response outcomes.
- AI confidence thresholds and a human-review route.
- RATAN state transitions that permit or prevent settlement.
- Idempotency across repeated sends, client replies, cashflow amendments, cancellations, and netting.
- Retention of the original response and the extracted result for audit.

The source establishes this as an intended capability rather than an implemented or validated workflow. The inbound portion is not designed; see [[affirmation-response-processing]].
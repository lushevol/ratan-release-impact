---
type: concept
title: Affirmation Response Processing
tags: [affirmation, inbound-email, ai, settlement, exception-handling]
related: [cashflow-affirmation-automation, ai-factory, ratan, cashflow-identifier]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Email Affirmation Automation/Email Affirmation Automation Tech Design.md"]
---
# Affirmation Response Processing

Affirmation response processing is the inbound capability required to turn a client email reply into an actionable affirmation result for settlement processing.

The source intends [[ai-factory]] to process client responses and drive automated settlement in [[ratan]], but provides no inbound-flow design. This concept is therefore a documented requirements gap rather than a settled implementation design.

## Required Design Decisions

An implementable process must specify:

- How inbound client messages are received.
- Accepted response formats, including free text, structured replies, and attachments.
- Correlation of a response to the original cashflow request.
- Interpretation of affirmative, negative, partial, ambiguous, and contradictory responses.
- Confidence scoring and the threshold for automatic processing.
- Human review and exception-management paths.
- Duplicate, late, and out-of-order response handling.
- RATAN lifecycle transitions and settlement gates.
- Audit retention for source emails, extracted values, decisions, and overrides.

See [[how-are-client-affirmation-responses-correlated-to-cashflows]] and [[what-ai-confidence-and-exception-rules-govern-automated-settlement]].
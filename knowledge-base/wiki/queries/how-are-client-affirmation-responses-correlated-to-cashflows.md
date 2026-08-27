---
type: query
title: How Are Client Affirmation Responses Correlated to Cashflows?
tags: [affirmation, inbound-email, correlation, cashflow]
related: [affirmation-response-processing, cashflow-affirmation-automation, outbound-affirmation-email, ai-factory, cashflow-identifier]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Email Affirmation Automation/Email Affirmation Automation Tech Design.md"]
---
# How Are Client Affirmation Responses Correlated to Cashflows?

The draft provides no inbound integration design. Although `FlowID` is mandatory in the outbound email, the source does not state that the client must return it or that it is the authoritative correlation key.

The correlation design must address replies containing no identifier, multiple cashflows, netted resultant cashflows, amended or cancelled cashflows, duplicate replies, forwarded email threads, and late responses.
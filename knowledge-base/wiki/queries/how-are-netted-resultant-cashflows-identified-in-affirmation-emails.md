---
type: query
title: How Are Netted Resultant Cashflows Identified in Affirmation Emails?
tags: [netting, cashflow, affirmation, correlation]
related: [outbound-affirmation-email, cashflow-affirmation-automation, cashflow-identifier, cashflow-aggregation-lineage]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Email Affirmation Automation/Email Affirmation Automation Tech Design.md"]
---
# How Are Netted Resultant Cashflows Identified in Affirmation Emails?

The draft uses the literal value `Net` as `Trade ID` for netted resultant cashflows and allows `Entity` and `Counterpart` to be blank.

This makes `Trade ID` unsuitable as a unique correlation key for these emails. The authoritative identifier, lineage information, and client-visible presentation for netted resultant cashflows must be defined. `FlowID` is mandatory in the draft but has not been confirmed as the authoritative inbound-response correlation key.
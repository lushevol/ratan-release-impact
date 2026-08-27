---
type: query
title: What Are the Authoritative Mandatory Fields for Affirmation Emails?
tags: [affirmation, email, cashflow-data, requirements]
related: [outbound-affirmation-email, cashflow-affirmation-automation, cashflow-identifier]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Email Affirmation Automation/Email Affirmation Automation Tech Design.md"]
---
# What Are the Authoritative Mandatory Fields for Affirmation Emails?

The proposed field list is explicitly subject to business confirmation.

The current draft marks `Counterpart` as mandatory while allowing it to be blank for netted resultant cashflows. It also provides no formats, validation constraints, definitions for beneficiary fields, or rule for conflicting `Amount` sign and `SCB Pay / Receive` values.

A confirmed data contract is required before building the email template or validation logic.
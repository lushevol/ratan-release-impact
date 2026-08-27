---
type: concept
title: Email-Based Cashflow Affirmation
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, affirmation, email, settlement, stp]
related: [affirmation-driven-cashflow-release, ai-factory-layer, ratan, sci, murex, what-is-the-authoritative-email-affirmation-eligibility-schedule-and-configuration-model, what-cashflow-and-settlement-instruction-data-may-be-disclosed-in-affirmation-emails, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requir--vhh9uf]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Email Affirmation Automation.md"]
---
# Email-Based Cashflow Affirmation

Email-based cashflow affirmation is a proposed settlement capability in which selected cashflow details are sent to a client by email and a returned affirmation is used as input to settlement processing.

The proposed payload includes trade and cashflow identifiers, value date, currency, amount, pay/receive direction, and optional settlement-instruction information. [[sci]] is the proposed source for booking-entity and counterparty FMCODE fields, while [[murex]] provides `Murex_Product_Strategy`.

For netted resultant cashflows, the requirement specifies that `Trade_Id` must be displayed as `Net`; counterpart may be blank, and taxonomy and portfolio are optional. This is an outbound-display rule and does not define the underlying netting lifecycle.

This remains a draft proposal. It does not define selection criteria, email timing, approved recipients, response correlation, authentication, or exception handling. The sensitive-data implications of including beneficiary account numbers and BICs are unresolved.
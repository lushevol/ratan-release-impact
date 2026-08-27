---
type: concept
title: Affirmation Email Scope Configuration
created: 2026-08-23
updated: 2026-08-23
tags: [scope, configuration, cashflow, settlement-affirmation]
related: [ratan, settlement-affirmation-email-automation, booking-and-counterparty-fmcode, cashflow-auto-netting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Derivative Settlement Affirmation - Email Automation.md"]
---
# Affirmation Email Scope Configuration

Affirmation email scope configuration determines which RATAN cashflows are published to CDUPS. Criteria may include Booking Entity, FMID or BIC, client, product, portfolio, source, payment type, settlement method, transaction ID, and cashflow or post-UBER trade values.

Status scenarios include sending selected WAITING and Pending Operator flows while excluding STP flows, or including all valid client cashflows. Processing states such as Pending fixing and Pending Another Leg are excluded. Additional exclusions include SLT-CUST, Loan-related cashflows, selected Swap Agent payment types, CCIL deals, SIP strategies, and selected Eclipse corporate clients.

These rules are specific to affirmation communication and must not be assumed to govern unrelated cashflow workflows.
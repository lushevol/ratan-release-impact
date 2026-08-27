---
type: concept
title: Outbound Affirmation Email
tags: [email, cashflow, affirmation, outbound, cdups]
related: [cashflow-affirmation-automation, email-distribution-audit, cdups, solace, cashflow-identifier]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Email Affirmation Automation/Email Affirmation Automation Tech Design.md"]
---
# Outbound Affirmation Email

An outbound affirmation email is a client-facing email containing cashflow details for confirmation. It is intended to replace the manual BAU process of collecting details, drafting an email, and sending it to a client.

## Proposed Payload

The draft requires `Trade ID`, `FlowID`, `Value Date`, `Counterpart`, `Cur`, `Amount`, and `SCB Pay / Receive`, while several other fields are optional.

`FlowID` is the required cashflow-level identifier and is the most plausible correlation value for future client-response processing, subject to confirmation.

## Netted Resultant Cashflows

For a netted resultant cashflow:

- `Trade ID` must be the literal `Net`, rather than a parent trade identifier.
- `Entity` may be blank.
- `Counterpart` may be blank, despite being marked mandatory.
- `Taxonomy` and `Portfolio` are optional.

The email must not use `Trade ID` alone for correlation because `Net` is not unique. See [[how-are-netted-resultant-cashflows-identified-in-affirmation-emails]].

## Direction Consistency

The `Amount` convention encodes SCB direction:

- Negative amount: SCB Pay.
- Positive amount: SCB Receive.

Because the payload also contains `SCB Pay / Receive`, the implementation requires a validation rule for mismatches between the direction label and amount sign.

## Unspecified Requirements

The source does not define the email template, recipient resolution, sender identity, formatting, field validation, amendment handling, duplicate-send controls, encryption, or sensitive-data protection.
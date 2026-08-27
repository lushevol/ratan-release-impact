---
type: source
title: Email Affirmation Automation Tech Design
authors: []
year: 2026
url: ""
venue: Internal technical design
tags: [cash-settlement, email-affirmation, automation, ratan, cdups, solace]
related: [cashflow-affirmation-automation, outbound-affirmation-email, affirmation-response-processing, email-distribution-audit, cdups, ai-factory, solace, ratan]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Email Affirmation Automation/Email Affirmation Automation Tech Design.md"]
---
# Email Affirmation Automation Tech Design

## Purpose

This draft design proposes automated client email affirmation to increase settlement straight-through processing (STP). The intended end-to-end flow is:

1. RATAN prepares and sends an affirmation email to the client.
2. The client responds to the email.
3. An AI factory layer processes the response.
4. The processed response drives automated settlement in RATAN.

The source defines part of the outbound distribution requirement but leaves the RATAN workflow and inbound affirmation integration as TBU or draft content.

## Outbound Email Proposal

The automated process is intended to reproduce the daily BAU activity in which users collect mandatory cashflow details, draft an email, and send it to the client.

The design proposes reuse of [[cdups]] existing email-distribution capability, with [[solace]] as the connection protocol. It references:

[Outbound Affirmation Emails - FM re-platforming - Confluence](https://confluence.global.standardchartered.com/display/FMRP/Outbound+Affirmation+Emails)

The stated outbound requirements are:

- Confirm the mandatory cashflow details with the business.
- Define country-specific email sending timing.
- Audit the time sent to CDUPS and the time CDUPS sends the email to the client.
- Confirm non-functional requirements with the Product Owner.
- Define CDUPS distribution ack/nack behavior.

## Proposed Cashflow Detail Contract

The following table is reproduced from the source and remains subject to business confirmation.

| Email Field Name | Mandatory (Y/N) | Description | User Email Sample |
| --- | --- | --- | --- |
| Trade ID | Y | for Gross cashflow, value is parent trade id, for netted resultant cashflow, value is **Net** | |
| FlowID | Y | cashflow id | |
| Entity | N | cashflow booking entity name, could be blank for net resultant | |
| Value Date | Y | value date | |
| Counterpart | Y | counterparty name, could be blank for net resultant | |
| Cur | Y | currency | |
| Amount | Y | credit / debit, SCB pay will be less than zero (-12,270.00), SCB receive will be greater than zero (12,270.00) | |
| SCB Pay / Receive | Y | SCB Pay / SCB Receive | |
| Taxonomy | N | optional for resultant cashflow | |
| Portfolio | N | optional for resultant cashflow | |
| Strategy | N | | |
| Bene_AC | N | | |
| Bene_Agent | N | | |
| Bene_Int | N | | |

## Noted Data Rules and Ambiguities

- For gross cashflows, `Trade ID` is the parent trade ID. For netted resultant cashflows, it is the literal value `Net`.
- `FlowID` is mandatory and is the stated cashflow identifier; it is a likely correlation candidate for future inbound processing.
- `Entity` and `Counterpart` may be blank for net resultant cashflows. This conflicts with the `Counterpart` mandatory designation and requires an explicit exception rule.
- `Amount` sign indicates direction: a negative amount is SCB Pay and a positive amount is SCB Receive.
- `SCB Pay / Receive` represents the same direction independently. Validation and precedence are unspecified if this field conflicts with the amount sign.
- Definitions and formatting rules for `Bene_AC`, `Bene_Agent`, and `Bene_Int` are not provided.

## Distribution and Audit Boundary

The design distinguishes two distribution events:

1. Submission of the request to CDUPS.
2. CDUPS sending the email to the client.

It does not define whether either event demonstrates client delivery, whether bounce or delivery evidence is required, or which timestamp is authoritative for reporting. See [[email-distribution-audit]].

## Inbound Processing Gap

The section titled *Automated Affirmation Integration (Inbound Flow)* contains no substantive design. The source does not define how client emails are received, correlated, interpreted by [[ai-factory]], reviewed when uncertain, or translated into a RATAN state transition.

Consequently, the proposed settlement automation objective cannot be implemented from this document alone. See [[affirmation-response-processing]] and [[cashflow-affirmation-automation]].

## Open Requirements

- [[what-are-the-authoritative-mandatory-fields-for-affirmation-emails]]
- [[how-are-netted-resultant-cashflows-identified-in-affirmation-emails]]
- [[what-is-the-authoritative-country-specific-affirmation-email-timing]]
- [[what-is-the-cdups-affirmation-email-acknowledgement-contract]]
- [[how-are-client-affirmation-responses-correlated-to-cashflows]]
- [[what-ai-confidence-and-exception-rules-govern-automated-settlement]]
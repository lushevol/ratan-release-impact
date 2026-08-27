---
type: source
title: Email Affirmation Automation
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, affirmation, email, stp, functional-requirement, settlement-day2]
related: [ratan, ai-factory-layer, email-based-cashflow-affirmation, affirmation-driven-cashflow-release, sci, murex, held-cashflow-reinstatement, dvp-nstp-exception-handling, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requi--1x97cc1]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Email Affirmation Automation.md"]
authors: []
year: 2026
url: ""
venue: "Settlement Day2 Requirement"
---
# Email Affirmation Automation

This draft functional requirement proposes email-based cashflow affirmation to improve settlement straight-through processing (STP). It proposes that [[ratan]] sends selected cashflow details to a client, receives an affirmation through an [[ai-factory-layer]], and releases an eligible cashflow from the NSTP queue.

The document describes intended behavior, not an approved implementation or confirmed production capability. Eligibility, scheduling, authentication, response validation, exception handling, and release controls remain undefined.

## Proposed workflow

1. A cashflow is received in [[ratan]] and held in `WAITING` with a “Pending Affirmation” status.
2. The system sends an affirmation email at a scheduled time.
3. A user replies with an affirmation.
4. The system receives the confirmation through a technical integration.
5. The system triggers STP by closing the “pending affirmation” exception and releasing the cashflow from the NSTP queue.

The requirement does not specify the authoritative exception code, post-release status, release atomicity, duplicate-reply behavior, or downstream payment, SWIFT, accounting, and audit effects.

## Candidate outbound email fields

| Email Field Name | Logic Model Field | Mandatory (Y/N) | Description |
|---|---|---:|---|
| Trade ID | `Trade_Id` | Y | For gross cashflow, the value is the parent trade ID. For netted resultant cashflow, the value is `Net`. |
| FlowID | `Cashflow_Id` | Y | Cashflow ID. |
| Entity | `Booking_Entity_SCI_FMCODE` | ? | Cashflow booking entity name. |
| Value Date | `Payment_Date` | Y | Value date. |
| Counterpart | `Counterparty_SCI_FMCODE` | ？ | Counterparty name; may be blank for a net resultant. |
| Cur | `Payment_Currency` | Y | Currency. |
| Amount | `Payment_Amount` | Y | Credit/debit amount. SCB pay is less than zero, for example `-12,270.00`; SCB receive is greater than zero, for example `12,270.00`. |
| SCB Pay / Receive | `Pay_Receive_Indicator` | Y | SCB Pay / SCB Receive. |
| Taxonomy | `ISDA_Taxonomy` | N | Optional for resultant cashflow. |
| Portfolio | `Booking_Entity_Trade_Portfolio_Name` | N | Optional for resultant cashflow. |
| Strategy | `Murex_Product_Strategy` | N |  |
| Bene_AC | `Settlement_Instruction.Account. Beneficiary_Account_Number` | N | Proposed special format: hide part of the number, for example `XXX XXX 51869`. |
| Bene_Agent | `settlement_Instruction.account. beneficiary_Bank_BIC_code` | N |  |
| Bene_Int | `settlement_Instruction.account. beneficiary_Correspondent_BIC_code` | N |  |

The settlement-instruction paths have inconsistent capitalization in the source. The mandatory status of Entity and Counterpart is undecided. The source also does not specify whether FMCODE values must be translated to display names.

## Unresolved requirement areas

- Whether dispatch occurs at `VD -1` or another configurable schedule.
- Cashflow eligibility criteria, including booking entity, payment date, status, and exception code.
- Whether eligibility rules and email properties are hard-coded or dynamically configured.
- Client/contact identity, authorization, and cashflow entitlement.
- Reply-to-cashflow correlation, confirmation validity, and replay protection.
- The AI factory layer’s authority, confidence threshold, output contract, and manual-review path.
- Processing of rejection, silence, ambiguity, partial confirmation, late response, duplicate response, amendment, withdrawal, and already-settled cashflows.
- Masking, encryption, recipient controls, retention, and audit policy for beneficiary account and BIC data.

See [[email-based-cashflow-affirmation]] for the proposed end-to-end capability and [[affirmation-driven-cashflow-release]] for the intended `WAITING` and NSTP release chain.
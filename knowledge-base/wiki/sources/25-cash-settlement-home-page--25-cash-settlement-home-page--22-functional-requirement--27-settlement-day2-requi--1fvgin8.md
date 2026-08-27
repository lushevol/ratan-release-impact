---
type: source
title: Derivative Settlement Affirmation - Email Automation
authors: []
year: 2026
url: ""
venue: "Cash Settlement Home Page functional requirements"
created: 2026-08-23
updated: 2026-08-23
tags: [settlement, affirmation, email-automation, RATAN, CDUPS, MDIS, artificial-intelligence]
related: [ratan, cdups, mdis, settlement-affirmation-email-automation, affirmation-email-scope-configuration, settlement-email-template-and-contact-governance, settlement-email-dispatch-audit, ai-assisted-affirmation-response-classification, affirmation-email-cashflow-correlation, cashflow-lineage-and-amendment-correlation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Derivative Settlement Affirmation - Email Automation.md"]
---

# Derivative Settlement Affirmation - Email Automation

## Summary

This functional requirement defines automation for outbound derivative settlement-affirmation emails and inbound processing of client responses. The design separates responsibilities across [[entities/ratan]], [[entities/cdups]], [[entities/mdis]], and an AI classification layer.

RATAN determines the cashflow population, applies configurable scope and status rules, publishes cashflow and settlement-instruction data, schedules or suppresses triggers, and records dispatch outcomes. CDUPS maintains templates and client contacts, generates and dispatches emails through MDIS, applies encryption where required, and returns audit and exception information to RATAN.

## Outbound automation

RATAN must support granular publishing criteria based on Booking Entity, client FMID or BIC, client, product, portfolio, source, payment type, settlement method, and cashflow or post-UBER trade values. Configuration must support both scenario-specific status rules and broader inclusion of valid cashflows, including STP flows where required.

The requirements identify the following affirmation exclusions or routing conditions:

- Pending fixing and Pending Another Leg cashflows are excluded while processing is incomplete.
- SLT-CUST and Loan-related cashflows are excluded.
- Swap Agent Coupon and Interim MTM payments are excluded.
- CCIL deals are excluded from this email trigger.
- SIP trades may be excluded by strategy.
- Eclipse corporate clients may be excluded while interbank flows remain in scope according to portfolio.
- Islamic trades may require separate routing when the portfolio begins with `ISL`; feasibility and FMRP taxonomy support remain to be confirmed.
- NDF deals may be split between Razor and RATAN and therefore require clear ownership of affirmation scope.

The source requests affirmation based on transaction ID rather than only on trades that fail STP. The process must include client SSI information, SCB Nostro information, and, for netting scenarios, both the net amount and the underlying cashflow breakdown. IRS and CCS calculation details are identified as an area for exploration.

RATAN must support configurable trigger times, including one time for multiple Booking Entities, Booking Entity-specific times, one release time across a Booking Entity's clients, and different release times for individual clients. East sites are given as an example requiring publication at 1pm MYT; West-country timing is not settled.

RATAN must also support manual triggers for new or revised cashflows and manual suppression of publication. Revised cashflows may require email regeneration with updated details.

## CDUPS configuration and dispatch

CDUPS must maintain standard templates and configurable variants for Gross, Bilateral Netting, and BIC Netting settlements. Templates may vary by country, product, client, location, strategy, subject, body, and other parameters. Chaser capability using the original email is identified for a later phase.

Client contacts require maker-checker maintenance. Contacts may be configured at FMID or BIC level and by product taxonomy granularity, with support for both Murex and FMRP. Contacts for affirmation must be stored separately from Confirmation and FX-netting contacts.

The contact model must support:

- One address across several products.
- Separate emails to the same address for different products.
- Different addresses for different products.
- Product-specific bank-client contacts.
- Configurable copies to SCB contacts by Booking Entity and Product.

The sample addresses are illustrative rather than production configuration:

- UOB OPT: `CommoditiesDerivatives@UOBgroup.com`
- UOB FX: `TCMOPreciousMetals@UOBgroup.com`
- Nomura OPT: `otcsettlements@nomura.com`
- Nomura FX: `fxopssettlements@nomura.com`

CDUPS generates the email and sends it through [[entities/mdis]]. Attachments must be encrypted according to bank standards. Dispatch audit information must record success or failure and feed back to RATAN. RATAN must store the client-email dispatch date and time and allow filtering for successful, failed, and pending-response states.

Delivery failures must be reported to configured SCB contacts, including partial failure cases such as one NACK among multiple client IDs. CDUPS must highlight configuration problems, such as missing email addresses, to users. The authoritative sender address and the distinction between acknowledgement, dispatch, delivery, and client response remain unresolved.

## Inbound AI response automation

Inbound client responses are routed to an AI layer that classifies each response as positive, negative, or ambiguous. The outcome is sent to RATAN as a positive indicator such as `Y/N`, with an audit trail covering both the outbound email and received response.

For a positive affirmation, RATAN records a checker indicator showing that the affirmation is AI-based and removes the pending affirmation check, thereby automating the maker portion. The cashflow remains NSTP when other outstanding exceptions remain.

Negative or ambiguous responses receive a maker-intervention indicator. They do not automatically clear the affirmation requirement. The source does not define model confidence thresholds, classification evidence, override permissions, retention, or remediation for misclassification.

## Operational gaps

The source identifies several unresolved integration and control questions:

- How late-arriving cashflows are linked to a prior email batch.
- The canonical identifier for correlating an email, response, transaction, and cashflow version.
- Rule precedence when client, product, portfolio, strategy, and settlement-method criteria overlap.
- Whether exclusions are configurable, hard-coded, or both.
- Retry behavior and status semantics for dispatch failures and partial failures.
- The sender address to which clients should reply.
- Handling of client-initiated or manually sent affirmation emails.
- Suppression behavior when data has already been sent to CDUPS versus when it remains in RATAN.
- AI confidence, human override, and audit requirements.

These requirements are specific to settlement-affirmation communications and should not be generalized to unrelated RATAN workflows such as auto-netting, auto-DVP, cashflow splitting, or manual fail.
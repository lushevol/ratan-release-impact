---
type: concept
title: SCBML CashflowData Message
created: 2026-08-23
updated: 2026-08-23
tags: [SCBML, CashflowData, LMS, XML, integration]
related: [scbml, lms, swift-suppressed-lms-feed-contract, manual-entity-lms-reference-data-feed]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/LMS/Include Swift Suppressed status in LMS feed (only for receipts).md"]
---
# SCBML CashflowData Message

The SCBML `CashflowData` message is the proposed downstream payload for sending cashflow information to LMS.

## Message structure

The template contains:

- An SCBML `4-0` envelope.
- Header metadata, sender information, timestamps, and tracking ID.
- An `Insert` processing event.
- A cashflow business event, such as `New` or `Withdrawal`.
- Netting and cashflow identifiers.
- Payment amount, currency, date, and party references.
- Trade ID, source system, product, allotment, portfolio, and workflow state.
- Party, FM, legal-entity, and dealer identifiers.
- Optional cashflow SSI and routing information.

## Contract limitation

The message template does not explicitly map the `Swift Suppressed` cashflow status. It is therefore not sufficient to infer that LMS can distinguish:

- An initial receipt in Swift Suppressed status.
- Undo Swift Suppression.
- A withdrawal that changes the cashflow to `CANCELLED`.
- Manual Failed status.

The LMS team must confirm the event vocabulary, status representation, payload requirements, and behavior for absent SSI data.

---
type: concept
title: Derivative Settlement Affirmation Email Routing
created: 2026-08-23
updated: 2026-08-23
tags: [derivative-settlement, affirmation, email-automation, routing, counterparty-data]
related: [murex, booking-and-counterparty-fmcode, is-counterparty-fmid-400799441-duplicated-or-misassigned, what-is-the-authoritative-affirmation-email-routing-key, how-are-affirmation-email-addresses-validated-and-governed]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Derivative Settlement Affirmation - Email Automation/Cashflow Scope & Email Ids.md"]
---
# Derivative Settlement Affirmation Email Routing

Derivative settlement affirmation email routing is the configuration-driven selection of recipients for settlement or affirmation communications based on counterparty and product context.

The supplied matrix indicates a configuration dependency for `SCB LONDON*LDN`: rows associate a Counterparty FMID and, in most cases, [[murex]] Family, Group, and Type values with destination addresses.

## Apparent selection attributes

The matrix contains the following potential routing attributes:

- Booking Entity
- Counterparty FMID
- Commodity Flag
- Murex Family
- Murex Group
- Murex Type
- Strategy
- Stella Taxonomy
- Settlement Method

It does not specify which attributes form the authoritative key, their precedence, whether blank values are wildcard criteria, or which attributes are mandatory. The repeated FMID identified in [[is-counterparty-fmid-400799441-duplicated-or-misassigned]] means an FMID-only match is not safe to assume.

## Recipient-control requirements not specified

The source records recipient lists but does not define:

- whether addresses are To, CC, or BCC recipients;
- whether multiple destinations are sent in one message or separately;
- behavior when no configuration matches;
- validation before a contact is activated;
- treatment of malformed addresses;
- delivery retry, alerting, or manual remediation;
- approval, ownership, recertification, and change control.

These gaps are tracked in [[what-is-the-authoritative-affirmation-email-routing-key]] and [[how-are-affirmation-email-addresses-validated-and-governed]].

## Scope boundary

The source is evidence for a routing matrix, not an end-to-end automation design. It does not identify a sending application, a triggering cashflow or trade event, an integration flow, or a settlement-state eligibility rule.
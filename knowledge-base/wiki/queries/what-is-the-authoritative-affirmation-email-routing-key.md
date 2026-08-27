---
type: query
title: What Is the Authoritative Derivative Settlement Affirmation Email Routing Key?
created: 2026-08-23
updated: 2026-08-23
tags: [derivative-settlement, affirmation, email-routing, reference-data, murex]
related: [derivative-settlement-affirmation-email-routing, murex, booking-and-counterparty-fmcode, is-counterparty-fmid-400799441-duplicated-or-misassigned]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Derivative Settlement Affirmation - Email Automation/Cashflow Scope & Email Ids.md"]
---
# What Is the Authoritative Derivative Settlement Affirmation Email Routing Key?

The routing matrix includes Booking Entity, Counterparty FMID, Commodity Flag, Murex Family, Murex Group, Murex Type, Strategy, Stella Taxonomy, and Settlement Method. It does not declare an authoritative matching key or precedence rule.

## Questions to resolve

- Is Counterparty FMID sufficient, or is a compound key required?
- Which Murex attributes are mandatory for matching?
- Are blank values wildcards, ignored values, or invalid configuration?
- What is the priority between an exact product classification match and a less-specific row?
- Are Strategy, Stella Taxonomy, Settlement Method, and the unnamed columns reserved future criteria or omitted required data?
- What happens when zero, one, or multiple records match?
- How are recipient roles represented when a row contains multiple addresses?

The duplicate `400799441` entry makes this an implementation-critical question. The source supports a configuration-based routing model but does not provide an executable contract.

See [[derivative-settlement-affirmation-email-routing]] and [[is-counterparty-fmid-400799441-duplicated-or-misassigned]].
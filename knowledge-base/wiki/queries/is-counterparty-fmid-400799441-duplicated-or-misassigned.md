---
type: query
title: Is Counterparty FMID 400799441 Duplicated or Misassigned?
created: 2026-08-23
updated: 2026-08-23
tags: [counterparty-fmid, data-quality, email-routing, derivative-settlement]
related: [derivative-settlement-affirmation-email-routing, booking-and-counterparty-fmcode, what-is-the-authoritative-affirmation-email-routing-key]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Derivative Settlement Affirmation - Email Automation/Cashflow Scope & Email Ids.md"]
---
# Is Counterparty FMID 400799441 Duplicated or Misassigned?

The source contains two routing entries for Counterparty FMID `400799441` under `SCB LONDON*LDN`:

- an unclassified row routed to `SG-Commodities Derivatives` at UOBgroup.com;
- a `NOMURAFIN/TYO`, `CS`, `IRD` row routed to Nomura OTC settlements.

The records have materially different classification and recipient data.

## Why this matters

If the FMID is an exclusive counterparty identifier or the primary routing key, the duplicate can cause incorrect recipient selection. If both rows are valid, the routing contract must specify the compound attributes that select one record rather than the other, including the semantics of missing Murex classification values.

## Required resolution

Confirm whether either entry is misassigned, whether both are valid, and what key dimensions disambiguate them. Do not implement or rely on an FMID-only routing rule until this is resolved.

See [[derivative-settlement-affirmation-email-routing]] and [[what-is-the-authoritative-affirmation-email-routing-key]].
---
type: source
title: Ratan and Falcon 55055
authors: []
year: 2026
url: ""
venue: ""
created: 2026-08-25
updated: 2026-08-25
tags: [ratan, falcon, interface, market-data, pv, bts]
related: [ratan, falcon, tds3, solace, ratan-falcon-market-data-interface, ratan-bts-pv-calculation, what-is-the-authoritative-ratan-falcon-55055-interface-contract, ratan-interface-inventory, ratan-trade-control, trade-validation]
sources: ["RATAN/RATAN -Interfaces/Ratan and Falcon 55055.md"]
---
# Ratan and Falcon 55055

## Summary

This source describes interface `55055`, a high-level integration supporting RATAN's BTS trade present-value (PV) check. As part of the C&A project, RATAN is expected to calculate BTS bond PV in real time by combining BTS trade information from TDS3 with bond-price and FX-rate information obtained from Falcon.

The document identifies the business purpose and the two principal data flows, but it does not provide a production-ready technical contract. Review, ownership, OLA, interface specifications, known issues, and troubleshooting sections are blank.

## Source status

The review metadata in the source is:

| Updated by | Update Date | Reviewed by | Review Date | Status |
| --- | --- | --- | --- | --- |
| | | | | |

The source indicates that status should be updated to `Published` after review, but the blank review table does not demonstrate that publication or review has occurred. This page therefore treats the document as an unverified reference.

## Business purpose

The source states that, as part of the C&A project, RATAN must run a PV check for BTS trades and calculate BTS bond PV. RATAN calls the Falcon API to fetch bond price and FX rate data required for the calculation.

## End-to-end data flow

```text
1. TDS3 BTS trade --(Solace)--> RATAN
2. Falcon --(API)--> RATAN

RATAN calculates trade PV in real time based on:
- Trade information from flow 1
- Market-data information from flow 2
```

The Falcon flow is shown as data returning from Falcon to RATAN, while the API request is initiated by RATAN. The source does not establish whether bond price and FX rate are returned by one operation or by separate API calls.

## Roles and boundaries

- **RATAN** consumes the trade and market-data inputs and performs the real-time PV calculation.
- **TDS3** supplies BTS trade information to RATAN.
- **Solace** transports the TDS3 trade message to RATAN.
- **Falcon** supplies bond-price and FX-rate information through an API.
- **BTS** is the trade subject for the PV check, but the source does not define the acronym or its required trade attributes.

Falcon's internal pricing or FX-rate production methodology is not described. Solace is identified as a transport layer and is not assigned business-calculation responsibility.

## Missing implementation and operational details

The source does not specify:

- Falcon endpoint names, API version, HTTP methods, authentication, timeout, retry, or response schemas.
- Whether bond price and FX rate are returned together or through separate calls.
- Solace topic or queue names, message schema, delivery guarantees, subscription details, or replay behavior.
- Market-data timestamps, valuation conventions, currency rules, stale-data handling, caching, or fallback behavior.
- The PV formula, discounting assumptions, valuation date, sequencing rules, or rounding rules.
- Interface ownership, support contacts, OLA, escalation paths, known issues, or troubleshooting procedures.

The interface should not be treated as an authoritative implementation specification until these details are validated against the canonical interface inventory and system owners.

## Related wiki context

This source extends the existing RATAN interface knowledge with a high-level Falcon dependency under identifier `55055`. It should be read alongside [[ratan-interface-inventory]], [[ratan-interface-architecture]], [[ratan-trade-control]], and [[trade-validation]].

The principal subject-specific pages are [[falcon]], [[ratan-falcon-market-data-interface]], and [[ratan-bts-pv-calculation]]. The open contract question is tracked in [[what-is-the-authoritative-ratan-falcon-55055-interface-contract]].
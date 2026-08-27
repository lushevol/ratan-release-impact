---
type: query
title: What Is the Authoritative RATAN Markets UDP PV Interface Contract?
created: 2026-08-25
updated: 2026-08-25
tags: [ratan, markets-udp, ssdr, api-contract, open-question]
related: [ratan-markets-udp-pv-integration, marketudp, ssdr-51507, ovv, solace, cna-exception-generation, ratan-interface-architecture, what-is-the-relationship-between-ssdr-dqsl-and-marketudp]
sources: ["RATAN/RATAN -Interfaces/Ratan and Markets UDP（SSDR）.md"]
---
# What Is the Authoritative RATAN Markets UDP PV Interface Contract?

## Question

What are the authoritative API, event, data, ownership, and operational contracts for the RATAN integration with Markets UDP?

## Known Evidence

The source documents this high-level sequence:

1. OVV sends RATAN a Solace notification when PV data is ready.
2. RATAN fetches PV data through the Markets UDP API.
3. RATAN calculates P&L or PV impacts.
4. RATAN generates CnA exceptions for user review.

## Missing Contract Details

The following remain unspecified:

- Markets UDP API endpoint, request, response, and authentication;
- Solace subject, notification payload, and correlation mechanism;
- batch identification and idempotency;
- timeout, retry, and failure behavior;
- PV-data validation rules;
- CnA exception-generation criteria;
- ownership and support contacts;
- the meanings of `UKT` and `UST`;
- the relationship between SSDR and Markets UDP;
- readiness ownership for `VALUATION_DATA_VER_HIS`.

## Why It Matters

Without these details, the source supports the business-level flow but cannot serve as a complete implementation or production-support contract. The identity question should be considered alongside [[queries/what-is-the-relationship-between-ssdr-dqsl-and-marketudp]].

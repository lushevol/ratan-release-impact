---
type: query
title: What Is the Authoritative RATAN-Falcon 55055 Interface Contract?
created: 2026-08-25
updated: 2026-08-25
tags: [ratan, falcon, interface-55055, api-contract, open-question]
related: [ratan-and-falcon-55055-187hvsp, falcon, ratan-falcon-market-data-interface, ratan-bts-pv-calculation, ratan-interface-inventory, ratan-interface-architecture, tds3, solace]
sources: ["RATAN/RATAN -Interfaces/Ratan and Falcon 55055.md"]
---
# What Is the Authoritative RATAN-Falcon 55055 Interface Contract?

## Question

What document or system record authoritatively defines interface `55055` between RATAN and Falcon, including its API contract, data semantics, operational ownership, and production status?

## Current evidence

The source describes a high-level use case in which RATAN calculates BTS bond PV in real time. TDS3 provides BTS trade data through Solace, and Falcon provides bond-price and FX-rate data through an API.

The source's review and publication fields are blank. It should therefore be treated as an unverified reference rather than a confirmed production contract.

## Information to verify

1. Whether `55055` is the authoritative interface identifier.
2. Falcon's official application name, owner, support contact, and environment endpoints.
3. Falcon API operations, version, authentication, request schema, response schema, and error model.
4. Whether bond price and FX rate are returned together or through separate calls.
5. Data timestamps, freshness thresholds, valuation conventions, currency treatment, and correlation rules.
6. TDS3 Solace topic or queue, BTS message schema, delivery semantics, and replay behavior.
7. Sequencing and correlation behavior when trade data and market data arrive at different times.
8. Timeout, retry, caching, stale-data, fallback, monitoring, and alerting rules.
9. RATAN's PV formula, valuation assumptions, rounding rules, and PV-check tolerance.
10. Interface OLA, production support ownership, escalation path, known issues, and troubleshooting procedure.

## Systems and concepts involved

The query connects [[ratan]], [[falcon]], [[tds3]], and [[solace]]. The calculation boundary is described in [[ratan-bts-pv-calculation]], while the market-data dependency is described in [[ratan-falcon-market-data-interface]]. Reconciliation should include [[ratan-interface-inventory]] and [[ratan-interface-architecture]].
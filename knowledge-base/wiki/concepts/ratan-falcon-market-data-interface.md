---
type: concept
title: RATAN-Falcon Market-Data Interface
created: 2026-08-25
updated: 2026-08-25
tags: [ratan, falcon, market-data, api, interface-55055]
related: [ratan, falcon, ratan-bts-pv-calculation, ratan-interface-inventory, ratan-interface-architecture, what-is-the-authoritative-ratan-falcon-55055-interface-contract]
sources: ["RATAN/RATAN -Interfaces/Ratan and Falcon 55055.md"]
---
# RATAN-Falcon Market-Data Interface

## Definition

The RATAN-Falcon market-data interface is the documented dependency through which RATAN obtains bond-price and FX-rate information from Falcon for the real-time calculation of BTS trade PV. The source associates this flow with interface identifier `55055`.

## High-level interaction

```text
RATAN --API request--> Falcon
RATAN <--bond price and FX-rate response-- Falcon
```

The source presents two inputs to the RATAN calculation:

1. BTS trade information from TDS3 through Solace.
2. Bond-price and FX-rate information from Falcon through an API.

RATAN combines these inputs to calculate PV in real time. Falcon provides market-data inputs; RATAN owns the calculation described by the source.

## Contract boundaries

The source does not establish:

- The Falcon endpoint or API version.
- Authentication and authorization requirements.
- Request and response schemas.
- Whether bond price and FX rate are retrieved in one call or separate calls.
- Correlation, timestamp, currency, and valuation semantics.
- Timeout, retry, caching, stale-data, or fallback behavior.
- Ownership, OLA, monitoring, or escalation procedures.

Consequently, this page records the architectural relationship rather than a complete implementation contract.

## Related calculation

The market-data response is an input to [[ratan-bts-pv-calculation]]. The trade-data path is separately described by the relationship between [[tds3]], [[solace]], and [[ratan]].
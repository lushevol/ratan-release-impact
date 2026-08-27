---
type: entity
title: Falcon
created: 2026-08-25
updated: 2026-08-25
tags: [falcon, market-data, api, bond-price, fx-rate]
related: [ratan, ratan-falcon-market-data-interface, ratan-bts-pv-calculation, what-is-the-authoritative-ratan-falcon-55055-interface-contract]
sources: ["RATAN/RATAN -Interfaces/Ratan and Falcon 55055.md"]
---
# Falcon

## Role

Falcon is an external application or API provider that supplies RATAN with bond-price and FX-rate information for the real-time PV calculation of BTS trades.

The source supports Falcon's role as a market-data provider dependency. It does not describe Falcon's internal pricing methodology, FX-rate production, ownership, service levels, or operational support model.

## Interaction with RATAN

The documented high-level flow is:

```text
RATAN --(API request)--> Falcon
Falcon --(bond price and FX-rate response)--> RATAN
```

The source labels the data flow as `Falcon --(API)--> Ratan`, but does not provide endpoint names, API version, authentication, request or response schemas, or whether the two market-data values are returned together.

## Evidence limitations

The Falcon integration is documented only at a high level in interface `55055`. The authoritative API contract, data freshness requirements, timeout and retry behavior, caching policy, and ownership remain to be confirmed. See [[what-is-the-authoritative-ratan-falcon-55055-interface-contract]].
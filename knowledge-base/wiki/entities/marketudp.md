---
type: entity
title: MarketUDP
created: 2026-08-25
updated: 2026-08-25
tags: ["marketudp", "ssdr", "ratan", "rest-api", "cashflow", "markets-udp", "market-data", "pv-data"]
related: [ratan, ssdr-51507, ratan-rest-cashflow-query-integration, what-is-the-authoritative-ratan-rest-cashflow-query-api-contract, ovv, solace, sabre, ratan-markets-udp-pv-integration, what-is-the-relationship-between-ssdr-dqsl-and-marketudp]
sources: ["RATAN/RATAN -Interfaces/Ratan and FMMIS-51406  CIS-31946  SSDR-51507 (DQSL) PacMan-51406 CNEDMp-50584.md", "RATAN/RATAN -Interfaces/Ratan and Markets UDP（SSDR）.md"]
---
# MarketUDP / Markets UDP

## Overview

The available sources use both `MarketUDP(SSDR)` and “Markets UDP.” They do not conclusively define whether these names refer to the same system, component, interface, or data product.

## Cashflow Query Role

According to **RATAN -Interfaces/Ratan and FMMIS-51406 CIS-31946 SSDR-51507 (DQSL) PacMan-51406 CNEDMp-50584**, `MarketUDP(SSDR)` is shown as a sub-application that triggers a REST API call to query cashflow data from [[ratan]]:

```text
MarketUDP(SSDR)–(REST API)→RATAN
```

That source does not specify the API endpoint, data scope, authentication, ownership, or the exact meaning of the `SSDR` qualifier.

## PV Data Role

According to **RATAN -Interfaces/Ratan and Markets UDP（SSDR）**, Markets UDP is the upstream application or market-data platform that exposes the API used by [[ratan]] to retrieve PV data.

### RATAN Integration

Within the documented flow:

- Sabre provides feed data to [[ovv]], a service within Markets UDP.
- OVV sends a PV-ready notification to RATAN through [[solace]].
- RATAN then retrieves PV data through the Markets UDP API.
- RATAN uses the data for P&L and PV-impact calculations and generates CnA exceptions.

This source does not provide the API contract or identify whether the Solace notification contains data beyond readiness information.

## Operational Timing

The Markets UDP source describes Batch 1, Batch 2, Batch 3, and Batch EOD processing windows. It identifies EOD data as the source for previous-version trade PV used in PV-impact calculation.

The same source records a Friday release dependency: Sabre or MRB release activity may delay readiness of `VALUATION_DATA_VER_HIS`.

## SSDR Identity Caveat

The Markets UDP source filename includes `SSDR`, but its body does not define whether SSDR is a component of Markets UDP, an interface identifier, a data product, or a separate system. This relationship remains open in [[what-is-the-relationship-between-ssdr-dqsl-and-marketudp]].
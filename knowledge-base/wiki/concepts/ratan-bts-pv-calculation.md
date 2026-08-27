---
type: concept
title: RATAN BTS PV Calculation
created: 2026-08-25
updated: 2026-08-25
tags: [ratan, bts, pv, trade-control, real-time-calculation]
related: [ratan, falcon, tds3, solace, ratan-falcon-market-data-interface, ratan-trade-control, trade-validation, what-is-the-authoritative-ratan-falcon-55055-interface-contract]
sources: ["RATAN/RATAN -Interfaces/Ratan and Falcon 55055.md"]
---
# RATAN BTS PV Calculation

## Definition

RATAN BTS PV calculation is the real-time calculation of present value for BTS bond trades. The use case is described as part of the C&A project and is intended to support a PV check for BTS trades.

## Inputs

The source identifies two required input paths:

- **Trade information:** BTS trade data delivered from TDS3 to RATAN through Solace.
- **Market data:** Bond-price and FX-rate information retrieved by RATAN from Falcon through an API.

```text
TDS3 BTS trade --(Solace)--> RATAN
Falcon --(API)--> RATAN

RATAN: trade information + market data -> real-time PV calculation
```

## Calculation boundary

The source assigns the calculation to RATAN. It does not state Falcon's internal pricing methodology, and it does not provide the PV formula or valuation rules.

The following details remain unspecified:

- Valuation timestamp and valuation date.
- Bond-pricing methodology and discounting assumptions.
- FX conversion convention and currency treatment.
- Required trade and market-data fields.
- Sequencing when trade and market data arrive at different times.
- Rounding, tolerance, and comparison rules for the PV check.
- Behavior when market data is unavailable, delayed, stale, or inconsistent.

This page should therefore be used as a high-level use-case description, not as a complete valuation specification.

## Relationship to trade controls

The use case is related to [[ratan-trade-control]] and [[trade-validation]], but a BTS PV calculation should not be treated as equivalent to the complete RATAN trade-validation framework without further evidence.
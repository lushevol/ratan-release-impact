---
type: concept
title: RFR Payment-Type Classification
created: 2026-08-22
updated: 2026-08-22
tags: [rfr, payment-type, murex, cashflow, cash-settlement]
related: [swap-agent, murex-2-11, ratan, pending-fixing, settlement-suppression, what-is-the-authoritative-rfr-payment-type-mapping]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/RFR and Swap Agent.md"]
---

# RFR Payment-Type Classification

RFR payment-type classification derives `Cashflow.Payment_Type` from Murex strategy, typology, `FLOW_TYPE2`, and `X_DUMMY2`. The documented mapping is specific to a three-trade RFR structure and must not be inferred solely from shared `LTI_ID` values.

## Latest mapping

```text
Initial Notional:
Strategy in (‘SWAP_AGENT,'RECALC') &&
Typology=‘RFR CCS MTM Fixing’ &&
FLOW_TYPE2==’INIT’

Interim MTM:
Strategy in (‘SWAP_AGENT,'RECALC') &&
Typology=‘RFR CCS MTM Fixing’ &&
FLOW_TYPE2!=’INIT’ &&
X_DUMMY2==’0’

Coupon:
Strategy in (‘SWAP_AGENT,'RECALC') &&
Typology=’Vanilla X-ccy swap’

Final Notional:
Strategy in (‘SWAP_AGENT,'RECALC') &&
Typology=‘RFR CCS MTM Fixing’ &&
X_DUMMY2==’1’
```

The mapping was revised on 2025-01-07 after UAT found a new typology. The revised coupon rule includes `RECALC` but restricts typology to `Vanilla X-ccy swap`.

## Settlement interpretation

Classification does not by itself determine external message generation:

- Trade2 initial and final notionals are documented as bilateral settlement flows.
- Trade2 interim MTM and Trade1 coupons can be eligible for RATAN while SWIFT-suppressed.
- Dummy flows can be excluded from RATAN even where they are related to the same RFR structure.

See [[settlement-suppression]] for the distinction between eligibility and release.
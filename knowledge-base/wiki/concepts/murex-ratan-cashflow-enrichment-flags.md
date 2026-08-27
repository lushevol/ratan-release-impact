---
type: concept
title: Murex-Ratan Cashflow Enrichment Flags
created: 2026-08-24
updated: 2026-08-24
tags: [murex-211, ratan, cashflow-message, enrichment, commodity, clearing, fixing]
related: [murex-ratan-cashflow-message-contract, fmrp-outbound-cashflow-enrichment, precious-metal-currency-classification, when-is-hau-commodity-flag-treatment-effective]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/Settlement - Murex 2.11 DOI Document - H2 2024.md"]
---
# Murex-Ratan Cashflow Enrichment Flags

The DOI defines Murex business enrichment used by Ratan to route or interpret cashflows. Several fields are existing Murex UDFs used for multiple integration purposes, creating a message-contract and regression risk.

## Flag semantics

- `COM_FLOW`: marks a commodity cashflow for Commodity Ops. Conditions include commodity trade family, selected bullion-currency cases, commodity portfolio, or commodity strategy. `XAF`, `XOF`, and `XOH` are excluded; counterparties with `M_PB_CUST` are excluded.
- `X_DUMMY2`: identifies final RFR or Swap Agent coupon/principal conditions when the family group is `CS`, linked trade ID is non-zero, strategy is `RECALC` or `SWAP_AGENT`, and value date equals maturity date.
- `X_DUMMY3`: identifies qualifying bilateral payments pending clearing. The source covers SWAPSWIRE IRS/CCS and adds CFETS/cfets `OPT` trades where `ADD_COMMENTS` is empty.
- `COMMENTS`: carries an NDS duplicate-warning string in the form `Potential duplication of FXD 999999999`.
- `WAIT_FIX`: indicates whether related cashflows remain pending fixing. T−1 through T+1 flows are initially sent as `X` and updated within one hour to `Y` or `N`; T+2 through T+7 flows are sent directly as `Y` or `N`.

The source’s version 2.7 states that HAU is bullion and must produce commodity flag `Y`, despite not beginning with `X`. Its stated effective date requires confirmation in [[when-is-hau-commodity-flag-treatment-effective]].
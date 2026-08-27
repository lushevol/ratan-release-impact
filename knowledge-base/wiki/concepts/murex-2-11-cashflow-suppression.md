---
type: concept
title: "Murex 2.11 Cashflow Suppression"
created: 2026-08-23
updated: 2026-08-23
tags: [murex, cashflow, suppression, razor, ratan, fx, publishing-criteria]
related: [stella-ratan-cashflow-filtering, suspended-versus-projected-cashflow-status, cpn-netting, cpn, razor, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SUSPENDED vs PROJECTED cashflow status in Ratan.md"]
---
# Murex 2.11 Cashflow Suppression

## Publishing scope

Murex 2.11 publishing criteria distinguish payments routed to Ratan from payments settled in Razor, Razor FX, Razor ALM, or dedicated queues. Criteria use product, entity, portfolio, currency, strategy, typology, trade status, amount, date, and settlement-route attributes.

## Main suppression criteria

The source identifies suppression for:

- Internal funding deals settled in Razor ALM.
- Dummy portfolios defined by `TABLE#LIST#FLTPF_IN_DBF`.
- Non-deliverable currency payments, subject to `PHP_DELIVERABLE`, `IDR_DELIVERABLE`, and Hong Kong `TWD` exceptions.
- FXD payments settled in Razor FX, subject to exceptions for `NDF`, `Phy_Precious`, `Emissions FX`, `FEDSVALIDATOR`, XIT payments, specified `FX_PDC`/`FX_DCD`/`DCD` conditions, option-exercise FXD, and bullion-currency FXD.
- Payments already covered by auto-suppression.
- CPN-eligible payments.

The source states that Ratan has no equivalent logic for CPN eligibility. Dedicated queues cover `RFR`, `Swap Agent`, and `NDS Fixing` payments.

## Existing controls

The publishing criteria also reference `VALD` or `COMP` trade status, H2 entity scope, positive amounts, non-zero `TRN_ID` except for `SWAP_AGENT`, exclusion of `CLIENT_CLRG_LCH` and `CLIENT_CLR_HKEX`, and payment value dates from T-1 to T+7 business days. The value-date range is marked out of scope in the source.

## Implementation gaps

The source reports no current Stella booking for dummy portfolios and no non-deliverable currency payments in Stella. XIT payments and special FXD typologies require monitoring. The relationship between Murex suppression labels and Ratan filtering is not defined as an authoritative, versioned contract.
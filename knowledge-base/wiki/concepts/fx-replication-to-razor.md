---
type: concept
title: "FX Replication to Razor"
created: 2026-08-23
updated: 2026-08-23
tags: [fx, replication, razor, ratan, tds3, fxd, fx-dcd, fx-pcd]
related: [stella-ratan-cashflow-filtering, suspended-versus-projected-cashflow-status, fx-leg-netting-consistency, tds3, razor, fmrp, scbml]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SUSPENDED vs PROJECTED cashflow status in Ratan.md"]
---
# FX Replication to Razor

## Scope

The replication design governs which Stella-originated FX cashflows are processed in Ratan or replicated toward Razor. Rules are expected to be editable through the front end, and manually suspended cashflows can be STPed through maker-checker control.

The principal source identifier is `FMRPSTELLA`. Core FX taxonomy values are `ForeignExchange:Spot`, `ForeignExchange:Forward`, and `ForeignExchange:Swap`.

## Routing rules

The design includes:

- Excluding booking entities `401036553`, `400991880`, and `400007847` under the EG/NP/SA rule.
- Applying PCD/DCD logic using `Contract_Typology`, `Parent_Position_Id`, counterparty country, and SCB internal-entity lists.
- Applying entity/counterparty exclusion lists, including dated additions.
- Excluding payment types containing `Fees`.
- Requiring booking and counterparty SCI FMIDs to differ.
- Excluding duplicate bookings where `Is_Duplicate_Booking == true`.
- Restricting trade processing to `Trade_State == "BOOKED"`.
- Limiting market events by business event and `Last_Action_Type`.

The PCD/DCD expression contains multiple `OR` conditions and requires authoritative parentheses before implementation.

## FXO structure exception

An FXO structure may include `FXO`, `LNBR`, and `CCS`. When an FXO exercise produces an FXD sharing the structure or contract ID, the FXD must remain processable in Ratan with `PROJECTED` status so the structure can be netted consistently.

## Amendment risk

If `Contract_Typology` changes during an amendment, filtering only the current trade state can retain the original Razor cashflows or suppress the replacement Ratan cashflows incorrectly. Effective-version and cashflow-event processing is required to avoid duplicate or missing payments.
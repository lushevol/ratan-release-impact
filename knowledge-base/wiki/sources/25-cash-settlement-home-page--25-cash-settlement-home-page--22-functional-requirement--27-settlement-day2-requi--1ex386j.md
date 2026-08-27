---
type: source
title: Auto Netting Static Go-Live Process
authors: []
year: 2025
url: ""
venue: "Cash Settlement Home Page — Functional Requirement"
tags: [cash-settlement, auto-netting, static-data, go-live, NSTP, SWIFT-suppression]
related: [cash-settlement-home-page, ratan, cashflow-auto-netting, auto-netting-static-go-live-sequencing, auto-netting-resultant-nstp, clearing-swift-suppression, net-over-net, manual-to-auto-netting-migration, maker-checker-settlement-control, bic-netting, ccil-guaranteed-and-non-guaranteed-netting]
created: 2026-08-22
updated: 2026-08-22
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Auto Netting Static Go Live Process.md"]
---
# Auto Netting Static Go-Live Process

## Scope

This functional requirement defines a sequenced production static-data process for [[concepts/cashflow-auto-netting]] within the [[entities/cash-settlement-home-page]] context. It covers NSTP handling, SWIFT suppression, netting-static rules, manual-rule migration, and later TAIFEX/CITIC net-over-net extensions.

The source contains configuration intent and partial implementation evidence. It does not provide a complete production sign-off, full activation history, or confirmation that every listed rule was deployed.

## Required sequencing

The source specifies the following order:

1. Create or update NSTP rules.
2. Create or update SWIFT suppression rules.
3. Create or update netting-static rules.

This ordering is intended to ensure that netting resultants receive the correct approval handling and downstream message suppression after the relevant netting rules are enabled.

## NSTP rules

| Action | Description | Rule Condition | Exception Code | Operation Level | Exception Category | Bulk Eligible | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| New | NSTP rule for auto netting resultant cashflow-maker checker | `Cashflow__Is_Auto_Netting == true && Cashflow__Auto_Netting_Stp_Level == "NSTP_MAKER_CHECKER"` | Auto Netting | MAKER_CHECKER | NSTP | un-ticked | 2025-08-25 |
| New | NSTP rule for auto netting resultant cashflow-checker only | `Cashflow__Is_Auto_Netting == true && Cashflow__Auto_Netting_Stp_Level == "NSTP_CHECKER_ONLY"` | Auto Netting | CHECKER_ONLY | NSTP | un-ticked | 2025-08-25 |
| Update | Add auto-netting exclusion to the existing net-cashflow rule | `Cashflow__Netting_Id != null && Cashflow__Netting_Id != "" && Cashflow__Is_Auto_Netting == false` | Net Cashflow | MAKER_CHECKER | OTHER | ticked | 2025-08-25 |

The exclusion is intended to prevent auto-netting resultants from also matching the generic net-cashflow NSTP rule.

## SWIFT suppression rules

| Action | Description | Rule Condition | Rule Reason | Comment |
| --- | --- | --- | --- | --- |
| New | Auto suppress SAL Coupon/MTM net resultants and single auto-netted cashflows | `(Cashflow__Payment_Type in ("SAL Coupon Netting", "SAL MTM Netting") && (Cashflow__Netting_Id != null && Cashflow__Netting_Id != "")) || (Cashflow__Payment_Type in ("Interim MTM", "Coupon") && Cashflow__Is_Auto_Netting == true)` | SAL Coupon/MTM Net Resultant | Takes effect once the SWAP AGENT auto-netting rule is created |
| New | Auto suppress LCH net resultants and single auto-netted cashflows | `Entity__Counterparty_SCI_FMID == "10037537" && Entity__Booking_Entity_SCI_FMID == "10075222" && ((Cashflow__Netting_Id != null && Cashflow__Netting_Id != "") || ((Cashflow__Netting_Id == null || Cashflow__Netting_Id == "") && Cashflow__Is_Auto_Netting == true))` | LCH Net Resultant | Create when the LCH auto-netting rule is enabled |
| New | Auto suppress CME/EUREX/JSCC/ICE net resultants and single auto-netted cashflows | `Entity__Counterparty_SCI_FMID in ("400902327", "400923856", "400947070", "400971369") && Entity__Booking_Entity_SCI_FMID == "10075222" && ((Cashflow__Netting_Id != null && Cashflow__Netting_Id != "") || ((Cashflow__Netting_Id == null || Cashflow__Netting_Id == "") && Cashflow__Is_Auto_Netting == true))` | CME EUREX JSCC ICE Net Resultant | Create when the corresponding auto-netting rules are created |
| Update | Remove `400902327` from an existing suppression rule | `Entity__Booking_Entity_SCI_FMID == "10075222" && Entity__Counterparty_SCI_FMID in ("400821167", "400902327")` | UK ICECLEAR/NY and CMECCP/WMN | Source marks `400902327` for removal |
| Update | Remove `400971369`, `400923856`, and `400947070` from an existing suppression rule | `Entity__Booking_Entity_SCI_FMID == "10075222" && Entity__Counterparty_SCI_FMID in ("400971369", "401039149", "401035089", "400923856", "400947070")` | Swift Suppression for ICECLRCRDCCP/NY and CCPOTCCSCHK/HKG and OTCCHKEXCCP/HKG and EUREXCAGCCP/FRA and JSCC/TYO and SCBOTCCCP/HKG in UK Entity | Source marks the three counterparties for removal |

## Netting-static rules

The principal conditions are reproduced below.

```text
SHACITIC/BJG Clearing:
Entity__Booking_Entity_SCI_FMID in ("2", "300075472") && Entity__Counterparty_SCI_FMID == "401014221" && (Cashflow__Netting_Id == null || Cashflow__Netting_Id == "")

FMO SG Netting:
Entity__Booking_Entity_SCI_FMID in ("400452428", "400451508", "3", "300036368") && Entity__Counterparty_SCI_FMID == "400839031" && (Cashflow__Netting_Id == null || Cashflow__Netting_Id == "")

SCH IRS Rule:
Entity__Booking_Entity_SCI_FMID == "400899993" && Entity__Counterparty_SCI_FMID == "400202766" && (Instrument_Common__ISDA_Taxonomy == "IRD|IRS" || Instrument_Common__ISDA_Taxonomy matches "^InterestRate:IRSwap:.*$") && (Cashflow__Payment_Type == "IRS Netting" || (Cashflow__Netting_Id == null || Cashflow__Netting_Id == ""))

SCH OPT Rule:
Entity__Booking_Entity_SCI_FMID == "400899993" && Entity__Counterparty_SCI_FMID == "400202766" && Instrument_Common__ISDA_Taxonomy in ('CURR|OPT|SMP') && (Cashflow__Netting_Id == null || Cashflow__Netting_Id == "")

Eclipse Client Auto Netting:
(Cashflow__Netting_Id == null || Cashflow__Netting_Id == "") && Entity__Booking_Entity_SCI_FMID == "10075222" && Entity__Counterparty_SCI_FMID == "400617196" && Instrument_Common__ISDA_Taxonomy == "CURR|OPT|SMP"

Commodity Auto Netting:
Entity__Counterparty_SCI_BIC_Net_Flag == "Y" && Entity__Counterparty_SCI_BIC_Code == "CITIGB2LXXX" && (Cashflow__Netting_Id == null || Cashflow__Netting_Id == "") && Cashflow__Payment_Currency == "USD" && Instrument_Common__Murex_Product_Typology != "NDF"

Commodity Auto Netting – PM Currencies:
Entity__Counterparty_SCI_BIC_Net_Flag == "Y" && Entity__Counterparty_SCI_BIC_Code == "CITIGB2LXXX" && (Cashflow__Netting_Id == null || Cashflow__Netting_Id == "") && Cashflow__Payment_Currency in ("XAU", "XAG", "XPD", "XPT") && (Instrument_Common__Murex_Product_Strategy == null || Instrument_Common__Murex_Product_Strategy == "") && Instrument_Common__Murex_Product_Typology != "NDF"

SAL MTM NETTING:
Instrument_Common__Murex_Product_Strategy == "SWAP_AGENT" && Cashflow__Payment_Type == "Interim MTM" && (Cashflow__Netting_Id == null || Cashflow__Netting_Id == "")

SAL COUPON NETTING:
Instrument_Common__Murex_Product_Strategy == "SWAP_AGENT" && Cashflow__Payment_Type == "Coupon" && (Cashflow__Netting_Id == null || Cashflow__Netting_Id == "")

CCIL Netting:
Settlement_Method == "CCIL" && (Cashflow__Netting_Id == null || Cashflow__Netting_Id == "") && Entity__Booking_Entity_SCI_FMID == "4" && Entity__Counterparty_SCI_FMID != "400021949"

CCIL Guarantee:
Entity__Booking_Entity_SCI_FMID == "4" && Entity__Counterparty_SCI_FMID == "400021949" && Settlement_Method == "CCIL" && (Cashflow__Netting_Id == null || Cashflow__Netting_Id == "")

CME EUREX JSCC ICE Netting:
Entity__Booking_Entity_SCI_FMID == "10075222" && Entity__Counterparty_SCI_FMID in ("400902327", "400923856", "400947070", "400971369") && ((Cashflow__Netting_Id == null || Cashflow__Netting_Id == ""))
```

The source records the following timing and control metadata:

- SHACITIC/BJG Clearing: `01:00 GMT on VD`; NSTP for Maker+Checker; Bilateral Netting.
- FMO SG Netting: `04:00 GMT on VD`; NSTP for Maker+Checker; existing manual rule to be switched to auto netting.
- SCH IRS and SCH OPT: `01:00 GMT on VD`; NSTP for Maker+Checker; Bilateral Netting.
- Eclipse Client Auto Netting: `15:30 GMT V-1`; NSTP for Maker+Checker; Bilateral Netting.
- Beneficiary BIC, Commodity Auto Netting, and Commodity Auto Netting – PM Currencies: `14:30 GMT V-1`; NSTP for Maker+Checker; BIC Netting.
- SAL MTM and SAL Coupon: `01:00 GMT on VD`; NSTP for Maker+Checker.
- CCIL Netting and CCIL Guarantee: `03:30 GMT on VD`; NSTP for Maker+Checker.
- CME/EUREX/JSCC/ICE Netting: `12:00 GMT on VD`; NSTP for Checker.

## TAIFEX and CITIC net-over-net rules

Added on 2025-11-18 and 2025-11-20 respectively:

```text
TAIFEX IRS Net-over-net rule:
Entity__Booking_Entity_SCI_FMID == "10038345" && Entity__Counterparty_SCI_FMID == "401040938" && (Instrument_Common__ISDA_Taxonomy == "IRD|IRS" || Instrument_Common__ISDA_Taxonomy matches "^InterestRate:IRSwap:.*$") && (Cashflow__Payment_Type == "IRS Netting" || (Cashflow__Netting_Id == null || Cashflow__Netting_Id == ""))

CITIC IRS Net-over-net rule:
Entity__Booking_Entity_SCI_FMID == "2" && Entity__Counterparty_SCI_FMID == "401014221" && (Instrument_Common__ISDA_Taxonomy == "IRD|IRS" || Instrument_Common__ISDA_Taxonomy matches "^InterestRate:IRSwap:.*$") && (Cashflow__Payment_Type == "IRS Netting" || (Cashflow__Netting_Id == null || Cashflow__Netting_Id == ""))
```

The TAIFEX post-update suppression condition is:

```text
Entity__Counterparty_SCI_FMID == "401040938" && Entity__Booking_Entity_SCI_FMID == "10038345" && ((Cashflow__Netting_Id != null && Cashflow__Netting_Id != "" && Cashflow__Payment_Type != "IRS Netting") || ((Cashflow__Netting_Id == null || Cashflow__Netting_Id == "") && Cashflow__Is_Auto_Netting == true) || (Cashflow__Payment_Type == "IRS Netting" && Cashflow__Is_Auto_Netting == true))
```

The source gives no post-update condition for the equivalent CITIC suppression rule.

## Implementation evidence and limitations

The source reports that five cashflows were auto netted on 2025-08-25 for the SHACITIC/BJG Clearing rule. It also records historical volume estimates, including 328 for FMO SG, 3,234 for Beneficiary BIC, 666 for the struck-through generic SCH rule, and 33 for CCIL.

eOPS references include `SCH202G210A1020925068966`, `SCH202G210A1020925048378`, and `SCH202G210A1020925048299`. These references demonstrate that work was raised, but do not independently establish completion.

Open operational questions include the deployment status of each rule, manual-rule retirement, exact precedence, cutoff-calendar semantics, whether the generic SCH rule was disabled, and whether the CITIC suppression update is complete.
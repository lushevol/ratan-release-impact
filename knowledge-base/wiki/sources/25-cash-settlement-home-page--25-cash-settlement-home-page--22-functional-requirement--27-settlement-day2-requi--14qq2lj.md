---
type: source
title: Cashflow Auto Netting UAT
authors: []
year: 2025
url: ""
venue: Internal UAT documentation
created: 2026-08-22
updated: 2026-08-22
tags: [uat, cash-settlement, ratan, auto-netting, static-configuration]
related: [cashflow-auto-netting, pending-auto-netting-state, auto-netting-rule-management, netting-rule-change-cashflow-refresh, sal-mtm-and-coupon-auto-netting, clearing-resultant-swift-suppression, was-cashflow-auto-netting-uat-formally-passed]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Cashflow Auto Netting UAT.md"]
---
# Cashflow Auto Netting UAT

This document is a July–August 2025 UAT test plan, test-data register, static-rule change register, and limited issue log for RATAN cashflow auto netting. It specifies expected behaviours for rule administration, scheduled aggregation, resultant handling, lifecycle actions, refresh after rule changes, and clearing- or product-specific configurations.

## Evidence status

The document primarily records intended test steps and expected results. Most `Test Status` and `Rule Status` fields are blank, so it does not demonstrate consistent execution completion, approval, production deployment, or formal UAT sign-off.

The document explicitly notes that Swap Agent testing was incomplete: “the current test for Swap Agent does not meet our expectation. Some details are missing.”

## UAT target behaviour

For Bilateral, CCIL, and BIC auto-netting rules, the documented expected sequence is:

1. Matching inputs become `WAITING` with sub-state `Pending Auto Netting`.
2. They remain pending before the configured netting time.
3. At the applicable schedule, inputs become `NETTED` and a resultant such as `N1` is generated.
4. The resultant is expected to be `Affirmed`, receive the rule-configured NSTP handling, and use the applicable netting payment type.
5. Operations release the resultant from RATAN.

The applicable resultant payment types are scoped to the rule scenario: `Bilateral Netting`, `CCIL Netting`, `BIC Netting`, `SAL MTM Netting`, or `SAL Coupon Netting`. This source does not establish that these outcomes passed UAT.

## Lifecycle and refresh acceptance criteria

The UAT design expects the following behaviours:

- Manual fail followed by reinstate returns a cashflow to `WAITING` / `Pending Auto Netting`.
- Hold followed by unhold returns a cashflow to `WAITING` / `Pending Auto Netting`.
- Verified SWIFT suppression produces `SWIFT_SUPPRESSED`; confirmed cashflow suppression produces `CASHFLOW_SUPPRESSED`. In either case, the affected cashflow is excluded from the later auto-netting set.
- A manual net can consume selected pending-auto-netting inputs; un-netting its resultant marks that resultant `DEAD` and restores the underlying cashflows to pending auto netting.
- Withdrawal before netting cancels the withdrawn input while remaining inputs may be netted.
- Withdrawal after netting is expected to kill `N1`, cancel the withdrawn input, restore the remaining inputs to `Pending Auto Netting`, and allow a subsequent `N2` to be created.
- New, updated, disabled, and Manual ↔ Auto rules are expected to refresh matching cashflows. A documented currency-filter update from unrestricted currency to `USD` is expected to remove pre-existing CNY cashflow `M00120421308` from `Pending Auto Netting`.

These are UAT acceptance criteria supporting [[pending-auto-netting-state]], [[netting-un-net-lifecycle]], and [[netting-rule-change-cashflow-refresh]], not confirmed production facts.

## Rule selection and grouping

The document specifies that a cashflow matching multiple rules should use the rule with the higher-priority netting type. If the netting types are the same, the latest-created rule should be selected. Its documented example expects `SAL Coupon Netting` to take precedence over `Bilateral Netting`.

It separately requires isolation across distinct rules: cashflows under product-specific Rule1 and Rule2 must not net together merely because booking entity, counterparty, currency, and payment date coincide. This supports [[netting-scenario-priority]] and [[cross-rule-netting-isolation]].

## Calendar examples

| Casfflow | ccy | payment date | date from netting static | auto netting date | |
| --- | --- | --- | --- | --- | --- |
| C1 | SGD | 1st Apr. 2025 (Tuesday) | VD-1 | 20250328 (Last Friday) | SGD holiday in Monday (2025/03/31) |
| C2 | CNY | 1st Apr. 2025 (Tuesday) | VD-1 | 20250331 (Monday) | working day in Monday (2025/03/31) |
| C3 | CNY | 28th Apr. 2025 (Monday) | VD-1 | 20250427 (Sunday) | CNY working weekend in Sunday (2025/04/27) |
| C4 | GBP | 21st Apr. 2025(Holiday) | VD | 20250421(Holiday) | payment date is weekend/holiday |

These examples support currency-calendar-relative `VD` and `VD-1` processing, including holidays and working weekends. They do not define the complete calendar-provider or multi-currency policy.

## Static configuration extracts

### Suppression rules

| Action | Rule ID | Pre-Rule ID | Post-Rule ID | Description | Rule Condition | Rule Reason | Rule Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| New | 7351885393248022528 |  | NA | Auto Suppress SAL Coupon/MTM Net Resultant and single cashflow which has no other cashflow to net with | (Cashflow__Payment_Type in ("SAL Coupon Netting", "SAL MTM Netting") && (Cashflow__Netting_Id != null && Cashflow__Netting_Id != "")) \|\| (Cashflow__Payment_Type in ("Interim MTM", "Coupon") && Cashflow__Is_Auto_Netting == true) | SAL Coupon/MTM Net Resultant |  |
| Update |  | 7351244948348235776 | 7351891133699129344 | Auto Suppress LCH Net Resultant | Entity__Counterparty_SCI_FMID == "10037537" && Entity__Booking_Entity_SCI_FMID == "10075222" && ((Cashflow__Netting_Id != null && Cashflow__Netting_Id != "") \|\| ((Cashflow__Netting_Id == null \|\| Cashflow__Netting_Id == "") && Cashflow__Is_Auto_Netting == true)) | LCH Net Resultant |  |
| New | 7355932145617928192 |  | 7356611640855298048 | Auto Suppress CME EUREX JSCC ICE Net Resultant | Right rule condition Entity__Counterparty_SCI_FMID in ("400902327", "400923856", "400947070", "400971369") && Entity__Booking_Entity_SCI_FMID == "10075222" && ((Cashflow__Netting_Id != null && Cashflow__Netting_Id != "") \|\| ((Cashflow__Netting_Id == null \|\| Cashflow__Netting_Id == "") && Cashflow__Is_Auto_Netting == true)) Wrong rule condition Entity__Counterparty_SCI_FMID == "400902327,400923856,400947070,400971369" && Entity__Booking_Entity_SCI_FMID == "10075222" && ((Cashflow__Netting_Id != null && Cashflow__Netting_Id != "") \|\| ((Cashflow__Netting_Id == null \|\| Cashflow__Netting_Id == "") && Cashflow__Is_Auto_Netting == true)) | CME EUREX JSCC ICE Net Resultant |  |
| Disable | 7251072415746830336 |  |  |  | Entity__Booking_Entity_SCI_FMID == "10075222" && Entity__Counterparty_SCI_FMID in ("400821167", "400902327") | UK ICECLEAR/NY and CMECCP/WMN |  |
| Disable | 7285145506718269440 |  |  |  | Entity__Booking_Entity_SCI_FMID == "10075222" && Entity__Counterparty_SCI_FMID in ("400971369", "401039149", "401035089", "400923856", "400947070") | Swift Suppression for ICECLRCRDCCP/NY and CCPOTCCSCHK/HKG and OTCCHKEXCCP/HKG and EUREXCAGCCP/FRA and JSCC/TYO and SCBOTCCCP/HKG in UK Entity |  |
| New | 7356241418356981760 |  |  | SCH IRS Rule | Entity__Booking_Entity_SCI_FMID == "400899993" && Entity__Counterparty_SCI_FMID == "400202766" && (Instrument_Common__ISDA_Taxonomy == "IRD\|IRS" \|\| Instrument_Common__ISDA_Taxonomy matches "^InterestRate:IRSwap:.*$") && (Cashflow__Payment_Type == "IRS Netting" \|\| (Cashflow__Netting_Id == null \|\| Cashflow__Netting_Id == "")) | SCH IRS Rule |  |
| New | 7356241729352040448 |  |  | SCH OPT Rule | Entity__Booking_Entity_SCI_FMID == "400899993" && Entity__Counterparty_SCI_FMID == "400202766" && Instrument_Common__ISDA_Taxonomy in ('CURR\|OPT\|SMP') && (Cashflow__Netting_Id == null \|\| Cashflow__Netting_Id == "") | SCH OPT Rule |  |

### NSTP rule changes

| Action | Rule ID | Description | Rule Condition | Exception Code | Operational Level | Exception Category | Bulk Eligible | Rule Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| New | 7349345971143090176 | NSTP rule for auto netting resultant cashflow-maker checker | Cashflow__Is_Auto_Netting == true && Cashflow__Auto_Netting_Stp_Level == "NSTP_MAKER_CHECKER" | Auto Netting | MAKER_CHECKER | NSTP | un-ticked |  |
| New | 7349346171361292288 | NSTP rule for auto netting resultant cashflow-checker only | Cashflow__Is_Auto_Netting == true && Cashflow__Auto_Netting_Stp_Level == "NSTP_CHECKER_ONLY" | Auto Netting | CHECKER_ONLY | NSTP | un-ticked |  |
| Update | 7349346493806800896 | Add "&& Cashflow__Is_Auto_Netting == false" condition to existing rule | Cashflow__Netting_Id != null && Cashflow__Netting_Id != "" && Cashflow__Is_Auto_Netting == false | Net Cashflow | MAKER_CHECKER | OTHER | ticked |  |

### SAL netting rules

| Owner | Action | Rule ID | Rule Reason | Rule Condition | Auto Netting Time & Date in GMT | STP for Netting Resultant | Netting Type | Rule Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Yew Fuong | New | 7351573889412694016 | SAL MTM NETTING | Instrument_Common__Murex_Product_Strategy == "SWAP_AGENT" && Cashflow__Payment_Type == "Interim MTM" && (Cashflow__Netting_Id == null \|\| Cashflow__Netting_Id == "") | 01:00 GMT on VD | NSTP for Maker+Checker | SAL MTM NETTING |  |
| Yew Fuong | New | 7351574062254944256 | SAL COUPON NETTING | Instrument_Common__Murex_Product_Strategy == "SWAP_AGENT" && Cashflow__Payment_Type == "Coupon" && (Cashflow__Netting_Id == null \|\| Cashflow__Netting_Id == "") | 01:00 GMT on VD | NSTP for Maker+Checker | SAL COUPON NETTING |  |

### Net-over-net rules

| Owner | Action | Rule ID | Rule Reason | Rule Condition | Counterparty FMCODE | Auto Netting Time & Date in GMT | STP for Netting Resultant | Netting Type | Rule Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Yew Fuong | NEW | 7353999020890193920 | SCH NET OVER NET | Entity__Counterparty_SCI_FMID == "400202766" && ((Cashflow__Payment_Type == "IRS Netting" && (Cashflow__Netting_Id != null && Cashflow__Netting_Id != "")) \|\| (Cashflow__Payment_Type != "IRS Netting" && (Cashflow__Netting_Id == null \|\| Cashflow__Netting_Id == ""))) | 400202766 | 01:00 GMT on VD | NSTP for Maker+Checker | Bilateral Netting |  |
| Pradeesh | NEW | 7356165970688147456 | Case 4 for pradeesh net over net Counterparty - EDELWEISS I S P*SIN | Entity__Counterparty_SCI_FMID == "400617196" && ((Cashflow__Payment_Type == "IRS Netting" && (Cashflow__Netting_Id != null && Cashflow__Netting_Id != "")) \|\| (Cashflow__Payment_Type != "IRS Netting" && (Cashflow__Netting_Id == null \|\| Cashflow__Netting_Id == ""))) | 400617196 | 04:30 GMT on VD | NSTP for Maker+Checker | Bilateral Netting |  |

## Recorded issues and qualifications

- A newly created BIC netting rule was reportedly removed after creation because the rule engine could not recognise the BIC code and required change.
- A currency-related issue is labelled “code bug, already fix” with date `2025-07-28`, but the document provides no formal regression result.
- Missing SSI information in `fmrp1` for specified CITIC, TAIFEX, and HKEX examples is described as non-blocking for this auto-netting UAT only. This does not establish that SSI is immaterial to end-to-end settlement.
- The CME/EUREX/JSCC/ICE predicate correction is documented, but blank rule-status fields do not prove activation.
- The LCH start-time amendment is described as completed, while its rule-status field remains blank.

Open matters are tracked in was cashflow auto netting uat formally passed, what is the authoritative auto netting priority order, was the bic netting rule engine defect remediated, and are clearing resultant swift suppression rules active.
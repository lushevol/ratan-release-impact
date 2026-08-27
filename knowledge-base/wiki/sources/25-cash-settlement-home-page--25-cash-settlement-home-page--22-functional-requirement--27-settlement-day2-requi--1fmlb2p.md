---
type: source
title: Auto Netting for TAIFEX, CITIC, LCH, HKEX, and ECLIPS
authors: []
year: 2026
url: ""
venue: Internal functional requirement
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, auto-netting, IRS, swift-suppression, UAT, RATAN]
related: [ratan, taifex, citic, lch, hkex, irs-net-over-net, cashflow-auto-netting, swift-versus-cashflow-suppression, how-will-eclips-400452428-cashflow-suppression-be-resolved, what-is-the-canonical-eclips-name-and-scope]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Auto Netting for TAIFEX CITIC LCH HKEX ECLIPS.md"]
---
# Auto Netting for TAIFEX, CITIC, LCH, HKEX, and ECLIPS

## Summary

This functional requirement defines RATAN auto-netting and SWIFT-suppression changes for specified FMID pairs covering TAIFEX, CITIC, LCH, HKEX, and ECLIPS.

TAIFEX and CITIC are restricted to IRS-product auto-netting. LCH, HKEX, and ECLIPS are intended to combine eligible IRS aggregation cashflows with other eligible cashflows sharing booking entity, counterparty, currency, and payment date. Resultant cashflows use `Clearing_Swift_Suppress` and are NSTP for Maker+Checker.

The source mandates that the auto-netting rule be approved before the associated SWIFT-suppression rule is changed. It also records an unresolved ECLIPS path for booking entity `400452428`, where a cashflow-suppression rule causes `CASHFLOW_SUPPRESSED` before auto-netting can be evaluated.

## Scope

| Scope | Booking entity FMID | Counterparty FMID | Intended netting scope |
|---|---:|---:|---|
| [[lch]] | `10075222` | `10037537` | All eligible products, including `IRS Netting` cashflows |
| [[hkex]] | `10075222` | `400831212` | All eligible products, including `IRS Netting` cashflows |
| ECLIPS / ECLIP / ECLIPSE | `2`, `400452428` | `400883001` | All eligible products, including `IRS Netting` cashflows |
| [[taifex]] | `10038345` | `401040938` | IRS products only |
| [[citic]] | `2` | `401014221` | IRS products only |

The naming variation ECLIPS, ECLIP, and ECLIPSE remains unresolved; see [[what-is-the-canonical-eclips-name-and-scope]].

## Operational requirements

1. Update and approve the auto-netting rule, including `Payment_Type = IRS Netting`.
2. Only then update the SWIFT-suppression rule to exclude non-auto-netted `IRS Netting` cashflows.
3. Existing cashflows already in `SWIFT_SUPPRESSED` are not retroactively affected by these rule changes.
4. LCH cashflows manually netted as `Ben Bic Netting` and manually SWIFT-suppressed must not be excluded.
5. For ECLIPS booking entity `400452428`, an existing cashflow-suppression rule must be remediated separately because it prevents cashflows from reaching auto-netting.

## Production auto-netting rules

```markdown
| Action | Rule Reason | Rule ID | Pre Rule Condition | Post Rule Condition | Auto Netting Time & Date in GMT | NSTP for Netting Resultant | Netting Type | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| New | TAIFEX IRS Net-over-net rule | 7396512458529169408 | NA | Entity__Booking_Entity_SCI_FMID == "10038345" && Entity__Counterparty_SCI_FMID == "401040938" && (Instrument_Common__ISDA_Taxonomy == "IRD\|IRS" \|\| Instrument_Common__ISDA_Taxonomy matches "^InterestRate:IRSwap:.*$") && (Cashflow__Payment_Type == "IRS Netting" \|\| (Cashflow__Netting_Id == null \|\| Cashflow__Netting_Id == "")) | 01:00 GMT on VD | NSTP for Maker+Checker | Clearing_Swift_Suppress | 2025-11-18 |
| New | CITIC IRS Net-over-net rule | 7396491047030874112 | NA | Entity__Booking_Entity_SCI_FMID == "2" && Entity__Counterparty_SCI_FMID == "401014221" && (Instrument_Common__ISDA_Taxonomy == "IRD\|IRS" \|\| Instrument_Common__ISDA_Taxonomy matches "^InterestRate:IRSwap:.*$") && (Cashflow__Payment_Type == "IRS Netting" \|\| (Cashflow__Netting_Id == null \|\| Cashflow__Netting_Id == "")) | 01:00 GMT on VD | NSTP for Maker+Checker | Clearing_Swift_Suppress | 2025-11-18 |
| Updated | UK LCH All Products netting | 7403803601990774784 | Entity__Counterparty_SCI_FMID == "10037537" && Entity__Booking_Entity_SCI_FMID == "10075222" && (Cashflow__Netting_Id == null \|\| Cashflow__Netting_Id == "") | Entity__Booking_Entity_SCI_FMID == "10075222" && Entity__Counterparty_SCI_FMID == "10037537" && (Cashflow__Payment_Type == "IRS Netting" \|\| Cashflow__Netting_Id == "" \|\| Cashflow__Netting_Id == null) | 12:00 GMT on VD | NSTP for Maker+Checker | Clearing_Swift_Suppress | 2025-12-09 |
| Updated | HKEX All Products netting | 7403799034279817216 | Entity__Booking_Entity_SCI_FMID == "10075222" && Entity__Counterparty_SCI_FMID == "400831212" && ((Cashflow__Netting_Id == null \|\| Cashflow__Netting_Id == "")) | Entity__Booking_Entity_SCI_FMID == "10075222" && Entity__Counterparty_SCI_FMID == "400831212" && (Cashflow__Payment_Type == "IRS Netting" \|\| Cashflow__Netting_Id == "" \|\| Cashflow__Netting_Id == null) | 01:00 GMT on VD | NSTP for Maker+Checker | Clearing_Swift_Suppress | 2025-12-09 |
| New | ECLIP SCB HK LCH*LDN | No existing rule |  | Entity__Booking_Entity_SCI_FMID in ("2", "400452428") && Entity__Counterparty_SCI_FMID == "400883001" && (Cashflow__Payment_Type == "IRS Netting" \|\| Cashflow__Netting_Id == "" \|\| Cashflow__Netting_Id == null) | 01:00 GMT on VD | NSTP for Maker+Checker | Clearing_Swift_Suppress | ![image-2026-1-5_9-49-31.png](attachments/image-2026-1-5_9-49-31.png) |
```

## Production SWIFT-suppression rules

```markdown
| Action | Pre Rule Condition | Post Rule Condition | Rule Reason | Existing Rule ID | Status |
| --- | --- | --- | --- | --- | --- |
| Update | Entity__Counterparty_SCI_FMID == "401040938" && Entity__Booking_Entity_SCI_FMID == "10038345" && ((Cashflow__Netting_Id != null && Cashflow__Netting_Id != "") \|\| ((Cashflow__Netting_Id == null \|\| Cashflow__Netting_Id == "") && Cashflow__Is_Auto_Netting == true)) | Entity__Counterparty_SCI_FMID == "401040938" && Entity__Booking_Entity_SCI_FMID == "10038345" && ((Cashflow__Netting_Id != null && Cashflow__Netting_Id != "" && Cashflow__Payment_Type != "IRS Netting") \|\| ((Cashflow__Netting_Id == null \|\| Cashflow__Netting_Id == "") && Cashflow__Is_Auto_Netting == true) \|\| (Cashflow__Payment_Type == "IRS Netting" && Cashflow__Is_Auto_Netting == true)) | TAIFEX Net Resultant | 7372176807130329088 | 2025-11-28 |
| Update | Entity__Counterparty_SCI_FMID == "401014221" && Entity__Booking_Entity_SCI_FMID == "2" && ((Cashflow__Netting_Id != null && Cashflow__Netting_Id != "") \|\| ((Cashflow__Netting_Id == null \|\| Cashflow__Netting_Id == "") && Cashflow__Is_Auto_Netting == true)) | Entity__Counterparty_SCI_FMID == "401014221" && Entity__Booking_Entity_SCI_FMID == "2" && ((Cashflow__Netting_Id != null && Cashflow__Netting_Id != "" && Cashflow__Payment_Type != "IRS Netting") \|\| ((Cashflow__Netting_Id == null \|\| Cashflow__Netting_Id == "") && Cashflow__Is_Auto_Netting == true) \|\| (Cashflow__Payment_Type == "IRS Netting" && Cashflow__Is_Auto_Netting == true)) | CITIC Net Resultant | 7396492598654918656 | 2025-11-27 |
| Update | Entity__Counterparty_SCI_FMID == "10037537" && Entity__Booking_Entity_SCI_FMID == "10075222" && ((Cashflow__Netting_Id != null && Cashflow__Netting_Id != "") \|\| ((Cashflow__Netting_Id == null \|\| Cashflow__Netting_Id == "") && Cashflow__Is_Auto_Netting == true)) | Entity__Counterparty_SCI_FMID == "10037537" && Entity__Booking_Entity_SCI_FMID == "10075222" && ((Cashflow__Netting_Id != null && Cashflow__Netting_Id != "" && Cashflow__Payment_Type != "IRS Netting") \|\| ((Cashflow__Netting_Id == null \|\| Cashflow__Netting_Id == "") && Cashflow__Is_Auto_Netting == true) \|\| (Cashflow__Payment_Type == "IRS Netting" && Cashflow__Is_Auto_Netting == true)) | LCH Net Resultant | Pre 7368641207195099136 Post 7403801024254767104 | 2025-12-09 |
| Update | Entity__Counterparty_SCI_FMID == "400831212" && Entity__Booking_Entity_SCI_FMID == "10075222" && ((Cashflow__Netting_Id != null && Cashflow__Netting_Id != "") \|\| ((Cashflow__Netting_Id == null \|\| Cashflow__Netting_Id == "") && Cashflow__Is_Auto_Netting == true)) | Entity__Counterparty_SCI_FMID == "400831212" && Entity__Booking_Entity_SCI_FMID == "10075222" && ((Cashflow__Netting_Id != null && Cashflow__Netting_Id != "" && Cashflow__Payment_Type != "IRS Netting") \|\| ((Cashflow__Netting_Id == null \|\| Cashflow__Netting_Id == "") && Cashflow__Is_Auto_Netting == true) \|\| (Cashflow__Payment_Type == "IRS Netting" && Cashflow__Is_Auto_Netting == true)) | HKEX Net Resultant | Pre 7370706055416492032 Post 7403797646082633728 | 2025-12-09 |
| Update | Entity__Booking_Entity_SCI_FMID == "2" && Entity__Counterparty_SCI_FMID == "400883001" | Entity__Counterparty_SCI_FMID == "400883001" && Entity__Booking_Entity_SCI_FMID in ("2", "400452428") && ((Cashflow__Netting_Id != null && Cashflow__Netting_Id != "" && Cashflow__Payment_Type != "IRS Netting") \|\| ((Cashflow__Netting_Id == null \|\| Cashflow__Netting_Id == "") && Cashflow__Is_Auto_Netting == true) \|\| (Cashflow__Payment_Type == "IRS Netting" && Cashflow__Is_Auto_Netting == true)) | SCB HK - ECLIPSE SCB HK LCH - Swift suppression | 7312735397309550592 | ![image-2026-1-5_9-49-42.png](attachments/image-2026-1-5_9-49-42.png) |
```

## UAT evidence and limitation

UAT scenarios were recorded for TAIFEX, CITIC, LCH, HKEX, and ECLIPS. Hui Chien Khoo is listed as tester for the first four scopes; Hii Yew Fuong is listed for ECLIPS. The `Test Result` field is blank for every scenario, so the material evidences test execution and screenshots rather than formal acceptance.

A separate mock-data test by Grace showed that ECLIPS booking entity `400452428` and counterparty `400883001` enter `CASHFLOW_SUPPRESSED` under an existing suppression rule and do not reach auto-netting. This path is an unresolved dependency tracked in [[how-will-eclips-400452428-cashflow-suppression-be-resolved]].

## Implications

- The scope is explicitly limited to the stated booking-entity and counterparty FMID pairs.
- `SWIFT_SUPPRESSED` and `CASHFLOW_SUPPRESSED` have different operational consequences. Historical `SWIFT_SUPPRESSED` cashflows are not retrospectively remediated; `CASHFLOW_SUPPRESSED` can prevent initial auto-netting eligibility.
- The detailed rule table gives `01:00 GMT on VD` for TAIFEX, CITIC, HKEX, and ECLIPS, and `12:00 GMT on VD` for LCH. The narrative’s `-01:00 GMT on VD` notation remains ambiguous.
- The TAIFEX and CITIC rule expressions allow `IRS Netting` payment types or empty/null `Cashflow__Netting_Id` subject to IRS taxonomy; intended eligibility semantics require confirmation.
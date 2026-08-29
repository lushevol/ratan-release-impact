---
type: entity
title: CITIC
created: 2026-08-22
updated: 2026-08-23
tags: ["counterparty", "cash-settlement", "auto-netting", "IRS", "CITIC", "net-over-net", "SWIFT-suppression", "uat", "cashflow-auto-netting", "hong-kong"]
related: ["ratan", "irs-net-over-net", "cashflow-auto-netting", "net-over-net", "clearing-swift-suppression", "bic-netting", "shanghai-clearing-house", "uat-test-case"]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Auto Netting Static Go Live Process.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Auto Netting for TAIFEX CITIC LCH HKEX ECLIPS.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Cashflow Auto Netting UAT testing sample.md"]
---
# CITIC

CITIC is an FMID-scoped business scope in the documented RATAN auto-netting requirement. It is also identified as the counterparty for the SHACITIC/BJG Clearing rule and a later IRS net-over-net rule.

## IRS net-over-net configuration

According to the **Auto Netting for TAIFEX CITIC LCH HKEX ECLIPS** source, the applicable CITIC pair is booking entity `2` and counterparty `401014221`. Auto-netting is limited to IRS products.

That source identifies rule `7396491047030874112` as the CITIC IRS net-over-net rule, scheduled for `01:00 GMT on VD`.

According to the **Auto Netting Static Go Live Process** source, the later IRS net-over-net rule applies to booking entity `2`, counterparty `401014221`, and the following IRS taxonomy and cashflow criteria:

```text
Entity__Booking_Entity_SCI_FMID == "2" && Entity__Counterparty_SCI_FMID == "401014221" && (Instrument_Common__ISDA_Taxonomy == "IRD|IRS" || Instrument_Common__ISDA_Taxonomy matches "^InterestRate:IRSwap:.*$") && (Cashflow__Payment_Type == "IRS Netting" || (Cashflow__Netting_Id == null || Cashflow__Netting_Id == ""))
```

The Static Go Live Process source classifies this rule as `Clearing_Swift_Suppress`, specifies NSTP for Maker+Checker, and schedules it for `01:00 GMT on VD`.

## SWIFT suppression

According to the **Auto Netting for TAIFEX CITIC LCH HKEX ECLIPS** source, the related SWIFT-suppression rule is `7396492598654918656`.

The **Auto Netting Static Go Live Process** source lists a CITIC suppression update with pre-update logic but does not provide a post-update condition. Therefore, that source leaves the final suppression behavior unresolved and should not be treated as complete production configuration.

## UAT cohort

According to the **Cashflow Auto Netting UAT testing sample** source, CITIC is a named UAT cohort in the Cashflow Auto Netting test inventory. It contains 9 cashflows booked by `SCB HONGKON*HKG` against `CITICSECCOLTD*BJG`.

That source identifies CITIC as a test cohort but does not provide execution results, netting expectations, or additional organizational details.
---
type: entity
title: TAIFEX
created: 2026-08-22
updated: 2026-08-23
tags: [clearing, cash-settlement, auto-netting, IRS, clearing-house, TAIFEX, net-over-net, exchange, uat, cashflow-auto-netting, taipei]
related: [ratan, irs-net-over-net, cashflow-auto-netting, net-over-net, clearing-swift-suppression, uat-test-case]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Auto Netting for TAIFEX CITIC LCH HKEX ECLIPS.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Auto Netting Static Go Live Process.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Cashflow Auto Netting UAT testing sample.md"]
---
# TAIFEX

TAIFEX is an FMID-scoped business scope and clearing-house scope for an IRS net-over-net auto-netting rule in the documented RATAN requirement.

TAIFEX is also a named UAT cohort in the Cashflow Auto Netting test inventory. The UAT sample contains 16 cashflows booked by `SCB TAIPEI*TPE` against `TAIFEX/TWN*TPE`. The UAT source identifies TAIFEX as a test cohort but does not provide execution results, netting expectations, or additional exchange details.

## Auto-netting rule

The applicable pair in the RATAN requirement is booking entity `10038345` and counterparty `401040938`. The requirement limits auto-netting to IRS products and identifies rule `7396512458529169408` as the TAIFEX IRS net-over-net rule, scheduled for `01:00 GMT on VD`.

The generated static go-live process version describes a rule that matches IRS taxonomy values or patterns and either IRS netting payment types or cashflows without a `Cashflow__Netting_Id`:

```text
Entity__Booking_Entity_SCI_FMID == "10038345" && Entity__Counterparty_SCI_FMID == "401040938" && (Instrument_Common__ISDA_Taxonomy == "IRD|IRS" || Instrument_Common__ISDA_Taxonomy matches "^InterestRate:IRSwap:.*$") && (Cashflow__Payment_Type == "IRS Netting" || (Cashflow__Netting_Id == null || Cashflow__Netting_Id == ""))
```

That static go-live process version classifies the rule as `Clearing_Swift_Suppress` and states that it uses NSTP for Maker+Checker at `01:00 GMT on VD`.

## SWIFT suppression behavior

The related SWIFT-suppression rule is `7372176807130329088`.

The RATAN auto-netting requirement states that its updated condition excludes non-auto-netted `IRS Netting` cashflows while allowing auto-netted IRS Netting cashflows to be suppressed as resultants.

The generated static go-live process version describes the TAIFEX suppression update as including:

- Existing netting-ID resultants whose payment type is not `IRS Netting`.
- Cashflows without a netting ID when `Cashflow__Is_Auto_Netting == true`.
- IRS netting cashflows when `Cashflow__Is_Auto_Netting == true`.

This static go-live process version explicitly links suppression to auto-netting status for IRS net-over-net cashflows.
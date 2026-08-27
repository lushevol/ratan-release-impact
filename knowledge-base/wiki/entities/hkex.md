---
type: entity
title: HKEX
created: 2026-08-22
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Auto Netting for TAIFEX CITIC LCH HKEX ECLIPS.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Cashflow Auto Netting UAT testing sample.md"]
tags: ["exchange", "cash-settlement", "auto-netting", "IRS", "uat", "cashflow-auto-netting", "hong-kong"]
related: ["ratan", "irs-net-over-net", "cashflow-auto-netting", "swift-versus-cashflow-suppression", "uat-test-case"]
updated: 2026-08-23
---

# HKEX

## RATAN auto-netting requirement

In the documented RATAN requirement for all-product auto-netting, HKEX is a clearing scope that incorporates `IRS Netting` cashflows.

The applicable pair is booking entity `10075222` and counterparty `400831212`. Updated auto-netting rule `7403799034279817216` runs at `01:00 GMT on VD`; resultant cashflows are NSTP for Maker+Checker under `Clearing_Swift_Suppress`.

The associated SWIFT-suppression rule changed from `7370706055416492032` to `7403797646082633728`.

## UAT test cohort

In the Cashflow Auto Netting UAT testing sample, HKEX is a named UAT cohort containing 44 cashflows booked by `SCB LONDON*LDN` against `SCBOTCCCP*HKG`.

That source identifies HKEX as a test cohort but does not provide execution results, netting expectations, or additional exchange details.
---
type: entity
title: LCH
created: 2026-08-22
updated: 2026-08-23
tags: [clearing-house, cash-settlement, auto-netting, IRS, LCH, SWIFT-suppression, uat, cashflow-auto-netting, london]
related: [ratan, irs-net-over-net, cashflow-auto-netting, swift-versus-cashflow-suppression, clearing-swift-suppression, uat-test-case]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Auto Netting for TAIFEX CITIC LCH HKEX ECLIPS.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Auto Netting Static Go Live Process.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Cashflow Auto Netting UAT testing sample.md"]
---
# LCH

LCH appears in two source contexts:

- In the documented RATAN requirement, LCH is a clearing-house scope for planned all-product auto-netting incorporating `IRS Netting` cashflows and resultant SWIFT suppression.
- In the Cashflow Auto Netting UAT test inventory, LCH is a named UAT cohort. It is the largest cohort, containing 69 cashflows booked by `SCB LONDON*LDN` against `LCH*LDN`.

## RATAN requirement scope

The applicable booking-entity and counterparty pair is:

- Booking entity: `10075222`
- Counterparty: `10037537`

## Auto-netting and SWIFT suppression

### Existing-version requirements

The existing version records that updated auto-netting rule `7403803601990774784` runs at `12:00 GMT on VD`.

Resultant cashflows are NSTP for Maker+Checker under `Clearing_Swift_Suppress`.

Cashflows manually netted as `Ben Bic Netting` and manually SWIFT-suppressed remain in scope and must not be excluded.

The associated SWIFT-suppression rule changed from `7368641207195099136` to `7403801024254767104`.

### Newly generated version: proposed suppression criteria

The newly generated version describes a proposed suppression rule for booking entity `10075222` and counterparty `10037537`. The rule suppresses:

- Cashflows with a populated `Cashflow__Netting_Id`
- Single cashflows marked `Cashflow__Is_Auto_Netting == true`

According to that version, the suppression rule should be created when the LCH auto-netting rule is enabled. It does not provide a final activation record.

## UAT cohort information

The UAT-testing-sample source identifies LCH as a test cohort but does not provide execution results, netting expectations, or clearing rules.
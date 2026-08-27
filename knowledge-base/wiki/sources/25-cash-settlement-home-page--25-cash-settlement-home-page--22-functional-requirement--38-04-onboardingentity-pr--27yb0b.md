---
type: source
title: China Hefei Branch Setup
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, entity-onboarding, hefei, swift, ebbs, ssi]
related: [scb-hefei, cash-settlement-entity-onboarding, does-hefei-ssi-propagate-as-a-global-murex-ssi, is-hefei-bridge-account-560100000001910205-approved]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/New Entity onboarding checking list/China Hefei Branch Setup.md"]
authors: []
year: 2026
url: ""
venue: ""
---
# China Hefei Branch Setup

## Summary

This operational checklist defines the configuration needed to onboard China Hefei Branch as a booking and settlement entity across LMS, SWIFT, EBBS, static data, business rules, and the Cash Settlement Home Page interface.

The document specifies the intended SWIFT identifiers and branch mapping, inherited China Head Office release timing, and limited branch-specific SSI requirements. It also records unresolved dependencies: confirmation of the bridge account, possible propagation of Hefei SSIs into [[murex-211]] as Global SSIs, GUI dropdown completion, and end-to-end UAT and regression evidence.

“Done” markers on suppression-related rules establish task-status assertions only. The source provides no deployment environment, effective date, approval, or test evidence.

## Key Configuration

- Booking Entity FMID: `401053411`
- Booking Entity FMCODE: `SCB CHINA*HFI`
- Sender BIC: `SCBLCNSXHFI`
- Field 53 BIC: `SCBLCNSXGMO`
- Field 58 BIC in Flip MT202: `SCBLCNSXGMO`
- Branch code: `73`
- EBBS branch code: `73`
- Proposed bridge account: `560100000001910205`, subject to confirmation by Balaji
- Currency release timing: follow China Head Office
- Currency mapping: no new codes to be mapped

See [[scb-hefei]] for the entity-specific configuration profile and [[cash-settlement-entity-onboarding]] for the reusable onboarding control model.

## Original Checklist

| # | Description | Type | Data | Done By |
| --- | --- | --- | --- | --- |
| 1 | LMS Feed Entity List Update | Config | Send to LMS | Dev Team (CR) |
| 2 | SWIFT Generation Changes - Booking Entity SWIFT BIC - Field 53 SWIFT BIC - Branch code mapping - Any other branch specific requirement on SWIFT | Config | - Booking Entity FMID: 401053411<br>- Booking Entity FMCODE: SCB CHINA*HFI<br>- Booking Entity BIC: SCBLCNSXHFI (Sender BIC in SWIFT)<br>- Field 53 BIC: SCBLCNSXGMO (LCY & Over-Account)<br>- Field 58 in Flip MT202: SCBLCNSXGMO<br>- Branch code: 73<br>- Assumption: No other branch specific requirement on SWIFT |  |
| 3 | Currency Release Time | Config | Follow China HO Release Time |  |
| 4 | Currency Configuration (if applicable) - Non-ISO to ISO Code mapping - Precious Currency Mapping | Config | No new codes to be mapped |  |
| 5 | Settlement Accounting - Bridge Account # - EBBS Branch code - EBBS Transaction code - Any other branch specific requirement | Config | - Bridge Account # 560100000001910205 (TBC by Balaji)<br>- EBBS branch code: 73<br>- EBBS Transaction code: Follow China<br>- No other branch specific requirement |  |
| 6 | Include new branch in GUI Drop down - Cashflow Blotter - Dashboard | Config |  |  |
| 7 | Nostro Static Setup | Static | Provided via Email | Data Ops / Dev Team (CR) |
| 8 | Vostro Static Setup (Vostro to drive Nostro assignment) | Static | - Existing SSI's which are Global will be auto picked up<br>- Hefei branch specific SSI's will be required only for SUPPRESSXX (Nostro auto debit) or Over-Account clients. External Client SSI's not expected to be traded as of now<br>- Open Issue: SSI created for Hefei branch flown into MX2.11 as a Global SSI | Data Ops |
| 9 | Business Rules Setup (Suppression / NSTP / Netting) | Static | - No NSTP<br>- Swift Suppression: SCB Hefei to be added as a Counterparty + FCY<br>- Weng Hien to raise to data ops SCH202G210A1190225096333 // Rule ID 7230060232576802816 Done<br>- Existing Rules which have China Booking Entities: Sumi/WH Done via eOps SCH202G210A1200225022654<br>- Existing Rules which have China Entities as Counterparty: Sumi/WH Done via eOps SCH202G210A1200225022654 | Data Ops |
| 10 | Downstream Engagement to determine additional requirements if any | Analysis |  | Dev Team |
| 11 | UAT | Testing |  | Settlement Ops |
| 12 | Regression Testing | Testing |  | Dev Team |

## Outstanding Evidence

The checklist does not establish completion or validation for the LMS update, SWIFT configuration, China Head Office release-time dependency, bridge-account approval, GUI changes, SSI setup, downstream assessment, UAT, or regression testing.

The explicit SSI issue is tracked in [[does-hefei-ssi-propagate-as-a-global-murex-ssi]]. Bridge-account confirmation and EBBS posting validation are tracked in [[is-hefei-bridge-account-560100000001910205-approved]].
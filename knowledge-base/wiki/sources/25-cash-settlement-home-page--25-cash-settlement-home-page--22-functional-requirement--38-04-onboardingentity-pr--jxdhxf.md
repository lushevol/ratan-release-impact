---
type: source
title: F2B Milestone Onboarding Checklist for FXO
authors: []
year: 2025
url: ""
venue: ""
created: 2026-08-22
updated: 2026-08-22
tags: [fxo, onboarding, cash-settlement, fmrp, ratan, functional-requirements]
related: [fxo, fmrp, ratan, murex, razor, stella, aspire, ebbs, cashflow-blotter, grouping-blotter, currency-transformation-for-settlement-instructions, netting-over-netting, cashflow-suppression-rules, pending-fixing-stp-nstp-control, migration-duplicate-payment-prevention, cross-product-netting, netting-key-selection]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/F2B Milestone Onboarding check list/F2B Milestone check list - FXO.md"]
---
# F2B Milestone Onboarding Checklist for FXO

## Summary

This working checklist identifies functional and configuration considerations for onboarding [[fxo]] into a front-to-back settlement architecture involving [[murex]], [[fmrp]], [[ratan]], [[razor]], [[stella]], [[aspire]], and [[ebbs]]. Its scope includes settlement-instruction stamping, cashflow status, booking models, netting, SWIFT messaging, accounting, migration, static data, business rules, and branch configuration.

The document is a discovery and readiness checklist rather than evidence that the capabilities have been approved, implemented, or tested. Most entries have no owner, status, acceptance criteria, test evidence, or completion date.

## Key Requirements and Constraints

FX spot, forward, and swap cashflows are expected to enter `SUSPENDED` processing and bypass MO validation in the [[grouping-blotter]]. Exercise events are expected to generate an FXD trade in `SUSPENDED` status. The checklist does not define release authority, status transitions, or downstream behavior.

SSI and Nostro stamping depend on the selected hierarchy, CFI code, settlement method, agent topology, and currency transformation. One-agent and two-agent arrangements are listed as supported, while three-agent processing is explicitly unsupported. The proposed UK hierarchy gives `Country Specific + Global Product` SSI priority over `Global Entity + Product Specific` SSI, but its approval and FXO applicability are not recorded.

The booking model determines the proposed netting identifier:

- RFR Booking Model uses LTID.
- ND CCS and ND IRS use NID.
- Structures use Structure ID.

These associations are specific to the listed booking models and do not establish a universal netting algorithm.

The messaging inventory covers SWIFT MT and ISO 20022 MX messages. Exact profiles, field mappings, validation rules, and the complete version for `camt.057` remain unspecified.

The accounting direction favors [[ebbs]], while [[aspire]] remains relevant for suspense accounting in the Keystone (HK) example. It is unclear whether this split is transitional or a permanent regional exception.

Migration from [[murex]] to [[fmrp]] must prevent duplicate payments and account for near-value cashflows, historical cashflows, and events applied to past-value cashflows after cutover. The checklist does not define the required reconciliation, idempotency, freeze-window, or rollback controls.

## Open Issues

The source leaves several material questions unresolved:

- Whether the UK SSI hierarchy replaces the old hierarchy for FXO.
- Which system is the golden source for Nostro data.
- How unsupported three-agent trades are handled.
- Whether ND CCS may use netting over netting.
- Whether [[ebbs]] and [[aspire]] coexist in the target accounting model.
- Which rules control routing between [[razor]] and [[ratan]].
- Which exact SWIFT MX versions and implementation profiles apply.
- How Murex fields map to FMRP fields.
- Which entries are FXO-specific and which are reusable onboarding controls.

See [[which-ssi-hierarchy-applies-to-fxo]], [[what-is-the-golden-source-for-nostro-data]], [[how-are-three-agent-trades-handled]], and [[should-nd-ccs-support-netting-over-netting]].

## Referenced Images

The source references two images whose contents were not available for evaluation:

- [image-2025-4-25_11-35-37.png](../media/26-auto-netting-page-md-files--195-cash-settlement-home-page-cash-settlement-home-page-functional-requirement-04--qhy3fk/image-2025-4-25_11-35-37.png)
- [image-2025-5-21_15-16-14.png](../media/26-auto-netting-page-md-files--195-cash-settlement-home-page-cash-settlement-home-page-functional-requirement-04--qhy3fk/image-2025-5-21_15-16-14.png)

## Preserved Checklist

| | Function | Feature | | Consideration | Test Case/Scenario |
| --- | --- | --- | --- | --- | --- |
| 1 | GENERIC | SI INPUT | - Missing Vostro - Multi Vostro - Adhoc SI update - Missing Nostro | | |
| 2 | | SSI Auto Stamping | - SSI Auto Stamping Hierarchy (Old vs New) - CFI code Selection - Settlement Method (FEDWIRE / CASH) - Single Agent / Two Agent Supported (3 Agent not supported) - Trade SSI Stamping to CDUPS (XML + Product based) - Currency code transformation (when receive SGO, lookup SGD) | Any new currency transformation required | - To check whether is it all booked under inter entity for Loan; - if inter entity is expected, then should check SSI Stamping - FXO is expected to see SSI Stamping |
| 3 | | Nostro Auto Stamping | - Default Nostro Stamping - Currency code transformation (when receive SGO, lookup SGD) | | |
| 4 | | Dashboard | | | FX cashflows are in SUSPENDED status |
| 5 | | Grouping Blotter | | 1. FX cash (spot/forward/swap) should be in SUSPENED Status 2. Bypass MO validation for FX cash (spot/forward/swap) | |
| 6 | | Cashflow Blotter | - New Fields introduced for Murex Flow - LIEN - Pending Fixing - Duplicate NDS - LTID, Structure ID, NID - Commodity Flag - Alpha Clearing | - New Fields Required - Murex Fields Equivalent in FMRP | |
| 7 | | SWIFT Generation | - MT Generation - MT103, 202, MT103+202COV, MT210, FlipMT202, MT192, MT292, MT604, MT605, MT692 - MX Generation - Pacs.008.001.08 (MT103) - Pacs.009.001.08 (MT202 & 202COV) - Camt.056.001.08(MT192 & MT292) - **camt.057(MT210)** | - New Message types required - Format changes required for new product / flow | |
| 8 | | Accounting Generation | - EBBS - Real Time Feed - ASPIRE Integration - EOD Feed | - Keystone (HK): Feed Nostro & Over Account to EBBS, feed Suspense to Aspire - Move from Aspire to EBBS model - handling of historic cashflows & events on past value cashflows post cutover | |
| 9 | New Event | Exercise | | | will generate a FXD trade which in SUSPENDED status |
| 10 | | Expiry | | | Trade is settled with settlement fee |
| 11 | Booking Model Impact | Package Bookings | B2B Package | | |
| 12 | | | Package Booking Model | | |
| 13 | | | RFR Booking Model (Netting based on LTID) | | |
| 14 | | | Swap Agent | | |
| 15 | | | ND Currency Handling (ND CCS / ND IRS) (Netting based on NID) | | |
| 16 | | | Structures (Netted based on Structure ID) | | |
| 17 | | Rollover | | | |
| 18 | | Fixing | | | |
| 19 | | Option | Exercise & Expiry | | |
| 20 | | Strategy / Typology | | How Strategy / Typology will be supported in FMRP | |
| 21 | | Clearing | | | |
| 22 | | LIEN | | How LIEN will be available as part of Trade Migration | |
| 23 | | Allocation | | | |
| 24 | | FX Replication | | - Razor FX Dev team to be engaged on Dev changes / UAT support required - Razor FX Settlement team needs to be engaged for UAT support | |
| 25 | NETTING | BILATERAL MANUAL NETTING | | | |
| 26 | | CCIL MANUAL NETTING | | | |
| 27 | | BIC NETTING (MANUAL) | | | |
| 28 | | NDS AUTO NETTING | | | |
| 29 | | IRS AUTO NETTING | | | |
| 30 | | CROSS PRODUCT NETTING WITHIN RATAN | | | |
| 31 | STATIC | BILATERAL NETTING | | | |
| 32 | | BIC NETTING | | | |
| 33 | | VOSTRO SSI | | New Settlement Means & Settlement Account | |
| 34 | | NOSTRO [Golden Source TBC ] | | New Settlement Means & Settlement Account | |
| 35 | BUSINESS RULES | NSTP RULES | | - Add new entity to Rules where SCB Entities as Counterparty is bypassed - Add new entity to Rules where SCB entities are added as Booking Entity | |
| 36 | | SWIFT SUPPRESSION RULES | - Auto Debit by Agent - Nostros shared with other entity (example: China) | | |
| 37 | | CASFHLOW SUPPRESSION RULES | | - There're specific filter logic in Murex → RATAN cashflow interface to exclude auto suppression counterparties. Need to config these as RATAN suppression rule so that they can be suppressed for STELLA cashflows | |
| 38 | | Authorization Limits | | | |
| 39 | Settlement Method | CCIL | | | |
| 40 | | DVP | NSTP based on DVP | | |
| 41 | Migration | - Murex to FMRP Migration - Prevent Duplicate payment - Cutover handling - New Function / Changes - Historical data handling | | ISO Migration: handling of near value cashflows & events on past value cashflows post cutover | |
| 42 | CONFIG | LMS Entity List | | | |
| 43 | | [Murex Cash Migration Only] Entity list for the Batch Solution | | | |
| 44 | | - BCS vs Strategic Routing - Entity whitelist for in scope entities (covered via Cashflow Suppression rule) - Entity whitelist setup to send to RAZOR or handle in RATAN (RATAN generates SWIFT & Accounting | | | |
| 45 | | SWIFT Generation Changes - Booking Entity FMID - Booking Entity SWIFT BIC (Sender BIC in SWIFT) - Field 53 SWIFT BIC (for Local Currency LCY & Over Account) - Field 58 SWIFT BIC (for Flip MT202) - Branch code mapping - Any other branch specific requirement on SWIFT | | | |
| 46 | | Currency Release Time | | | |
| 47 | | NDS Auto Netting | | | |
| 48 | | Pending Fixing STP/NSTP Control( in case new product have fixing events) | | New STELLA products which require pending fixing - Loan Deposit: Principal and Interest netting together | |
| 49 | | SSI Stamping Hierarchy - Follow UK model (give priority to "Country Specific + Global Product" SSI over Global Entity + Product Specific SSI) | | | |
| 50 | | Currency Configuration (if applicable) - Non-ISO to ISO Code mapping - Precious Currency Mapping | | Whether onshore ccy is applicable | |
| 51 | | Currency Transformation (example SGO to SGD) - Use SGD to lookup Vostro - Use SGD to lookup Nostro | | | |
| 52 | | Settlement Accounting - Bridge Account # - EBBS Branch code - EBBS Transaction type - Any other branch specific requirement (example: Settlement Accounting is suppressed for Precious Metal CCY's in UK) | | Whether onshore ccy is applicable and what should be sent to downstream | |
| 53 | | Include new branch in GUI Drop down - Cashflow Blotter - Dashboard | | | |
| 54 | | Vostro SI Input Screen - Include New Settlement Means | | | |
| 55 | | Rounding | | | |
| 56 | | Restriction on Netting over Netting - only IRS is allowed. ND IRS follows same ISDA taxonomy | | Any new product that requires netting over netting to be supported Need to update config to allow ND CCS | | 
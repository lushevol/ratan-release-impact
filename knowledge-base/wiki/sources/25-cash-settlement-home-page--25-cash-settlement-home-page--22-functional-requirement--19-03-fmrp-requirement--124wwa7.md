---
type: source
title: Cashflow Migration Tranche 1 — FMRP Requirement
authors: []
year: 2025
url: "https://confluence.global.standardchartered.com/display/FMRP/2025+Settlements+Tranche+1+-+HK%2C+TW%2C+TH%2C+US+Requirements"
venue: Confluence
created: 2026-08-22
updated: 2026-08-22
tags: [fmrp, cashflow-migration, tranche-1, ratan, murex, settlements, functional-requirements]
related: [fmrp, ratan, murex, stella, uber, razor, projects/murex-cashflow-migration-to-ratan, fmrp-to-ratan-migration-scope, allocation-cashflow-state-handling, fmrp-market-event-settlement-impact, fmrp-trade-attribute-cashflow-nstp]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/03-FMRP Requirement.md"]
---
# Cashflow Migration Tranche 1 — FMRP Requirement

## Summary

This requirement document describes Cashflow Migration Tranche 1 and the associated FMRP business features for Hong Kong, Taiwan, Thailand, and the United States. It is a planning and requirements-tracking document rather than a finalized functional specification. The document identifies candidate Murex entities, F2B milestones, feature dependencies, possible RATAN changes, UAT responsibilities, and new market events.

The central settlement impacts concern:

- Allocation events and the use of `SUSPENDED` and `PROJECTED` cashflow states.
- New trade attributes, including `Structure id` and `TRAN_CLEAR`.
- Hedge-accounting classification through `Trade_Purpose = 'Accrued_Interest'`.
- Clearing, Remaining Party, Refresh, UNDO, Step In, and Allocation events.
- Deliverable-currency and non-USD settlement for HK/TW products.
- Trade migration validation and duplicate-payment controls for approximately 70,000 live trades.

The source does not establish authoritative FMIDs, mandatory flags, target release dates, complete interface mappings, or final RATAN ownership for every feature.

## Tranche 1 entity list

| Murex Entity Name | Entity FMID | Mandatory | Target Release Date |
| --- | --- | --- | --- |
| HONGKONG |  |  |  |
| SCS HK |  |  |  |
| BANGKOK |  |  |  |
| TAIPEI |  |  |  |
| OBU TAIPEI |  |  |  |
| NEWYORK |  |  |  |

## F2B milestones and features

| Milestone | Features | Desc | RATAN Changes | Priority | Comment |
| --- | --- | --- | --- | --- | --- |
| - [FMRP 6.0 - BAU - Business Features List - Boards](https://dev.azure.com/sc-ado/FMQPR/_queries/query/80bd0d86-6575-4fbd-af6a-80caae0040e3/) | [FEATURE 7794805](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/7794805) | Business Feature - Make RATAN agnostic to schedule data |  |  |  |
|  | FEATURE 7617931 | Business Feature - Redesign of Allocation Flag and use of SUSPENDED cashflow states | Settlement Placeholder of Q2 BRP? |  | 1. Redesign the allocation event 2. RATAN to filter out the cashflows from allocation events. |
|  | [FEATURE 6525482](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/6525482) | Business Feature - Refactoring of Clearing Event and Remaining Party Full | Settlement Placeholder of Q2 BRP for analysis & UAT support? | Q2 | 1. New event: Clearing - no new trade id 2. RemainingPartyFull - new trade id for new trade |
|  | FEATURE 6904617 | Business Feature - Hedge acc - TM IRS Booking Flow (including trade, cash and position generation) |  |  | 1. "modular" terminations and partial terminations |
|  | FEATURE 6913820 | Business Feature - Enable UNDO for live trade |  |  | 1. Extend the Undo events for live trades & events( as Partial ET) |
|  | FEATURE 6968840 | Business Feature - Hedge acc - SCF split between accruals and PV MTM | 1. New SCF Usage (Trade_Purpose) = ‘Accrued_Interest’. |  | 1. New Cashflow Suppression rule with new SCF Usage? |
|  | FEATURE 7501397 | Business Feature - Redesign of Trade states on Trade State Model - Ensure we have complete E2E Workflow (with all required Controls) | 1. Trade lifecycle status redesign for MO validation |  | RATAN BRP Feature 7595894 |
|  | FEATURE 7703895 | Business Feature - FMRP should move all trades which do not require confirmation to NONCONFIRMED status | NA |  | 1. Historical data cleaning up |
|  | [FEATURE 7739211](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/7739211) | Business Feature - Ability to execute tests on production standard FMRP platform |  |  |  |
|  | FEATURE 7837120 | Business Feature - Hedge acc - Termination and partial termination cashflow payment type on flow products | Settlement Placeholder of Q2 BRP for analysis & UAT support? |  | 1. Payment type changes from fee to coupon for accrued interest |
|  | [FEATURE 7836247](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/7836247) | Business Feature - CCP stamping for FX | Settlement Placeholder of Q2 BRP for analysis & UAT support? |  | 1. CCP Settlement Method Stamping? |
|  | [FEATURE 6932617](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/6932617) | Business Feature - Bring BTB2/3/5/7 inline with new solution of BTB4/6 |  |  | 1. BTB4/6 booking |
| FMRP - Global Rates - HK&TW - Business Feature List | FEATURE 7547973 | Business Feature - HK - Support Cash Settlement on Deliverable Currency | Should be DOD in RATAN HK/TW feature 7759564? **No Dev, Only UAT Support** |  | 1. For HK/TW Spot/FWD USD/CNH 2. Booked as NDF product 3. Only one payment payment in USD, payment amount is the difference of the FX rate |
|  | FEATURE 7708829 | Business Feature - HKTW - Murex Consistency Rules (Pretrade+Posttrade) |  |  | 1. Potentially have rule requirement on Trade Blotter |
|  | [FEATURE 5998685](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/5998685) | Business Feature - Drop1 - HK LTFX | Should be DOD in RATAN HK/TW feature 7759564? **Only UAT required from RATAN for NDF, FX Cash replicated to Razor** |  | 1. LT == Long term FX products 2. No Special behavior on settlement 3. This feature is more for dealhub→tradehub transit |
|  | FEATURE 6159631 | Business Feature - Drop1 - CN BTB | Should be DOD in RATAN HK/TW feature 7759564? 1. **UAT support for BTB4/6** 2. **Potential change on CIBM booking** |  | 1. It's for CN BTB package & HK is Risk/Wash port 2. User Case 1. Generic BTB3/5/7 2. BTB4/6 3. CIBM booking |
|  | [FEATURE 6970185](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/6970185) | Business Feature - Drop1 - Additional Fields | Should be DOD in RATAN HK/TW feature 7759564? 1. **To consume the new trade attributes for cashflow NSTP ** 2. **Dependency with RATAN Uber feature 7797567** |  | 1. Structure id 2. TRAN_CLEAR → Intent to clear: |
|  | FEATURE 7778760 | Business Feature - 12 Countries UAT Support |  |  |  |
|  | FEATURE 6914963 | Business Feature - HKTW - ND-Convert | Should be DOD in RATAN HK/TW feature 7759564? 1. **No Dev, Only UAT Support** |  | 1. Similarly concept with 7547973 to convert the settlement CCY to USD 2. Product scope IRS/CCS 3. CNO as special ND CCY |
|  | [FEATURE 6915683](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/6915683) | Business Feature - HKTW - SID - Structured traders to identify hedges | Should be DOD in RATAN HK/TW feature 7759564? - **To consume the new trade attributes for cashflow NSTP ** - **Dependency with RATAN Uber feature 7797567** |  | 1. Structure id used for settlement NSTP? 2. To consume the new trade attributes for cashflow NSTP 3. Dependency with Uber onboarding |
|  | [FEATURE 6915693](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/6915693) | Business Feature - HK - Support LNBR Floating Rate and ALM Index |  |  | 1. Is this change in Blade & Stella only? |
|  | FEATURE 6915765 | Business Feature - TW - Strategy flag for ESG | NA |  | 1. Is this strategy used for any settlement process - No confirmed by Sumita |
|  | [FEATURE 6980403](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/6980403) | Business Feature - HK - LNBR_Asia | Should be DOD in RATAN HK/TW feature 7759564? |  | 1. Is there settlement requirement? - TBC |
|  | [FEATURE 7778714](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/7778714) | Business Feature - HK - Booking Split | Should be DOD in RATAN HK/TW feature 7759564? 1. **No Dev, Only UAT Support** |  | 1. It's Blade GUI enhancement which user can select multi counterparty & system auto split the trades |
|  | [FEATURE 7778736](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/7778736) | Business Feature - HKTW - Allow ND IRS/CCS settled in non USD currency | Should be DOD in RATAN HK/TW feature 7759564? 1. **No Dev, Only UAT Support** |  | 1. Config the delivery CCY as Non USD 2. Product scope: IRS/CCS |
|  | [FEATURE 7828777](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/7828777) | Business Feature - TRY - Enablement of BLADE booking {IRS/CCS} for MOX Bank Hongkong | Should be DOD in RATAN HK/TW feature 7759564? 1. **New entity onboarding MOX** |  | 1. New entity onboarding MOX( virtual entity) 2. Low priority( drop 2) |
|  | FEATURE 6933465 | Business Feature - TW - Broker & Brokerage (Solutioning Q2) |  |  | 1. Requirement not clear yet |
|  | [FEATURE 7778467](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/7778467) | Business Feature - TW - Unscheduled Holiday Update E2E | Should be DOD in RATAN HK/TW feature 7759564? 1. Most likely it's trade amendment like behaviors on cashflow |  | 1. Used for the unscheduled holiday like typhoon 2. Market event is still under discussion |
|  | [FEATURE 7839003](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/7839003) | Business Feature - HKTW - Trade Migration | Should be DOD in RATAN HK/TW feature 7759564? 1. Trade validation DR/Release( duplicate payment control) |  | 1. Existing live trade volume - 70k |
| FMRP - Global Rates - Core Features - Business Feature List | [FEATURE 6060657](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/6060657) | Business Feature - BTB4 & BTB6 Booking |  |  |  |
|  | FEATURE 5892215 | Business Feature - Global Rates - S2BX & TradeHub Integration (LTFX) | Same with [5998685](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/5998685)(HK/TW GR) |  | 1. New interface with tradehub 2. Product still FX Spot/Forward/Swap/NDF |
|  | FEATURE 6979084 | Business Feature - XVA cash premium adjustment posting process migration | Same with 6159631(HK/TW GR) |  | 1. Is there settlement requirement on XVA? |
|  | FEATURE 5892215 | Business Feature - FRA - Booking Workflow - Trade Booking, Cash and Fixing Notice Generation | 1. New product FRA booking? |  | 1. For global rates UK - in Q3 2. New rates product onboarding |
|  | [FEATURE 5892396](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/5892396) | M027 - Business Feature - Support Allocation Event as part of MW Flow | Same with 7617931( Stella BAU) |  | 1. Scope for both MW and Trianna 2. For all products 3. Separate functions |
|  | FEATURE 6012584 | Business Feature - Structured Trades | Same with [6915683](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/6915683)( HK/TW GR) |  | 1. How is the structure id captured 2. Any special settlement requirement |
|  | FEATURE 6159589 | Business Feature - Allocation is manual now |  |  | 1. not for Q2, in |
|  | FEATURE 6175163 | Business Feature - RTNS Integration (Tradehub) |  |  | 1. Not in Q2 2. Is part of Tradehub integration |
|  | FEATURE 6911951 | Business Feature - TW - Enable REFRESH Event | Should be DOD in RATAN HK/TW feature 7759564? 1. **No Dev, Only UAT Support** |  | 1. New event to build in Q2 2. For HK/TW milestone 3. User case is calendar data update |
|  | FEATURE 6914361 | Business Feature - Long Term Solution for NDF | Separate RATAN feature required for Stella core change? 1. **No Dev, Only UAT Support** |  |  | 1. Is the calendar auto update done as trade amendment? |
|  | FEATURE 7623522 | Business Feature - Early Risk Trade Processing | Separate RATAN feature required for Stella core change? 1. **No Dev, Only UAT Support** |  | 1. MW booking 2. Booked as placeholder trade & cashflow in SUSPENDED 3. Subsequent event |
|  | FEATURE 6992484 | Business Feature - HKTW - Support Novation - REMAINING_PARTY_PART/STEP_IN_FULL | Should be DOD in RATAN HK/TW feature 7759564? 1. **No Dev, Only UAT Support** |  | 1. Remaining party - Any linkage required to original trade? 2. Step in - can be considered as brand new trade? |
|  | FEATURE 7829798 | Business Feature - Support New Trade Events (Novations and Allocation) |  |  | - Step In Partial - Step In Full - Remaining Party Partial - TBA - Allocations |  | 1. Same with 6992484? 2. Is this for which milestone? 3. There's separate ticket to remodel of remaining party full to clearing & new event. |
|  | [FEATURE 6143065](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/6143065) | Business Feature - Support ALM Funding trade booking/pricing for IRS/CCS | Need more clarity |  | 1. For which millstone? 2. Any special requirement with generic IRS & CCS? |
|  | FEATURE 6792929 | Business Feature - TRS - Booking Workflow - Trade Booking, Cash and Fixing Notice Generation |  |  | 1. In Q3 for UK global rates |
|  | FEATURE 6933334 | Business Feature - RATAN - Support for Inter Entity LNBR bookings in Settlements | Need more clarity |  | 1. Is there actual settlement between Shanghai VS HO for LNBR? |
|  | [FEATURE 7548771](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/7548771) | Business Feature Support India BTB Booking Model | 1. BTB4/6 |  | 1. In Q3 for G10 |

## New market events

| Market Event Type | Feature | Milestone | Comment |
|---|---|---|---|
| Clearing | [FEATURE 6525482](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/6525482) |  | 1. New market event dedicate for clearing trade(like trade amendment) 2. No impact to RATAN |
| Remaining Party Full | [FEATURE 6525482](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/6525482) |  | 1. Non Clearing booking counterparty change( like trade amendment) 2. No impact to RATAN |
| Refresh | FEATURE 6911951 |  | 1. Trade event driven by calendar update( like trade amendment) |
| Allocations | FEATURE 7617931 |  | 1. New market event form MW prime booking( MW → VPA → Stella) 2. Block trade would generate cashflow with SUSPENDED status 3. Child trade would generate cashflow with PROJECTED status |
| Remaining Party Partial | FEATURE 6913820 |  | 1. Non Clearing booking counterparty change( like trade amendment) 2. No impact to RATAN |
| UNDO for live trade | FEATURE 6913820 |  |  |
| Step In Partial | FEATURE 7829798 |  | 1. Like new trade booking 2. No impact to RATAN |
| Step In Full | FEATURE 6913820 |  | 1. Like new trade booking 2. No impact to RATAN |

## Key findings

The document defines a candidate migration scope but leaves entity FMIDs, mandatory status, and target release dates blank. It also mixes confirmed requirements, tentative ownership, UAT-only support, future scope, and unresolved questions.

Allocation is the clearest direct settlement dependency. The documented flow is `MW → VPA → Stella`; allocation block-trade cashflows use `SUSPENDED`, child-trade cashflows use `PROJECTED`, and RATAN is expected to filter allocation-event cashflows.

The distinction between Clearing and Remaining Party Full is material for trade lineage: Clearing does not create a new trade ID, while Remaining Party Full creates a new trade ID for the new trade. Although both are labelled as having no RATAN impact, the source does not provide enough interface or reconciliation evidence to confirm that downstream settlement is unaffected.

HK/TW requirements may change settlement currency, payment count, settlement method, and NSTP classification. The source cites approximately 70,000 existing live trades for migration validation and duplicate-payment control.

The feature inventory contains a duplicated identifier: `FEATURE 5892215` is used for both Global Rates S2BX & TradeHub Integration (LTFX) and FRA Booking Workflow. This requires validation against Azure DevOps before the document is used for traceability.

## Related wiki context

This source extends [[projects/murex-cashflow-migration-to-ratan]], [[concepts/murex-ratan-cashflow-integration]], [[concepts/murex-ratan-migration-reconciliation]], [[concepts/cashflow-lifecycle-state-machine]], and [[concepts/nstp-exception-handling]]. It also depends on [[entities/fmrp]], [[entities/ratan]], [[entities/stella]], [[entities/uber]], and [[entities/razor]].

`SUSPENDED` and `PROJECTED` must not be assumed to be equivalent to `PendingAutoNetting`, payment suppression, cashflow suppression, or cashflow failure without an authoritative status mapping.
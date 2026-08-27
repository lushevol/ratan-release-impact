---
type: source
title: Manual Entities Onboarding Checklist
authors: []
year: 2026
url: ""
venue: Internal operational checklist
created: 2026-08-22
updated: 2026-08-22
tags: [settlement-day-2, manual-entities, onboarding, ratan, operations]
related: [manual-entity-settlement-onboarding, entity-routing-and-cashflow-suppression, swift-entity-configuration, ssi-stamping-hierarchy, settlement-day-2, fmrp, nostro-static, business-rule-maintenance]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/00 Manual Entities Onboarding Checklist.md"]
---
# Manual Entities Onboarding Checklist

This source is an operational readiness checklist for enabling Settlement Day 2 processing for new manual entities in the Cash Settlement and RATAN environment. It identifies configuration, static-data, routing, SWIFT, accounting, network, and testing activities.

It is not evidence that the listed work has been completed, approved, or deployed. Several entries are explicitly marked `TBD`, `No?`, “need to confirm,” or “double check.” The table’s ownership and applicability columns are also inconsistently aligned in several rows.

## Operational interpretation

Manual-entity onboarding requires explicit review of:

- LMS feed participation and entity filtering.
- Workflow routing, cashflow suppression, RAZOR routing, and RATAN/SWIFT/accounting handling.
- Entity-level SWIFT BICs, message-field mappings, branch mappings, and any message customization.
- Currency release times and applicable currency configuration.
- Settlement accounting, Nostro and Vostro static data, and branch-specific SSI.
- Business rules, including suppression, NSTP, shared Nostros, counterparty/booking-entity exceptions, and netting statics.
- Firewall access, downstream dependencies, UAT, regression testing, and the undefined `CPT` testing stage.

The source treats the former bypass-validation rule and Murex-only H2 Adaptor batch configuration as retired. It attributes their replacement to the New MO Validation Model and the FMRP process, respectively. These retired steps should not be treated as active onboarding requirements without current-process confirmation.

## Structured checklist data

| # | Description | Details | Type | Done By | Required for Manual Entities? | Comment |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | ~~Bypass Validation Rule~~ | ~~Bypass EG/NP/SAUDI/LOANIQ/CN(FX), rest need validation~~ ~~Post MO Validation moved to FMRP, then not required?~~ | | | ~~Not Applicable~~ | ~~Not required any longer as New MO Validation Model solved the issue. ~~ |
| 2 | LMS Feed Entity List Update | Blacklist includes: EG/NP/SAUDI/KL/TH/TW [LMS Feed - Derivative Strategy Projects - Confluence](https://confluence.global.standardchartered.com/display/DSP/LMS+Feed) | Config | Dev Team (CR) | Yes | 1.Confim with user if need to send to LMS 2.[Story 10917020 LMS - Remove the entity filter in LMS feed](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/10917020) but not delivered |
| 3 | ~~[Murex Cash Migration Only] Entity list for the Batch Solution~~ | ~~H2 Adaptor whitelist includes: Set as default [T-1, T+1] for group calculation, only for Murex~~ | ~~Config~~ | ~~Not Applicable~~ | ~~Old solution, FMRP process ,no need to config any entity for Murex~~ |
| 4 | - BCS vs Strategic Routing - Entity whitelist for in scope entities (covered via Cashflow Suppression rule) - Entity whitelist setup to send to RAZOR or handle in RATAN (RATAN generates SWIFT & Accounting | Workflow whitelist: 1. EG/NP/SAUDI/LOANIQ (legacy flow) 2. Strategic flow (CN/SG/MY/IN/UK/DE) 3. ++CPT list(HK/TW/TH) | Config | Yes | 1.Entity whitelist for in scope entities (covered via Cashflow Suppression rule), add manual entities list in existing NON FMRP cashflow suppress rule. Send to Razor Whitelist `ORIGINAL_SYSTME_TAG:LOANIQ`. Send to Swift Whitelist `STRATEGIC_FM_LIST: 401036553\|400991880\|400910415\|400007847\|400018439\|5\|8\|10036428\|7\|10036382\|400032489\|400045551\|300089409\|6\|2\|10038345\|300011345\|300075472\|10075222\|400041070\|400906330\|300036368\|3\|400452428\|400451508\|9\|400093619\|4\|400960089\|400001378\|400054741\|400220273\|400899993\|400075752\|400095464\|400209000\|400677737\|400229749\|400054708\|400130178\|400085753\|400683682\|400218197\|400667486\|400090093\|400130180\|10020899\|400057714\|10036642\|400054737\|400798477\|10032025\|235003861\|400516443\|400185419\|400193370\|10062461\|10078716\|400516442\|401053411`. CPT `CPT_ENTITY_LIST:` |
| 5 | SWIFT Generation Changes - Booking Entity FMID (mandatory for each entity) - Booking Entity SWIFT BIC (Sender BIC in SWIFT) (mandatory for each entity) - Field 53 SWIFT BIC (for LCY & Over Account) (mandatory for each entity) - Field 58 SWIFT BIC (for Flip MT202) (mandatory for each entity) - Receiver BIC (MT604/605) - Branch code mapping (mandatory for each entity) - Any other branch specific requirement on SWIFT | Need to be added for new entity | Config | Yes | 1.Is there any swift customization? 2.Receiver BIC(MT604/MT605),need to confirm with user is there any manual entities need to generate MT604/MT605 with customized Receiver BIC? 3.Get from user on Sender BIC,53 Swift Bic and CCY/58 Swift Bic/Branch Code |
| 6 | Currency Release Time | Need to be added for new entity | Config | Yes | 1.Get from user for each entity |
| 7 | NDS Auto Netting | Blacklist: TBD | Config | No? | Pending NDS Netting: `Instrument_Common__Murex_Product_Typology in ("NDS", "NDCF", "NDFRA", "ND CDS Fixing", "ND CDS", "ND-Convert", "NDS Fixing") && Cashflow__ND_Parent_Typology != "NDIRS" && Cashflow__Cashflow_Event_Reason not in ("Reversal", "Rebook") && (Cashflow__Netting_Id == null \|\| Cashflow__Netting_Id == "") && ((Cashflow__Duplicate_NDS_FXD == null \|\| Cashflow__Duplicate_NDS_FXD == ""))` I saw there is no entity list setup in the rule condition, so we don't need to consider this item? |
| 8 | Pending Fixing STP/NSTP Control( in case new product have fixing events) | Blacklist: TBD | Config | No? | `Cashflow__Pending_Fixing_Flag == "X" && ((Instrument_Common__Murex_Product_Family == "IRD" && Instrument_Common__Murex_Product_Group in ("IRS", "CS", "LN_BR", "CF")) \|\| (Instrument_Common__Murex_Product_Family == "COM" && Instrument_Common__Murex_Product_Group in ("SWAP", "ASIAN", "FWD")) \|\| (Instrument_Common__Murex_Product_Family == "CRD" && Instrument_Common__Murex_Product_Group == "RTRS"))` |
| 9 | SSI Stamping Hierarchy - Follow UK model (give priority to "Country Specific + Global Product" SSI over Global Entity + Product Specific SSI) | Whitelist: CN/MY/IN/SG/LOANID old logic Rest: new logic | Config | No? | 1.Check old and new model(UK model)logic 2.Manual entities should use new model? |
| 10 | Currency Configuration (if applicable) - Non-ISO to ISO Code mapping - Precious Currency Mapping | NA | Config | No? | If new PM currency added, the PM List replicated from Murex 2.11 identifies PM currency and drives MT604/MT605/MT692 template generation. Need to confirm with PO & users if there's new PM entity to be added for new onboarding entity; CR is required to release to production. Other UDF tables copied from Murex 2.11: `UDF_Strategy`; `UDF_SWF_LS`. |
| 11 | Settlement Accounting - Bridge Account # (mandatory for each entity) - EBBS Branch code & EBBS Transaction type (mandatory for each entity) - Any other branch specific requirement (example: Settlement Accounting is suppressed for Precious Metal CCY's in UK) | | Config | Yes | 1.Bridge Account information, Ebbs Nosro Account 2.Get from user about Transaction type?posting branch,txn dr code,txn cr code |
| 12 | Include new branch in GUI Drop down - Cashflow Blotter (mandatory for each entity) - Dashboard | | Config | No? | Tranche3 is already done-double check |
| 13 | Vostro SI Input Screen - Include New Settlement Means -NOX | | Config | No? | 1.If new settlement means added? |
| 14 | Rounding - applicable for special currency/requirement only | | Config | | No? | 1.New currency added ?if new ccy added, need to add rounding logic for the ccy |
| 15 | Nostro Static Setup (mandatory for each entity) | | Static | If volume high will be done by Dev Team (CR). Else Data Ops | | 1.Get from user for each entity |
| 16 | Vostro Static Setup (Vostro to drive Nostro assignment) - Over-Account Clients to be created as Branch specific SSI | | Static | Data Ops | No, data ops to setup | NA |
| 17 | Business Rules Setup - Cashflow Suppression - White List for in scope entities - Swift Suppression - Auto Debit by Agent - Nostros shared with other entity (example: China) - NSTP - Add new entity to Rules where SCB Entities as Counterparty is bypassed - Add new entity to Rules where SCB entities are added as Booking Entity - Netting Static - BIC Netting Static | | Static | Data Ops | | 1.Get from user for each entity |
| 18 | Open Firewall for users in new location | | Config | Dev Team | | [RATAN network segmentation - Derivative Strategy Projects - Confluence](https://confluence.global.standardchartered.com/display/DSP/RATAN+network+segmentation) |
| 19 | Downstream Engagement to determine additional requirements if any | | Analysis | Dev Team | No | |
| 20 | UAT | | Testing | Settlement Ops | No | |
| 21 | Regression Testing | | Testing | Dev Team | No | |
| 22 | CPT | | Testing | | | CPT ：control production testing？ |

## Open implementation issues

The checklist does not establish the following as settled policy:

- Whether NDS Auto Netting requires entity-specific configuration.
- Whether manual entities must use the UK SSI-stamping hierarchy.
- Whether LMS entity filtering remains active while Story 10917020 is undelivered.
- What `CPT` means and what its entry and exit criteria are.
- Whether `LOANIQ` and `LOANID` are distinct identifiers.
- Which SWIFT fields and accounting settings are conditionally required by message type, currency, or branch.

See [[manual-entity-settlement-onboarding]], [[entity-routing-and-cashflow-suppression]], [[swift-entity-configuration]], and [[ssi-stamping-hierarchy]].
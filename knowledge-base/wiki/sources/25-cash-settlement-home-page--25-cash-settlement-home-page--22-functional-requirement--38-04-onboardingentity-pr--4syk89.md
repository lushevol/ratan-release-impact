---
type: source
title: New Entity Onboarding Checking List
authors: []
year: 2024
url: ""
venue: Internal functional requirement
created: 2026-08-22
updated: 2026-08-22
tags: [ratan, cash-settlement, onboarding, configuration, static-data]
related: [ratan, murex, fmrp, lms, ebbs, configuration-driven-onboarding, entity-branch-onboarding, what-are-the-nds-auto-netting-and-pending-fixing-blacklists, has-loanid-been-used-intentionally-in-the-ssi-hierarchy, what-replaced-the-bypass-validation-rule]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/New Entity onboarding checking list.md"]
---
# New Entity Onboarding Checking List

This functional requirement defines a reusable control checklist for onboarding a new booking entity or product to [[ratan]]. It presents RATAN as a global settlement-platform model intended to support onboarding primarily through configuration, static data, business rules, and controlled releases.

The checklist does not establish that onboarding is self-service or risk-free. Dev Team deployment, firewall changes, regression testing, operational data approval, and downstream impact assessment remain required activities.

## Onboarding Change Checklist

| # | Description | Details | Type | Done By |
| ---: | --- | --- | --- | --- |
| 1 | ~~Bypass Validation Rule~~ Not required any longer as New MO Validation Model solved the issue. | ~~Bypass LOANIQ/FX, rest need validation~~ ~~Post MO Validation moved to FMRP, then not required?~~ |  |  |
| 2 | LMS Feed Entity List Update | Blacklist includes: EG/NP/SAUDI/KL/TH/TW | Config | Dev Team (CR) |
| 3 | [Murex Cash Migration Only] Entity list for the Batch Solution | H2 Adaptor whitelist includes: UK, DE (Set as default) H1 Adaptor whitelist includes: CN/SG/MY/IN | Config |  |
| 4 | BCS vs Strategic Routing; Entity whitelist for in scope entities; Entity whitelist setup to send to RAZOR or handle in RATAN (RATAN generates SWIFT & Accounting) | Workflow whitelist: 1. LOANIQ (legacy flow) 2. Strategic flow (CN/SG/MY/IN/UK/DE/EG/NP/SAUDI) | Config |  |
| 5 | SWIFT Generation Changes | Booking Entity FMID; Booking Entity SWIFT BIC; Field 53 SWIFT BIC; Field 58 SWIFT BIC; receiver BIC for MT604/605; branch-code mapping; other branch-specific SWIFT requirements. | Config |  |
| 6 | Currency Release Time | Mandatory for each entity. | Config |  |
| 7 | NDS Auto Netting | Blacklist: TBD | Config |  |
| 8 | Pending Fixing STP/NSTP Control | Applicable when a new product has fixing events. Blacklist: TBD. | Config |  |
| 9 | SSI Stamping Hierarchy | Follow UK model: prioritize “Country Specific + Global Product” SSI over “Global Entity + Product Specific” SSI. Whitelist: CN/MY/IN/SG/LOANID old logic; rest new logic. | Config |  |
| 10 | Currency Configuration | Non-ISO-to-ISO mapping; precious-currency mapping if applicable. | Config |  |
| 11 | Settlement Accounting | Bridge account; EBBS branch code and transaction type; other branch-specific requirements. | Config |  |
| 12 | GUI dropdown additions | Cashflow Blotter and Dashboard; mandatory for each entity. | Config |  |
| 13 | Vostro SI input screen | Include new settlement means. | Config |  |
| 14 | Rounding | Applicable only to special currency/requirement. | Config |  |
| 15 | Nostro Static Setup | Mandatory for each entity. | Static | Dev Team via CR if high volume; otherwise Data Ops |
| 16 | Vostro Static Setup | Vostro drives Nostro assignment; over-account clients must be branch-specific SSI. | Static | Data Ops |
| 17 | Business Rules Setup | Cashflow/SWIFT suppression, auto debit by agent, shared Nostros, NSTP, counterparty/booking-entity rules, netting static, BIC netting static. | Static | Data Ops |
| 18 | Firewall access | Open firewall for users in new location. | Config | Dev Team |
| 19 | Downstream engagement | Determine additional requirements. | Analysis | Dev Team |
| 20 | UAT |  | Testing | Settlement Ops |
| 21 | Regression Testing |  | Testing | Dev Team |
| 22 | CPT |  | Testing | MO/Settlement Ops |

## Murex Special Functions

The following behavior is specifically attributed to the [[murex]]–RATAN integration.

| # | Function Summary | Function Introduction | Confluence |
| ---: | --- | --- | --- |
| 1 | Batch File | For value date today, tomorrow and day after, Murex sends real-time messages; other value dates are in a batch file. |  |
| 2 | Pending Fixing | For COM ASIAN/FW/SWP IRD/CF/CS/FRA/IRS products, Murex provides a pending-fixing flag indicating whether RATAN should place a cashflow in `WAITING + Pending Another Leg`. | https://confluence.global.standardchartered.com/pages/viewpage.action?pageId=2726685251 |
| 3 | NDS Auto Netting | For ND products, Murex generates a child FXD trade to convert ND currency to delivery currency. RATAN auto-nets the delivery-currency cashflow in the parent trade with the delivery-currency cashflow in the child trade. | https://confluence.global.standardchartered.com/display/DSP/NDS+Auto+Netting |
| 4 | SWAP AGENT | RATAN marks payment type for RFR and Swap Agent based on a Murex identifier, for auto-netting and SWIFT-suppression handling. | https://confluence.global.standardchartered.com/display/DSP/RFR+and+Swap+Agent |
| 5 | Special Flag | COM or Non COM; Pending Clearing; Linked trade Id |  |

## LMS Feed Configuration

Settlement Team and [[lms]] must confirm whether each new entity needs to feed LMS.

| Entity | Entity FM Code | Entity FMID | Feeding to LMS |
| --- | ---: | --- | --- |
| SCB EGYPT*CAI | 401036553 |  | No |
| SCB SAUDI*RYD | 400991880 |  | No |
| NEPAL GRINDLAYS*KTM | 400007847 |  | No |
| SCB KL*KUL? | 9 |  | No |
| STANCHART SAADIQ*KUL | 400093619 |  | No |
| TAIPEI |  |  | No |
| OBU TAIPEI |  |  | No |
| BANGKOK |  |  | No |
| Other | Other |  | Yes |

The source table does not establish whether the listed numeric values are FM Codes or FMIDs.

## Source-System and Tag 20 Agreement

LMS must agree the source system and Tag 20 logic for each new entity.

| Booking System | Source System | Flow | Prefix of Field 20 | Comment |
| --- | --- | --- | --- | --- |
| SABRE EQ | STELLA | `SABRE EQ -> BCS STELLA -> STELLA -> TDS3 -> RATAN` | `EQ` | BAU stack, not strategic stack; informational only. |
| LOANIQ | LOANIQ | `LOANIQ -> STELLA -> TDS3 -> RATAN ONE` | `LQ` |  |
| BLADE/S2BX/CFETS | FMRP | `BLADE/S2BX/CFETS -> STELLA -> TDS3 -> RATAN` | `DV` |  |

## GUI SWIFT Query Sources and Tag 20 Logic

| Function Flow | Entities | SWIFT Message Source | Query Condition | Tag 20 Logic | Comment |
| --- | --- | --- | --- | --- | --- |
| BCS Stella | SG/UK/Jersey/HK | FMSRE | Tag 20 | `EQ + Branch Code + Cashflow ID` | BCS stack only, not strategic stack; informational only. |
| Egypt/Nepal/Saudi | Egypt/Nepal/Saudi | FMSRE | Tag 20 | `FX + Branch Code + Cashflow ID` |  |
| LOANIQ | LOANIQ entities | BLADE/S2BX/CFETS | Tag 20 | `LQ + Branch Code + Cashflow ID` |  |
| FMRP | SG/MY/IN/CN | RATAN | cashflow ID |  |  |

The LOANIQ query row names BLADE/S2BX/CFETS as its SWIFT message source, while the preceding flow table identifies LOANIQ as its source system. This remains unverified.

## Operating Model

Nostro data and business rules have two delivery paths:

- High-volume project onboarding uses reviewed operational data, Dev Team scripts, and a Change Request (CR) release.
- Low-volume BAU maintenance is performed through the RATAN GUI under maker/checker control.

Nostro data is defined at legal-entity-plus-currency granularity. Release cutoffs are also defined at legal-entity-plus-currency granularity and require reviewed and approved Operations input before Dev Team CR deployment.

Accounting configuration requires bridge-account information from [[ebbs]], EBBS branch codes, EBBS transaction types, and applicable booking-currency-to-ISO mappings. Downstream assessment includes RATAN EOD, SSDR, CIS, and [[fmmis]].

## Related Pages

- [[configuration-driven-onboarding]]
- [[entity-branch-onboarding]]
- [[nostro-static-management]]
- [[release-cutoff-configuration]]
- [[tag-20-logic]]
- [[settlement-accounting]]
- [[pending-fixing-stp-nstp-control]]
- [[maker-checker-segregation]]
- [[what-are-the-nds-auto-netting-and-pending-fixing-blacklists]]
- [[has-loanid-been-used-intentionally-in-the-ssi-hierarchy]]
- [[what-replaced-the-bypass-validation-rule]]
---
type: source
title: 2026 Indonesia Entity Onboarding Checklist
authors: []
year: 2026
url: ""
venue: ""
created: 2026-08-22
updated: 2026-08-22
tags: [Indonesia, Jakarta, entity-onboarding, cash-settlement, auto-netting, functional-requirement]
related: [entity-branch-onboarding, cash-settlement, auto-netting, cashflow-suppression, ssi-selection-hierarchy, swift-mt-mx-integration, settlement-accounting, nostro-configuration, nostrо-vostro-settlement-controls, murex, lms, ratan, razor, nds-auto-netting, cashflow-blotter, dev-team]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/New Entity onboarding checking list/2026 Indonesia Instance.md"]
---

# 2026 Indonesia Entity Onboarding Checklist

## Summary

This functional-requirement checklist defines the configuration, static-data, downstream-analysis, access, and testing activities required to onboard a new Indonesia/Jakarta entity instance into the cash-settlement and auto-netting platform.

The checklist demonstrates that entity onboarding is a cross-system readiness exercise rather than a single master-data change. Dependencies include validation and feed filtering, Murex cash migration, routing and cashflow suppression, SWIFT generation, currency release timing, netting controls, SSI selection, settlement accounting, user interfaces, Nostro/Vostro static data, business rules, firewall access, downstream analysis, UAT, and regression testing.

Indonesia-specific values remain undefined for several mandatory fields, including FMID, SWIFT BICs, branch mappings, bridge account, EBBS branch code, and transaction type. The document also leaves routing, blacklist, post-MO validation, and Tranche 2 scope questions unresolved.

## Referenced delivery items

- [Story 8419029 [Tranche2] LMS filter](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/8419029)
- [Story 8390122 [Tranche2] MX SWIFT Message for MU](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/8390122)
- [Story 8267534 Tranche 2 Entities - SWIFT message update](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/8267534)
- [Story 8118402 [Tranche2 Accounting] Transaction type set up as RTO for PH](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/8118402)
- [2025 Tranche 2 Go Live Readiness (Mauritius, Dubai, DIFC, Jakarta, Manila, Philippines FCU, Tokyo, Johanesburg) - Derivative Strategy Projects - Confluence](https://confluence.global.standardchartered.com/pages/viewpage.action?pageId=3244588508)

## Original checklist

```markdown
| # | Description | Details | Type | Done By | Required for Tranche2? |
| --- | --- | --- | --- | --- | --- |
| 1 | Bypass Validation Rule | Bypass EG/NP/SAUDI/LOANIQ/CN(FX), rest need validation Post MO Validation moved to FMRP, then not required? | | | No |
| 2 | LMS Feed Entity List Update [Story 8419029 [Tranche2] LMS filter](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/8419029) | Blacklist includes: EG/NP/SAUDI/KL/TH/TW | Config | Dev Team (CR) | |
| 3 | [Murex Cash Migration Only] Entity list for the Batch Solution | H2 Adaptor whitelist includes: Set as default [T-1, T+1] for group calculation, only for Murex | Config | No |
| 4 | - BCS vs Strategic Routing - Entity whitelist for in scope entities (covered via Cashflow Suppression rule) - Entity whitelist setup to send to RAZOR or handle in RATAN (RATAN generates SWIFT & Accounting | Workflow whitelist: 1. EG/NP/SAUDI/LOANIQ (legacy flow) 2. Strategic flow (CN/SG/MY/IN/UK/DE) 3. ++CPT list(HK/TW/TH) | Config | |
| 5 | SWIFT Generation Changes - Booking Entity FMID (mandatory for each entity) - Booking Entity SWIFT BIC (Sender BIC in SWIFT) (mandatory for each entity) - Field 53 SWIFT BIC (for LCY & Over Account) (mandatory for each entity) - Field 58 SWIFT BIC (for Flip MT202) (mandatory for each entity) - Receiver BIC (MT604/605) - Branch code mapping (mandatory for each entity) - Any other branch specific requirement on SWIFT - [Story 8390122 [Tranche2] MX SWIFT Message for MU](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/8390122) - [Story 8267534 Tranche 2 Entities - SWIFT message update](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/8267534) | Need to be added for new entity [2025 Tranche 2 Go Live Readiness (Mauritius, Dubai, DIFC, Jakarta, Manila, Philippines FCU, Tokyo, Johanesburg) - Derivative Strategy Projects - Confluence](https://confluence.global.standardchartered.com/pages/viewpage.action?pageId=3244588508) | Config | |
| 6 | Currency Release Time | Need to be added for new entity | Config | |
| 7 | NDS Auto Netting | Blacklist: TBD | Config | No |
| 8 | Pending Fixing STP/NSTP Control( in case new product have fixing events) | Blacklist: TBD | Config | No |
| 9 | SSI Stamping Hierarchy - Follow UK model (give priority to "Country Specific + Global Product" SSI over Global Entity + Product Specific SSI) | Whitelist: CN/MY/IN/SG/LOANID old logic Rest: new logic | Config | No |
| 10 | Currency Configuration (if applicable) - Non-ISO to ISO Code mapping - Precious Currency Mapping | NA | Config | No |
| 11 | Settlement Accounting - Bridge Account # (mandatory for each entity) - EBBS Branch code & EBBS Transaction type (mandatory for each entity) - Any other branch specific requirement (example: Settlement Accounting is suppressed for Precious Metal CCY's in UK) [Story 8118402 [Tranche2 Accounting] Transaction type set up as RTO for PH](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/8118402) | [2025 Tranche 2 Go Live Readiness (Mauritius, Dubai, DIFC, Jakarta, Manila, Philippines FCU, Tokyo, Johanesburg) - Derivative Strategy Projects - Confluence](https://confluence.global.standardchartered.com/pages/viewpage.action?pageId=3244588508) | Config | |
| 12 | Include new branch in GUI Drop down - Cashflow Blotter (mandatory for each entity) - Dashboard | [2025 Tranche 2 Go Live Readiness (Mauritius, Dubai, DIFC, Jakarta, Manila, Philippines FCU, Tokyo, Johanesburg) - Derivative Strategy Projects - Confluence](https://confluence.global.standardchartered.com/pages/viewpage.action?pageId=3244588508) | Config | |
| 13 | Vostro SI Input Screen - Include New Settlement Means -NOX | | Config | No |
| 14 | Rounding - applicable for special currency/requirement only | | Config | | No |
| 15 | Nostro Static Setup (mandatory for each entity) | | Static | If volume high will be done by Dev Team (CR). Else Data Ops | |
| 16 | Vostro Static Setup (Vostro to drive Nostro assignment) - Over-Account Clients to be created as Branch specific SSI | | Static | Data Ops | No, data ops to setup |
| 17 | Business Rules Setup - Cashflow Suppression - White List for in scope entities - Swift Suppression - Auto Debit by Agent - Nostros shared with other entity (example: China) - NSTP - Add new entity to Rules where SCB Entities as Counterparty is bypassed - Add new entity to Rules where SCB entities are added as Booking Entity - Netting Static - BIC Netting Static | [2025 Tranche 2 Go Live Readiness (Mauritius, Dubai, DIFC, Jakarta, Manila, Philippines FCU, Tokyo, Johanesburg) - Derivative Strategy Projects - Confluence](https://confluence.global.standardchartered.com/pages/viewpage.action?pageId=3244588508) | Static | Data Ops | |
| 18 | Open Firewall for users in new location | | Config | Dev Team | Done |
| 19 | Downstream Engagement to determine additional requirements if any | | Analysis | Dev Team | No |
| 20 | UAT | | Testing | Settlement Ops | No |
| 21 | Regression Testing | | Testing | Dev Team | No |
```

## Key implementation boundaries

The entity lists in the checklist are control-specific and must not be treated as interchangeable:

- The LMS blacklist is `EG/NP/SAUDI/KL/TH/TW`.
- The H2 Adaptor whitelist applies only to Murex cash migration batch processing.
- The routing whitelist separates legacy flow (`EG/NP/SAUDI/LOANIQ`), Strategic flow (`CN/SG/MY/IN/UK/DE`), and the CPT list (`HK/TW/TH`).
- The SSI old-logic whitelist is `CN/MY/IN/SG/LOANID`; other entities use the new logic.
- NDS Auto Netting and Pending Fixing STP/NSTP blacklists are both `TBD` and require separate decisions.

## Readiness gaps

The source does not confirm the final Indonesia/Jakarta entity identifier, branch identifier, routing destination, or entity-specific configuration values. It also does not establish whether blank Tranche 2 fields mean out of scope, not assessed, or awaiting completion. The `No` values for UAT and regression testing may describe Tranche 2 scope rather than a waiver of go-live testing.

This source should be read with [[entity-branch-onboarding]], [[cashflow-suppression]], [[ssi-selection-hierarchy]], [[swift-mt-mx-integration]], [[settlement-accounting]], [[nostro-configuration]], and [[nostro-vostro-settlement-controls]].

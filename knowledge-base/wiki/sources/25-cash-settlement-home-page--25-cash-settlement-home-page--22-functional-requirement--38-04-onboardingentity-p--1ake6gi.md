---
type: source
title: 2026 Entity Onboarding — New Branch Setup in Vietnam
authors: []
year: 2026
url: ""
venue: ""
created: 2026-08-22
updated: 2026-08-22
tags: [vietnam, entity-onboarding, cash-settlement, fmrp, planning]
related: [vietnam-ifc-branch, scb-singapore, scb-vietnam, fmrp, ratan, ebbs, lms, entity-branch-onboarding, nostro-static-management, release-cutoff-configuration, tag-20-logic]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/2026 Entity Onboarding - new branch setup in Vietnam.md"]
---
# 2026 Entity Onboarding — New Branch Setup in Vietnam

## Summary

This draft planning document estimates the work required to onboard a proposed branch in Vietnam’s International Financial Centre. The proposed [[vietnam-ifc-branch]] would not be part of [[scb-vietnam]]; it would be configured as a new branch of [[scb-singapore]] with a new FMID or entity identity.

The assumed scope is limited to the [[fmrp]] flow, standard onboarding without customized business features, and strategic trade [[ssi-stamping]]. The checklist nevertheless identifies accounting-service development, including a new [[solace]] topic or queue and adaptation for [[ebbs]] accounting.

The estimate assigns 34 person-days to Settlement and 10 person-days to Trade Control. C&A has no estimated effort. These are ballpark estimates rather than approved delivery commitments.

## Scope Assumptions

1. A new FMID or entity for Vietnam under SCB Singapore.
2. FMRP flow only.
3. Onboarding only, with no customized features.
4. Strategic trade SI stamping.

The branch model remains a proposal. The document does not provide the formal legal, architecture, or governance approval required to treat it as final.

## Effort Estimate

| Phase | Effort |
| --- | --- |
| Support EBBS accounting for new branch | 15 |
| Static setup (Swift, Accounting, Cutoff, Nostro, ISO Currency, Rules, Workflow) | 6 |
| SIT/Regression | 2 |
| UAT Support | 6 |
| Release | 5 |

- **Settlement:** 34 MD
- **Trade Control:** 10 MD
- **C&A:** No MD

The Settlement line items total 34 MD. Settlement and Trade Control together imply 44 MD, although the source does not explicitly present that combined figure.

## Onboarding Checklist

| # | Description | Details | Type | Required? | Done By |
| --- | --- | --- | --- | --- | --- |
| 1 | ~~Bypass Validation Rule ~~Not required any longer as New MO Validation Model solved the issue. | ~~Bypass LOANIQ/FX, rest need validation~~ ~~Post MO Validation moved to FMRP, then not required?~~ | | | |
| 2 | LMS Feed Entity List Update | Blacklist includes: EG/NP/SAUDI/KL/TH/TW | Config | No | Dev Team (CR) |
| 3 | [Murex Cash Migration Only] Entity list for the Batch Solution | H2 Adaptor whitelist includes: UK, DE (Set as default) H1 Adaptor whitelist includes: CN/SG/MY/IN | Config | |
| 4 | - BCS vs Strategic Routing - Entity whitelist for in scope entities (covered via Cashflow Suppression rule) - Entity whitelist setup to send to RAZOR or handle in RATAN (RATAN generates SWIFT & Accounting | Workflow whitelist: 1. LOANIQ (legacy flow) 2. Strategic flow (New Entity/SG/MY/IN/UK/DE/EG/NP/SAUDI) | Config | Yes |
| 5 | SWIFT Generation Changes - Booking Entity FMID(mandatory for each entity) - Booking Entity SWIFT BIC (Sender BIC in SWIFT) (mandatory for each entity) - Field 53 SWIFT BIC (for LCY & Over Account) (mandatory for each entity) - Field 58 SWIFT BIC (for Flip MT202) - Receiver BIC (MT604/605) - Branch code mapping (mandatory for each entity) - Any other branch specific requirement on SWIFT | Need to be added for new entity | Config | Yes |
| 6 | Currency Release Time (mandatory for each entity) | Need to be added for new entity | Config | Yes |
| 7 | NDS Auto Netting | Blacklist: TBD | Config | No for FMRP |
| 8 | Pending Fixing STP/NSTP Control( in case new product have fixing events) | Blacklist: TBD | Config | No |
| 9 | SSI Stamping Hierarchy - Follow UK model (give priority to "Country Specific + Global Product" SSI over Global Entity + Product Specific SSI) | All New logic | Config | No |
| 10 | Currency Configuration (if applicable) - Non-ISO to ISO Code mapping - Precious Currency Mapping | | Config | No |
| 11 | Settlement Accounting - Bridge Account # (mandatory for each entity) - EBBS Branch code & EBBS Transaction type (mandatory for each entity) - Any other branch specific requirement (example: Settlement Accounting is suppressed for Precious Metal CCY's in UK) | Need to be added for new entity New Solace topic/queue Accounting service adapt to new entity | Config/Dev | Yes |
| 12 | Include new branch in GUI Drop down - Cashflow Blotter (mandatory for each entity) - Dashboard (mandatory for each entity) | Need to be added for new entity | Config | Yes |
| 13 | Vostro SI Input Screen - Include New Settlement Means | | Config | No |
| 14 | Rounding - applicable for special currency/requirement only | | Config | No | |
| 15 | Nostro Static Setup (mandatory for each entity) | | Static | Yes | If volume high will be done by Dev Team (CR). Else Data Ops |
| 16 | Vostro Static Setup (Vostro to drive Nostro assignment) - Over-Account Clients to be created as Branch specific SSI | | Static | No | Data Ops |
| 17 | Business Rules Setup - Cashflow Suppression - White List for in scope entities - Swift Suppression - Auto Debit by Agent - Nostros shared with other entity (example: China) - NSTP - Add new entity to Rules where SCB Entities as Counterparty is bypassed - Add new entity to Rules where SCB entities are added as Booking Entity - Netting Static - BIC Netting Static | | Static | Yes | Data Ops |
| 18 | Open Firewall for users in new location | | Config | Yes | Dev Team |
| 19 | Downstream Engagement to determine additional requirements if any | | Analysis | No | Dev Team |
| 20 | UAT support | | Testing | Yes | Settlement Ops |
| 21 | Regression Testing / SIT | | Testing | Yes | Dev Team |
| 22 | CPT | | Testing | Yes | MO/Settlement Ops |
| 23 | Data Entitlement | | | | |
| 24 | Release Preparation on script, configuration chagne | | | Yes | |

## Murex Special Function Checklist

| | Function Summary | Function Introduction | Confluence |
| --- | --- | --- | --- |
| 1 | Batch File | For value date today, tomorrow and day after, Murex will send real time message, others will be in batch file. | |
| 2 | Pending Fixing | As there is pre-netting function in Murex, for COM ASIAN/FW/SWP IRD/CF/CS/FRA/IRS products, cashflow can be auto netted together. So when 1 cashflow comes, Murex will have a field pending fixing flag to mark whether the cashflow should be in WAITING + Pending Another Leg in Ratan | [IRS Fix Leg & Floating leg payment handling - Derivative Strategy Projects - Confluence](https://confluence.global.standardchartered.com/pages/viewpage.action?pageId=2726685251) |
| 3 | NDS Auto Netting | For ND products in Murex, it will generate child FXD trade to convert ND ccy to delivery ccy. So in Ratan side, it would auto net delivery ccy cashflow in parent trade with delivery ccy cashflow in child trade. | [NDS Auto Netting - Derivative Strategy Projects - Confluence](https://confluence.global.standardchartered.com/display/DSP/NDS+Auto+Netting) |
| 4 | SWAP AGENT | Ratan will mark payment type for RFR and Swap Agent based on identifier from Murex, for auto netting/SWIFT suppression handling in Ratan | [RFR and Swap Agent - Derivative Strategy Projects - Confluence](https://confluence.global.standardchartered.com/display/DSP/RFR+and+Swap+Agent) |
| 5 | Special Flag | - COM or Non COM - Pending Clearing - Linked trade Id | |

These functions are reference material rather than a complete statement of Vietnam requirements. NDS Auto Netting is explicitly not required for the FMRP-only scope, and Pending Fixing is also marked as not required.

## LMS Feeding Entity Configuration

| Entity FM Code | Entity FMID | Feeding to LMS |
| --- | --- | --- |
| SCB EGYPT*CAI | 401036553 | No |
| SCB SAUDI*RYD | 400991880 | No |
| NEPAL GRINDLAYS*KTM | 400007847 | No |
| SCB KL*KUL? | 9 | No |
| STANCHART SAADIQ*KUL | 400093619 | No |
| TAIPEI | | No |
| OBU TAIPEI | | No |
| BANGKOK | | No |
| Other | Other | Yes |

Settlement Team and [[lms]] must confirm whether the proposed branch should feed LMS. Values such as `SCB KL*KUL?`, FMID `9`, and the blank FMIDs appear provisional and should not be normalized without validation.

## Source System and Tag 20 Agreement

| Booking System | Source System | Flow | Prefix of field 20 | Comment |
| --- | --- | --- | --- | --- |
| SABRE EQ | STELLA | SABRE EQ -> BCS STELLA -> STELLA -> TDS3 -> RATAN | EQ | This is in the BAU stack not in the Strategy stack, just for information here. |
| LOANIQ | LOANIQ | LOANIQ -> STELLA -> TDS3 -> RATAN ONE | LQ | |
| BLADE/S2BX/CFETS | FMRP | BLADE/S2BX/CFETS -> STELLA -> TDS3 -> RATAN | DV | |

The new branch’s source-system designation and [[tag-20-logic]] require agreement with LMS. The in-scope strategic path is represented as [[blade]], S2BX, or [[cfets]] through [[stella]] and TDS3 to [[ratan]].

## GUI SWIFT Query Configuration

| **Function Flow** | **Entities** | **Swift Message Source** | **Query Condition** | **Tag 20 logic** | **Comment** |
| --- | --- | --- | --- | --- | --- |
| BCS Stella | SG/UK/Jersey/HK | FMSRE | Tag 20 | EQ + Branch Code + Cashflow ID | This is in the BCS Stack only not in the Strategy stack, put here for information only. |
| Egypt/Nepal/Saudi | Egypt/Nepal/Saudi | FMSRE | Tag 20 | FX + Branch Code + Cashflow ID | |
| LOANIQ | LOANIQ entities | BLADE/S2BX/CFETS | Tag 20 | LQ+ Branch Code + Cashflow ID | |
| FMRP | SG/MY/IN/CN | RATAN | cashflow ID | | |

The legacy and BAU rows are contextual. They must not be copied to the proposed branch without confirming the FMRP query model and authoritative SWIFT-message source.

## Static Data and Deployment

### Nostro

Nostro data is maintained at legal-entity-and-currency granularity. The source identifies two production patterns:

- Batch initialization by database script for projects with hundreds of rows. Settlement Ops supplies reviewed data in the `WMSUS.xlsx` format, and the technical team deploys it under a Change Request.
- Manual GUI maintenance by the RTS team with maker-checker approval.

See [[nostro-static-management]] and [[maker-checker-segregation]].

### Release Cutoff

Release cutoff data is maintained at legal-entity-and-currency granularity. Operations must supply reviewed and approved values, after which the [[dev-team]] deploys them under a Change Request. See [[release-cutoff-configuration]].

### Business Rules

NSTP, cashflow suppression, SWIFT suppression, and netting rules can be deployed by scripts under a Change Request for high-volume initialization. Alternatively, the Business Rule team can maintain them through the RATAN GUI as a BAU maker-checker process.

### SWIFT Static Data

Required or potentially applicable values include:

- Booking-entity FMID.
- Sender BIC.
- Field 53 BIC for local-currency and over-account cases.
- Field 58 BIC for Flip MT202.
- Receiver BIC for MT604 and MT605.
- Branch-code mapping.
- Booking-currency-to-ISO-code mapping.
- Precious-metal currency configuration.
- `UDF_Strategy` and `UDF_SWF_LS` data copied from [[murex-2-11]].

### Accounting Static Data

Required values include:

- EBBS branch code.
- EBBS transaction code or transaction type.
- Booking-currency-to-ISO-code mapping.
- EBBS bridge-account number.
- Any branch-specific accounting suppression.

The source expects a new Solace topic or queue and adaptation of the accounting service for the new entity.

## User Interfaces and Access

The new branch must be added to query dropdowns in [[cashflow-blotter]] and Dashboard. Firewall access for users in the new location is required. Data entitlement is listed but has no requirement status, owner, or implementation detail.

## Testing and Release

SIT, regression testing, UAT support, CPT, and release preparation are required. The source does not define test cases, environments, entry criteria, exit criteria, sign-off authorities, or a release owner.

## Downstream Dependencies

The source calls for checks with:

- RATAN EOD for report migration.
- SSDR for additional cashflow information.
- CIS for additional cashflow information.
- FMMIS for additional cashflow information.

This creates a planning tension because “Downstream Engagement” is marked as not required in the checklist even though specific downstream confirmations remain open.

## Key Unresolved Inputs

The document does not provide authoritative values or decisions for:

- Legal and architecture approval of the SCB Singapore branch model.
- FMID, FM code, BICs, or branch code.
- Currencies, Nostros, release cutoffs, and bridge accounts.
- LMS participation and Tag 20 behavior.
- SSI selection hierarchy.
- Data entitlement.
- Downstream-system changes.
- Trade Control deliverables behind the 10 MD estimate.
- Testing acceptance and release-readiness criteria.

These uncertainties are tracked in [[is-the-vietnam-ifc-branch-part-of-scb-singapore]], [[should-the-vietnam-ifc-branch-feed-lms]], and [[which-downstream-systems-require-vietnam-branch-changes]].
---
type: source
title: "Korea 2026 New Entity Onboarding Checklist"
authors: []
year: 2026
url: ""
venue: "Cash Settlement Home Page — Functional Requirement"
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, Korea, RATAN, entity-onboarding, functional-requirement]
related: [2026-korea-cash-settlement-onboarding, korea, configuration-driven-onboarding, entity-branch-onboarding, bypass-validation-rule, entity-specific-swift-generation, nostro-static-management, settlement-accounting, release-cutoff-configuration, pending-fixing, nds-auto-netting, tag-20-logic]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement/Korea Migration/New Entity onboarding checking list - Korea 2026.md"]
---
# Korea 2026 New Entity Onboarding Checklist

## Summary

This operational checklist describes the configuration, static-data, downstream-engagement, and testing activities expected when onboarding a new booking entity into the RATAN settlement platform for the Korea-related 2026 cash-settlement migration.

The source presents RATAN as a global settlement model intended to support booking entities and products through configuration and static-data changes rather than bespoke application development. However, many changes still require Dev Team deployment through controlled change requests (CRs). The document is therefore best understood as a configuration-led onboarding checklist, not evidence of completed implementation or go-live.

## Checklist

| # | Description | Details | Type | Done By |
| --- | --- | --- | --- | --- |
| 1 | Bypass Validation Rule | Marked as no longer required because the New MO Validation Model reportedly solved the issue. Historical notes refer to bypassing LOANIQ/FX and moving post-MO validation to FMRP. | Config | To be confirmed |
| 2 | LMS Feed Entity List Update | Blacklist includes EG/NP/SAUDI/KL/TH/TW. The LMS decision for a new entity must be confirmed with Settlement and LMS teams. | Config | Dev Team (CR) |
| 3 | Murex Cash Migration Batch Solution | H2 Adaptor whitelist: UK and DE as the default. H1 Adaptor whitelist: CN/SG/MY/IN. | Config | Dev Team |
| 4 | BCS versus Strategic Routing | Configure the workflow whitelist to send selected entities to RAZOR or process them in RATAN, where RATAN generates SWIFT and accounting. Legacy flow: LOANIQ. Strategic flow: CN/SG/MY/IN/UK/DE/EG/NP/SAUDI. | Config | Dev Team |
| 5 | SWIFT Generation | Add Booking Entity FMID, sender BIC, Field 53 BIC, Field 58 BIC, receiver BIC for MT604/MT605, branch-code mapping, and other branch-specific requirements. | Config | Dev Team (CR) |
| 6 | Currency Release Time | Add the release time at legal-entity-and-currency granularity. | Config | Dev Team (CR) |
| 7 | NDS Auto Netting | Confirm and configure the entity/product blacklist. | Config | To be confirmed |
| 8 | Pending Fixing STP/NSTP Control | If the new product has fixing events, confirm and configure the Pending Fixing blacklist. | Config | To be confirmed |
| 9 | SSI Stamping Hierarchy | Follow the UK model, prioritising Country Specific + Global Product SSI over Global Entity + Product Specific SSI. Exceptions are listed for CN/MY/IN/SG/LOANID. | Config | Dev Team |
| 10 | Currency Configuration | Configure non-ISO-to-ISO mappings and precious-metal currency mappings where applicable. | Config | Dev Team (CR) |
| 11 | Settlement Accounting | Add the bridge account, EBBS branch code, EBBS transaction type, currency mappings, and other branch-specific requirements. | Config | Dev Team (CR) |
| 12 | GUI Dropdowns and Queries | Add the new branch to the Cashflow Blotter and Dashboard dropdowns. Add `FinalCancelled` cashflow SWIFT status to the default Swift Error filter. | Config | Dev Team |
| 13 | Vostro SI Input Screen | Include the new settlement means. | Config | Dev Team |
| 14 | Rounding | Configure only where special currency or business requirements apply. | Config | To be confirmed |
| 15 | Nostro Static Setup | Maintain legal-entity-and-currency Nostro data. High-volume setup may be performed by Dev Team through CR; smaller volumes may be maintained by Data Ops. | Static | Dev Team or Data Ops |
| 16 | Vostro Static Setup | Configure Vostro to drive Nostro assignment. Create over-account clients as branch-specific SSI. | Static | Data Ops |
| 17 | Business Rules | Configure cashflow suppression, SWIFT suppression, Auto Debit by Agent, shared Nostros, NSTP, counterparty bypass, booking-entity, netting, and BIC netting rules. | Static | Data Ops |
| 18 | Firewall | Open firewall access for users in the new location. | Config | Dev Team |
| 19 | Downstream Engagement | Determine additional requirements for RATAN EOD, SSDR, CIS, FMMIS, LMS, and eBBS. | Analysis | Dev Team |
| 20 | UAT | Execute settlement-operations acceptance testing. | Testing | Settlement Ops |
| 21 | Regression Testing | Execute regression testing. | Testing | Dev Team |
| 22 | CPT | Execute CPT with MO and Settlement Ops. | Testing | MO/Settlement Ops |

## Murex special-function dependencies

- **Batch File:** Murex sends real-time messages for value dates today, tomorrow, and the day after; other messages are sent in batch files.
- **Pending Fixing:** For COM ASIAN/FW/SWP IRD/CF/CS/FRA/IRS products, Murex may mark a cashflow with a pending-fixing flag. RATAN should place it in `WAITING` with `Pending Another Leg` where pre-netting conditions are incomplete.
- **NDS Auto Netting:** Murex generates a child FXD trade to convert ND currency into delivery currency. RATAN auto-nets the delivery-currency cashflow on the parent trade against the delivery-currency cashflow on the child trade.
- **SWAP AGENT:** RATAN identifies RFR and Swap Agent payment types from Murex identifiers for auto-netting and SWIFT-suppression handling.
- **Special Flags:** The integration may carry COM or Non-COM, Pending Clearing, and Linked Trade ID flags.

See [[concepts/pending-fixing]], [[concepts/pending-another-leg]], and [[entities/nds-auto-netting]].

## LMS feeding configuration

The source states that LMS feeding for the new entity must be agreed with Settlement and LMS teams.

| Entity FM Code | Entity FMID | Feeding to LMS |
|---|---:|---|
| SCB EGYPT*CAI | 401036553 | No |
| SCB SAUDI*RYD | 400991880 | No |
| NEPAL GRINDLAYS*KTM | 400007847 | No |
| SCB KL*KUL? | 9 | No |
| STANCHART SAADIQ*KUL | 400093619 | No |
| TAIPEI |  | No |
| OBU TAIPEI |  | No |
| BANGKOK |  | No |
| Other | Other | Yes |

The source-system and Tag 20 convention must also be agreed with LMS.

| Booking System | Source System | Flow | Prefix of Field 20 | Comment |
|---|---|---|---|---|
| SABRE EQ | STELLA | SABRE EQ -> BCS STELLA -> STELLA -> TDS3 -> RATAN | EQ | BAU stack, not Strategy stack |
| LOANIQ | LOANIQ | LOANIQ -> STELLA -> TDS3 -> RATAN ONE | LQ |  |
| BLADE/S2BX/CFETS | FMRP | BLADE/S2BX/CFETS -> STELLA -> TDS3 -> RATAN | DV |  |

## SWIFT query logic

| Function Flow | Entities | Swift Message Source | Query Condition | Tag 20 Logic | Comment |
|---|---|---|---|---|---|
| BCS Stella | SG/UK/Jersey/HK | FMSRE | Tag 20 | EQ + Branch Code + Cashflow ID | BCS stack only |
| Egypt/Nepal/Saudi | Egypt/Nepal/Saudi | FMSRE | Tag 20 | FX + Branch Code + Cashflow ID |  |
| LOANIQ | LOANIQ entities | BLADE/S2BX/CFETS | Tag 20 | LQ + Branch Code + Cashflow ID |  |
| FMRP | SG/MY/IN/CN | RATAN | Cashflow ID |  |  |

## Static-data operating model

### Nostro

Nostro is maintained at legal-entity-and-currency granularity through either:

1. Batch initialisation using a database script for high-volume projects. Settlement Ops must provide reviewed data, and the technical team releases it through a CR.
2. Manual GUI maintenance by the RTS team with maker/checker control.

The source references `WMSUS.xlsx` as the bulk-initialisation input template.

### Release cutoff

Operations must provide reviewed and approved legal-entity-and-currency release cutoffs. The Dev Team deploys the values to production through a CR. See [[concepts/release-cutoff-configuration]].

### Business rules

For NSTP, cashflow suppression, suppression, and netting rules, large project-scale rule sets are supplied by Operations and deployed by scripts through CR. The Business Rule team maintains smaller BAU changes through the RATAN GUI with maker/checker control.

### SWIFT and accounting local static data

The onboarding requires entity-specific sender and receiver BICs, Field 53 and Field 58 values, branch mappings, booking-currency ISO mappings, precious-metal currency lists, and applicable UDF tables. Accounting setup requires the branch code, transaction code, currency mapping, and eBBS bridge account.

## Downstream engagement

The source requires impact assessment with:

- **RATAN EOD:** Determine whether reports require migration.
- **SSDR:** Determine whether additional cashflow information is required.
- **CIS:** Determine whether additional cashflow information is required.
- **FMMIS:** Determine whether additional cashflow information is required.
- **LMS:** Confirm entity feeding, source system, and Tag 20 logic.
- **eBBS:** Provide bridge-account data.
- **Settlement Ops and Product Owners:** Provide BIC, currency, PM, accounting, SSI, and cutoff data.

## Open issues

1. Korea is absent from the listed strategic-flow whitelist, so the final Korea routing scope is unresolved.
2. The retirement of the Bypass Validation Rule is asserted but not supported by release or test evidence.
3. NDS Auto Netting and Pending Fixing blacklists remain `TBD`.
4. New-entity FMID, BIC, branch, Field 53/58, bridge-account, cutoff, and currency mappings are not supplied.
5. Several LMS table entries have missing or uncertain values, including `SCB KL*KUL?` and blank FMIDs.
6. UAT, regression, and CPT are required checklist activities, but their entry and exit criteria are not defined.

## Referenced artifacts

- `WMSUS.xlsx` — bulk Nostro static-data template.
- `fxu-config.py` — FXU configuration-generation script.
- `nostro.py` — Nostro configuration-generation script.
- Azure DevOps work item `12776871` — documentation for the configuration scripts: https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/12776871

This source should be read with [[projects/2026-korea-cash-settlement-onboarding]] and the open questions [[what-is-the-authoritative-korea-2026-routing-and-entity-scope]], [[is-the-new-mo-validation-model-live-for-korea-onboarding]], [[what-are-the-korea-2026-nds-and-pending-fixing-blacklists]], and [[does-the-korea-2026-entity-feed-lms]].
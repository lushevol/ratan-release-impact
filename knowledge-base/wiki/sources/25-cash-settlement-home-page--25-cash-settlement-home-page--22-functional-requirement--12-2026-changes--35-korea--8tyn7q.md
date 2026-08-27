---
type: source
title: Korea Migration Functional Analysis
authors: []
year: 2026
url: ""
venue: ""
tags: [korea, cash-settlement, ratan, functional-analysis, migration]
related: [korea, ratan-settlement, tds3, korea-ssi-onboarding, korea-swift-mx-message-generation, korea-settlement-accounting, korea-settlement-localization, nostro-static-management, pending-fixing-stp-nstp-control]
created: 2026-08-22
updated: 2026-08-22
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Korea Migration Functional Analysis.md"]
---
# Korea Migration Functional Analysis

## Summary

This functional-analysis checklist examines the configuration, integration, dependency, and localization requirements for migrating Korea cash settlement capability into RATAN. It covers Murex integration, fixing and netting behavior, SWIFT generation, SSI and Nostro static data, settlement accounting, business rules, external dependencies, firewall access, and Korea-specific operational requirements.

The document records analysis topics and checklist requirements rather than approved designs, delivery status, test evidence, ownership, or final decisions. Items phrased as questions remain unresolved unless separately confirmed.

## Scope observations

Several settings are identified as mandatory for each entity:

- Booking Entity FMID.
- Booking Entity SWIFT BIC, used as the SWIFT sender BIC.
- Field 53 SWIFT BIC for LCY and over-account processing.
- Field 58 SWIFT BIC for Flip MT202.
- Branch-code mapping.
- Currency release time.
- Bridge account number.
- EBBS branch code and EBBS transaction type.
- Nostro static setup.

The proposed SSI priority follows the UK model: **Country Specific + Global Product SSI** takes priority over **Global Entity + Product Specific SSI**. The checklist records “Nothing special” for this hierarchy, while separately requiring branch-specific SSI for over-account clients.

TDS3 is an unresolved dependency involving trade-confirmation status, NDS auto netting, LIEN, and integration. TLM and LMS are also listed as dependencies without detailed requirements or acceptance criteria.

Potential Korea-specific topics include MT/MX behavior, Ensis integration through Solace, accounting, Korean-character support in SSI, SCI, and cashflow data, and manual handling of OUR payments, TPP, and decimal differences by OSCAR.

## Evidence boundaries

This source supports the existence of a documented analysis scope and explicit checklist requirements. It does not establish that the requirements are approved, configured, implemented, tested, or ready for production. In particular, it does not confirm:

- Korea SWIFT/MX functionality;
- Korean-character support;
- Ensis-Solace integration;
- resolution of TDS3, TLM, or LMS dependencies;
- OSCAR as an approved long-term operating model;
- FMID as a confirmed prerequisite for rule setup.

## Functional-analysis checklist

| # | Categories | Detailed Function | Comment |
|---:|---|---|---|
| 1 | All current Ratan business feature | Murex msg format, additional fields? | |
| 2 |  | Murex integration MQ + Batch? | |
| 3 |  | Fixing batch for rates product which may pending fixing | |
| 4 |  | SWIFT Generation Changes - Booking Entity FMID(mandatory for each entity) - Booking Entity SWIFT BIC (Sender BIC in SWIFT) (mandatory for each entity) - Field 53 SWIFT BIC (for LCY & Over Account) (mandatory for each entity) - Field 58 SWIFT BIC (for Flip MT202) (mandatory for each entity) - Receiver BIC (MT604/605) - Branch code mapping (mandatory for each entity) - Any other branch specific requirement on SWIFT | |
| 5 |  | Vostro SI Input Screen - Include New Settlement Means? | Nothing special |
| 6 |  | Currency Release Time (mandatory for each entity) | |
| 7 |  | NDS Auto Netting | |
| 8 |  | Pending Fixing STP/NSTP Control( in case new product have fixing events) | |
| 9 |  | SSI Stamping Hierarchy - Follow UK model (give priority to "Country Specific + Global Product" SSI over Global Entity + Product Specific SSI) | Nothing special |
| 10 |  | Currency Configuration (if applicable) - Non-ISO to ISO Code mapping - Precious Currency Mapping | |
| 11 |  | Settlement Accounting - Bridge Account # (mandatory for each entity) - EBBS Branch code & EBBS Transaction type (mandatory for each entity) - Any other branch specific requirement (example: Settlement Accounting is suppressed for Precious Metal CCY's in UK) | |
| 12 |  | Rounding - applicable for special currency/requirement only | Keep without decimal |
| 13 |  | Nostro Static Setup (mandatory for each entity) | Korea data management team. |
| 14 |  | Vostro Static Setup (Vostro to drive Nostro assignment) - Over-Account Clients to be created as Branch specific SSI | |
| 15 |  | Business Rules Setup - Cashflow Suppression - White List for in scope entities - Swift Suppression - Auto Debit by Agent - Nostros shared with other entity (example: China) - NSTP - Add new entity to Rules where SCB Entities as Counterparty is bypassed - Add new entity to Rules where SCB entities are added as Booking Entity - Netting Static - BIC Netting Static | Data entitlement, potentially Korea entity fmid is a mandatory condition for rule setup from Korea data static team. Yeon Su to advise on: NSTP/Netting/suppression rules |
| 16 | Open Firewall for users in new location | | |
| 17 | TDS3 dependency | Trade confirmation status (TDS3?) | |
| 18 | | NDS auto netting | |
| 19 | | LIEN | |
| 20 | | Integration | |
| 21 | TLM dependency | | |
| 22 | LMS dependency | | |
| 23 | Korea customized features? | MT/MX? | |
| 24 |  | Ensis integration by solace? | |
| 25 |  | Accounting? | |
| 26 |  | Korea language issue? Require to support in SSI, SCI, cashflow data? | |
| 27 |  | OUR payments, TPP | manually key in by OSCAR 1. TPP 2. Decimal diff |

## Related wiki context

This checklist extends the Korea onboarding material in sources/26-auto-netting-page-md-files--216-cash-settlement-home-page-cash-settlement-home-page-functional-requirement-04--lpgtrq. It should be read alongside [[entities/korea]], [[entities/ratan-settlement]], [[entities/tds3]], [[concepts/korea-ssi-onboarding]], [[concepts/korea-swift-mx-message-generation]], and [[concepts/korea-settlement-accounting]] without treating those related pages as evidence that the checklist items are delivered.
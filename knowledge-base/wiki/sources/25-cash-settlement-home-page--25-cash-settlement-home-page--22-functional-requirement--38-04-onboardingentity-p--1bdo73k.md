---
type: source
title: 2025 Tranche 1 HK TW TH Entity Onboarding Checklist
authors: []
year: 2025
url: ""
venue: "Cash Settlement Home Page — Functional Requirement"
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, onboarding, 2025-tranche-1, hong-kong, taiwan, thailand, functional-requirement]
related: [2025-tranche-1-hk-tw-th-onboarding, entity-branch-onboarding, legacy-versus-strategic-cash-settlement-routing, entity-specific-swift-generation, tranche-1-onboarding-readiness, settlement-message-routing, cashflow-suppression, ssi-selection-hierarchy, settlement-accounting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/New Entity onboarding checking list/2025 Tranch1 (HK, TW, TH) Onboarding.md"]
---

# 2025 Tranche 1 HK TW TH Entity Onboarding Checklist

## Summary

This functional-requirement checklist defines the configuration and static-data work needed for 2025 Tranche 1 cash-settlement onboarding. Its title identifies Hong Kong, Taiwan, and Thailand as the primary scope. A referenced go-live-readiness page also names Hongkong, Bangkok, Taipei, and New York; the relationship of New York to this checklist remains unresolved.

The checklist covers feed blacklists, Murex migration batches, routing, SWIFT generation, currency release times, netting controls, SSI hierarchy, settlement accounting, GUI changes, Vostro and Nostro setup, business rules, firewall access, downstream engagement, UAT, and regression testing.

The document is a requirements list rather than evidence of completed implementation. Firewall access is the only item explicitly marked done. Several blacklist values, ownership assignments, applicability fields, and testing decisions remain incomplete or ambiguous.

## Routing and processing scope

The source distinguishes the following lists:

- Legacy flow: `EG/NP/SAUDI/LOANIQ`
- Strategic flow: `CN/SG/MY/IN/UK/DE`
- CPT list: `HK/TW/TH`

The workflow whitelist determines whether processing is sent to [[entities/razor]] or handled in [[entities/ratan]], where RATAN generates SWIFT and accounting. The source also refers to “BCS vs Strategic Routing” without defining BCS.

For the Murex Cash Migration Only batch solution:

- H2 Adaptor whitelist: `UK, DE`, default, `[T-1, T+1]` group calculation.
- H1 Adaptor whitelist: `CN/SG/MY/IN`, `[VD-1, VD+9]` group calculation.
- These timings are specified only for Murex group calculation.

## Checklist

| # | Description | Details | Type | Done By | Required for Tranche1? |
| --- | --- | --- | --- | --- | --- |
| 1 | Bypass Validation Rule | Bypass EG/NP/SAUDI/LOANIQ/CN(FX), rest need validation Post MO Validation moved to FMRP, then not required? | | | No |
| 2 | LMS Feed Entity List Update | Blacklist includes: EG/NP/SAUDI/KL/TH/TW | Config | Dev Team (CR) | @Mingyang Zhong |
| 3 | [Murex Cash Migration Only] Entity list for the Batch Solution | H2 Adaptor whitelist includes: UK, DE (Set as default) [T-1, T+1] for group calculation H1 Adaptor whitelist includes: CN/SG/MY/IN [VD-1, VD+9] for group calculation only for Murex | Config | @Yang Chen | |
| 4 | - BCS vs Strategic Routing - Entity whitelist for in scope entities (covered via Cashflow Suppression rule) - Entity whitelist setup to send to RAZOR or handle in RATAN (RATAN generates SWIFT & Accounting | Workflow whitelist: 1. EG/NP/SAUDI/LOANIQ (legacy flow) 2. Strategic flow (CN/SG/MY/IN/UK/DE) 3. ++CPT list(HK/TW/TH) | Config | @Yang Chen | |
| 5 | SWIFT Generation Changes | Booking Entity FMID; Booking Entity SWIFT BIC; Field 53 SWIFT BIC (for LCY & Over Account); Field 58 SWIFT BIC (for Flip MT202); Receiver BIC (MT604/605); Branch code mapping; Any other branch specific requirement on SWIFT | Need to be added for new entity [2025 Tranche 1 Go Live Readiness (Hongkong, Bangkok, Taipei, New York) - Derivative Strategy Projects - Confluence] | Config | @Mingyang Zhong | |
| 6 | Currency Release Time | Need to be added for new entity | Config | @Yang Chen | |
| 7 | NDS Auto Netting | Blacklist: TBD | Config | @Lina Feng | |
| 8 | Pending Fixing STP/NSTP Control( in case new product have fixing events) | Blacklist: TBD | Config | No | |
| 9 | SSI Stamping Hierarchy | Follow UK model (give priority to "Country Specific + Global Product" SSI over Global Entity + Product Specific SSI) | Whitelist: CN/MY/IN/LOANID old logic Rest: new logic | Config | No | |
| 10 | Currency Configuration (if applicable) | Non-ISO to ISO Code mapping; Precious Currency Mapping | NA | Config | No Exclude SGO/SGD change @Chongxuan Li | |
| 11 | Settlement Accounting | Bridge Account #; EBBS Branch code & EBBS Transaction type; Any other branch specific requirement | [2025 Tranche 1 Go Live Readiness (Hongkong, Bangkok, Taipei, New York) - Derivative Strategy Projects - Confluence] | Config | @Chongxuan Li @Guiling Wang | |
| 12 | Include new branch in GUI Drop down | Cashflow Blotter; Dashboard | [2025 Tranche 1 Go Live Readiness (Hongkong, Bangkok, Taipei, New York) - Derivative Strategy Projects - Confluence] | Config | @Guiling Wang | |
| 13 | Vostro SI Input Screen | Include New Settlement Means -NOX | | Config | @Guiling Wang @Chongxuan Li | |
| 14 | Rounding | applicable for special currency/requirement only | | Config | | No |
| 15 | Nostro Static Setup | | Static | If volume high will be done by Dev Team (CR). Else Data Ops | @Yang Chen | |
| 16 | Vostro Static Setup (Vostro to drive Nostro assignment) | Over-Account Clients to be created as Branch specific SSI | | Static | Data Ops | No, data ops to setup |
| 17 | Business Rules Setup | Cashflow Suppression; White List for in scope entities; Swift Suppression; Auto Debit by Agent; Nostros shared with other entity; NSTP; Add new entity to Rules where SCB Entities as Counterparty is bypassed; Add new entity to Rules where SCB entities are added as Booking Entity; Netting Static; BIC Netting Static | [2025 Tranche 1 Go Live Readiness (Hongkong, Bangkok, Taipei, New York) - Derivative Strategy Projects - Confluence] | Static | Data Ops | @Chongxuan Li |
| 18 | Open Firewall for users in new location | | Config | Dev Team | Done |
| 19 | Downstream Engagement to determine additional requirements if any | | Analysis | Dev Team | No |
| 20 | UAT | | Testing | Settlement Ops | No |
| 21 | Regression Testing | | Testing | Dev Team | No |

## Key unresolved issues

- The authoritative Tranche 1 entity scope is unclear because New York appears in the referenced readiness page but not in the checklist title.
- `LOANIQ` and `LOANID` are used inconsistently.
- NDS Auto Netting and Pending Fixing STP/NSTP blacklists are `TBD`.
- The validation bypass is phrased as a question rather than a confirmed decision.
- UAT and regression testing are marked not required without a stated rationale or compensating control.
- Nostro setup ownership depends on volume, but no volume threshold is defined.
- `SGO/SGD` is mentioned in a currency-configuration exception without a canonical definition.
- Ownership and Tranche 1 applicability appear misaligned in several rows.

## Related context

This checklist extends [[concepts/entity-branch-onboarding]], [[concepts/cashflow-suppression]], [[concepts/settlement-message-routing]], [[concepts/swift-mt-mx-integration]], [[concepts/ssi-selection-hierarchy]], [[concepts/nostro-vostro-settlement-controls]], and [[concepts/settlement-accounting]]. It also relates to [[projects/cash-settlement-2025-roadmap]], [[entities/murex]], [[entities/lms]], [[entities/nds-auto-netting]], [[entities/ebbs]], and [[entities/cashflow-blotter]].
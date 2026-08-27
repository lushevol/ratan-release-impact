---
type: source
title: 2025 Tranche 2 New Entity Onboarding Checklist
authors: []
year: 2025
url: ""
venue: "Cash Settlement Home Page — Functional Requirement"
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, entity-onboarding, tranche-2, operational-checklist]
related: [2025-tranche2-entity-onboarding, entity-branch-onboarding, cashflow-migration, ssi-selection-hierarchy, settlement-accounting, swift-mt-mx-integration, cashflow-suppression]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/New Entity onboarding checking list/2025 Tranch2 Onboarding.md"]
---

# 2025 Tranche 2 New Entity Onboarding Checklist

## Summary

This functional requirement is an operational checklist for onboarding new legal entities and branches into the 2025 Tranche 2 Cash Settlement flow. It covers application configuration, static data, routing, settlement messaging, accounting, access, downstream analysis, and testing.

The checklist is a readiness artifact rather than evidence that all work is complete. The firewall-access item is explicitly marked `Done`; UAT and regression testing are marked `No`, while several configuration items remain unresolved or require further analysis.

## Scope

The named 2025 Tranche 2 go-live locations are Mauritius, Dubai, DIFC, Jakarta, Manila, Philippines FCU, Tokyo, and Johanesburg. The source does not normalize these locations into legal entities, branches, booking entities, branch codes, FMIDs, or BICs.

The checklist coordinates changes across [[entities/fmrp]], [[entities/murex]], [[entities/lms]], [[entities/razor]], [[entities/ratan]], [[entities/nds-auto-netting]], [[entities/ebbs]], and [[entities/cashflow-blotter]].

## Configuration and Readiness Checklist

| # | Description | Details | Type | Done By | Required for Tranche2? |
| --- | --- | --- | --- | --- | --- |
| 1 | Bypass Validation Rule | Bypass EG/NP/SAUDI/LOANIQ/CN(FX); remaining entities need validation. Post-MO Validation moved to FMRP, then not required? |  |  | No |
| 2 | LMS Feed Entity List Update [Story 8419029 [Tranche2] LMS filter](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/8419029) | Blacklist includes: EG/NP/SAUDI/KL/TH/TW | Config | Dev Team (CR) / Mingyang Zhong |  |
| 3 | Murex Cash Migration Only Entity List for the Batch Solution | H2 Adaptor whitelist; set as default [T-1, T+1] for group calculation; only for Murex | Config |  | No |
| 4 | BCS versus Strategic Routing | Entity whitelist for in-scope entities, covered through Cashflow Suppression; whitelist setup to send to RAZOR or handle in RATAN. RATAN generates SWIFT and Accounting. | Config | Yang Chen |  |
| 5 | SWIFT Generation Changes | Booking Entity FMID; Booking Entity SWIFT BIC as Sender BIC; Field 53 SWIFT BIC for LCY and Over Account; Field 58 SWIFT BIC for Flip MT202; Receiver BIC for MT604/605; branch-code mapping; and other branch-specific SWIFT requirements. Related stories: [8390122](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/8390122) and [8267534](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/8267534). | Config | Mingyang Zhong |  |
| 6 | Currency Release Time | Add for the new entity | Config | Yang Chen |  |
| 7 | NDS Auto Netting | Blacklist: TBD | Config |  |  |
| 8 | Pending Fixing STP/NSTP Control | Required if the new product has fixing events. Blacklist: TBD | Config |  |  |
| 9 | SSI Stamping Hierarchy | Follow the UK model: prioritize “Country Specific + Global Product” SSI over “Global Entity + Product Specific” SSI. Whitelist: CN/MY/IN/SG/LOANID use old logic; the remaining scope uses new logic. | Config |  |  |
| 10 | Currency Configuration | Non-ISO to ISO code mapping and precious-currency mapping, if applicable | Config |  | No |
| 11 | Settlement Accounting | Bridge Account number; EBBS branch code and EBBS transaction type; and other branch-specific requirements. Example: settlement accounting is suppressed for precious-metal currencies in the UK. Related story: [8118402](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/8118402), transaction type setup as RTO for PH. | Config | Chongxuan Li and Guiling Wang |  |
| 12 | Cashflow Blotter and Dashboard Branch Dropdown | Include each new branch in the GUI dropdown | Config | Guiling Wang |  |
| 13 | Vostro SI Input Screen | Include new settlement means: NOX | Config |  |  |
| 14 | Rounding | Applicable only for special currencies or requirements | Config |  | No |
| 15 | Nostro Static Setup | Mandatory for each entity. If volume is high, the Dev Team may perform the work through a CR; otherwise Data Ops performs it. | Static | Yang Chen / Data Ops |  |
| 16 | Vostro Static Setup | Use Vostro to drive Nostro assignment. Create over-account clients as branch-specific SSI. | Static | Data Ops | No, Data Ops to set up |
| 17 | Business Rules Setup | Cashflow Suppression; whitelist for in-scope entities; SWIFT Suppression; Auto Debit by Agent; Nostros shared with another entity, such as China; NSTP; rules bypassing SCB entities as counterparties; rules adding SCB entities as Booking Entity; Netting Static; and BIC Netting Static. | Static | Chongxuan Li / Data Ops |  |
| 18 | Firewall Access | Open the firewall for users in the new location | Config | Dev Team | Done |
| 19 | Downstream Engagement | Determine additional downstream requirements | Analysis | Dev Team | No |
| 20 | UAT | User acceptance testing | Testing | Settlement Ops | No |
| 21 | Regression Testing | Test impact on existing processing | Testing | Dev Team | No |

## Configuration Scope Boundaries

The source identifies separate populations for separate controls:

- LMS blacklist: `EG/NP/SAUDI/KL/TH/TW`
- Legacy workflow: `EG/NP/SAUDI/LOANIQ`
- Strategic flow: `CN/SG/MY/IN/UK/DE`
- Additional CPT list: `HK/TW/TH`
- SSI legacy-logic exceptions: `CN/MY/IN/SG/LOANID`
- NDS Auto Netting blacklist: `TBD`
- Pending Fixing STP/NSTP blacklist: `TBD`

These lists are not interchangeable. Their authoritative relationship remains an open question tracked in [[what-are-the-authoritative-tranche2-entity-routing-lists]].

## Ownership and Completion Interpretation

The `Done By` column mixes owners, assignment notes, explicit negative statuses, and the single explicit completion status `Done`. An assigned owner must not be interpreted as evidence of completion. In particular, the source does not provide completion evidence for UAT, regression testing, downstream engagement, or the unresolved blacklist decisions.

## Open Readiness Questions

- What are the authoritative legal entity and branch identifiers for each go-live location?
- What is the final decision table between BCS, RAZOR, and RATAN?
- What are the final NDS Auto Netting and Pending Fixing STP/NSTP blacklists?
- Is post-MO validation definitively out of scope because it moved to FMRP?
- Which rows are complete, in progress, blocked, or not applicable?
- What evidence and acceptance criteria are required for UAT and regression testing?
- Does `NOX` require a new settlement-means configuration, and who owns it?
- Are Dubai and DIFC, and Manila and Philippines FCU, separate onboarding units or aliases?

## Referenced Systems and Work Items

The checklist references the Cash Settlement Home Page, FMRP, Murex, LMS, RAZOR, RATAN, NDS Auto Netting, EBBS, Cashflow Blotter, SWIFT, Data Ops, Dev Team, and Settlement Ops.

Referenced work items:

- Story 8419029 — `[Tranche2] LMS filter`
- Story 8390122 — `[Tranche2] MX SWIFT Message for MU`
- Story 8267534 — `Tranche 2 Entities - SWIFT message update`
- Story 8118402 — `[Tranche2 Accounting] Transaction type set up as RTO for PH`

Referenced readiness material:

- `2025 Tranche 2 Go Live Readiness (Mauritius, Dubai, DIFC, Jakarta, Manila, Philippines FCU, Tokyo, Johanesburg)` — Derivative Strategy Projects Confluence page `3244588508`
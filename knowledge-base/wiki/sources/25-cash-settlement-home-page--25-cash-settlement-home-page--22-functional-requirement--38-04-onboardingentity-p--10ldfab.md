---
type: source
title: 2025 Hefei Branch Onboarding Checklist
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, onboarding, hefei, swift, accounting, configuration]
related: [hefei-branch, 2025-hefei-branch-onboarding, hefei-strategic-settlement-routing, is-post-mo-validation-required-for-hefei, are-hefei-uat-and-regression-tests-required, what-is-the-authoritative-hefei-entity-name, what-is-the-hefei-razor-ratan-routing-rule]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/New Entity onboarding checking list/2025 Hefei Branch Onboarding.md"]
authors: []
year: 2025
url: ""
venue: ""
---
# 2025 Hefei Branch Onboarding Checklist

This functional-requirement checklist defines the proposed cross-system configuration scope for onboarding the Hefei branch into cash settlement processing. It identifies required changes for validation, strategic routing, SWIFT generation, currency release timing, settlement accounting, GUI dropdowns, and firewall access.

The document is evidence of intended scope, configuration values, and assigned release owners. It does not provide reliable evidence that all required changes were implemented, tested, approved, or deployed.

## Key configuration records

### Entity and branch mapping

| Entity | Entity Name(Murex 2.11) | Entity FMID | Branch code |
| --- | --- | --- | --- |
| Heifei | HEFEI | 401053411 | 73 |

### Field 53 and Field 58 customization mapping

| Entity FMID | Entity Name(Murex 2.11) | Currency | 53 BIC (Rule1) | 58 BIC (Rule2) |
| --- | --- | --- | --- | --- |
| 401053411 | HEFEI | CNY | SCBLCNSXGMO | SCBLCNSXGMO |

### Sender's BIC mapping

| Entity FMID | Entity Name(Murex 2.11) | Sender's BIC |
| --- | --- | --- |
| 401053411 | HEFEI | SCBLCNSXHFI |

### eBBS static

| Murex_Label | Entity FMID | Country | Posting Branch | Txn Type code | Dr Txn Code | Cr Txn Code |
| --- | --- | --- | --- | --- | --- | --- |
| HEIFEI | 401053411 | CN | 10000 | RTN | 100 | 200 |

### eBBS Bridge account

| LegalEntity | FMID | EBBS Bridge Account |
| --- | --- | --- |
| SCB CHINA*HFI | 401053411 | 560100000001910205 |

### GUI dropdown mapping

| LegalEntity | FMID | Country Code |
| --- | --- | --- |
| SCB CHINA*HFI | 401053411 | CHINA |

## Checklist scope

| # | Description | Details | Type | Done By | Required for Hefie? | Released by |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Bypass Validation Rule | Post MO Validation moved to FMRP, then not required? |  |  | Yes | @Xinmiao Huang |
| 2 | LMS Feed Entity List Update | Blacklist includes: EG/NP/SAUDI/KL/TH/TW | Config | Dev Team (CR) | No |  |
| 3 | [Murex Cash Migration Only] Entity list for the Batch Solution | H2 Adaptor whitelist includes: UK, DE (Set as default). H1 Adaptor whitelist includes: CN/SG/MY/IN | Config |  | No |  |
| 4 | BCS vs Strategic Routing — Entity whitelist for in scope entities | Covered via Cashflow Suppression rule. Entity whitelist setup to send to RAZOR or handle in RATAN (RATAN generates SWIFT & Accounting). Workflow whitelist: 1. EG/NP/SAUDI/LOANIQ (legacy flow) 2. Strategic flow (CN/SG/MY/IN/UK/DE) | Config |  | Yes | @Mingyang Zhong |
| 5 | SWIFT Generation Changes | Booking Entity FMID; Booking Entity SWIFT BIC (Sender BIC in SWIFT); Field 53 SWIFT BIC (for LCY & Over Account); Field 58 SWIFT BIC (for Flip MT202); Receiver BIC (MT604/605); Branch code mapping; any other branch specific requirement on SWIFT; need to be added for new entity: SWIFT Field 20 | Config |  | Yes | @Mingyang Zhong |
| 6 | Currency Release Time |  | Config |  | Yes | @Chen Yang |
| 7 | NDS Auto Netting | Blacklist: TBD | Config |  | No |  |
| 8 | Pending Fixing STP/NSTP Control( in case new product have fixing events) | Blacklist: TBD | Config |  | No |  |
| 9 | SSI Stamping Hierarchy | Follow UK model (give priority to "Country Specific + Global Product" SSI over Global Entity + Product Specific SSI). Whitelist: CN/MY/IN/SG/LOANID old logic Rest: new logic | Config |  | No |  |
| 10 | Currency Configuration (if applicable) | Non-ISO to ISO Code mapping; Precious Currency Mapping. NA | Config |  | No |  |
| 11 | Settlement Accounting | Bridge Account #; EBBS Branch code & EBBS Transaction type; any other branch specific requirement | Config |  | Yes | @Chongxuan Li |
| 12 | Include new branch in GUI Drop down | Cashflow Blotter; Dashboard | Config |  | Yes | @Guiling Wang |
| 13 | Vostro SI Input Screen | Include New Settlement Means | Config |  | No |  |
| 14 | Rounding | applicable for special currency/requirement only | Config |  | No |  |
| 15 | Nostro Static Setup | If volume high will be done by Dev Team (CR). Else Data Ops | Static |  | No, data ops to setup |  |
| 16 | Vostro Static Setup (Vostro to drive Nostro assignment) | Over-Account Clients to be created as Branch specific SSI | Static | Data Ops | No, data ops to setup |  |
| 17 | Business Rules Setup | Cashflow Suppression; White List for in scope entities; Swift Suppression; Auto Debit by Agent; Nostros shared with other entity (example: China); NSTP; SCB entity counterparty and booking-entity rules; Netting Static; BIC Netting Static. Cashflow suppression: Non FMRP entities; China Precious Metal. Swift suppress for FCY BTB between 30 China intra entities (except FTU). NSTP: Murex 2.11 CRD CDS product; China Precious Metal; Murex 2.11 CRD RTRS product; CN AdhocNET except CURR/OPT | Static | Data Ops | No, data ops to setup |  |
| 18 | Open Firewall for users in new location |  | Config | Dev Team | Done |  |
| 19 | Downstream Engagement to determine additional requirements if any |  | Analysis | Dev Team | No |  |
| 20 | UAT |  | Testing | Settlement Ops | No |  |
| 21 | Regression Testing |  | Testing | Dev Team | No |  |

## Interpretation boundaries

The strategic routing configuration includes `CN`, but the checklist does not define the complete transaction-level decision rule for whether activity is sent to [[razor]] or handled in [[ratan]]. The statement that RATAN generates SWIFT and accounting is limited to the routing model described here.

The China business-rule items are assigned to Data Ops and are not marked as required specifically for Hefei. They should not be treated as proof that every listed China control was changed for this branch.

The source uses `Hefie`, `Heifei`, and `HEFEI`; the legal-entity record is `SCB CHINA*HFI`. See [[what-is-the-authoritative-hefei-entity-name]] before using these identifiers as interchangeable names.
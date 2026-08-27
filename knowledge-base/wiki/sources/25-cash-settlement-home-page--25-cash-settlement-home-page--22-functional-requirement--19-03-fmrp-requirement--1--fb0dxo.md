---
type: source
title: 2025 FMRP Requirement Backlog
authors: []
year: 2025
url: ""
venue: ""
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, fmrp, roadmap, backlog, migration, day-2, ktlo]
related: [fmrp, f2b, cash-settlement-2025-roadmap, cash-settlement-re-platforming, cashflow-migration, auto-netting, maker-checker-segregation, standard-settlement-instructions, delivery-versus-payment, netting-on-netting, nostro-vostro-settlement-controls, swift-status-reconciliation, which-2025-f2b-milestones-actually-went-live, what-was-the-uk-prime-pm-go-live-date]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/03-FMRP Requirement/2025 backlog.md"]
---
# 2025 FMRP Requirement Backlog

## Summary

This internal planning artifact records a broad 2025 backlog associated with [[fmrp]] and cash settlement. It covers four overlapping areas:

1. F2B product and regional go-live milestones.
2. Murex cashflow migration tranches.
3. Day 2 settlement features.
4. KTLO enhancements, controls, and defect remediation.

The document provides Azure DevOps work-item identifiers for much of the planned scope. It does not provide owners, acceptance criteria, dependencies, completion status, or evidence that the planned releases occurred. Month and quarter references should therefore be treated as planned windows rather than confirmed delivery dates.

## F2B Milestones

| **Mile****s****tone** | **Products** | **Market Events** | **Entities** | **Trade Migration** | **Requirement For Settlement** | **UAT & Release Plan** | **ADO** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Loan Depo (Drop 4.0) | Loan Depo | Events built for CN Rates | CN | NA | UAT & Release support | Release in Jan | [Feature 6469299 F2B: CN Loan Depo Go Live](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/6469299/) |
| Prime PM | | | UK | NA | | Release in Feb | [Feature 6469316 F2B: UK Prime PM Go Live](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/6469316/) |
| Prime Rates | | | UK | Yes | UAT & Release support | Release in Apr | [Feature 6469341 F2B: UK Prime Rates Go Live](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/6469341/) |
| CN CCS Trade Migration | CCS | Events built for CN Rates | CN | Yes | UAT & Release support | Q1 | [dev.azure.com/sc-ado/FMQPR/_workitems/edit/6469344/](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/6469344/) |
| FXO | TBC | TBC | TBC | TBC | TBC | TBC | [https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/6469382/](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/6469382/) |
| Global Rates - HK - TW - IN(LK, BD) - ASEAN(SG, MY, TH, VN) - G10 | * * | | | | | | [Feature 6469360 F2B: Global Rates Go Live](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/6469360/) |
| E- Precious(products same as Prime PM) | Same as Prime PM | Same as Prime PM | UK | Yes | UAT & Release support | Q2 | |
| Central Entitlements | | | | | | | [Feature 6469387 F2B: Central Entitlements](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/6469387/) |
| Keystone (Hongkong) | | | | | | | 6470013 |
| F2B: Continuous Testing | | | | | | | 6469401 |
| F2B: Build & Maintain | | | | | | | 6469448 |
| Strategic CPN | | | | | | | 5848448 |
| FXU | | | | | | | |
| CLS | | | | | | | |
| LOANIQ Day2 | | | | | | | |

The clearest planned release windows are January for CN Loan Depo, February for UK Prime PM, April for UK Prime Rates, Q1 for CN CCS Trade Migration, and Q2 for UK E-Precious. The year is inferred from the source filename and context rather than stated in the table.

The UK Prime PM row narrows the planned release window to February but does not establish an exact date or confirm that go-live occurred. The question tracked by [[what-was-the-uk-prime-pm-go-live-date]] therefore remains open.

## Murex Cashflow Migration

| Milestone | Entity | Requirement | ADO |
| --- | --- | --- | --- |
| Tranche 1 | HONGKONG SCS HK BANGKOK TAIPEI OBU TAIPEI NEWYORK | 1. New Accounting Interface: RATAN->Aspire 2. Static Data setup 3. UAT support & release process | [6469476 ](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/6469476/) |
| Tranche 2 | MAURITIUS DUBAI JAKARTA MANILA TOKYO JOBURG PHILIP FCU DIFC | 2. Static Data setup 3. UAT support & release process | 6469488 |
| Tranche 3 | JERSEY_BR Others | 2. Static Data setup 3. UAT support & release process | 6469527 |
| Manual Entities | | | |

The migration plan uses three named tranches plus an undefined Manual Entities category. Tranche 1 includes a new accounting interface from [[ratan]] to [[aspire]], static-data setup, and UAT and release support. Tranches 2 and 3 list static-data setup and UAT and release support but do not repeat the accounting-interface requirement.

The source says “Murex Cashflow Migration” without specifying a version. These requirements should not be attributed specifically to [[murex-2-11]] without corroborating evidence.

## Day 2 New Features

| Function | Priority | Entity & Business flow | ADO |
| --- | --- | --- | --- |
| Auto Netting | | Swap Agent Clearing Payment | [6469617](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/6469617/) |
| Split | | | [6469564](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/6469564/) |
| Concurrent User Warning | | Global | [6469584](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/6469584/) |
| Automate DVP | | Phase 1: Over Account DVP Phase 2: Precious Metals DVP (via CIS) Phase 3: External Nostro (can move to 2026) | [6469622](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/6469622/) |
| Auto Deduct WHT | | | [6469632](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/6469632/) |
| CDUPS - Trade SI (Strategic) | | | 3624175 |
| Swap Agent Clearing ID | | Swap Agent Clearing Payment | |
| New Feature: Public Filter Creation / Modification Controls | | Global | 6470023 |
| New Feature: Swift MT101 | | | 6470024 |
| New Feature: Save SI | | | 6470035 |
| New Feature: CHATS / PvP | | | |
| SI Hierarchy Change | | | 6470039 |

The Day 2 portfolio combines automation and operational controls. Its priority column is empty, so the source does not establish an ordering among these features.

The DVP proposal is the only item with an explicit phased scope: Over Account DVP, Precious Metals DVP via CIS, and External Nostro. The third phase is identified as movable to 2026, making its inclusion in the committed 2025 baseline uncertain. See [[delivery-versus-payment]].

Trade SI, Save SI, and SI hierarchy changes extend the scope around [[standard-settlement-instructions]] and [[ssi-selection-hierarchy]].

## KTLO Backlog

- Settlement method change & exception handling: [Feature 2659506 [1] CN: Settlement Method change to be considered as a Financial Amendment](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/2659506/)
- Stella Event filter( e.g. expiry): [Stella Inbond cashflow filter - Derivative Strategy Projects - Confluence](https://confluence.global.standardchartered.com/display/DSP/Stella+Inbond+cashflow+filter)

- M: 6472953: Enable NDS Auto Netting for SG
- M: 6472969: Bulk Fail with Maker Checker
- M: 6472976: Bulk in Group Blotter
- M: 6472987: Remove Upper / Lower Case match between Maker & Checker for SI Input
- M: 6472996: Allow other actions on HOLD (SI input, netting, suppression)
- M: 6473001: Receipt Cashflow should not require Vostro if Adhoc Nostro SI is done (to ensure control exists for PM receipts & over account)
- M: 6275726: Notice to receive flag not ticked for SCB receive cashflow (bug)
- M: 5967610: Set Vostro as mandatory for Precious Metal receipts
- M: 6473021: Remove the BIC netting tagging after 'settle as gross' is done
- M:6286998: Egypt / Saudi: Auto select Nostro SI based on currency pair
- M: 6473032: Duplication check in RATAN (Same financials under Trade ID)
- S:6473039: BCS: Support Settlement for CN / MY for Equity Derivatives BCS
- S: 6473043: Nepal: New High Risk Approval Profile for USD 300 Mio
- S: 6473045: FX: Consume Confirmation Match status for FX Swap near leg for Cashflow STP
- M: 6473051: Static: Make business rules case agnostic (to prevent risk of failure)
- S: 6473055: Static: Make Business Rules Static Screen user friendly
- S: 6473062: COB feature for UAT purpose
- S: 6473065: Nostro duplication check - allow multiple nostro setup for FXBRREC when Ebbs account number is different
- S: 6473080: Display exceptions for Checker when Suppression is done
- 6419293: [China Group Pending] Offset the new/withdrawal on same payment within same group
- S: 6473084: Block Netting on Netting except for netting on IRS Fixed + Floating auto netted payments
- S: 6473089: Allow user who did netting to act as Checker
- S: 6473093: Include Debit / Credit indicator on SSI stamping
- S: 5997360: Auto Cashflow Suppress Zero amount cashflows
- S: 6473025: Break STP for Settlement using Blade Comments [subject to BLADE prioritization]
- S: 6473009: STP SCB counterparty cashflows
- S: 6343884: Ratan Release cutoff shifter refinement
- S: 5997797: 103&202Cov: swift status “Released by AMH” but cashflow are still in “Released” status
- S: 6473019: Update Dashboard SWIFT Error criteria to include MT103+202COV
- S:6090337: Update Cashflow status a Swift Suppressed for auto deleted cases in FMSGW
- M: 6040818: Add InterestRate:IRSwap:FixedFixed into IRS pending another leg check
- S: Generate warning for net resultant cancellation that user must manually send Swift cancellation

The source does not define the `M:` and `S:` prefixes. They are preserved as written and should not be interpreted as priority classes without supporting documentation.

## Control and Operational Themes

The KTLO backlog emphasizes operational integrity and exception handling as much as new functionality. Recurring themes include:

- Maker-checker behavior, including bulk-fail controls and an exception that would allow the user who performed netting to act as Checker.
- [[auto-netting]] behavior, including NDS Auto Netting, BIC-tag cleanup, and restrictions on [[netting-on-netting]].
- [[nostro-vostro-settlement-controls]], including mandatory fields, currency-pair selection, and duplicate-account handling.
- Settlement suppression, HOLD behavior, and visibility of suppression exceptions.
- STP enablement and deliberate STP interruption.
- [[swift-status-reconciliation]] across AMH, FMSGW, dashboard criteria, and cashflow status.
- Static-data resilience, including case-agnostic business rules.
- [[ssi-stamping]], including a proposed Debit/Credit indicator.

The maker-checker and netting items are narrowly scoped. They do not support a general conclusion that segregation controls are being removed or that all netting on netting is prohibited.

## Evidence Limitations

This source establishes intended scope and traceability identifiers, not delivery outcomes. In particular:

- An ADO identifier does not prove implementation or release.
- Planned months and quarters are not actual go-live dates.
- Blank fields do not imply that a requirement is unnecessary.
- FXO remains TBC apart from its ADO link.
- Manual Entities, “Others,” and several regional groupings are undefined.
- The source does not identify the relevant Murex version.
- External Nostro DVP may have moved to 2026.
- No rationale or compensating control is supplied for allowing the netting user to act as Checker.

Actual delivery remains tracked through [[which-2025-f2b-milestones-actually-went-live]].
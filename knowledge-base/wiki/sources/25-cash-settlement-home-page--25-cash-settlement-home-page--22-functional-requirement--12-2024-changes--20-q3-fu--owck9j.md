---
type: source
title: Q3 2024 Cash Settlement Functional Requirements and Delivery Status
authors: []
year: 2024
url: ""
venue: ""
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, auto-netting, functional-requirements, q3-2024, uat, rat an, murex]
related: [cash-settlement, auto-netting, murex-2-11, ratan, settlement-suppression, ssi-stamping, cashflow-monitoring, ukde]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/Q3 Function Analysis.md"]
---
# Q3 2024 Cash Settlement Functional Requirements and Delivery Status

## Summary

This source is a Q3 2024 functional-requirement and delivery-status tracker for Cash Settlement, auto netting, cashflow processing, settlement-instruction stamping, SWIFT generation, accounting suppression, and UK-specific migration work. The latest status recorded is 2024-09-20.

The portfolio combines requirements at different lifecycle stages. Some items were in UAT, one item was marked UAT Done, some were deferred to Q4 or marked out of scope, and three auto-netting items had only reached a high-level requirement and settled approach. The tracker does not provide sufficient evidence to infer production deployment, UAT pass rates, defect closure, or go-live approval.

## Main Themes

- UK-specific settlement modernization was the dominant workstream.
- Murex 2.11 was identified as a cashflow source for RATAN batch consumption and as a dependency for fixing-product STP.
- SWIFT/MX generation, settlement accounting suppression, SSI stamping, and clearing-status settlement were separate requirements.
- Cashflow Blotter and Group Blotter enhancements addressed exception visibility, filtering, dashboard monitoring, and self-service operations.
- Operational ownership for Murex-to-RATAN exception monitoring remained unresolved between PSS and Ops as of 2024-09-20.
- RFR Auto Netting, UK Swap Agent Settlement, and NDS Auto Netting had settled approaches but no demonstrated implementation or production status.

## Status Interpretation

The source uses several materially different lifecycle states:

- **In UAT:** testing was underway; this does not establish that testing passed.
- **UAT Done:** UAT was recorded as complete, but defect closure and production approval were not documented.
- **Function documentation fully ready:** functional documentation was ready, but this does not establish implementation acceptance.
- **Analysis to be closed:** analysis was expected to close, but the final outcome was not recorded.
- **High level requirement & approach settled:** requirements and approach were aligned at a high level; build, UAT, and production status were not demonstrated.
- **Move to Q4:** the item was deferred from the Q3 scope.
- **Out of scope:** the item was excluded from the recorded scope; the source does not state whether it was cancelled permanently or deferred elsewhere.

## Verbatim Requirement Tracker

| **ADO Ticket** | **Description** | **Assignee** | **Analysis Status** | **Demo Session** | **UAT Status** | **Comment** |
| --- | --- | --- | --- | --- | --- | --- |
| 4038613 | UKDE: PM - Generate SWIFT but Suppress Settlement Accounting & UK Accounting UAT | Lina | | | 1. Test Case Readiness 2. Dev Readiness 3. UAT Running | |
| 3888688 | UK: MX2.11 Cashflows consumption via batch | Carrie | | | 2024-08-23 Function documentation fully ready 2024-09-20 In UAT, open question for exception handling process( who take responsibility to monitor the exception, PSS or ops) | Doc: [UK - Murex -> RATAN cashflow feeding - Derivative Strategy Projects - Confluence (standardchartered.com)](https://confluence.global.standardchartered.com/display/DSP/UK+-+Murex+-%3E+RATAN+cashflow+feeding) |
| 4602664 | PS3 - Prime Data Entitlement | Carrie | | | | Out of scope |
| 4110302 | UK: Enable Auto Netting for Bilateral Netting | Carrie | | | | Out of scope |
| 4350036 | Add Exceptions into Cashflow Blotter, Custom Filter and Enhance Dashboard | Lina | | | 2024-08-23 Function documentation fully ready 2024-09-20 In UAT | |
| 2300350 | UK: Beneficiary BIC based Netting | Lina | | | 2024-08-16 Function documentation fully ready 2024-09-20 In UAT. | Doc: [Beneficiary BIC Netting - Derivative Strategy Projects - Confluence (standardchartered.com)](https://confluence.global.standardchartered.com/display/DSP/Beneficiary+BIC+Netting) |
| 3624175 | PS2 - Prime Rates: Trade & Fixing SI stamping enhancements | Wayne | | | | Move to Q4 |
| 2659470 | [Should Have] Country based Data Entitlement | Carrie | | | | Move to Q4 |
| 2659494 | UK: Consume Lien Amount from MX2.11 and NSTP | Wayne | | | | |
| 2826141 | Clearing Status based Settlement | Wayne | | | 2024-09-20 In UAT | |
| 3875533 | UK: Enable STP for fixing product cashflows of MX2.11 <<<MX2.11 DEV Required>>> | Lina | | | 2024-08-16 Function documentation fully ready 2024-09-20 In UAT | Doc: [IRS Fix Leg & Floating leg payment handling - Derivative Strategy Projects - Confluence (standardchartered.com)](https://confluence.global.standardchartered.com/pages/viewpage.action?pageId=2726685251) |
| 3875593 | UK: Queue Segregation for Commodities vs Non-Commodities | Carrie | | | 2024-08-16 Function documentation fully ready 2024-09-20 In UAT | |
| 5163470 | Group Blotter Enhancement to make it self service | Wayne | | | 2024-08-16 Proposed solution brief 2024-09-20 UAT Done. | Doc: [Grouping Blotter Monitoring - Derivative Strategy Projects - Confluence (standardchartered.com)](https://confluence.global.standardchartered.com/display/DSP/Grouping+Blotter+Monitoring) |
| 4858340 | Design/Analysis for non-EBBS entities migration for accounting | | | | | |
| 4860328 | UK specific Swift logic | Carrie | | | 2024-09-20 In UAT | Doc: [FMRP Swift Generation - Derivative Strategy Projects - Confluence (standardchartered.com)](https://confluence.global.standardchartered.com/display/DSP/FMRP+Swift+Generation) |
| 5353739 | FEDWIRE SSI Stamping | Wayne | | | 2024-09-20 Analysis to be closed by this week. | |
| 4888384 | Add new CFI Code for CCS/IRS - SSI Stamping enhancement | Wayne | | | 2024-09-20 In UAT | |
| [5679760](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/5679760) | RFR Auto Netting | Wayne | | | 2024-09-20 High level requirement & approach settled. | Doc: [Auto Netting Features - FM re-platforming - Confluence (standardchartered.com)](https://confluence.global.standardchartered.com/display/FMRP/Auto+Netting+Features) |
| 3878089 | UK: Swap Agent Settlement | Wayne | | | 2024-09-20 High level requirement & approach settled. | Doc: [Auto Netting Features - FM re-platforming - Confluence (standardchartered.com)](https://confluence.global.standardchartered.com/display/FMRP/Auto+Netting+Features) |
| [5679828](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/5679828) | NDS Auto Netting | Wayne | | | 2024-09-20 High level requirement & approach settled. | Doc: [Auto Netting Features - FM re-platforming - Confluence (standardchartered.com)](https://confluence.global.standardchartered.com/display/FMRP/Auto+Netting+Features) |

## Dependencies

The recorded dependencies include:

- [[entities/murex-2-11]] as the source of UK cashflows and fixing-product development dependency.
- [[entities/ratan]] as the destination for Murex cashflow feeding and settlement processing.
- [[concepts/swift-mt-mx-integration]] and [[concepts/iso-20022-mx]] for settlement-message generation.
- [[concepts/settlement-suppression]] for UKDE PM processing.
- [[entities/cashflow-blotter]] and [[concepts/cashflow-monitoring]] for operational exception handling.
- [[concepts/ssi-stamping]] for Prime Rates, FEDWIRE, and CFI-code-related requirements.
- [[entities/azure-devops]] for work-item tracking, including tickets 5679760 and 5679828.

## Evidence Limitations and Open Questions

The tracker does not specify:

- Whether UAT items passed or entered production.
- Which defects, regression issues, or acceptance criteria were recorded.
- The final owner for Murex-to-RATAN exception monitoring: PSS or Ops.
- Detailed eligibility and grouping rules for beneficiary BIC-based netting.
- The accounting entries and exception conditions covered by UKDE suppression.
- The eventual disposition of non-EBBS accounting migration.
- Whether RFR Auto Netting or NDS Auto Netting progressed beyond high-level design.
---
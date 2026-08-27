---
type: source
title: Cashflow Migration Readiness
authors: []
year: 2023
url: ""
venue: ""
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, migration, readiness, Murex, Ratan, Razor, static-data, cutover]
related: [cashflow-migration-readiness, cashflow-migration, murex-ratan-migration-reconciliation, murex-to-ratan-cashflow-integration, murex-ratan-reversal-and-replacement-lifecycle, nstp-exception-handling, irs-fix-leg-floating-leg-netting, expected-ratan-to-razor-accounting-break, static-data-readiness]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/01- Function Flow/Cashflow Migration Readiness.md"]
---
# Cashflow Migration Readiness

## Summary

This document is a functional-readiness tracker and migration runbook for the Cash Settlement Home Page migration involving Murex 2.11, Ratan, Razor, EBBS, PSGL, TLM, FMSRE, AMH, and Aspire.

The tracker shows uneven readiness. Failed Process, Hold/Unhold, and USD Limit Control are marked done. Multi Exception, Suppression, LMS Feeding, Trade Confirmation Status, Murex 2.11 Cashflow Event, and Stella Event Handling remain in progress or have unresolved requirements. IRS Netting has completed analysis and documentation, but function verification is still in progress and UAT test cases had not started.

The source records a planned staged cutover, but it does not establish that the runbook was executed. The year of the September runbook is not explicitly stated; the surrounding readiness notes are dated June and July 2023.

## Readiness Interpretation

The source distinguishes between requirements and documentation review, function verification, UAT preparation, UAT execution, and operational go-live. A completed review or documentation item should not be treated as evidence of completed UAT or production readiness.

Important unresolved areas include:

- Vostro migration and SSI stamping UAT.
- Reversal and new-cashflow matching.
- Murex cashflow event exception handling.
- Non-economic trade amendment handling in Stella.
- LMS treatment of Auto Swift Suppression.
- Rollback triggers, ownership, and execution steps.

## Function Readiness Verification

| Function | Epic | Sub Module | Status | Owner | Analysis ETA | Dev owner | Documentation | UAT Test Case | Comment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Multi Exception | | | In Progress | Yash | | Joey,Eric,Caroline | [NSTP Workflow](https://confluence.global.standardchartered.com/display/DSP/NSTP+Workflow) [Multi Exceptions](https://confluence.global.standardchartered.com/display/DSP/Multi+Exceptions) | | Documentation of the Multi exception is pending and is being worked on currently |
| Cashflow Blotter | | | | Wayne | 7th July 2023 | Lu, Shuai, Caroline | [Cashflow Prototype](https://www.figma.com/file/crlFDt3cKfWzIXWdUhrtQ7/Exceptions-in-Cashflow-CN?type=design&node-id=521-2) | | 1. To consolidate & document the latest cashflow blotter requirement. |
| SSI Service | | Auto Stamping | | Yash | | Eric | [FMRP SSI Stamping Flow](https://confluence.global.standardchartered.com/display/DSP/FMRP+-+SSI+Stamping+Flow) | | POC completed Vostro migration still in progress |
| | | SSI Exception | | Yash | | Eric | [FMRP SSI Stamping Flow](https://confluence.global.standardchartered.com/display/DSP/FMRP+-+SSI+Stamping+Flow) | | |
| | | Adhoc SSI | | Yash | | Eric | [Adhoc SI](https://confluence.global.standardchartered.com/display/DSP/Adhoc+SI) | | |
| | | SSI Refresh | | Yash | | Guangqing | [SSI Notification Flow](https://confluence.global.standardchartered.com/display/DSP/SSI+Notification+Flow) | | |
| IRS Netting | | | 1. Analysis & Document done 2. Function verification in progress 3. UAT Test cases not started | Yash | | Eddie | [IRS Legs Netting](https://confluence.global.standardchartered.com/pages/viewpage.action?pageId=2726685251) | | UAT pending, Analysis and documentation completed |
| Manual Netting/Un-Net | | | | Jill | | Eddie | [Netting](https://confluence.global.standardchartered.com/display/DSP/Netting) | | |
| Failed Process | | | Done | Wayne | | Joey | [Failed Process](https://confluence.global.standardchartered.com/display/DSP/Failed+Process) | | As confirmed by Dinesh, Ratan won't send the failed cashflow to Razor for accounting, the accounting break between trade & cashflow would be expected in the recon process. |
| Suppression | | | In Progress | Jill | | Eddie,Caroline | [Cashflow/Swift Suppression](https://confluence.global.standardchartered.com/pages/viewpage.action?pageId=2738540597) | | 2023-07-27 Function requirement review/documentation and test case review are all done. |
| Hold/Unhold | | | Done | Jill | | Joey | [Hold/Unhold](https://confluence.global.standardchartered.com/pages/viewpage.action?pageId=2742543606) | | 2023-06-23 Aligned the requirement details with business and IT teams. Requirement approvals are received from Dinesh and Sumita. 2023-07-27 Function requirement review/documentation and test case review are all done. |
| LMS Feeding | | | In Progress | Jill | | Caroline, Zhaolei | [LMS Feed](https://confluence.global.standardchartered.com/display/DSP/LMS+Feed) | | 2023-07-06 There is still 2 remaining items open. A meeting is scheduled on 7 July to align up these 2 items between business and IT teams. - AUTO Swift Suppression, whether send it to LMS or not? - Swift suppression logic at LMS? 2023-07-27 Function requirement review/documentation and test case review are all done. |
| Trade Confirmation Status | | Blade/Stella Booking | In Progress | Wayne | | Eddie | [CDU Confirmation Status](https://confluence.global.standardchartered.com/pages/viewpage.action?pageId=2678216072) | | 1. Murex 2.11 trade confirmation status are available in CDU Lake 2. Paper is handled by CDU PS and swift is CityNet 3. CDU Lake will check the effort to publish Murex 2.11 confirmation status to Solace 4. [https://confluence.global.standardchartered.com/display/FXRCCPE/CDULAKE+-TRUST+2.0+flow#CDULAKETRUST2.0flow-ConfirmationStatusvalues](https://confluence.global.standardchartered.com/display/FXRCCPE/CDULAKE+-TRUST+2.0+flow#CDULAKETRUST2.0flow-ConfirmationStatusvalues) |
| | | Murex 2.11 Booking | | Wayne | | | [CDU Confirmation Status](https://confluence.global.standardchartered.com/pages/viewpage.action?pageId=2678216072) | | |
| Murex 2.11 Cashflow Event | | Batch & Sequence Control | In Progress | Wayne | | | [Ratan MxML->SCBML Adaptor](https://confluence.global.standardchartered.com/display/DSP/Ratan+MxML-%3ESCBML+Adaptor) | | Murex would provide the snapshot of all the history SNTR cashflows, Ratan can rely on this to identify the batches. 2023-07-05 Discussed with Dinesh & ops how to identify the linkage between the reversal & new cashflows, Predeesh will confirm with team and come back. |
| | | Reversal & New Matching | | | | | | | Pending on Sumita's input to identify the reversal & new cashflows |
| | | Exception Handling | | | | | | | Need more input |
| USD Limit Control | | | Done | Jill | | Guangqing | [Profile USD Limit](https://confluence.global.standardchartered.com/display/DSP/Profile+USD+Limit) | | |
| Stella Event Handling | | Withdrawal & New cashflow batch management | In Progress | Wayne | 7th July 2023 | | | | |
| | | Non Economic Trade Amendment handling | In Progress | Wayne | 7th July 2023 | | | | 2023-07-04 Raised the proposal to drop the non economic cashflow to Stella, Stella will have internal discussion and confirm. |

## Static Data

| Data Type | Status | Action Owner | Dependency | Comments | Next Actions |
| --- | --- | --- | --- | --- | --- |
| Vostro | | | | 1. CFI Code 2. SSI+ changes verification 1. Settlement account/means 2. Bene BIC/Name 3. Order customer 4. Swift Type 3. Ratan changes 1. Vostro Validation Rules 2. Effective Date 3. MT202 Cover Payment | 1. Dinesh confirm the CFI Code 2. SSI Release preparation & UAT 1. Dinesh & Sumita share the CN client list 2. SSI+ team to update the data & review with PO/ops, and upload to UAT env 3. Ratan team to verify the Vostro in ES 4. Ratan team to run the SSI stamping UAT test cases 5. Razor team to run the Swift Generation test cases 3. Yash to follow up the SSI+ open items. |
| Nostro | | | | | |
| Currency Cutoff | | | | | |
| Netting Rules | | | | | |
| Suppression Rules | | | | | |
| NSTP Rules | | | | | |
| USD Limit | | | | | |

## Planned Runbook

```text
- On 2-3 Sep Murex, Ratan, Razor tech go live
- On 2-3 Sep Murex publish cashflows to Ratan, VD 11th Sep
- CPT during 4th Sep to 8th Sep: Real time flow/Murex 2.11 VS Ratan cashflow recon/Razor accounting->EBBS/PSGL->TLM EOD & recon
- On 8th Sep Ratan early release the payments to Razor/FMSRE/AMH
- 9th-10th Sep: Aspire release and go not to go decision
- 11th Sep: Formal business go live & first Aspire EOD running
```

The planned sequence moves from technical go-live and cashflow publication, through a controlled reconciliation period, to early payment release, Aspire release, a go/no-go decision, and formal business go-live. The source does not identify the year of these September dates.

## CPN and Rollback

The source contains `CPN` and `Rollback` sections, but both are empty. No rollback triggers, decision owner, data-reconciliation strategy, recovery sequence, or execution evidence is provided.

## Evidence Boundaries

This source is a readiness plan and tracker rather than an execution record. It provides status notes, ownership, dependencies, and planned dates, but does not provide completed UAT results, defect metrics, acceptance sign-offs, go/no-go outcomes, rollback evidence, or confirmation that the September runbook occurred.

The failed-process note is scoped specifically to the stated Ratan behavior: failed cashflows are not sent to Razor for accounting, and the resulting trade-versus-cashflow accounting break is expected in reconciliation. This should be tracked as [[expected-ratan-to-razor-accounting-break]] rather than generalized to every failure scenario.
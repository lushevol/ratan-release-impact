---
type: source
title: Cashflow Blotter User Actions and Eligibility Requirements
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, cashflow-blotter, fmrp, bcs, functional-requirements, maker-checker]
related: [ratan-cashflow-blotter, cashflow-blotter-action-eligibility, swift-versus-cashflow-suppression, cashflow-failure-and-reinstatement, ad-hoc-cashflow-netting, cashflow-splitting, cashflow-hold-unhold]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Cashflow Blotter/User Actions on Cashflow Blotter.md"]
authors: []
year: 2026
url: ""
venue: ""
---
# Cashflow Blotter User Actions and Eligibility Requirements

This functional-requirement source specifies menu-action eligibility for two distinct operational surfaces: the FMRP Cashflow Blotter and the BCS Cashflow Blotter. It is requirements evidence only and does not establish implementation, testing, or production enforcement.

The models are not interchangeable. FMRP uses detailed settlement-method, SWIFT-routing, netting, and split-cashflow conditions. BCS makes authorization explicit through `RATAN_CASHFLOW_BLOTTER` permissions and maker/checker-oriented state transitions.

## FMRP Cashflow Blotter Action-Eligibility Matrix

| | Menu Item | Cashflow State | Cashflow Sub State | Cashflow Sub State Type | Other Condition |
| --- | --- | --- | --- | --- | --- |
| 1 | Early Materialization | PROJECTED | | | |
| 2 | ReInstate | FAILED | | | |
| 3 | QUEUED | | Pending Exception | |
| 4 | Settle As Gross | WAITING | NA Pending Operator | Pending Another Leg | Settlement_Method<> "UTIL" |
| 5 | WAITING | | Pending Netting Pending Auto Netting | Settlement_Method<> "UTIL" |
| 6 | Status Write Back | RELEASED SETTLED NOSTRO_MATCHED | | | |
| 7 | Regenerate Swift | READY | | Pending Ack | Cashflow Swift Message Standard = 'STRATEGIC' |
| 8 | Resend To Razor | READY | | Pending Ack | Cashflow Swift Message Standard <> 'STRATEGIC' |
| 9 | Early Release | READY | NA | NA | Settlement_Method<> "UTIL" |
| 10 | Update Affirmation | WAITING | | Pending Exception | Cashflow Affirmation Status<>Affirmed and Settlement_Method<> "UTIL" |
| 11 | Swift Suppression | PROJECTED WAITING READY | | <>Swift Suppression <>Undo Swift Suppression <>Cashflow Suppression <>Undo Cashflow Suppression | Settlement_Method<> "UTIL" |
| 12 | Verify Swift Suppression | WAITING | Pending Verification | Swift Suppression | Settlement_Method<> "UTIL" |
| 13 | Undo Swift Suppression | SWIFT_SUPPRESSED | | | Settlement_Method<> "UTIL" |
| 14 | Verify Undo Swift Suppression | WAITING | Pending Verification | Undo Swift Suppression | Settlement_Method<> "UTIL" |
| 15 | Suppress Cashflow | "PROJECTED", "WAITING", "READY" | | <>Swift Suppression <>Undo Swift Suppression <>Cashflow Suppression <>Undo Cashflow Suppression | Settlement_Method<> "UTIL" |
| 16 | **FAILED && after value date.** | | | Settlement_Method<> "UTIL" |
| 17 | Confirm Suppression | WAITING | Pending Verification | Cashflow Suppression | Settlement_Method<> "UTIL" |
| 18 | Un-Suppress Cashflow | CASHFLOW_SUPPRESSED | | | Settlement_Method<> "UTIL" |
| 19 | Confirm Un-Suppression | WAITING | Pending Verification | Undo Cashflow Suppression | Settlement_Method<> "UTIL" |
| 20 | Manual Fail | "QUEUED", "WAITING", "READY" | | | Settlement_Method<> "UTIL" |
| 21 | SWIFT_SUPPRESSED", "CASHFLOW_SUPPRESSED | | | Current Date > Payment_Date and Settlement_Method<> "UTIL" |
| 22 | Confirm Manual Fail | | Pending Verification | Pending Manual Fail | Settlement_Method<> "UTIL" |
| 23 | BIC Net Selected Cashflow | WAITING | | Pending Netting Pending Auto Netting | Booking Entity SCI FMCODE='SCB LONDON*LDN' ~~Booking Entity SCI FMCODE <> 'SCB HONGKON*HKG'~~ and Counterparty SIC BIC Net Flag ='Y' and Splitting Id is empty and Settlement_Method<> "UTIL" |
| 24 | CCIL Net Selected Cashflow | WAITING | | Pending Netting Pending Auto Netting | Counterparty SCI FMID<>400021949 and Counterparty SIC BIC Net Flag <>Y and Settlement Method = 'CCIL' and Splitting Id is empty and Settlement_Method<> "UTIL" |
| 25 | Net Selected Cashflow | "PROJECTED", "WAITING", "READY" | | | Counterparty SIC BIC Net Flag <>Y and Settlement Method <> 'CCIL' and Splitting Id is empty and Settlement_Method<> "UTIL" |
| 26 | WAITING | | Pending Netting Pending Auto Netting | Counterparty SCI FMID=400021949 and Counterparty SIC BIC Net Flag <>Y and Settlement Method = 'CCIL' and Splitting Id is empty and Settlement_Method<> "UTIL" |
| 27 | Un-Net Cashflow | <>NETTED and <> SPLIT | | | Netting Id is not null and Settlement_Method<> "UTIL" |
| 28 | Hold | ~~"QUEUED", ~~"WAITING", "READY" | | | Settlement_Method<> "UTIL" |
| 29 | Unhold | HOLD | | | Settlement_Method<> "UTIL" |
| 30 | Send To WAITING | HOLD | | | Settlement_Method<> "UTIL" |
| 31 | View Swift Message | RELEASED SETTLED | | | |
| 32 | Manual Settle | RELEASED | | | swift status list ("AMH Error", "Check in FMSGW", "Check in FMSRE", "FMSGW Deleted", "FMSGW Error", "FMSRE Deleted", "FMSRE Error", "Manual Delete", "SCPAY Error", "Pending FMSGW Disp", "Pending FMSRE Disp") |
| 33 | Bulk Submit | “WAITING” | "Pending Operator" | "Pending Exception" | |
| 34 | Bulk Approve | | "Pending Verification" | "Pending Exception" | |
| 35 | Bulk Submit/Approve | | | | (selected cashflow sub state same but not follow above bulk status will show with disabled) |
| 36 | Split Cashflow | "WAITING", "READY" | | | Netting Is is empty and Splitting Id is empty and Cashflow Event Type = "New" and Trade Original Source System Name <>'LOANIQ' and Settlement_Method<> "UTIL" |
| 37 | Amend Split Amount | WAITING | | | Splitting Id Exists and Cashflow Event Type = "New" and Settlement_Method<> "UTIL" |
| 38 | **Un-Split Cashflow** | NOT IN ('RELEASED','SETTLED') | | | Splitting Id Exists and Cashflow Event Type = "New" and Settlement_Method<> "UTIL" |
| 39 | ** Settlement Method Update** ** **** ** | WAITING | | | Settlement Method in ('GROSS','') and Data_Flow.Data_Source_System <>Ratan and Instrument_Common.ISDA_Taxonomy in ('ForeignExchange:Forward','ForeignExchange:Spot','ForeignExchange:Swap') |
| 40 | READY | NA | NA | |
| 41 | WAITING, READY, PASTDUE | | | Settlement Method is UTIL and Data_Flow.Data_Source_System <>Ratan and Instrument_Common.ISDA_Taxonomy in ('ForeignExchange:Forward','ForeignExchange:Spot','ForeignExchange:Swap') |
| 42 | **Comment** | | | | |
| 43 | **adhoc SSI** | | | | |
| 44 | **Submit** | | | | |
| 45 | **Approve** | | | | |

## BCS Cashflow Blotter Action, Permission, and Eligibility Matrix

| | Menu Name | Maker/Checker action? | lastChecker | StpFlag (true STP) | Permission | Cashflow.Cashflow_State | Cashflow_Sub_Status | Cashflow_Sub_Status_Type | Other Condition |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Reinstate | maker | | N | RATAN_CASHFLOW_BLOTTER:F_Reinstate | FAILED | Pending Operator | NSTP Release | |
| 2 | **Update Affirmation Status** | maker | **user maker id as the checker** | N | RATAN_CASHFLOW_BLOTTER:F_Cashflow_Affirmation_Status_Change | PROJECTED\|QUEUED\|PENDING | | | |
| 3 | Net Selected Cashflow | maker | | N | RATAN_CASHFLOW_BLOTTER:F_Perform_Ad_Hoc_Netting | PROJECTED\|QUEUED | | Must NOT be Auto Netting for selected rows | |
| 4 | Un-Net Cashflow | | | N | RATAN_CASHFLOW_BLOTTER:F_Perform_Un_Net_Initiate | QUEUED (for maker role) | Pending Operator (for maker role) | NSTP Release (for maker role) | |
| 5 | Verify Un-Net Cashflow | | | | RATAN_CASHFLOW_BLOTTER:F_Perform_Un_Net_Verify | QUEUED (for checker role) | Pending Verification | Un-Net | |
| 6 | Adhoc SSI Input - Maker | | | | RATAN_CASHFLOW_BLOTTER:F_Ad_Hoc_SSI_Initiate | PROJECTED\|QUEUED | EMPTY or Pending Operator | EMPTY or Adhoc SSI Amendment or NSTP Release | |
| 7 | Adhoc SSI Input - Checker | | | | RATAN_CASHFLOW_BLOTTER:F_Ad_Hoc_SSI_Verify | PROJECTED\|QUEUED | Pending Verification | Adhoc SSI Amendment | |
| 8 | Release Cashflow | | | | RATAN_CASHFLOW_BLOTTER:F_Cashflow_Status_Change_Release | QUEUED or FAILED | Pending Operator | NSTP Release | |
| 9 | Confirm Release > Accept Release | | | | RATAN_CASHFLOW_BLOTTER:F_Cashflow_Status_Change_Release | QUEUED or FAILED | Pending Verification | NSTP Release | |
| 10 | Confirm Release > Reject Release | | | | RATAN_CASHFLOW_BLOTTER:F_Cashflow_Status_Change_Release | QUEUED or FAILED | Pending Verification | NSTP Release | |
| 11 | Release Failed Cashflow > Set Value Date to Deal Value Date | | | | RATAN_CASHFLOW_BLOTTER:F_Cashflow_Status_Change_Release | FAILED | Pending Operator | NSTP Release | |
| 12 | Release Failed Cashflow > Set Value Date to Current System Date | | | | RATAN_CASHFLOW_BLOTTER:F_Cashflow_Status_Change_Release | FAILED | Pending Operator | NSTP Release | |
| 13 | Confirm Release Failed Cashflow > Accept Deal Value Date | | | | RATAN_CASHFLOW_BLOTTER:F_Cashflow_Status_Change_Release | FAILED | Pending Verification | NSTP Release | |
| 14 | Confirm Release Failed Cashflow > Confirm Current System Date | | | | RATAN_CASHFLOW_BLOTTER:F_Cashflow_Status_Change_Release | FAILED | Pending Verification | NSTP Release | |
| 15 | Confirm Release Failed Cashflow > Reject Release | | | | RATAN_CASHFLOW_BLOTTER:F_Cashflow_Status_Change_Release | FAILED | Pending Verification | NSTP Release | |
| 16 | Add Comment | | | | RATAN_CASHFLOW_BLOTTER:F_Add_Settlement_Comment | | | | |
| 17 | Suppress Cashflow | | | | RATAN_CASHFLOW_BLOTTER:F_Ad_Hoc_Suppress | PROJECTED\|QUEUED | | != Adhoc Suppression | |
| 18 | Confirm Suppression > Accept Suppression | | | | RATAN_CASHFLOW_BLOTTER:F_Ad_Hoc_Suppress | PROJECTED\|QUEUED | Pending Verification | Adhoc Suppression | |
| 19 | Confirm Suppression > Reject Suppression | | | | RATAN_CASHFLOW_BLOTTER:F_Ad_Hoc_Suppress | PROJECTED\|QUEUED | Pending Verification | Adhoc Suppression | |
| 20 | Un-Suppress Cashflow | | | | RATAN_CASHFLOW_BLOTTER:F_Ad_Hoc_Suppress | SUPPRESSED | | | |
| 21 | View Trade Details | | | | None | Any, but hidden for non-NETTED rows with Netting_Id | | | |
| 22 | Manual Fail | | | | RATAN_CASHFLOW_BLOTTER:F_Ad_Hoc_Suppress | FAILED\|QUEUED | | | |
| 23 | View Cashflow Details | | | | None | Any | | | |
| 24 | View Cashflow History | | | | None | Any | | | |
| 25 | View Swift Message | | | | None | RELEASED\|SETTLED | | | | |

## Operational Requirements

For FMRP, suppression and reversal are maker/checker flows. SWIFT suppression applies where payment is not required; cashflow suppression applies where both payment and settlement accounting are not required. Reversal is limited to before value date. Post-value-date handling is routed through AMH / Oscar for payment and through Oscar for payment plus accounting.

Manual failure is intended to highlight cashflows that missed settlement timing. A `FAILED` cashflow has no further RATAN action other than Re-Instate, although new cashflow events from [[stella]] can overwrite it. Reinstatement returns the cashflow to `QUEUED`, reruns Netting Client Check and Exception Check, and creates a `Cashflow Re-Instate` maker/checker exception.

FMRP strategy netting can use cashflows from [[stella]], Murex 2.11, and [[mxcash]]. Netting creates a resultant `QUEUED` cashflow, marks components `Netted`, and generates a `Net Cashflow` exception for checker review. A market event affecting a netted component should initiate un-netting, place the cashflow under NSTP review, and generate a `Previously Netted` exception.

## Interpretation Limits

Several FMRP rows appear to be continuation rows rather than complete actions, including rows 3, 5, 16, 21, 26, 40, and 41. The source also contains conflicting Hold eligibility, inconsistent state labels, and inconsistent field identifiers such as `SCI`/`SIC`, `Splitting Id`/`Splitting Is`, and `Settlement_Method`/`Settlement Method`. These items require resolution before using this source as an implementation specification.
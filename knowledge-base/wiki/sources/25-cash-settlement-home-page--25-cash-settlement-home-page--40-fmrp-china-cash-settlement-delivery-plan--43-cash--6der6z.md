---
type: source
title: "FXO Mini Trade Migration - Ratan Cash Settlement Runbook (2026-08-15 Weekend)"
authors: []
year: 2026
url: ""
venue: "Operational migration runbook"
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, migration, FXO, FMRP, Murex2.11, Stella, Ratan-Settlement, runbook]
related: [fxo-mini-trade-migration-ratan-cash-settlement, murex-2-11, stella, ratan-settlement, fmrp, fxo, cash-settlement-migration, high-risk-nstp-rule, cashflow-suppression, trade-cashflow-reconciliation, pending-cashflow-monitoring, authoritative-migration-date-and-final-scope]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/FMRP China Cash Settlement Delivery Plan/Cash Settlement RATAN ONE 2026 Release Plan/FXO Mini Trade Migration - Ratan Cash Settlement - RunBook (2026-08-15 weekend).md"]
---
# FXO Mini Trade Migration - Ratan Cash Settlement Runbook

## Purpose and context

This source is an operational runbook for a controlled FXO mini trade migration involving [[murex-2-11]], [[stella]], and [[ratan-settlement]] within the [[fmrp]] programme. It describes how selected cashflows are identified, held, monitored, released, reconciled, and returned to normal BAU processing.

The source references:

- [FMRP Trade Migration - Ratan Cash Settlement - PROD Approach]
- [FXO Tech Readiness - 8.0 - FM re-platforming - Confluence](https://confluence.global.standardchartered.com/display/FMRP/FXO+Tech+Readiness+-+8.0)
- [Runbook_MiniMigration_FXO.xlsx](https://standardcharteredbank-my.sharepoint.com/:x:/r/personal/1521275_zone1_scb_net/_layouts/15/Doc.aspx?sourcedoc=%7B96537F3C-69C0-4DD0-8A71-219D80E98DA3%7D&file=Runbook_MiniMigration_FXO.xlsx&action=default&mobileredirect=true)

The document is a plan with partial execution annotations, not a validated post-migration report. It does not provide final reconciliation results or an overall pass/fail outcome.

## Scope

The source describes a limited migration of more than 100 trades, with an interim count of 130 trades recorded on 3 August. The portfolio pairs are:

```text
| OP_GBL_THO       | OP_GBL_THO_STL       |
| OP_BTB_THAI      | OP_BTB_THAI_STL      |
| OP_GBL_CNY       | OP_GBL_CNY_STL       |
| OP_BTB_TANZNIA   | OP_BTB_TANZNIA_STL   |
| OP_GBL_ZAR       | OP_GBL_ZAR_STL       |
```

The source does not establish that 130 was the final migration population, nor does it explain the meaning of the `_STL` suffixes.

## Control configuration

The initial Murex control is specified as:

```text
Rule: FXO-Mini_TM_Murex_Cfs

Data Source System in (MUREX, Ratan)
Payment Date in (Next Mon., Next Tue.)
In-Scope Portfolio
```

The migration-window update replaces the portfolio condition with a cancelled or original trade-ID list:

```text
Data Source System in (MUREX, Ratan)
Payment Date in (Next Mon., Next Tue.)
Cancelled Trade Id / Original Trade Id List
```

The Stella control is specified as:

```text
Rule: FXO-Mini_TM_Stella_Cfs

Data Source System in (Stella, Ratan)
Payment Date in (Next Mon., Next Tue.)
In-Scope Portfolio
```

The source distinguishes these rules from cashflow filters:

```text
00Elena_TM_Murex_NSTP_Cfs
00Elena_TM_Stella_NSTP_Cfs
```

The Murex filter is used to obtain cashflows affected by the Murex NSTP rule and to support suppression and un-suppression. The Stella filter is created later to obtain cashflows with the Stella High Risk NSTP exception and export them for processing.

## Operational runbook

The source contains the following operational fields: `Steps`, `Date`, `Events`, `TODO`, `By`, `By Date`, `Status`, and `Comment`.

| Steps | Date | Events | TODO | By | By Date | Status | Comment |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | VD-7BD: Thur. - VD: Next Monday - 2026-08-06 | **BAU Behavior** - Murex2.11 cashflows **feeding **into Ratan Settlement | Provide In-Scope **Portfolio **List | Migration Team @Yonggang Carter Deng | 2026-08-06 | | |
| 2 | VD-6BD: Fri. - 2026-08-07 | NA | Setup **Murex High Risk NSTP rule: FXO-Mini_TM_Murex_Cfs ** before Materialization Date - **Data Source System in (MUREX, Ratan)** - **Payment Date in (Next Mon. , Next Tue.)** - **In-Scope Portfolio** | - @Cordelia Sumita K Thirunavukarasu - Rule User | 2026-08-07 | | |
| 3 | **UVT to Murex High Risk NSTP rule: FXO-Mini_TM_Murex_Cfs** | @Kuan Wang (Elena) | | | Elena: 2026-08-07 done by @Bin Abdul Kadir Abdullah ![image-2026-8-10_14-32-26.png](attachments/image-2026-8-10_14-32-26.png) |
| 4 | Each day until Migration Weekend | | **Monitor **cashflows(until 14th Aug - Friday 9PM) in Pending Auto Netting / Pending Netting / Pending Another Leg which will not hit Above High risk NSTP rule. Ops user not do net in advance. - Check the list if there are any In-Scope Murex cashflows wrongly RELEASED/SETTLED **Note**: If Murex cashflows **wrongly** RELEASED/SETTLED, the cashflow will be WAITING + Reversal after Murex Cancellation feeding in. **Next Step**: Release the withdraw murex cashflows and Stella cashflows. | @Kuan Wang (Elena) | | | ** **By Create filter or by sql in sql_byPort.txt |
| 5 | VD-5BD: Mon. - 2026-08-10 | **BAU Behavior** - Murex Cashflows **materialized**, then STP'd or NSTP | **Create Filter: 00Elena_TM_Murex_NSTP_Cfs** to get Murex2.11 cashflows hit above NSTP rule | @Kuan Wang (Elena) | | | **No Reversal Payment from Murex feeding in** |
| 6 | **Migration Weekend** - **Saturday** - 2026-05-16 | NA | 1. Provide **Cancelled Trade Id list** - final version - Murex_ratan_cancel_report.csv** - 9:30?** - **Mapping **between FXD trade id and Parent NDS trade id(for future 7 days recon) if there is 2. **Murex → Ratan** **Settlement**** cashflow list** - murex_ratan_cashflow_report.csv 3. Pending Cash Cancellation List.csv | Murex Team @Linzhen Wu (Wythe) | | | |
| 7 | 1. **Stella → Ratan** **Settlement Cashflow List - 9:30?** 2. **Mapping** between Murex Trade Id and Stella Trade Id | Migration Team @Nagaraj Ponnuchamy | | | |
| 8 | Export cashflows in **Filter: 00Elena_TM_Murex_NSTP_Cfs** - Get cashflow id list for **Cashflow Suppress & un-Suppress** | @Kuan Wang (Elena) | | | |
| 9 | Export Murex future 7 days cashflows by Trade ID(original trade id) for future 7 days recon - 10am stand by? | - @Kuan Wang (Elena) - PSS | | | |
| 10 | Update **Murex High Risk NSTP rule** - - **Data Source System in (MUREX, Ratan)** - **Payment Date in (Next Mon. , Next Tue.)** - ~~**In-Scope Portfolio**~~ - **Cancelled Trade Id / Original Trade Id List** - **Stand by 11am?** | - Ops User - Rule User | | | |
| 11 | Setup **Stella High Risk NSTP rule:** FXO-Mini_TM_Stella_Cfs - **Data Source System in (Stella, Ratan)** - **Payment Date in (Next Mon. , Next Tue.)** - **In-Scope Portfolio** | - Ops User - Rule User | | | |
| 12 | **Cashflow Suppress & un-Suppress** the cashflows in **Filter: 00Elena_TM_Murex_NSTP_Cfs **so that the out of scope cashflows can be processed as normal BAU behavior - STP'd - **NSTP'd cashflows** – (Elena provide out of migration scope cf list) | - Ops User - @Kuan Wang (Elena) | | | Elena: 2026-08-15 Done by Babu on 14th Aug - Friday |
| 14 | **Migration Behavior:** - **Stella cashflows**** feeding** into Ratan Settlement ** ** | Monitor Stella cashflows feeding in | - PSS - @Kuan Wang( Elena) | | | ** ** |
| 15 | NA | Export future 7 days cashflows for Stella by Trade ID | - PSS | | | ** ** |
| 18 | NA | **Recon Report**: Stella vs RATAN Cashflow feed Recon - Total Number in Group Blotter & Cashflow Blotter - No Pending cfs in Group Blotter - etc... | - @Kuan Wang( Elena) | | | |
| 19 | **Recon Report:** Stella vs Murex2.11 7 days Cashflow Recon | - @Kuan Wang( Elena) | | | |
| 20 | **Disable **Murex & Stella NSTP rule - FXO-Mini_TM_Murex_Cfs - FXO-Mini_TM_Stella_Cfs **Stand By 4 pm** | - Ops User - Rule User | | | Murex Rule: done on 14th Aug - Friday |
| 21 | **Migration Behavior:** - **Murex cashflows feeding** into Ratan Settlement ** ** | ** **Monitor Cancellation feeding | PSS | | | |
| 22 | NA | Export future 7 days cashflows for Murex by Trade ID | - PSS | | | |
| 23 | ** **NA | Murex2.11 vs RATAN Cancellation Recon - Murex cashflows **cancelled naturally **along with Trade Cancellation | - @Kuan Wang( Elena) | | | |
| 24 | ** **NA | Create Filter: 00Elena_TM_Stella_NSTP_Cfs to get Cashflow list with Stella High Risk NSTP Exception - Export excel | - @Kuan Wang( Elena) | | | e.g. ![image-2026-1-21_17-38-21-1.png](attachments/image-2026-1-21_17-38-21-1.png) |
| 25 | ** **NA | 1. Recon reports review 2. Bulk cashflow_suppress & un-cashflow_suppress Stella cashflows in Filter: 00Elena_TM_Stella_NSTP_Cfs so that cashflows can be processed as normal BAU behavior. | - Ops User | | | |

## Responsibilities and execution notes

Named responsibilities include:

- **Migration Team:** provide the in-scope portfolio list and Stella-to-Ratan cashflow and trade-ID mappings.
- **Murex Team:** provide the cancelled-trade list, Murex-to-Ratan settlement cashflow list, pending cash-cancellation list, and FXD-to-Parent NDS mapping.
- **Rule User:** configure and update the Murex and Stella High Risk NSTP rules.
- **Ops User:** perform suppression, un-suppression, rule updates, monitoring, and bulk processing.
- **PSS:** monitor flows, export future seven-day cashflows, and monitor cancellation feeds.
- **Kuan Wang (Elena):** coordinate filters, monitoring, exports, reconciliation, and rule-related activities.

The source records that the Murex rule UVT was completed on 2026-08-07 by Bin Abdul Kadir Abdullah. It also records that cashflow suppression and un-suppression preparation was completed by Babu on 2026-08-14, and that the Murex rule was disabled on 2026-08-14. These annotations do not establish complete migration closure.

## Reconciliation and exception handling

Required checks include:

- Stella versus Ratan Settlement cashflow-feed reconciliation.
- Stella versus Murex2.11 seven-day cashflow reconciliation.
- Murex2.11 versus Ratan cancellation reconciliation.
- Group Blotter and Cashflow Blotter record-count checks.
- Confirmation that no pending cashflows remain in Group Blotter.
- Future seven-day comparison by original trade ID or mapped trade ID.
- Confirmation that Murex cashflows cancel naturally with trade cancellation.

The runbook monitors `Pending Auto Netting`, `Pending Netting`, and `Pending Another Leg`. It warns that in-scope Murex cashflows may be incorrectly `RELEASED` or `SETTLED`. The described path is for such cashflows to enter `WAITING`, receive a reversal after Murex cancellation feeds in, and then be released as withdrawn Murex and Stella cashflows.

The source does not specify matching tolerances, formal acceptance criteria, exception owners, sign-off requirements, or evidence-retention requirements.

## Source ambiguities

The file name and surrounding dates indicate an August 2026 migration window, but Step 6 states `2026-05-16`. The relationship between `VD-7BD`, `2026-08-06`, and “Next Monday” is also unclear. Steps 13, 16, and 17 are absent from the supplied numbering. The source does not clarify whether the later trade-ID condition fully supersedes the initial portfolio condition.

These questions are tracked in [[authoritative-migration-date-and-final-scope]].
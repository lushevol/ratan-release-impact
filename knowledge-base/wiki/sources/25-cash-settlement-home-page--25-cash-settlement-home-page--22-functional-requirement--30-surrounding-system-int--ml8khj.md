---
type: source
title: Murex 2.11 Cashflow Integration
authors: []
year: 2023
url: ""
venue: Internal functional requirement
created: 2026-08-22
updated: 2026-08-22
tags: [murex, ratan, cashflow-integration, china, migration, settlement]
related: [murex-to-ratan-cashflow-integration, murex-cashflow-status-lifecycle, murex-ratan-migration-reconciliation, murex-cashflow-migration-to-ratan, razor, how-are-past-value-date-murex-reversals-reconciled-in-ratan, how-is-nds-deliverable-currency-routing-enforced-between-murex-and-ratan, is-cashplatform-an-alias-or-component-of-ratan, which-murex-payment-reports-move-to-razor-ratan-or-remain-for-precious-metals]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration.md"]
---
# Murex 2.11 Cashflow Integration

This internal functional requirement describes the interim China settlement architecture while Murex G2000 is decommissioned in phases. [[murex]] remains the source of trades and cashflows until trade migration to [[stella]], while qualifying non-precious-metal cashflows move to [[ratan]] for netting or gross settlement, SWIFT, and settlement processing. [[razor]] is the proposed target component for non-precious-metal settlement accounting and associated reporting.

This is a requirements and design source, not evidence that the design was implemented, tested, or remains current.

## Intended responsibility split

- Murex continues trade-accounting output to Aspire.
- Eligible non-precious-metal cashflows are sent to RATAN for NET/GROSS, SWIFT, and settlement-accounting processing through RATAN and Razor.
- Precious-metal cashflows remain in Murex BAU, including accounting and TLM reconciliation.
- Murex suppresses duplicate outbound processing for RATAN-eligible cashflows to LMS, FMSRE, Aspire, and EBBS.
- Cashflows are dispatched only once their value date is within seven days (VD-7).

## RATAN eligibility

Murex is intended to send only cashflows that meet the following documented criteria. The struck-through trade-validation criterion is not treated as active.

| # | Criteria | Murex Filter Logic | Comment |
| --- | --- | --- | --- |
| 1 | China entity | entity in the list of fmrp enabled entities | |
| 2 | Cashflow in initial status | Payment.status = 'INIT' | |
| 3 | ~~Trade is validated~~ | ~~Trade.valid_status in (VALD,COMP)~~ | sync with trade insertion |
| 4 | Value Date condition | Bringing cashflows as early immediately after its generation in Murex 2.11 into RATAN will create additional overhead when there are changes due to trade amendments/cancellation & others Agreed with PO will take VD-7 cashflow flow to Ratan | RATAN-10820 |
| 5 | Exclude precious metal deal cashflow | A trade is treated as a precious-metal deal when the entity is in scope and the trade CCY, underlying CCY, or first three characters of the instrument is a Bullion CCY. All cashflows under that trade continue to settle from Murex 2.11. | RATAN-11017 |
| 6 | Exclude Non deliverable CCY | Agreed with PO to exclude Non deliverable CCY for NDS Trades. | RATAN-13997 |
| 7 | Exclude zero payment | Payment.Amount = 0 | |
| 8 | FXD | Exclude the trade flow to Razor FXD logic is updated for H1 go live in Jul-2024 | |

## FXD routing retained in Murex

| Settle System | Criteria | Murex Logic |
| --- | --- | --- |
| MX | typology in ('NDF','NDS Fixing','ND CDS Fixing','Phy_Precious','PayModeSett','Emissions FX','COM INDEX') | `PAY.M_TYPOLOGY IN('NDF','NDS Fixing','ND CDS Fixing','Phy_Precious','PayModeSett','Emissions FX','COM INDEX')` |
| MX | Early Terminate Fee | `(PAY.M_FLOW_TYPE0='CAP' and (PAY.M_FLOW_TYPE1='XIT' or PAY.M_ACTION='XIT') and (PAY.M_MOP_ID<>0))` |
| MX | PayModeSett SMP generated FXD | `PAY.M_TRN_ID in (select M_NB from TRN_HDR_DBF where M_TRN_GTYPE = 77 and M_CREATOR <> 0 and M_CREATOR in ( select M_NB from TRN_HDR_DBF where M_TRN_GTYPE = 84 and M_TRN_TYPO = 'PayModeSett'))` |
| MX | typology in FX_PCD,FX_DCD,DCD & (external counterparty \|\| counterparty country is JERSEY) | `(PAY.M_STRATEGY in ('FX_PCD','FX_DCD','DCD') AND (CPTN.M_STATUS=0 AND (CP.M_CLASSIFY='EXTERNAL' OR CPTN.M_COUNTRY='JERSEY') ))` |
| MX | Non PVB Bullion CCY Payment | `PAY.M_CNTRP not in (select M_LABEL from MUREXDB.TABLE#DATA#COUNTERP_DBF where M_PB_CUST='Y' ) and (exists(select 1 from MUREXDB.TABLE#DATA#CURRENCY_DBF CCY2 where (TRN.M_BRW_NOMU1=CCY2.M_LABEL or TRN.M_BRW_NOMU2=CCY2.M_LABEL or TRN.M_BRW_ODNC0=CCY2.M_LABEL or TRN.M_BRW_ODNC1=CCY2.M_LABEL) and CCY2.M_BUL_CUR_FL='Y') or exists(select 1 from MUREXDB.TABLE#DATA#CURRENCY_DBF CCY3 where (substring(TRN.M_INSTRUMENT,1,3))= CCY3.M_LABEL and CCY3.M_BUL_CUR_FL='Y'))` |
| MX | COM Payment | `PAY_COMMODITY_VIEW` |
| MX | SG MY Wealth Management Payment | `PAY.M_PORTFOLIO in (select T1.M_REF from MUREXDB.TRN_PFLD_DBF T1 where M_LABEL in ('CMWM_COMBTB_SAC','CMWM_COMBTB_SDB','CB_COMMOSCB_ACU','CB_COMMOSCB_DBU','WM_MY_COMM'))` |

## Murex status and acknowledgement model

The stated Murex lifecycle for a newly eligible cashflow is:

```text
INIT → SNTR → RLSR
```

`SNTR` indicates dispatch to RATAN or “CashPlatform”; `RLSR` follows release from RATAN. For every outbound cashflow, RATAN is expected to return an ACK. Murex should retain the RATAN ID, ACK timestamp, and UDF value `Ratan acknowledged`. An ACK timeout should create a technical exception.

Amendments do not modify a previously sent cashflow in place. Murex retains the original `SNTR` or `RLSR` cashflow and creates reversal and replacement cashflows in `INIT`, which are separately routed when eligible. See [[murex-cashflow-status-lifecycle]].

## Migration control

The planned control requires three matching extracts:

```text
Extraction 1: RATAN-eligible Murex cashflows expected to be sent
Extraction 2: Post-migration Murex cashflows in SNTR/RLSR
Extraction 3: RATAN cashflows received from Murex
Expected result: Extractions 1, 2, and 3 match
```

The source marks this approach as requiring review and inclusion in the migration runbook. See [[murex-ratan-migration-reconciliation]].

## Report ownership impacts

| Owner | Report Name | Current Logic | Proposed target or unresolved point |
| --- | --- | --- | --- |
| EBBS | `CNYYYYMMDD0001Req.TXT` | `(STATUS="SENT".OR.STATUS="PEND")` | Generated from Razor. |
| ASPIRE | `MXG_PAYMENTTRANSACTION.csv` | `M_PF_STATUS IN ('SENT','PEND')` or `M_PF_STATUS = 'RLSD'` | PAYMENT BCDF generated from Razor. |
| TLM | `MUREX_TLM_NOS_GB_NEW_YYYYMMDD.dat` | `M_STATUS IN ('RLSD', 'SENT','PEND')` | Murex continues for precious metals; RATAN EOD is proposed for FMRP enrichment. China applicability remains questioned. |
| CRRS | `SD_INT.csv` | `M_CNTRP<>'SGE/SHA' and portfolio under CHINA_ALL_ON` | RATAN EOD feed combines RATAN ONE non-PM and Murex PM data. |
| CCRS | `SD_XB.csv` | `M_ENTITY='SHANGHAI' and M_STATUS<>'CNCL'` | RATAN EOD feed combines RATAN ONE non-PM and Murex PM data. |
| Payment Operation | `EXT_PAY_ACT_OP.csv` | `M_O_CPU_DATE <= convert(datetime, convert(char(8), dateadd(day, -6, getdate()), 112))` | FMMIS report generated in RATAN ONE. |
| Payment Operation | `derivatives_settlements.csv` | `M_GROUP= 'GBL_DO_SET' and M_VALUE_DATE>=7` | No weekly user-download record identified. |
| Payment Operation | `EXT_PAY_FW_TAB.csv` | `PAY_FLOW_DBF` | FMMIS report generated in RATAN ONE. |

## Open design risks

The source leaves unresolved the identity of CashPlatform, NDS deliverable-leg routing, the control for past-value-date reversals, duplicate-payment prevention during amendment and trade migration, and final report ownership. The listed CPT and go-live issue register was still marked `OPEN`.
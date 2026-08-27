---
type: source
title: UK - Murex - RATAN Cashflow Feeding
authors: []
year: 2024
url: ""
venue: Internal functional requirement
created: 2026-08-24
updated: 2026-08-24
tags: [uk, murex-211, ratan, fmrp, cashflow, csv, batch-processing, integration]
related: [uk-murex-ratan-high-volume-cashflow-feeding, murex-ratan-batch-file-triplet, ratan-batch-ack-nack-gating, canonical-uk-murex-ratan-cashflow-id-format, authoritative-uk-batch-file-schema, ratan-payment-level-validation-errors-retried-and-reconciled, ratan-batch-acknowledgement-confirm, uk-business-day-holiday-calendar-murex-feeding]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/UK - Murex -  RATAN cashflow feeding.md"]
---
# UK - Murex - RATAN Cashflow Feeding

## Scope

This functional requirement specifies a UK-specific, high-volume cashflow feed from [[murex-211]] to [[ratan]] under the [[fmrp]] migration. It states that the existing CN/SG/IN/MY model is not suitable for UK payment volume.

The design separates cashflows into non-overlapping value-date horizons:

- Individual real-time MxML files: VD-1, VD, and VD+1 business day.
- Multi-payment CSV batch files: VD T+2 through T+7 business day.
- CSV processing excludes weekends, 12.25, and 01.01.

Batch publishing is proposed for GMT 00:00 to 19:00, pending confirmation by Ren, Eric Shiyi.

## Batch file protocol

Each batch has a date, a daily sequence number, and a Base-file payment count:

```text
FMRP_Murex_Payments_YYYYMMDD_XXX_Base.csv
FMRP_Murex_Payments_YYYYMMDD_XXX_Snapshot.csv
FMRP_Murex_Payments_YYYYMMDD_XXX_Completion_ZZZZ.csv
FMRP_Murex_Payments_YYYYMMDD_END.csv
```

- `YYYYMMDD` is the batch date.
- `XXX` is the intra-day sequence, for example `001`, `002`, or `010`.
- `ZZZZ` is the Base-file payment count used for reconciliation.
- `END.csv` indicates that all batches for the date have been published, including days with no batches.

See [[murex-ratan-batch-file-triplet]].

## Processing and response control

Murex cannot automatically regenerate a batch. Therefore, it must await a RATAN response before publishing the next batch:

```text
FMRP_Murex_Payments_YYYYMMDD_XXX_Ack.csv
FMRP_Murex_Payments_YYYYMMDD_XXX_Nack.csv
```

A missing RATAN response after 30 minutes puts processing on hold. [[murex-pss]] investigates timeout root causes; RATAN PSS raises NACK issues to Murex PSS. A file-level NACK stops subsequent batches, whereas payment-level validation errors should not stop the batch.

See [[ratan-batch-ack-nack-gating]] and [[ratan-pss]].

## File-level exception contract

| Category | Description | Exception code | RATAN behavior | Expected action |
| --- | --- | --- | --- | --- |
| File NACK | Completion file received but Base or Snapshot is missing | `BatchFileNotComplete` | Move received batch files to the error folder and send NACK | Murex replays the same file |
| File NACK | Completion-file count differs from Base-file count | `BatchReconError` | Move received batch files to the error folder and send NACK | Murex investigates and resends |
| File NACK | Column number or sequence is incorrect | `BatchFormatError` | Move received batch files to the error folder and send NACK | Murex investigates and resends |
| File NACK | Batch `001` received but the expected daily ending file is absent | `BatchDateNotEnd` | Hold batch `001` and wait for the ending file | Murex investigates and resends the ending file |
| No exception | Batch `001` received but batch `002` is absent | No exception stated | Repeatedly check whether `002_completion` has arrived | Not specified |
| Payment error | Missing mandatory value, invalid value, or Base payment absent from Snapshot | `PaymentValidationError` | TBC | TBC |

## Snapshot status handling

RATAN processes only `CNCL` and `SNTR` records from Snapshot files. `INIT` may appear in Snapshot files but is not processed by RATAN. The relationship between Base `STATUS`, Snapshot status, and the resulting RATAN lifecycle state remains incomplete.

## Batch field contract

| RATAN Fields | Derivation Logic | Mandatory? | Field Name in Mx Batch Report | Field Type in Murex DB | Sample Xpath in MXML | Sample Value in MXML | SameValue:MXML vs DB | DB Sample Value | Filed extraction in DB | DBValueGenerationApproach |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Cashflow.Cashflow_Id | Formula_CashflowID | Y | FLOW_ID | numeric(10,0) | /MxPayML/flowID | 107791234 | Y | 107791234 | pay.M_FLOW_ID, | |
|  |  | N | LTI_ID | numeric(10,0) | /MxPayML/linkedTradeID | 5741473.000000 | N | 5741473 | pay.M_LTI_ID, | |
|  |  | Y | TRN_LINK | numeric(10,0) | /MxPayML/transactionLinkID | 96137655.000000 | N | 96137655 | pay.M_TRN_LINK, | |
|  |  | Y | TRN_ID | numeric(10,0) | /MxPayML/transactionOriginID | 96137655.000000 | N | 96137655 | pay.M_TRN_ID, | |
|  |  | Y | TRN_REF | numeric(10,0) | /MxPayML/transactionID | 96137655.000000 | N | 96137655 | pay.M_TRN_REF, | |
|  |  | Y | AMOUNT | numeric(19,3) | /MxPayML/flowAmount | 3394.730000 | N | 3394.730 | pay.M_AMOUNT, | |
|  |  | N | CPU_TIME | numeric(8,0) | /MxPayML/computerTime | 09:24:31 | Y | 09:24:31 | convert(char(8),dateadd(ss,pay.M_CPU_TIME,pay.M_CPU_DATE),108)M_CPU_TIME, | ToFormulate for recon: char(8) |
|  |  | N | CPU_DATE | datetime | /MxPayML/computerDate | 20240729 | Y | 20240729 | convert(char(8),pay.M_CPU_DATE, 112) AS 'M_CPU_DATE', | ToFormulate for recon: char(8) |
|  |  | Y | STATUS | char(4) | /MxPayML/flowStatus | INIT | Y | INIT | pay.M_STATUS as 'M_STATUS', | Status of base flow ID (<>MXML:INIT) |
|  |  | Y | TRN_FMLY | char(5) | /MxPayML/transactionFamily | SCF | Y | SCF | rtrim(pay.M_TRN_FMLY)M_TRN_FMLY, | RTRIM |
|  |  | Y | TRN_GRP | char(5) | /MxPayML/transactionGroup | SCF | Y | SCF | rtrim(pay.M_TRN_GRP)M_TRN_GRP, | RTRIM |
|  |  | N | TRN_TYPE | char(5) | /MxPayML/transactionType | SCF | Y | SCF | rtrim(pay.M_TRN_TYPE)M_TRN_TYPE, | RTRIM |
|  |  | Y | ENTITY | char(10) | /MxPayML/entity | SDBU SING | Y | SDBU SING | rtrim(pay.M_ENTITY)M_ENTITY, | RTRIM |
|  |  | Y | CNTRP | char(15) | /MxPayML/counterparty | GUEC00HSHK/HKG | Y | GUEC00HSHK/HKG | rtrim(pay.M_CNTRP)M_CNTRP, | RTRIM |
|  |  | N | COMMENT | char(30) | /MxPayML/comment |  | Y |  | rtrim(pay.M_COMMENT) as 'M_COMMENT', | RTRIM |
|  |  | N | TYPOLOGY | char(20) | /MxPayML/transactionTypology | Premium | Y | Premium | rtrim(pay.M_TYPOLOGY)M_TYPOLOGY, | RTRIM |
|  |  | Y | CREDIT | char(1) | /MxPayML/isCredit | Y | Y | Y | case when pay.M_CREDIT = 'C' then 'Y' else 'N' end as 'M_CREDIT', | ToFormulate |
|  |  | Y | VALUE_DATE | datetime | /MxPayML/valueDate | 20240731 | Y | 20240731 | convert(char(8),pay.M_VALUE_DATE, 112) AS 'M_VALUE_DATE', | ToFormulate for recon: char(8) |
|  |  | Y | CURRENCY | char(3) | /MxPayML/currency | USD | Y | USD | rtrim(pay.M_CURRENCY)M_CURRENCY, | RTRIM |
|  |  | N | STRATEGY | char(15) | /MxPayML/strategy | FX_TRF | Y | FX_TRF | rtrim(pay.M_STRATEGY)M_STRATEGY, | RTRIM |
|  |  | Y | LABEL | char(15) | /MxPayML/portfolio | PAE_T24_TRFDM_S | Y | PAE_T24_TRFDM_S | rtrim(port.M_LABEL)M_LABEL, | RTRIM |
|  |  | Y | INST_TYPE | char(5) | /MxPayML/type | Cash | Y | Cash | case when pay.M_INST_TYPE = 0 then 'Cash' when pay.M_INST_TYPE = 1 then 'DVP' when pay.M_INST_TYPE = 2 then 'FOP' when pay.M_INST_TYPE = 3 then 'CashR' end as M_INST_TYPE, | ToFormulate |
|  |  | N | FLOW_TYPE0 | char(4) | /MxPayML/flowType/flowType0 |  | Y |  | rtrim(pay.M_FLOW_TYPE0)M_FLOW_TYPE0, | RTRIM |
|  |  | N | FLOW_TYPE1 | char(4) | /MxPayML/flowType/flowType1 |  | Y |  | rtrim(pay.M_FLOW_TYPE1)M_FLOW_TYPE1, | RTRIM |
|  |  | N | FLOW_TYPE2 | char(4) | /MxPayML/flowType/flowType2 |  | Y |  | rtrim(pay.M_FLOW_TYPE2)M_FLOW_TYPE2, | RTRIM |
|  |  | N | FLOW_TYPE3 | char(4) | /MxPayML/flowType/flowType3 |  | Y |  | rtrim(pay.M_FLOW_TYPE3)M_FLOW_TYPE3, | RTRIM |
|  |  | N | FLOW_TYPE4 | char(4) | /MxPayML/flowType/flowType4 | INT | Y | INT | rtrim(pay.M_FLOW_TYPE4)M_FLOW_TYPE4, | RTRIM |
|  |  | N | COM_FLOW | numeric(1,0) | /MxPayML/flowUserDefinedFields/userDefinedField/fieldLabel/@COM_FLOW | 0 | Y | 0 | payudf.M_COM_FLOW, | |
|  |  | N | NID | numeric(15,0) | /MxPayML/flowUserDefinedFields/userDefinedField/fieldLabel/@NID | 0 | y | 0 | payudf.M_NID, | |
|  |  | Y | SID | numeric(15,0) | /MxPayML/flowUserDefinedFields/userDefinedField/fieldLabel/@SID | 5741469 | Y | 5741469 | payudf.M_SID, | |
|  |  | N | X_DUMMY1 | numeric(19,3) | /MxPayML/flowUserDefinedFields/userDefinedField/fieldLabel/@X_DUMMY1 | 3394.73 | N | 3394.730 | payudf.M_X_DUMMY1, | |
|  |  | N | X_DUMMY2 | numeric(1,0) | /MxPayML/flowUserDefinedFields/userDefinedField/fieldLabel/@X_DUMMY2 | 0 | Y | 0 | payudf.M_X_DUMMY2, | |
|  |  | N | X_DUMMY3 | numeric(1,0) | /MxPayML/flowUserDefinedFields/userDefinedField/fieldLabel/@X_DUMMY3 | 0 | Y | 0 | payudf.M_X_DUMMY3, | |
|  |  | N | X_DUMMY4 | numeric(1,0) | /MxPayML/flowUserDefinedFields/userDefinedField/fieldLabel/@X_DUMMY4 | 0 | Y | 0 | payudf.M_X_DUMMY4, | |
|  |  | N | TRN_DATE | datetime | /MxPayML/tradeDate | 20240729 | Y | 20240729 | convert(char(8),trade.M_TRN_DATE, 112) AS 'M_TRN_DATE', | ToFormulate for recon: char(8) |
|  |  | Y | PUB_DATE_T | datetime | /MxPayML/scbExtraInfoBlock/publicationDateTime | 20-08-2024 08:32:54:550 | N | 30-08-2024 07:22:33:520 | rtrim(convert(char(10),getdate(),105)) + ' ' + rtrim(convert(char(12),getdate(),20)) as 'M_PUB_DATE_T', | ToFormulate for recon: char(23) |
|  |  | N | VAL_STATUS | char(4) | /MxPayML/scbExtraInfoBlock/validationLevel | VALD | Y | VALD | trade.M_VAL_STATUS, | |
|  |  | Y | LEID | char(10) | /MxPayML/scbExtraInfoBlock/entityFMID | 400451508 | Y | 400451508 | case when entity.M_ATLAS_LEID = null then '0' else entity.M_ATLAS_LEID end as 'M_LEID', | ToFormulate |
|  |  | Y | SCI_ID | char(10) | /MxPayML/scbExtraInfoBlock/entityLEID | 12921313 | Y | 12921313 | case when entity.M_SCI_ID = null then '0' else entity.M_SCI_ID end as 'M_SCI_ID', | ToFormulate |
|  |  | Y | ATLAS_LEID | char(10) | /MxPayML/scbExtraInfoBlock/counterpartyFMID | 400949160 | Y | 400949160 | case when cpty.M_ATLAS_LEID = null then '0' else cpty.M_ATLAS_LEID end as 'M_ATLAS_LEID', | ToFormulate |
|  |  | Y | L_CODE | char(20) | /MxPayML/scbExtraInfoBlock/traderID | SYSTEMID | Y | SYSTEMID | rtrim(psid.M_L_CODE) as 'M_L_CODE', | RTRIM |
|  |  | N | BIZ_UNIT | char(30) | /MxPayML/scbExtraInfoBlock/portBizUnit | WM - FX | Y | WM - FX | rtrim(portudf.M_BIZ_UNIT) as 'M_BIZ_UNIT', | RTRIM |
|  |  | N | AMD_FLAG | char(1) | /MxPayML/scbExtraInfoBlock/amendmentFlag | N | Y | N | CASE WHEN EXISTS (SELECT 1 from MKT_OP_DBF mop where M_DEST_NB=pay.M_TRN_REF and (M_TYPE='RPL' or M_TYPE='RPL_M') and mop.M_SYS_DATE = pay.M_SYS_DATE) then 'Y' else 'N' end as 'M_AMD_FLAG', | ToFormulate |
|  |  | N | DATE | datetime | /MxPayML/scbExtraInfoBlock/mxSystemDate | 20240725 | N | 20240801 | convert(char(8),sysdate.M_DATE, 112) AS 'M_DATE', | ToFormulate for recon: char(8) |
|  |  | N | ACTION | char(10) | /MxPayML/scbExtraInfoBlock/action | INS | Y | INS | rtrim (pay.M_ACTION) as 'M_ACTION', | RTRIM |
|  |  | N | MOP_LAST | char(5) | /MxPayML/scbExtraInfoBlock/tradeLastMKT | EXP | Y | EXP | rtrim(case when trade.M_MOP_LAST = 1 then 'EXR' when trade.M_MOP_LAST = 2 then 'EXP' when trade.M_MOP_LAST = 3 then 'XIT' when trade.M_MOP_LAST = 4 then 'NET' when trade.M_MOP_LAST = 5 then 'RPL' when trade.M_MOP_LAST = 6 then 'RPL_M' when trade.M_MOP_LAST = 7 then 'RPL_D' when trade.M_MOP_LAST = 0 then '' end) as M_MOP_LAST, | ToFormulate |
|  |  | N | CREATOR | char(10) | /MxPayML/scbExtraInfoBlock/TrnParentID | 0 | Y | 0 | convert(varchar(10), trade.M_CREATOR) 'M_CREATOR', | ToFormulate |
|  |  | Y | TRN_ORGID | char(10) | /MxPayML/scbExtraInfoBlock/TrnOrginalID | 96137655 | Y | 96137655 | convert(varchar(10), CASE WHEN trade.M_MRPL_ONB<1 THEN trade.M_NB ELSE trade.M_MRPL_ONB END) 'M_TRN_ORGID', | ToFormulate |
|  |  | N | WAIT_FIX | char(1) | /MxPayML/scbExtraInfoBlock/isWaitingFixing | N | Y | N | CASE WHEN EXISTS (select pay.M_FLOW_ID from EST_FMRP_DBF EST, FXNG_DBF F where pay.M_TRN_REF = EST.M_NB and pay.M_VALUE_DATE = EST.M_F_VALUE and pay.M_CURRENCY=EST.M_F_CURRENCY and F.M_TRN_NUMBER = EST.M_NB and F.M_CALC_END = EST. M_F_CCFRMCD2 and F.M_LEG = EST. M_F_LEG and F.M_FIRST_FXNG = 0) THEN 'Y' ELSE 'N' END AS 'M_WAIT_FIX' | To Calculate |

## Cashflow ID formula

```java
Set prefix = ' M0'
-- Init the prefix
--get payment flow id from MxML or batch file
murexFlowId=getMxML('/MxPayML/flowID')
--e.g. the flow id is '87755146'
If the length(murexFlowId) <10 then murexFlowId = '0' + murexFlowId
-- e.g. if the murexFlowId length is 8 then we need to add '00' as prefix.
-- Concact the prefix with the murexFlowId
murexFlowId= prefix + murexFlowId
-- if muurex sent the flow aid as 87755146, then the final cashflow id would be M00087755146
```

## Material unresolved items

- `Cashflow.Cashflow_Id` is listed as `numeric(10,0)` but the formula produces an `M`-prefixed identifier.
- Padding behavior, the leading space in `' M0'`, and the intended identifier length are ambiguous.
- `LEID`, `SCI_ID`, and `ATLAS_LEID` formulas use `= null`, which does not provide intended null handling in standard SQL.
- `PUB_DATE_T` compares an MxML publication timestamp with a `getdate()` extraction timestamp.
- The formal CSV schema does not specify delimiter, encoding, quoting, headers, line endings, precision, or timezone.
- ACK meaning, duplicate/replay handling, late and out-of-order files, and missing-sequence handling are not defined.
- Payment-level error lifecycle, correction, retry, reporting, and reconciliation are TBC.
- The UK business-day calendar and the batch publication window need confirmation.
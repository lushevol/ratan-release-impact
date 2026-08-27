---
type: source
title: CN Settlement - Murex 2.11 Workflow Change-0118
created: 2026-08-24
updated: 2026-08-24
tags: [murex-211, fmrp, ratan, cashflow-integration, workflow-configuration, historical]
related: [fmrp, murex-211, scb-fmrp-dbf, fmrp-murex-cashflow-status-synchronization, fmrp-payment-insertion-eligibility, fmrp-outbound-cashflow-enrichment, fmrp-retry-and-purge-policy, ratan-murex-211-cashflow-integration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Murex 2.11 workflow change/CN Settlement - Murex 2.11 workflow change-0118.md"]
authors: [Lyn]
year: 2023
url: ""
venue: "Internal functional requirement"
---
# CN Settlement - Murex 2.11 Workflow Change-0118

This January 2023 implementation document records Murex 2.11 workflow and formula changes for FMRP/RATAN cashflow integration. It covers external-settlement routing, `SCB_FMRP_DBF` status persistence, message enrichment, MQ transport, payment-insertion filtering, retry handling, and inbound acknowledgements.

The document contains an explicit update dated 17 January 2023. That update supersedes the earlier direct `docPayment → INIT2SNTR` insertion link and removes the legacy inbound-acknowledgement implementation. Earlier task and link definitions should therefore be treated as historical unless retained by the revision.

## Final revision implications

Under RATAN-11101:

- The direct `docPayment → INIT2SNTR` link is deleted.
- `PayInsertionFilter` becomes the insertion decision point.
- `process` routes to `SNTR`; `discard` routes to `FmrpPurge`.
- Eligibility requires an entity configured in `FMRP_ENTITY_DBF` and no precious-metal flow for the same trade reference.

Under RATAN-10822:

- `FmrpAckRouter`, `msgRouter`, `razorID`, `razorAckVald`, and `recordCount` are deleted.
- Replacement formulas and tasks are named but not defined in this source.
- The final acknowledgement state model cannot be determined from the available material.

## External-settlement routing

`client.scb.fmrp.ExtSettleRouter` routes selected payment actions to FMRP while retaining MLS routing for other actions.

```xml
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <xsl:variable name="action" select="/MxPayML/action"></xsl:variable>
        <xsl:choose>
            <xsl:when test="$action='RI2C' or $action='MCXI' or $action='MIXC'">mls</xsl:when>
            <xsl:when test="$action='FAIS' or $action='FMIS' or $action='FMSI' or $action='I2SR'">fmrp</xsl:when>
        </xsl:choose>
    </xsl:template>
</xsl:stylesheet>
```

The historical workflow was:

```text
docPayment
  ├─ extSettle → extSettleRouter
  │                ├─ fmrp → FmrpFilter → FmrpSettleEnrichment
  │                │                         → FmrpSettleFilter → FmrpOutboundMQ
  │                └─ mls → PaymentMLSOUTboundRouter
  └─ insert → INIT2SNTR
```

The revised insertion workflow is:

```text
docPayment → PayInsertionFilter
  ├─ process → SNTR
  └─ discard → FmrpPurge
```

## FMRP status persistence

[[scb-fmrp-dbf]] stores Murex flow identifiers, integration status, RATAN identifiers, and timestamps. The legacy `client.scb.fmrp.SyncStatus` configuration uses `INIT`, `SENT`, and `CANC` as status values.

```sql
select count(1) 
from SCB_FMRP_DBF
WHERE M_STATUS='MxCTX#STATUS#Mx'
and   M_FLOW_ID=MxCTX#FLOW_ID#Mx
```

```sql
select count(1) 
from SCB_FMRP_DBF
WHERE M_FLOW_ID=MxCTX#FLOW_ID#Mx
```

```sql
declare @publish   CHAR(20)
begin
UPDATE SCB_FMRP_DBF
SET M_STATUS='SENT'
WHERE M_STATUS='MxCTX#STATUS#Mx'
and   M_FLOW_ID=MxCTX#FLOW_ID#Mx
select 'out[STPDOC_DATA_TYPE2=publish]'
end
```

```sql
declare @publish   CHAR(20)
begin
UPDATE SCB_FMRP_DBF
SET M_STATUS='CANC'
WHERE M_STATUS='SENT'
and   M_FLOW_ID=MxCTX#FLOW_ID#Mx
select 'discard[STPDOC_DATA_TYPE2=cancel]'
end
```

```sql
begin    
insert into  MUREXDB.SCB_FMRP_DBF(M_FLOW_ID,M_STATUS,M_RATAN_ID,M_INS_DATETIME)
values (MxCTX#FLOW_ID#Mx ,'SENT',0,  GETDATE())
select 'out[STPDOC_DATA_TYPE2=publish]'
end
```

The document does not provide table DDL, a uniqueness constraint, transaction boundaries, or concurrency controls for `M_FLOW_ID`.

## Outbound enrichment

`client.scb.fmrp.fmrpEnrich` adds the following block to outbound `MxPayML`.

```xml
<scbExtraInfoBlock>
  <publicationDateTime>...</publicationDateTime>
  <validationLevel>...</validationLevel>
  <entityFMID>...</entityFMID>
  <entityLEID>...</entityLEID>
  <counterpartyFMID>...</counterpartyFMID>
  <traderID>...</traderID>
  <portBizUnit>...</portBizUnit>
  <amendmentFlag>...</amendmentFlag>
</scbExtraInfoBlock>
```

```sql
select        rtrim(M_ATLAS_LEID ) 'LEID', rtrim(M_SCI_ID) 'SCIID'
from    TABLE#DATA#COUNTERP_DBF c,
            TABLE#DATA#ENTITY_DBF e 
where  c.M_LABEL = e.M_CTP_COD
and e.M_LABEL = 'MxCTX#NAME#Mx'
```

```sql
select top 1 rtrim(M_L_CODE)  from TRN_USRD_DBF WHERE M_LABEL ='Mx#client.scb.fmrp.trader#Mx'
```

```sql
select CASE WHEN M_COMMENT_BS = 'B' THEN rtrim(M_BTRADER) ELSE rtrim(M_STRADER) END from TRN_HDR_DBF WHERE M_NB=Mx#client.scb.pay.trade.tradeid#Mx
```

```sql
select rtrim(convert(CHAR,getdate(),105)) + ' ' + rtrim(convert(CHAR,getdate(),20))
```

```sql
select count(1) 
 from MKT_OP_DBF 
where M_DEST_NB=MxCTX#tradeRef#Mx and (M_TYPE='RPL' or M_TYPE='RPL_M') and M_SYS_DATE = 'MxCTX#sysDate#Mx'
```

```sql
select top 1 rtrim(M_BIZ_UNIT) from TABLE#DATA#PORTFOLI_DBF WHERE M_LABEL ='Mx#client.scb.pay.flow.portfolio#Mx'
```

The labels in the transformation map `M_ATLAS_LEID` to `entityFMID` and `M_SCI_ID` to `entityLEID`. The source does not establish whether this naming is contractually intentional.

## Payment-insertion eligibility

`PayInsertionFilter` discards a payment if its entity is not FMRP-enabled or if its trade contains a precious-metal flow.

```xml
<Operator Code="If">
	<Operator Code="Or">
		<Operator Code="Equal">
			<Operand Code="ScalarString">Mx#client.scb.fmrp.isFmrpEntity#Mx</Operand>
			<Operand Code="ScalarString">N</Operand>
		</Operator>
		<Operator Code="Equal">
			<Operand Code="ScalarString">Mx#client.scb.fmrp.isPreciousMetalDealFlow#Mx</Operand>
			<Operand Code="ScalarString">Y</Operand>
		</Operator>
	</Operator>
	<Operand Code="ScalarString">discard</Operand>
	<Operand Code="ScalarString">process</Operand>
</Operator>
```

```sql
select count(1) 
from FMRP_ENTITY_DBF
where M_ENTITY = 'MxCTX#entity#Mx'
```

```sql
SELECT count(*)
FROM PAY_FLOW_DBF T
WHERE EXISTS( select 1 from PAY_FLOW_DBF A
INNER JOIN TABLE#DATA#CURRENCY_DBF B ON A.M_CURRENCY = B.M_LABEL
WHERE A.M_TRN_REF = T.M_TRN_REF
AND B.M_BUL_CUR_FL='Y')
AND T.M_FLOW_ID  = MxCTX#flowID#Mx
```

This is a trade-level exclusion: one precious-metal leg excludes every payment flow that shares its `M_TRN_REF`.

## Retry and purge

The retry counter is stored in `STPDOC_DATA_TYPE3`. An empty value becomes `1`; a populated value is incremented. Retries continue only while the count is below `3`; otherwise the message is stopped and linked to `FmrpPurge`.

```xml
<Operator Code="If">
    <Operator Code="Or">
        <Operator Code="Equal">
            <Operand Code="ScalarField">STPDOC_DATA_TYPE3</Operand>
            <Operand Code="ScalarString"></Operand>
        </Operator>
        <Operator Code="LessThan">
            <Operator Code="StringToDouble">
                <Operand Code="ScalarField">STPDOC_DATA_TYPE3</Operand>
            </Operator>
            <Operand Code="ScalarDouble">3.0</Operand>
        </Operator>
    </Operator>
    <Operand Code="ScalarString">retry[STPDOC_DATA_TYPE3=Mx#client.scb.fmrp.retryCnt#Mx]</Operand>
    <Operand Code="ScalarString">stop</Operand>
</Operator>
```

```xml
<Operator Code="If">
	<Operator Code="Equal">
		<Operand Code="ScalarField">STPDOC_DATA_TYPE3</Operand>
		<Operand Code="ScalarString"/>
	</Operator>
	<Operand Code="ScalarDouble">1</Operand>
	<Operator Code="Plus">
		<Operator Code="StringToDouble">
			<Operand Code="ScalarField">STPDOC_DATA_TYPE3</Operand>
		</Operator>
		<Operand Code="ScalarDouble">1</Operand>
	</Operator>
</Operator>
```

No dead-letter queue, alerting, retry delay, audit retention, or remediation owner is specified.

## Historical MQ configuration

The following configuration is historical and explicitly UAT-labelled for outbound traffic; it is not evidence of current production endpoints.

| Task | Host | Port | Channel | Queue manager | Queue | User |
|---|---:|---:|---|---|---|---|
| `FmrpOutboundMQ` | `10.198.198.93` | `8212` | `UKMXGCLNTS2` | `UKFM02S1` | `GM.MXG.MLS.FEDS.UAT` | `ukmxgmq` |
| `FmrpInboundMQ` | `10.193.106.152` | `1414` | `UKMXGCLNTS1` | `UKIG01S2` | `GMPCI.MLS.MXG.RQSTIN` | `ukmxgmq` |

Inbound document metadata was configured as:

| Field | Value |
|---|---|
| `STPDOC_ACTION` | `ACK_ALLEGE` |
| `STPDOC_DATA_TYPE1` | `RATAN_CASHFLOW` |
| `STPDOC_DATA_TYPE2` | `client.scb.fmrp.inbound.razorID` |
| `STPDOC_DATA_TYPE3` | `client.scb.fmrp.inbound.murexID` |
| `STPDOC_REF` | `client.scb.fmrp.inbound.murexID` |
| `STPDOC_REF_TYPE` | `PAYMENT` |
| `STPDOC_CONTENT_TYPE` | `RES.XML` |
| `STPDOC_TEMPLATE_GRAMMAR` | `mlspayml.dtd` |
| `XMLFLOW_TYPE` | `UserDefined` |

## Superseded acknowledgement logic

The removed legacy implementation updated matching records to `MATH`, populated `M_RATAN_ID` from `razorID`, and recorded receipt time.

```sql
begin
if len('Mx#client.scb.fmrp.inbound.razorAckVald#Mx')>1
    begin
            update  SCB_FMRP_DBF
            set M_STATUS='MATH',M_RATAN_ID=Mx#client.scb.fmrp.inbound.razorID#Mx, M_REC_DATETIME=GETDATE()
            where  M_FLOW_ID IN (Mx#client.scb.fmrp.inbound.murexID#Mx)
    select  'success'
    end
else 
    begin
            select  'discard'
    end
end
```

RATAN-10822 replaces that implementation with `FmrpInboundRouter`, `SNTR2RLSR`, `FmrpAckProcessor`, `FmrpReleaseProcessor`, and new formulas. Their definitions are absent. See [[what-replaced-the-legacy-fmrp-inbound-acknowledgement-status-model]].
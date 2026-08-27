---
type: source
title: CN Settlement — Murex 2.11 Workflow Change
authors: []
year: 2023
url: ""
venue: "Cash Settlement Home Page functional requirement"
tags: [cash-settlement, murex-211, fmrp, ratan, mls, workflow, mq-integration]
related: [murex-211, fmrp, ratan-10123, fmrp-murex-211-settlement-workflow, fmrp-cashflow-status-synchronization, ratan-cashflow-acknowledgement-and-release-processing, scb-fmrp-dbf, fmrp-outbound-mq, fmrp-inbound-mq]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Murex 2.11 workflow change/CN Settlement - Murex 2.11 workflow change-0130.md"]
---

# CN Settlement — Murex 2.11 Workflow Change

## Scope

This functional and configuration specification documents changes to the CN Settlement payment workflow for Murex 2.11 cashflows. The change separates ordinary payment insertion from external settlement routing, introduces an FMRP route alongside the existing MLS route, adds outbound and inbound MQ integration, synchronizes FMRP statuses in `SCB_FMRP_DBF`, and provides bounded retry handling.

The source also records a later update dated 2023-01-17. That update supersedes the initial inbound acknowledgement design by replacing `FmrpAckRouter` with specialized inbound routing and processing tasks.

## Workflow topology

The initial outbound topology is:

```text
docPayment
  ├─ insert → INIT2SNTR
  └─ extSettle → extSettleRouter
                    ├─ fmrp → FmrpFilter
                    │            └─ FmrpSettleEnrichment
                    │                 └─ FmrpSettleFilter
                    │                      └─ FmrpOutboundMQ
                    └─ mls → PaymentMLSOUTboundRouter
```

The retry path is:

```text
INIT2SNTR
  ├─ Triggered → FmrpPurge
  └─ Error → FmrpRemoveError → FmrpRetryCheck
                                  ├─ stop → FmrpPurge
                                  └─ retry → INIT2SNTR
```

The initial inbound link was:

```text
FmrpInboundMQ → FmrpAckRouter
```

The 2023-01-17 update deletes `FmrpAckRouter` and creates:

```text
FmrpInboundMQ
  └─ FmrpInboundRouter
       ├─ acknowledged → FmrpAckProcessor
       └─ released → FmrpReleaseProcessor
```

The update also introduces `SNTR2RLSR` and moves payment insertion behind `PayInsertionFilter`.

## Action-based external settlement routing

`client.scb.fmrp.ExtSettleRouter` maps Murex actions to settlement branches:

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

The MLS route handles `RI2C`, `MCXI`, and `MIXC`. The FMRP route handles `FAIS`, `FMIS`, `FMSI`, and `I2SR`. There is no explicit fallback branch for an unrecognized or empty action.

## FMRP status formulas

The source uses the following checks against `SCB_FMRP_DBF`:

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

The update, cancellation, and insertion formulas are:

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

## Payment enrichment

`client.scb.fmrp.fmrpEnrich` copies the Murex payment XML and appends an `scbExtraInfoBlock`:

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

The values are derived from Murex formulas and static data. Entity identifiers come from `client.scb.fmrp.LEIDandSCIIDMatrix`, counterparty identification comes from `client.scb.tds.common.getLEID`, trader identification comes from `TRN_USRD_DBF`, portfolio business unit comes from `TABLE#DATA#PORTFOLI_DBF`, and amendment status is based on same-day replacement records in `MKT_OP_DBF`.

## MQ configuration

The documented outbound MQ configuration is:

```text
Host: 10.198.198.93
Port: 8212
Channel: UKMXGCLNTS2
Queue manager: UKFM02S1
Queue: GM.MXG.MLS.FEDS.UAT
User: ukmxgmq
```

The documented inbound MQ configuration is:

```text
Host: 10.193.106.152
Port: 1414
Channel: UKMXGCLNTS1
Queue manager: UKIG01S2
Queue: GMPCI.MLS.MXG.RQSTIN
User: ukmxgmq
```

The queue names contain `MLS`, although the surrounding workflow is described as FMRP/RATAN integration. The source does not establish whether this reflects legacy naming, shared transport, or MLS ownership.

## Retry control

`client.scb.fmrp.retryCheck` retries while `STPDOC_DATA_TYPE3` is empty or less than `3.0`:

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

The counter starts at `1` when empty and otherwise increments by one.

## Inbound RATAN validation and synchronization

Inbound routing accepts only messages satisfying all of these conditions:

- `sourceSystem` is `RATAN`.
- `objectNature` is `cashflow`.
- The Murex flow ID is greater than zero.
- The message is `RATAN Acknowledged` or `RATAN Released`.

```xml
<xsl:choose>
    <xsl:when test="$sourceSystem='RATAN' and $objectNature='cashflow' and $murexID>0 and $ratanMsgType='RATAN Acknowledged'">acked</xsl:when>
    <xsl:when test="$sourceSystem='RATAN' and $objectNature='cashflow' and $murexID>0 and $ratanMsgType='RATAN Released'">released</xsl:when>
    <xsl:otherwise>discard</xsl:otherwise>
</xsl:choose>
```

The acknowledgement update is:

```sql
begin
    update SCB_FMRP_DBF
    set M_RATAN_ID='MxCTX#ratanID#Mx', M_REC_DATETIME=convert(datetime,'MxCTX#ratanTimestamp#Mx')
    where M_FLOW_ID = MxCTX#murexID#Mx
    update TABLE#DATA#PAYFLOW_DBF
    set M_REASONS='MxCTX#ratanMsgType#Mx'+' '+'MxCTX#ratanID#Mx'
    where M_FLOW_ID = MxCTX#murexID#Mx
    select 'success'
end 
```

The release update is:

```sql
begin
update SCB_FMRP_DBF
set M_STATUS='MATH'
where M_FLOW_ID = Mx#client.scb.fmrp.inbound.murexID#Mx
select 'success'
end    
```

## Inbound insertion filters

A flow is discarded when its entity is not configured in `FMRP_ENTITY_DBF` or when it is associated with a precious-metal currency:

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

Entity eligibility is checked with:

```sql
select count(1) 
from FMRP_ENTITY_DBF
where M_ENTITY = 'MxCTX#entity#Mx'
```

Precious-metal detection is based on currency static data:

```sql
SELECT count(*)
FROM PAY_FLOW_DBF T
WHERE EXISTS( select 1 from PAY_FLOW_DBF A
INNER JOIN TABLE#DATA#CURRENCY_DBF B ON A.M_CURRENCY = B.M_LABEL
WHERE A.M_TRN_REF = T.M_TRN_REF
AND B.M_BUL_CUR_FL='Y')
AND T.M_FLOW_ID  = MxCTX#flowID#Mx
```

## Change history and qualification

The 2023-01-17 update records changes associated with `RATAN-11101` and `RATAN-10822`. It updates payment-routing formulas, deletes `client.scb.fmrp.fmrpPortfolioCheck`, creates entity and payment-insertion formulas, removes the direct `docPayment → INIT2SNTR` link, and replaces the original inbound acknowledgement task.

The source contains duplicate definitions of `client.scb.fmrp.inbound.inboundRouter` and several naming inconsistencies, including `fmrpPrecioiusMetalCheck`, references to `FRMP`, and an inbound `razorID` field later removed by the update. These are retained as source evidence and require configuration verification before implementation assumptions are made.
---
type: source
title: CN Settlement — Murex 2.11 Workflow Change
authors: []
year: 2023
url: ""
venue: "Cash Settlement Home Page — Functional Requirement — Surrounding System Integration"
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, Murex-2-11, RATAN, FMRP, payment-workflow, IBM-MQ]
related: [fmrp, murex-211, ratan-10123, fmrp-cashflow-publication-lifecycle, fmrp-payment-eligibility-and-suppression, murex-ratan-cashflow-message-contract, cashflow-suppression-rules, netting-eligibility-static-data]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Murex 2.11 workflow change.md"]
---
# CN Settlement — Murex 2.11 Workflow Change

## Purpose and scope

This source specifies a Murex 2.11 payment-workflow change for publishing eligible FMRP cashflows to RATAN and processing RATAN acknowledgements and release messages. The implementation uses Murex XSL, XSLTREE, XMLF, and SQL formulas, payment actions, timers, persistence updates, and IBM MQ tasks.

The document describes configuration intent. It does not provide test results, deployment confirmation, production-readiness evidence, or operational monitoring evidence.

## Workflow architecture

The payment workflow changes `docPayment` by adding `insert` and `extSettle` nodes and removing the `mls` node. `extSettleRouter` routes external settlement actions as follows:

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

`client.scb.mls.cpnEligible` recognizes both existing CPN transitions and FMRP transitions:

- `INIT` to `CNET`
- `CNET` to `INIT`
- `INIT` to `SNTR`
- `SNTR` to `INIT`

The main outbound tasks are `FmrpFilter`, `FmrpSettleEnrichment`, `FmrpSettleFilter`, `FmrpOutboundMQ`, and `FmrpPub`. The inbound path uses `FmrpInboundMQ`, `FmrpInboundRouter`, `FmrpAckProcessor`, `FlowEntrySpliter`, `SNTR2RLSR`, `FmrpReleaseProcessor`, `ReleaseAckEnrichment`, and `FmrpOutboundMQ2`.

## Outbound lifecycle

`client.scb.fmrp.SyncStatus` examines the payment action and the existing `SCB_FMRP_DBF` record:

- `FAIS`, `I2SR`, or `FMIS` with an `INIT` record updates the record to `SENT` and publishes.
- `FMSI` with a `SENT` record changes the record to `CANC` and discards the message from publication.
- `FMIS` with a `CANC` record updates it to `SENT` and publishes, supporting replay.
- `FMIS` or `I2SR` with no existing record inserts a new `SENT` record and publishes.
- Other combinations are discarded.

The persistence statements are:

```sql
begin   
insert into  MUREXDB.SCB_FMRP_DBF(M_FLOW_ID,M_STATUS,M_RATAN_ID,M_RATAN_NET_ID,M_INS_DATETIME)
values (MxCTX#FLOW_ID#Mx ,'SENT','0','0', GETDATE())
select 'out[STPDOC_DATA_TYPE2=publish]'
end
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

After publication, `client.scb.fmrp.updatePubDate` records the publication timestamp:

```sql
begin
UPDATE  MUREXDB.SCB_FMRP_DBF
SET M_PUB_DATETIME=getdate()
WHERE M_FLOW_ID=MxCTX#FLOW_ID#Mx
select 'out'
end
```

## Eligibility and suppression

`client.scb.fmrp.inbound.payInsertionFilter` discards a flow when any static-data condition fails:

- The payment entity is absent from `FMRP_ENTITY_DBF`.
- The currency is non-deliverable.
- The payment amount is zero.

For trade-related flows, it additionally suppresses flows identified as precious-metal deals, disallowed by the FXD suppression check, or matching the literal CPT formula result `Y`.

For non-trade-related flows, an empty or numerically low `STPDOC_DATA_TYPE2` value causes retry; otherwise the flow is discarded.

The entity check is:

```sql
select count(1) 
from FMRP_ENTITY_DBF
where M_ENTITY = 'MxCTX#entity#Mx'
```

The non-deliverable currency check is:

```sql
select count(1) 
from MUREXDB.TABLE#DATA#CURRENCY_DBF
where M_LABEL = 'MxCTX#ccy#Mx'
AND M_NDF_CCY='Y'
```

The literal CPT logic is potentially counterintuitive:

```xml
<xsl:choose>
    <xsl:when test="$isCPTeligible = 0">Y</xsl:when>
    <xsl:otherwise>N</xsl:otherwise>
</xsl:choose>
```

`payInsertionFilter` discards when `isCPT='Y'`, meaning that no matching `fmrp_test` record causes suppression under the supplied formulas. This requires business confirmation.

## Outbound message enrichment

`client.scb.fmrp.fmrpEnrich` adds `scbExtraInfoBlock` to `MxPayML`. The block contains:

- `publicationDateTime`
- `validationLevel`
- `entityFMID`
- `entityLEID`
- `counterpartyFMID`
- `traderID`
- `portBizUnit`
- `amendmentFlag`
- `mxSystemDate`
- `action`
- `tradeLastMKT`
- `TrnParentID`
- `TrnOrginalID`
- `Flows`

`tradeLastMKT` maps values `1` through `7` to `EXR`, `EXP`, `XIT`, `NET`, `RPL`, `RPL_M`, and `RPL_D`. `Flows` contains related payment-flow information retrieved from `MUREXDB.PAY_FLOW_DBF`.

The source assigns the value named `LEID` to `entityFMID` and the value named `SCIID` to `entityLEID`; these labels and mappings require validation.

## Inbound response processing

The inbound router accepts only messages satisfying all of the following:

- `sourceSystem='RATAN'`
- `objectNature='cashflow'`
- `MXG2000/flowID > 0`
- `message='RATAN Acknowledged'` or `message='RATAN Released'`

The exact routing formula is:

```xml
<xsl:choose>
    <xsl:when test="$sourceSystem='RATAN' and $objectNature='cashflow' and $murexID>0 and $ratanMsgType='RATAN Acknowledged'">acked</xsl:when>
    <xsl:when test="$sourceSystem='RATAN' and $objectNature='cashflow' and $murexID>0 and $ratanMsgType='RATAN Released'">released</xsl:when>
    <xsl:otherwise>discard</xsl:otherwise>
</xsl:choose>
```

`FlowEntrySpliter` creates one output line per inbound `flowID`, placing its `@id` in `STPDOC_DATA_TYPE2`. The transformation retains only the matching flow:

```xml
<xsl:variable name="flow.id" select="normalize-space('Mx#client.scb.fmrp.datatype2#Mx')"></xsl:variable>
...
<MXG2000>
    <xsl:copy-of select="MXG2000/flowID[@id=$flow.id]"></xsl:copy-of>
</MXG2000>
```

Acknowledgement processing updates the RATAN identifier and acknowledgement timestamp and writes message details to `PAYFLOW_DBF.M_REASONS`:

```sql
begin
    update SCB_FMRP_DBF
    set M_RATAN_ID='MxCTX#ratanID#Mx', M_ACK_DATETIME=GETDATE()
    where M_FLOW_ID = MxCTX#murexID#Mx
    update TABLE#DATA#PAYFLOW_DBF
    set M_REASONS='MxCTX#ratanMsgType#Mx'+' ['+'MxCTX#ratanID#Mx'+'] ['+'MxCTX#ratanEvent#Mx'+']'
    where M_FLOW_ID = MxCTX#murexID#Mx
    select 'success'
end 
```

Release processing accepts a `sourceID` beginning with `N` as the RATAN network identifier; otherwise it uses `0`. It then sets the FMRP status to `MATH`:

```sql
begin
update SCB_FMRP_DBF
set M_STATUS='MATH',M_RATAN_NET_ID='MxCTX#ratanNetId#Mx',M_RLS_DATETIME= GETDATE()
where M_FLOW_ID = MxCTX#murexID#Mx
select 'success'
end    
```

`releasedEnrich` changes the response to:

```xml
<sourceSystem>MX2.11</sourceSystem>
<message>MX2.11 Acknowledged</message>
<event>Released</event>
```

## MQ configuration

The documented outbound endpoint is:

| Setting | Value |
|---|---|
| Task | `FmrpOutboundMQ` |
| Host | `10.198.198.93` |
| Port | `8212` |
| Channel | `UKMXGCLNTS2` |
| Queue manager | `UKFM02S1` |
| Queue | `GM.MXG.MLS.FEDS.UAT` |
| User | `ukmxgmq` |

The documented inbound endpoint is:

| Setting | Value |
|---|---|
| Task | `FmrpInboundMQ` |
| Host | `10.193.106.152` |
| Port | `1414` |
| Channel | `UKMXGCLNTS1` |
| Queue manager | `UKIG01S2` |
| Queue | `GMPCI.MLS.MXG.RQSTIN` |
| User | `ukmxgmq` |

The `.UAT` queue name indicates that at least the outbound configuration is UAT-oriented. Production topology, TLS, certificates, credential management, durability, and operational retry settings are not specified.

## Retry and configuration caveats

The source contains several unresolved implementation questions:

- `payInsertionFilter` uses a retry threshold below `3.0`.
- `retryCheck` uses a retry threshold below `5.0`.
- `FmrpRetryCheck` is described as having a maximum of three retries.
- Both `FmrpTimerTask` and `FmrpRetryTimer` use task code `FmrpTimerTask`.
- `FmrpInboundMQ` metadata references `client.scb.fmrp.inbound.razorID`, while the supplied formulas define `ratanID` and `murexID`, not `razorID`.
- `MATH` is written as a release status but is not defined in a state model.
- `client.scb.pay.insertPay` calls the undefined `client.scb.fmrp.fmrpPortfolioCheck`, while other formulas use entity-based eligibility.
- `MLS` is used in this source and should not be assumed equivalent to the wiki’s `LMS` without confirmation.

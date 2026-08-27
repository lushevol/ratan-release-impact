---
type: concept
title: RATAN Cashflow Acknowledgement and Release Processing
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, fmrp, cashflow, acknowledgement, release, inbound-integration]
related: [ratan-10123, fmrp, scb-fmrp-dbf, fmrp-inbound-mq, fmrp-murex-211-settlement-workflow]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Murex 2.11 workflow change/CN Settlement - Murex 2.11 workflow change-0130.md"]
---

# RATAN Cashflow Acknowledgement and Release Processing

## Message acceptance

The inbound router accepts a response only when:

```text
sourceSystem = RATAN
objectNature = cashflow
MxPayMLResponse/MXG2000/flowID > 0
message = RATAN Acknowledged or RATAN Released
```

All other responses are discarded.

The Murex flow ID defaults to `0` when `/MxPayMLResponse/MXG2000/flowID` is absent or empty. The RATAN identifier is taken from `/MxPayMLResponse/sourceID`, and the response timestamp is taken from `/MxPayMLResponse/timestamp`.

## Acknowledgement processing

For `RATAN Acknowledged`, processing:

1. Updates `SCB_FMRP_DBF.M_RATAN_ID`.
2. Records the response time in `SCB_FMRP_DBF.M_REC_DATETIME`.
3. Writes the RATAN message type and identifier to `PAYFLOW_DBF.M_REASONS`.

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

## Release processing

For `RATAN Released`, processing changes the corresponding FMRP record to `MATH`:

```sql
begin
update SCB_FMRP_DBF
set M_STATUS='MATH'
where M_FLOW_ID = Mx#client.scb.fmrp.inbound.murexID#Mx
select 'success'
end    
```

## Inbound insertion controls

Before inbound insertion proceeds, the entity must be present in `FMRP_ENTITY_DBF`, and the flow must not be associated with a precious-metal currency. Failure of either check routes the message to `discard`.

These checks are specific to FMRP inbound insertion and do not establish a general rule for Vostro selection or other cashflow workflows.
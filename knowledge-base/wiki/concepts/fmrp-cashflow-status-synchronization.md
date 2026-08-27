---
type: concept
title: FMRP Cashflow Status Synchronization
created: 2026-08-24
updated: 2026-08-24
tags: [fmrp, cashflow-status, status-synchronization, murex-211, database]
related: [scb-fmrp-dbf, fmrp-murex-211-settlement-workflow, cashflow-lifecycle-state-model, fmrp]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Murex 2.11 workflow change/CN Settlement - Murex 2.11 workflow change-0130.md"]
---

# FMRP Cashflow Status Synchronization

## State record

FMRP synchronization is backed by `SCB_FMRP_DBF`, keyed operationally by `M_FLOW_ID`. The workflow checks for records in `INIT`, `SENT`, and `CANC` states before deciding whether to publish, cancel, insert, or discard.

## Action-specific behavior

| Condition | Result |
|---|---|
| `FAIS` or `I2SR` with an `INIT` record | Update the record to `SENT` and publish |
| `FMSI` with a `SENT` record | Update the record to `CANC` and issue a cancel/discard instruction |
| `FMIS` with a `CANC` record | Update the record to `SENT` and publish |
| `FMIS` or `I2SR` without an existing record | Insert a `SENT` record and publish |
| `FMIS` with an `INIT` record | Update the record to `SENT` and publish |
| No matching condition | Discard |

The `FMIS`/`CANC` branch therefore appears to implement replay by changing a cancelled record back to `SENT`. Whether this is intentional must be confirmed.

## Database operations

The workflow uses these status values:

- `INIT`: staging or initial state.
- `SENT`: published to FMRP.
- `CANC`: cancellation state.
- `MATH`: release-completed state recorded after a RATAN release.

The release update is:

```sql
begin
update SCB_FMRP_DBF
set M_STATUS='MATH'
where M_FLOW_ID = Mx#client.scb.fmrp.inbound.murexID#Mx
select 'success'
end    
```

## Control implications

The status checks prevent duplicate insertion and distinguish replay, cancellation, and release processing. They apply specifically to the FMRP persistence record and should not be treated as the state model for MLS or other settlement routes without separate evidence.
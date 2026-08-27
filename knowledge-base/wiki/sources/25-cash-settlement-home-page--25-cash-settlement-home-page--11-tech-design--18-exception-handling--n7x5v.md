---
type: source
title: Cash Settlement Exception Handling
authors: []
year: 2023
url: ""
venue: ""
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, exception-handling, operations, runbook, ratan, cashflow]
related: [cash-settlement-exception-handling, cashflow-reinstatement-and-replay, cash-settlement-ola-break-monitoring, cash-settlement-dependent-service-failure, murex, razor, bpsi, dqsl, itrs, ims, oscar, ratan-pss]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Exception Handling.md"]
---
# Cash Settlement Exception Handling

This operational design defines detection, ownership, recovery, and database investigation procedures for Cash Settlement processing failures across Ratan, Murex, Razor, BPSI/DQSL, and dependent Ratan services.

The runbook distinguishes upstream data errors, operational-level agreement (OLA) breaks, dependent-service outages, technical failures, and acknowledgement failures. Recovery actions include service restart, Kafka redelivery, `ReInstate`, status replay, trade amendment, and manual booking in [[oscar]].

## Operational scenarios

| Case | Owner | Cashflow Status | Monitor | Solution | Comment |
| --- | --- | --- | --- | --- | --- |
| OLA break Murex→Ratan | Murex PSS OPS |  | Murex ITRS alert to Murex PSS; confirm missing cashflows with RATAN PSS | If cashflows are missing, OPS manually replays them | Agreed |
| Not all cashflows arrived within the same group | RATAN PSS | `PENDING` group | RATAN PSS is alerted when a group remains pending for more than five minutes; notify Murex PSS for investigation | Group blotter shows pending items. Murex real-time OLA monitoring is the primary control; Ratan monitoring is a second-level guarantee | Monitoring ownership was revised toward RATAN PSS alerting Murex PSS |
| Upstream publish error: missing entity/counterparty FMID, negative payment amount, missing currency, invalid date, cashflow ID length not 12, or missing CFI | RATAN PSS, OPS, FO | `ERROR` | Lifecycle log: `Allowed action on [cashflow id] from [Previous Status] to [ERROR+NA+NA]` | Display `ERROR` in Ratan; require trade amendment | CN should follow the BCS data-error model. Missing key messages are confirmed as an Interface Exception |
| BPSI API via DQSL unavailable before FMCODE retrieval | RATAN PSS, DQSL PSS, BPSI PSS, OPS | `QUEUED+Pending Exception`; may become technical failure | Lifecycle log records pending exception or missing booking entity/counterparty FMCODE | Restore BPSI, notify OPS, and reprocess with `Reinstate` | Agreed |
| BPSI unavailable after FMCODE retrieval | RATAN PSS, DQSL PSS, BPSI PSS, OPS | `WAITING` | Not specified | Generates `GSAM client Unknown` and `CORP client Unknown` NSTP exceptions | Further discussion required; a participant proposed `TechFail` instead |
| Multiple exception handling | OPS | `WAITING` | Not applicable | Referenced Confluence multiple-exception design | Agreed |
| Razor NACK | OPS | `FAILED` | Razor acknowledgement monitoring | Use `ReInstate` and process again, or manually book in OSCAR | Agreed |
| OLA break Ratan→Murex status write-back failure | RATAN PSS, Murex PSS, OPS | `RELEASED SETTLED` | Murex adaptor log and ITRS alert | PSS alerts OPS; OPS decides whether to replay the status in the Ratan UI | Agreed. Ratan supports replay; Murex has no manual status-update procedure |
| OLA break Ratan→Razor | RATAN PSS, Razor PSS, OPS | `READY+Pending Ack` | IMS alerting path | Configure Ratan API calls to IMS; notify OPS for possible manual replay from the cashflow blotter | Agreed |
| Ratan Camunda unavailable | RATAN PSS |  | Service inactive | Restart service; do not commit Kafka message so it remains available in the topic | Agreed |
| Ratan Lifecycle Service unavailable | RATAN PSS |  | Service inactive | Camunda does not commit Kafka after failed Lifecycle Service call; restart service and reprocess | Agreed |
| Common Ratan service unavailable, including SSI, Rule, Netting, and Static Data | RATAN PSS, OPS | `QUEUED+Pending Exception` | Service health and Lifecycle Service `TechFail` log pattern | Restore the unavailable service or third-party dependency, then notify OPS to use `ReInstate` | Agreed |
| Ratan Murex adaptor unavailable | RATAN PSS |  | Service inactive | Restart service; withhold Kafka commit to retain the message for reprocessing | Agreed |

## Diagnostic SQL

### Find end-to-end event history

```sql
select * from ratanone.event_history eh where reference_id ='M62220000005' order by create_timestamp asc;
```

### Get the latest SCBML for a cashflow

```sql
select * from ratan_cashflow_lifecycle_service.ratan_cashflow_scbml_message rcsm where id =( select body_event_rowkey from ratan_cashflow_lifecycle_service.ratan_cashflow_scbml_history where cashflow_id in ('N00000023997') and active = 'ACTIVE');
```

### Find an active `ERROR` cashflow and its reason

```sql
select cashflow_id , "comments" from ratan_cashflow_lifecycle_service.ratan_cashflow_scbml_history where active ='ACTIVE' and cashflow_status in ('ERROR') and cashflow_id='004342334540';
```

### Find Razor ACK/NACK information

```sql
select * from ratan_cashflow_lifecycle_service.razor_acknack_event_source where cashflow_id ='592023041591';
```

### Find Razor status information through tracking UUID

```sql
select * from ratan_cashflow_lifecycle_service.razor_cashflow_status_event_source rcses where exists (select 1 from ratan_cashflow_lifecycle_service.ratan_stella_message_event_source rsmes where rsmes.cashflow_id = 'N00000024006' and rcses .tracking_uuid = rsmes .tracking_uuid );
```

### Find Murex ACK state for RELEASED status write-back

```sql
select * from rantan_mxg_cashflow_adaptor.mxg_cashflow_history mch where tracking_id like '%94829942%' order by created_at asc;
```

### Find MXML consumed from Murex

```sql
select * from rantan_mxg_cashflow_adaptor.mxg_cashflow_message mcm where tracking_id like '%94829942%' order by created_at asc;
```

### Find SCBML transformed by the Murex adaptor

```sql
select * from rantan_mxg_cashflow_adaptor.mxg_cashflow_message mcm where tracking_id like '%94829942%' order by created_at asc;
```

### Find pending groups older than five minutes

```sql
select * from ratan_cashflow_group_management_service.ratan_cashflow_group where status = 'PENDING' and updated_at < now()-interval'5 M';
```

The interval syntax is preserved verbatim from the source and requires validation before operational use.

### Find active pending exceptions

```sql
select create_time ,cashflow_id ,cashflow_status, sub_status, sub_status_event_type, sub_status_updater , active , "action" , body_event_rowkey from ratan_cashflow_lifecycle_service.ratan_cashflow_scbml_history rsmes where cashflow_status='QUEUED' and sub_status_event_type='Pending Exception' and "active" ='ACTIVE';
```

## Error-log mappings

| Service | Log location | Key signal | Stated response |
| --- | --- | --- | --- |
| Murex adaptor | `/apps/ratanrt/logs/ratan-mxg-cashflow-adaptor.0.log` | `++++++++Receive ack overtime, flowid and netted resultant cashflow id` | Monitor through ITRS; notify OPS; OPS may replay the status on the cashflow blotter |
| Cashflow Group Management Service | `/apps/ratanrt/logs/ratan-cash-settlement-group-management-service.0.log` | Not specified | Not specified |
| Camunda workflow | `/apps/ratanrt/logs/ratan-cash-settlement-orchestration.0.log` | Not specified | Restart service and preserve uncommitted Kafka messages |
| Cashflow Lifecycle Service | `/apps/ratanrt/logs/ratan-cashflow-lifecycle-service.0.log` | `Processing status setup for , TechFail, cashflowid is [xxxxxx]` | Notify OPS and reprocess from the cashflow blotter |
| Netting Service | `/apps/ratanrt/logs/ratan-cash-settlement-netting-service.0.log` | Not specified | Not specified |
| Query Service | `/apps/ratanrt/logs/ratan-cash-settlement-query-service.9006.log` | `Exception while executing data fetcher for /counterPartyDetails: I/O error on POST request` | Check service availability with DQSL PSS |
| Rule Service | `/apps/ratanrt/logs/ratan-rule-service.0.log` | Not specified | Not specified |
| SSI stamping service | `/apps/ratanrt/logs/ratan-cash-settlement-ssi-stamping-service.0.log` | Not specified | Not specified |
| LMS service | `/apps/ratanrt/logs/ratan-cash-settlement-lms-service.0.log` | Not specified | Not specified |

## Constraints and unresolved points

The source is an operational runbook, not a canonical lifecycle-state specification. It uses both `TechFail` and `TechFailed`, and both `ReInstate` and `Reinstate`. It also leaves unresolved whether BPSI failures occurring after FMCODE retrieval should produce NSTP exceptions or technical failures.

See [[what-is-the-canonical-cash-settlement-exception-state-machine]], [[should-post-fmcode-bpsi-failures-be-techfail-or-nstp-exceptions]], and [[what-is-the-valid-pending-cashflow-monitoring-query]].
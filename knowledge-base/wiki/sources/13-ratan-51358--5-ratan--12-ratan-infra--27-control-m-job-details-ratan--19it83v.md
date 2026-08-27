---
type: source
title: RATAN Control-M Job Details and ITRS EOD File Monitor Mapping
authors: [Yunzhe Ta]
year: 2026
url: ""
venue: "Internal operational document"
created: 2026-08-22
updated: 2026-08-22
tags: [ratan, control-m, batch-operations, itrs, aspire, settlement]
related: [ratan, controlm, aspire, itrs, ratan-batch-operational-maintenance, itrs-to-control-m-file-monitor-mapping, auto-netting-job-time, last-mile-payment-release-control, cashflow-fail-and-reinstatement, what-is-the-canonical-auto-netting-job-schedule-and-timezone, why-does-rat-cn-acc-hk-identify-two-different-accounting-jobs, what-are-the-complete-itrs-monitoring-parameters-for-ratan-eod-files]
sources: ["RATAN - 51358/RATAN/RATAN -Infra/Control-M Job Details RATAN.md"]
---
# RATAN Control-M Job Details and ITRS EOD File Monitor Mapping

This internal inventory, updated by @Yunzhe Ta on 2026-01-09, records RATAN Control-M jobs, their stated purposes, hosts, and Control-M folder paths. It also maps four ITRS EOD file monitors to RATAN jobs that generate Aspire accounting outputs.

It is evidence of the documented inventory, not proof that every job remains active, production-approved, correctly scheduled, or fully monitored. Commands, owners, dependencies, alert thresholds, recovery runbooks, and most schedules are absent.

## Operational findings

- `RAT_AUTO_NETTING` and `RAT_AUTO_NETTING_WEEKEND` are documented as running every 30 minutes on `uklvapapp590`.
- `RAT_STL_CSH_HOLD_RELEASE` is documented to release cashflows in `Queued Cut Off` from 1 AM GMT every 30 minutes on `uklvapapp590`.
- Standard and China-specific jobs separately handle past-date failure, queued-cut-off release, and settlement processing.
- Four Aspire EOD filenames have explicit mappings to jobs in `RATAN_Settlement_Aspire_P`.
- The inventory covers log cleanup, HashiCorp account rotation, service restart, PostgreSQL backup and transfer, database purge, and reconciliation, in addition to settlement work.

See [[ratan-batch-operational-maintenance]] for the operational-maintenance grouping and [[itrs-to-control-m-file-monitor-mapping]] for the limited EOD mapping.

## Control-M job inventory

| Application Name | Control-M Job Name | Description | Host | Control-M Job Full Path | Commands | Comments |
| --- | --- | --- | --- | --- | --- | --- |
| RATAN | RAT_LOG_CLEANER_W (parent folder) | for log clean |  | RATAN → RATAN_AUTO_P → RAT_LOG_CLEANER_W |  |  |
|  | RAT_ARK_LOG_CLEAN | This job is used to clean up the ELK,Kibana, Kafka & ZK historical logs on Ark Host Group |  |  |  |  |
|  | RAT_WAT_LOG_CLEAN | This job is used to clean up the ELK,Kibana Kafka & ZK historical logs on WAT Host Group |  |  |  |  |
| RATAN | RATAN_FULL_HCV(parent folder) | for monthly enable hashicorp, VIP and clusters on all servers (Mar, Jul, Nov) |  | RATAN → RATAN_AUTO_P → RATAN_FULL_HCV |  |  |
|  | RAT_HCV_CHECK | check all hashicorp account rotate info |  |  |  |  |
|  | RAT_HCV_REFRESH | refresh all hashicorp account to Redis |  |  |  |  |
|  | RAT_HCV_ROTATE | rotate all hashicorp account |  |  |  |  |
|  | RAT_RESTART_ALL_SERV_HCV | Restart VIP and the whole clusters from ARK servers |  |  |  |  |
|  | RAT_STOP_ALL_SERV_HCV | Stop all services on whole cluster |  |  |  |  |
| RATAN | RATAN_FULL_M(parent folder) | for monthly enable VIP and clusters on all servers (Jan, Feb, Apr, May, Jul, Aug, Oct, Nov) |  | RATAN → RATAN_AUTO_P → RATAN_FULL_M |  |  |
|  | RAT_RESTART_ALL_SERVICES | Restart VIP and the whole clusters from ARK servers |  |  |  |  |
|  | RAT_STOP_ALL_SERVICES | Stop all services on whole cluster |  |  |  |  |
| RATAN | RAT_PGBackup_P590 | This job is used to scan info on server uklvapapp590 | uklvapapp590 | RATAN → RATAN_AUTO_PGBACKUP_PROD → RAT_PGBackup_P590 |  |  |
| RATAN | RAT_PGBackup_S590 | This job is used to scan event_record info on server uklvasapp590 | uklvasapp590 | RATAN → RATAN_AUTO_PGBACKUP_PROD → RAT_PGBackup_S590 |  |  |
| RATAN | RAT_PGDump_Transfer_P590 | This job is used to transfer PG dump on server uklvapapp590 to Dev | uklvapapp590 | RATAN → RATAN_AUTO_PGBACKUP_PROD → RAT_PGDump_Transfer_P590 |  |  |
| RATAN | RAT_PGDump_Transfer_S590 | This job is used to transfer PG tar dump on server uklvasapp590 to Dev | uklvasapp590 | RATAN → RATAN_AUTO_PGBACKUP_PROD → RAT_PGDump_Transfer_S590 |  |  |
| RATAN | RATAN_Auto_Purge_P(parent folder) | automatically |  | RATAN → RATAN_AUTO_Purge_P → RATAN_Auto_Purge_P |  |  |
|  | RAT_PG_PURGE | Auto purge DB |  |  |  |  |
|  | RAT_PG_PURGE_CO | Auto purge DB - comunda |  |  |  |  |
|  | RAT_PG_PURGE_EVENT | Auto purge DB version - event |  |  |  |  |
|  | RAT_PG_PURGE_V2 | Auto purge DB version2 |  |  |  |  |
|  | RAT_PG_PURGE_V3 | Auto purge DB version3 |  |  |  |  |
| RATAN | RATAN_Auto_Recon(parent folder) | automatically |  | RATAN → RATAN_AUTO_Recon → RATAN_Auto_Recon |  |  |
|  | RAT_Recon_P590 | This job is used to scan info on server uklvapapp590 |  |  |  |  |
|  | RAT_Recon_P591 | This job is used to scan info on server uklvapapp591 |  |  |  |  |
|  | RAT_Recon_P676 | This job is used to scan info on server uklvapapp676 |  |  |  |  |
|  | RAT_Recon_S590 | This job is used to scan info on server uklvasapp590 |  |  |  |  |
|  | RAT_Recon_S591 | This job is used to scan info on server uklvasapp591 |  |  |  |  |
|  | RAT_Recon_S676 | This job is used to scan info on server uklvasapp676 |  |  |  |  |
|  | RAT_Recon_Transfer_P590 | This job is used to transfer scan info on server uklvapapp590 |  |  |  |  |
|  | RAT_Recon_Transfer_P591 | This job is used to transfer scan info on server uklvapapp591 |  |  |  |  |
|  | RAT_Recon_Transfer_P676 | This job is used to transfer scan info on server uklvapapp676 |  |  |  |  |
|  | RAT_Recon_Transfer_S590 | This job is used to transfer scan info on server uklvasapp590 |  |  |  |  |
|  | RAT_Recon_Transfer_S591 | This job is used to transfer scan info on server uklvasapp591 |  |  |  |  |
|  | RAT_Recon_Transfer_S676 | This job is used to transfer scan info on server uklvasapp676 |  |  |  |  |
| RATAN | RAT_AUTO_NETTING | cycle auto Netting job, every 30 mins | uklvapapp590 | RATAN → RATAN_AUTO_SETTLEMENT_P → RATAN_AUTO_SETTLEMENT_P →RAT_AUTO_NETTING |  |  |
| RATAN | RAT_AUTO_NETTING_WEEKEND | cycle auto Netting job, every 30 mins | uklvapapp590 | RATAN → RATAN_AUTO_SETTLEMENT_P → RATAN_AUTO_SETTLEMENT_P →RAT_AUTO_NETTING_WEEKEND |  |  |
| RATAN | RAT_STL_CSH_HOLD_RELEASE | Release cashflow with Queued Cut Off, from 1AM GMT, every 30 mins | uklvapapp590 | RATAN → RATAN_AUTO_SETTLEMENT_P → RATAN_AUTO_SETTLEMENT_P → RAT_STL_CSH_HOLD_RELEASE |  |  |
| RATAN | RAT_STL_FAIL | Move past date cashflow to Failed | uklvapapp590 | RATAN → RATAN_AUTO_SETTLEMENT_P → RATAN_AUTO_SETTLEMENT_P → RAT_STL_FAIL |  |  |
| RATAN | RAT_STL_NETTING | Auto Netting base on netting rule | uklvapapp590 | RATAN → RATAN_AUTO_SETTLEMENT_P → RATAN_AUTO_SETTLEMENT_P → RAT_STL_NETTING |  |  |
| RATAN | RAT_CN_ACC_AE | CN: ebbs accounting for AE | uklvasapp590 | RATAN → RATAN_CN_AUTO_JOB_P → RATAN_CN_AUTO_JOB_P → RAT_CN_ACC_AE |  | It will be manually triggered from 30th May |
| RATAN | RAT_CN_ACC_CN | CN: ebbs accounting for CN | uklvasapp590 | RATAN → RATAN_CN_AUTO_JOB_P → RATAN_CN_AUTO_JOB_P → RAT_CN_ACC_CN |  | It will be manually triggered from 30th May |
| RATAN | RAT_CN_ACC_DE | CN: ebbs accounting for DE | uklvasapp590 | RATAN → RATAN_CN_AUTO_JOB_P → RATAN_CN_AUTO_JOB_P → RAT_CN_ACC_DE |  | It will be manually triggered from 30th May |
| RATAN | RAT_CN_ACC_HK | CN: ebbs accounting for HK | uklvasapp590 | RATAN → RATAN_CN_AUTO_JOB_P → RATAN_CN_AUTO_JOB_P → RAT_CN_ACC_HK |  | It will be manually triggered from 30th May |
| RATAN | RAT_CN_ACC_ID | CN: ebbs accounting for ID | uklvasapp590 | RATAN → RATAN_CN_AUTO_JOB_P → RATAN_CN_AUTO_JOB_P → RAT_CN_ACC_ID |  | It will be manually triggered from 30th May |
| RATAN | RAT_CN_ACC_IN | CN: ebbs accounting for IN | uklvasapp590 | RATAN → RATAN_CN_AUTO_JOB_P → RATAN_CN_AUTO_JOB_P → RAT_CN_ACC_IN |  | It will be manually triggered from 30th May |
| RATAN | RAT_CN_ACC_JP | CN: ebbs accounting for JP | uklvasapp590 | RATAN → RATAN_CN_AUTO_JOB_P → RATAN_CN_AUTO_JOB_P → RAT_CN_ACC_JP |  | It will be manually triggered from 30th May |
| RATAN | RAT_CN_ACC_MU | CN: ebbs accounting for MU | uklvasapp590 | RATAN → RATAN_CN_AUTO_JOB_P → RATAN_CN_AUTO_JOB_P → RAT_CN_ACC_MU |  | It will be manually triggered from 30th May |
| RATAN | RAT_CN_ACC_MY | CN: ebbs accounting for MY | uklvasapp590 | RATAN → RATAN_CN_AUTO_JOB_P → RATAN_CN_AUTO_JOB_P → RAT_CN_ACC_MY |  | It will be manually triggered from 30th May |
| RATAN | RAT_CN_ACC_SG | CN: ebbs accounting for SG | uklvasapp590 | RATAN → RATAN_CN_AUTO_JOB_P → RATAN_CN_AUTO_JOB_P → RAT_CN_ACC_SG |  | It will be manually triggered from 30th May |
| RATAN | RAT_CN_ACC_UK | CN: ebbs accounting for UK | uklvasapp590 | RATAN → RATAN_CN_AUTO_JOB_P → RATAN_CN_AUTO_JOB_P → RAT_CN_ACC_UK |  | It will be manually triggered from 30th May |
| RATAN | RAT_CN_ACC_PH | CN: ebbs accounting for PH | uklvasapp590 | RATAN → RATAN_CN_AUTO_JOB_P → RATAN_CN_AUTO_JOB_P → RAT_CN_ACC_PH |  | It will be manually triggered from 30th May |
| RATAN | RAT_CN_ACC_US | CN: ebbs accounting for US | uklvasapp590 | RATAN → RATAN_CN_AUTO_JOB_P → RATAN_CN_AUTO_JOB_P → RAT_CN_ACC_US |  | It will be manually triggered from 30th May |
| RATAN | RAT_CN_ACC_ZA | CN: ebbs accounting for ZA | uklvasapp590 | RATAN → RATAN_CN_AUTO_JOB_P → RATAN_CN_AUTO_JOB_P → RAT_CN_ACC_ZA |  | It will be manually triggered from 30th May |
| RATAN | RAT_CN_BATCH | CN Release with batch jobs | uklvapapp590 | RATAN → RATAN_CN_AUTO_JOB_P → RATAN_CN_AUTO_JOB_P → RAT_CN_BATCH |  |  |
| RATAN | RAT_CN_BATCH_PURGE | CN: purge batch files and keep 15 days | uklvapapp590 | RATAN → RATAN_CN_AUTO_JOB_P → RATAN_CN_AUTO_JOB_P → RAT_CN_BATCH_PURGE |  |  |
| RATAN | RAT_CN_BATCHFIX | CN Release with batchFix jobs | uklvapapp590 | RATAN → RATAN_CN_AUTO_JOB_P → RATAN_CN_AUTO_JOB_P → RAT_CN_BATCHFIX |  |  |
| RATAN | RAT_CN_FAIL | CN: Move past date cashflow to failed | uklvapapp590 | RATAN → RATAN_CN_AUTO_JOB_P → RATAN_CN_AUTO_JOB_P → RAT_CN_FAIL |  |  |
| RATAN | RAT_CN_HOLD_RELEASE | CN Release cashflow with Queued Cut Off | uklvapapp590 | RATAN → RATAN_CN_AUTO_JOB_P → RATAN_CN_AUTO_JOB_P → RAT_CN_HOLD_RELEASE |  |  |
| RATAN | RAT_CN_ACC_JE | CN: aspire accounting for JE | uklvasapp590 | RATAN →RATAN_Settlement_Aspire_P →RAT_CN_ACC_JE |  |  |
| RATAN | RAT_CN_ACC_HK | CN: aspire accounting for HK | uklvasapp590 | RATAN → RATAN_Settlement_Aspire_P→RAT_CN_ACC_HK |  |  |
| RATAN | RAT_CN_ACC_TH | CN: aspire accounting for TH | uklvasapp590 | RATAN → RATAN_Settlement_Aspire_P →RAT_CN_ACC_TH |  |  |
| RATAN | RAT_CN_ACC_TW | CN: aspire accounting for TW | uklvasapp590 | RATAN → RATAN_Settlement_Aspire_P →RAT_CN_ACC_TW |  |  |
| RATAN | RAT_CN_GEF_JE | CN: region empty file generation for JE | uklvasapp590 | RATAN →RATAN_Settlement_Aspire_P → RAT_CN_GEF_JE |  |  |
| RATAN | RAT_CN_GEF_HK | CN: region empty file generation for HK | uklvasapp590 | RATAN → RATAN_Settlement_Aspire_P→ RAT_CN_GEF_HK |  |  |
| RATAN | RAT_CN_GEF_TH | CN: region empty file generation for HK | uklvasapp590 | RATAN → RATAN_Settlement_Aspire_P → RAT_CN_GEF_TH |  |  |
| RATAN | RAT_CN_GEF_TW | CN: region empty file generation for TW | uklvasapp590 | RATAN → RATAN_Settlement_Aspire_P → RAT_CN_GEF_TW |  |  |
| RATAN | RAT_CN_MLZ | CN: Move past date cashflow to materialization | uklvapapp590 | RATAN → RATAN_CN_AUTO_JOB_P → RATAN_CN_AUTO_JOB_P → RAT_CN_MLZ |  |  |
| RATAN | RAT_PAYMENT_HOL | Refresh payment holiday everyday | uklvapapp590 | RATAN → RATAN_TRADE_REVIEW_P → RAT_PAYMENT_HOL |  |  |
| RATAN | RAT_PCT2_REFRESH | Refresh PCT2 portfolio by automation | uklvapapp590 | RATAN → RATAN_TRADE_REVIEW_P → RAT_PCT2_REFRESH |  |  |

## ITRS-to-Control-M mapping

| Application Name | Filename | Description | Control-M Job Name | Host | Control-M Job Full Path | Commands | Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RATAN | RATAN_PAYMENT_TRANSACTION_HK | CN: aspire accounting for HK | RAT_CN_ACC_HK | uklvasapp590 | RATAN→ RATAN_Settlement_Aspire_P→ RAT_CN_ACC_HK |  |  |
| RATAN | RATAN_PAYMENT_TRANSACTION_TH | CN: aspire accounting for TH | RAT_CN_ACC_TH | uklvasapp590 | RATAN→ RATAN_Settlement_Aspire_P→ RAT_CN_ACC_TH |  |  |
| RATAN | RATAN_PAYMENT_TRANSACTION_TW | CN: aspire accounting for TW | RAT_CN_ACC_TW | uklvasapp590 | RATAN→ RATAN_Settlement_Aspire_P→ RAT_CN_ACC_TW |  |  |
| RATAN | RATAN_PAYMENT_TRANSACTION_JE | CN: aspire accounting for JE | RAT_CN_ACC_JE | uklvasapp590 | RATAN→ RATAN_Settlement_Aspire_P→ RAT_CN_ACC_JE |  |  |

## Document limitations and data-quality issues

`RAT_CN_ACC_HK` appears twice with distinct paths and purposes: eBBS accounting under `RATAN_CN_AUTO_JOB_P`, and Aspire accounting under `RATAN_Settlement_Aspire_P`. The mapping above identifies the Aspire-path instance as the producer of `RATAN_PAYMENT_TRANSACTION_HK`, but whether this is a valid same-name pair or an error remains open in [[why-does-rat-cn-acc-hk-identify-two-different-accounting-jobs]].

The description for `RAT_CN_GEF_TH` says it generates an empty file for HK despite its TH-specific name and path. The source does not resolve this discrepancy.

The source claims to map ITRS monitoring values, but supplies filenames only. Monitor identifiers, directories, expected delivery times, tolerance windows, alert severity, escalation ownership, and runbooks are absent; see [[what-are-the-complete-itrs-monitoring-parameters-for-ratan-eod-files]].
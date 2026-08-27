---
type: concept
title: RATAN Batch Operational Maintenance
created: 2026-08-22
updated: 2026-08-22
tags: [ratan, control-m, batch-operations, maintenance, backup, reconciliation, credential-rotation]
related: [ratan, controlm, itrs, auto-netting-job-time, last-mile-payment-release-control, cashflow-fail-and-reinstatement]
sources: ["RATAN - 51358/RATAN/RATAN -Infra/Control-M Job Details RATAN.md"]
---
# RATAN Batch Operational Maintenance

RATAN batch operational maintenance is the Control-M-scheduled operational work that supports the application outside its direct settlement lifecycle. The documented inventory groups this work into log cleanup, HashiCorp account rotation and cluster restarts, PostgreSQL backup and Dev transfer, database purge, and reconciliation scanning and transfer.

## Documented job groups

- `RAT_LOG_CLEANER_W` contains `RAT_ARK_LOG_CLEAN` and `RAT_WAT_LOG_CLEAN` for historical ELK, Kibana, Kafka, and ZK log cleanup on Ark and WAT host groups.
- `RATAN_FULL_HCV` contains account-rotation checking, Redis refresh, account rotation, and service/VIP stop and restart jobs. It is documented for March, July, and November.
- `RATAN_FULL_M` contains service/VIP stop and restart jobs. It is documented for January, February, April, May, July, August, October, and November.
- `RATAN_AUTO_PGBACKUP_PROD` includes scans and PostgreSQL dump transfers to Dev for `uklvapapp590` and `uklvasapp590`.
- `RATAN_Auto_Purge_P` includes database purge jobs, including `RAT_PG_PURGE_CO` for `comunda` as written in the source.
- `RATAN_Auto_Recon` includes scan and transfer jobs for `uklvapapp590`, `uklvapapp591`, `uklvapapp676`, `uklvasapp590`, `uklvasapp591`, and `uklvasapp676`.

The inventory does not provide commands, schedule times, execution dependencies, retention rules beyond the China batch-file retention statement, maintenance windows, owners, success criteria, or recovery procedures.

July and November are listed for both `RATAN_FULL_HCV` and `RATAN_FULL_M`; the intended ordering and change controls are not established by this source.
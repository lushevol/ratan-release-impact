---
type: query
title: How Should Cash Settlement Coordinate pg_dump and Schema Migrations?
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, postgresql, pg_dump, schema-migration, production-readiness, release-management]
related: [postgresql, postgresql-backup-ddl-lock-contention, 25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--54-alter-table-add-column-took-long--129ct4c, deployment-cd-script, cash-settlement-platform]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Alter table add column took long time on prod analysis.md"]
---
# How Should Cash Settlement Coordinate pg_dump and Schema Migrations?

## Question

What approved production procedure should prevent or safely manage contention between `pg_dump` and PostgreSQL schema migrations used by Cash Settlement releases?

## Evidence

The recorded reproduction links an active `pg_dump` with a blocked `ALTER TABLE` operation: 266 ms without the dump, at least 42 seconds blocked with it active, and success after the dump request was terminated. See [[25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--54-alter-table-add-column-took-long--129ct4c]].

## Information required

- Exact PostgreSQL version, configuration, and `pg_dump` options.
- Exact DDL, target-table size, and relevant table definition.
- Blocking and waiting PIDs, lock modes, wait events, transaction states, and lock-queue order.
- Whether the dump was expected to be long-running or was extended by an open or idle transaction.
- The approved owner and validation procedure for cancelling a conflicting backup.
- Whether [[deployment-cd-script]] should fail early when it detects backup-related blocking.
- Appropriate lock timeout, retry, maintenance-window, and rollback behavior.

## Candidate policy direction

A policy should prefer prevention and observability over ad hoc cancellation: verify that scheduled backups are complete before migration, detect blocking sessions before executing DDL, and escalate any required backup cancellation to the accountable backup owner. Any final policy should be captured in an approved decision after the missing operational evidence is collected.
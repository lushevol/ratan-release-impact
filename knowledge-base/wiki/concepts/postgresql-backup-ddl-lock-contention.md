---
type: concept
title: PostgreSQL Backup and DDL Lock Contention
created: 2026-08-24
updated: 2026-08-24
tags: [postgresql, pg_dump, ddl, locking, schema-migration, release-operations]
related: [postgresql, 25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--54-alter-table-add-column-took-long--129ct4c, how-should-cash-settlement-coordinate-pg-dump-and-schema-migrations, deployment-cd-script]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Alter table add column took long time on prod analysis.md"]
---
# PostgreSQL Backup and DDL Lock Contention

PostgreSQL backup and schema-change operations can contend when concurrent sessions hold incompatible locks or when lock queues delay a restrictive DDL request. A schema migration can therefore spend most of its elapsed time waiting for locks rather than executing its database change.

## Cash Settlement observation

In the recorded Cash Settlement reproduction, an add-column operation completed in 266 ms without an active dump. After `pg_dump` was started, the same operation was blocked for at least 42 seconds. Terminating the dump released the observed blockage, after which the DDL succeeded.

This supports treating concurrent backup activity as a release-operability risk for that environment. It is not evidence that `pg_dump` universally blocks all DDL, or that all add-column operations have identical lock and execution behavior.

## Operational controls to evaluate

A controlled migration process may need to include:

- separation of backup and schema-migration windows;
- a pre-deployment check for active backup and blocking sessions;
- bounded lock-wait timeouts with clear diagnostics;
- capture of blocking PID, lock mode, transaction state, and wait event;
- a defined escalation and approval path before cancelling a backup; and
- post-intervention validation of backup and migration outcomes.

The exact PostgreSQL version, dump command options, lock chain, and affected DDL definition must be captured before selecting a permanent control. The open policy question is tracked in [[how-should-cash-settlement-coordinate-pg-dump-and-schema-migrations]].
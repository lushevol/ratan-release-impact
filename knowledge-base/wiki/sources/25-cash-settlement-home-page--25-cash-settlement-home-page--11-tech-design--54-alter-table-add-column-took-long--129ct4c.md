---
type: source
title: "Alter Table Add Column Took Long Time on Production Analysis"
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, postgresql, pg_dump, schema-migration, production-incident, locking]
related: [postgresql, postgresql-backup-ddl-lock-contention, how-should-cash-settlement-coordinate-pg-dump-and-schema-migrations, cash-settlement-platform, deployment-cd-script]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Alter table add column took long time on prod analysis.md"]
authors: []
year: 2025
url: ""
venue: ""
---
# Alter Table Add Column Took Long Time on Production Analysis

This technical note records a Cash Settlement production/reproduction scenario in which a PostgreSQL `ALTER TABLE` operation was delayed while a `pg_dump` job was running. The stated impact was a release issue caused by the schema-change script being blocked.

## Reproduction record

1. With no dump running, the alter-table operation reportedly completed in **266 ms**.
2. The added column was dropped to restore the test state.
3. A dump was started. The source states that many locks associated with `pg_dump` were visible.
4. The alter-table operation was run again and was blocked for **42 seconds or more**.
5. The dump request was killed. The lock was released and the alter operation succeeded, with a reported elapsed time of **1 minute 37 seconds**.

The source conclusion is that a long-running `pg_dump` job blocked the alter script and thereby caused a release problem.

## Interpretation and scope

The measured contrast—266 ms without an active dump versus at least 42 seconds of blocking while one was active—supports an environment-specific association between concurrent dump activity and delayed DDL. It does not show that adding a column is inherently slow, nor that every `pg_dump` operation blocks every `ALTER TABLE` variant.

PostgreSQL version, dump options, the exact DDL statement, table size, lock modes, session identifiers, wait events, and transaction states are not transcribed in the available text. The difference between the reported 42-second-or-more block and the final 1-minute-37-second elapsed time is also unexplained.

## Evidence retained by the original document

The original note references screenshots, but their contents are not available as text in the supplied source:

- `attachments/image-2025-7-28_14-18-33.png`
- `attachments/image-2025-7-28_14-20-27.png`
- `attachments/image-2025-7-28_14-20-6.png`
- `attachments/image-2025-7-28_14-24-5.png`
- `attachments/image-2025-7-28_14-25-16.png`

It also refers to an attached email whose contents are not present.

## Operational implication

Schema migrations for [[cash-settlement-platform]] should account for possible lock contention with PostgreSQL backup activity. Killing a dump unblocked this reproduction, but the source does not establish it as an approved production response or assess backup consistency, ownership, or recovery implications.

See [[postgresql-backup-ddl-lock-contention]] for the lock-contention pattern and [[how-should-cash-settlement-coordinate-pg-dump-and-schema-migrations]] for the unresolved production policy.
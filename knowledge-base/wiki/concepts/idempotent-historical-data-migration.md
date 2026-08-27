---
type: concept
title: Idempotent Historical Data Migration
created: 2026-08-24
updated: 2026-08-24
tags: [data-migration, idempotency, historical-data, opensearch, postgresql]
related: [opensearch, postgresql, opensearch-business-live, three-way-data-reconciliation, double-writing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/OpenSearch Business Live Plan.md"]
---
# Idempotent Historical Data Migration

## Definition

Idempotent historical data migration allows the OpenSearch backfill to be retried or resumed without creating duplicate, dirty, or inconsistent documents.

## Business-live requirements

The migration should establish:

- A defined source and cutoff time.
- Complete historical coverage before cutover.
- A controlled treatment of writes occurring during migration.
- Deterministic document identity.
- Safe restart and checkpoint behavior.
- Validation against the source dataset.
- Reconciliation after loading.
- A rollback or repair procedure.

The source frames these requirements as necessary to preserve data integrity and user trust when changing the underlying query source.

## Candidate tools

The source lists `pgsync`, Apache NiFi, Logstash, and self-developed Java or Python tooling. The inventory does not select an approach. Selection requires evaluation of source compatibility, transformation capability, throughput, restartability, monitoring, security, operational ownership, and validation support.

## Relationship to live event replay

Historical migration idempotency is related to, but distinct from, OpenSearch-agent event replay. Both require stable identity and version handling; event replay additionally requires ordering and poison-message controls.

---
type: concept
title: Database-OpenSearch Reconciliation
created: 2026-08-24
updated: 2026-08-24
tags: [reconciliation, opensearch, database, data-consistency, migration]
related: [opensearch, db-to-opensearch-data-migration, ratan-opensearch-rollout, what-is-the-authoritative-db-to-opensearch-reconciliation-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Open Search Plan.md"]
---
# Database-OpenSearch Reconciliation

Database-OpenSearch reconciliation is the planned comparison of relational-database data with its OpenSearch representation during the migration and parallel-run period.

The source identifies missing real-time reconciliation as a known issue and lists both a “Recon strategy” activity and “Recon between DB and Open Search” as go-live work. It does not define the reconciliation frequency, matching keys, source of authority, acceptable lag, discrepancy tolerances, alerting, ownership, or remediation workflow.

Until those rules are approved, reconciliation remains a release-critical design gap rather than an implemented control.
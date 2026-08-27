---
type: query
title: What Is the Authoritative Ratan Cashflow History Index Deployment Contract?
created: 2026-08-23
updated: 2026-08-23
tags: [ratan, postgresql, database-indexing, production-deployment, cashflow-auto-netting]
related: [ratan, ratan-cashflow-scbml-history, ratan-cashflow-history-composite-index, postgresql-concurrent-index-creation, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requir--x4ci4w]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Create Index on  table ratan_cashflow_scbml_history.md"]
---
# What Is the Authoritative Ratan Cashflow History Index Deployment Contract?

The source recommends a concurrent creation of `ratan_cashflow_scbml_history_active_status_idx` on [[ratan-cashflow-scbml-history]], but it does not establish an approved operational deployment contract.

## Questions to resolve

- Which Cashflow Auto Netting queries require the index, and do their predicates support the proposed key order?
- What indexes, constraints, and similarly named objects already exist on the target table?
- Which PostgreSQL version is deployed, and does the deployment mechanism permit `CREATE INDEX CONCURRENTLY` outside a transaction block?
- What are the table size, write rate, storage headroom, replication topology, and expected resource impact?
- What monitoring thresholds require pausing, cancelling, or rescheduling the build?
- How will invalid-index state be identified through catalog metadata and safely cleaned up?
- What query-plan and performance measurements define successful deployment?
- What rollback or retry procedure applies if production impact exceeds acceptable limits?
- If table replacement is considered, how will concurrent changes, dependencies, grants, triggers, sequences, and consistency validation be controlled?

## Current evidence

The source contains an index definition and monitoring queries, but no workload evidence or execution results. The concurrent-build approach should be validated before being treated as a completed decision. The alternative replacement-table procedure is insufficiently specified for safe production use.
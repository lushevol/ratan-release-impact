---
type: concept
title: Three-Way Data Reconciliation
created: 2026-08-24
updated: 2026-08-24
tags: [reconciliation, data-quality, opensearch, postgresql, cashflow]
related: [opensearch, postgresql, ratanone-opensearch-agent, cashflow, kafka-persistent-retry-and-dlt-recovery]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/OpenSearch Business Live Plan.md"]
---
# Three-Way Data Reconciliation

## Definition

Three-way data reconciliation compares corresponding cashflow and cashflow-history records across:

1. Lifecycle service SCBML history.
2. Query service PG cashflow data and cashflow history.
3. OpenSearch cashflow and cashflow-history indexes.

## Purpose

Reconciliation provides operational confidence during the OpenSearch transition and identifies missing or divergent records after double writing or migration.

The intended outcome is actionable detection: when records are missing, operators should be able to identify the specific cashflows affected and initiate remediation.

## Required contract

The source identifies the need but does not define the implementation contract. The reconciliation design must specify:

- Canonical correlation key.
- Fields and transformations compared.
- Eventual-consistency windows.
- Completeness and freshness thresholds.
- Schedule or streaming frequency.
- Treatment of delayed, duplicated, stale, and semantically divergent records.
- Mismatch ownership and remediation workflow.
- Dashboard accuracy and alert thresholds.
- Post-PG-decommission validation sources.

The existing production Grafana reconciliation section is described as inaccurate and requires enhancement.

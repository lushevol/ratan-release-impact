---
type: query
title: What Are the Canonical Cash Settlement OpenSearch Indices, Mappings, and Data-Retention Rules?
created: 2026-08-24
updated: 2026-08-24
tags: [opensearch, cash-settlement, indices, mappings, retention, governance]
related: [opensearch, opensearch-business-data-visibility, sql-over-opensearch]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/OpenSearch Business Live Plan/Open Search Data Visiability.md"]
---
# What Are the Canonical Cash Settlement OpenSearch Indices, Mappings, and Data-Retention Rules?

## Question

Which OpenSearch indices expose Cash Settlement data, who owns each index and mapping, and what retention, freshness, reconciliation, and access rules govern them?

## Gap

The source describes tools for querying OpenSearch but contains no index names, mappings, data classifications, ingestion paths, freshness objectives, retention schedules, or recovery requirements.

## Evidence needed

- Index inventory and business-domain ownership.
- Versioned mappings and field definitions.
- Source systems, ingestion streams, and update semantics.
- Freshness SLAs and reconciliation controls.
- Retention, archival, deletion, backup, and restore policies.
- Data classification and permitted query/export rules.
---
type: query
title: Is OpenSearch the Authoritative Store or a Read Model for Cash Settlement?
created: 2026-08-24
updated: 2026-08-24
tags: [opensearch, cash-settlement, data-architecture, authority]
related: [opensearch, opensearch-business-data-visibility, eventual-consistency-for-cashflow-exceptions-and-swift-status]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/OpenSearch Business Live Plan/Open Search Data Visiability.md"]
---
# Is OpenSearch the Authoritative Store or a Read Model for Cash Settlement?

## Question

Does [[opensearch]] hold authoritative Cash Settlement business records, or is it a search, operational-read, or analytics projection sourced from other persisted domain data?

## Why it matters

The source calls OpenSearch a main NoSQL database but provides no record-of-truth designation, source-of-data model, reconciliation process, or recovery boundary. Existing Cash Settlement materials also describe database persistence, Kafka integration, caching, and eventual consistency.

## Evidence needed

- Approved target architecture and domain ownership record.
- Index ingestion and update paths.
- Authoritative upstream stores for each indexed business domain.
- Reconciliation, retention, backup, and recovery contracts.
- A clear policy for operational queries versus business reporting.
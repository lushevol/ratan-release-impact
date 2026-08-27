---
type: query
title: What Is the Authoritative RATAN Holiday Data Ingestion Path?
created: 2026-08-24
updated: 2026-08-24
tags: [rdm, fileit, holiday-calendar, ingestion, authority]
related: [rdm-holiday-and-weekend-ingestion, fileit-file-arrival-notification, ratan-static-rdm-holiday-weekend-message, ratan-static-cashflow-currency-holiday, rdm]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan holiday data process from RDM introduction.md"]
---
# What Is the Authoritative RATAN Holiday Data Ingestion Path?

The source documents raw RDM messages, a structured holiday table, FileIT full BCDF files, and FileIT arrival notifications. It does not specify whether these are alternative ingestion paths, sequential stages, or inputs requiring reconciliation.

## Evidence needed

- The component that processes the FileIT notification and file.
- The component that populates each table.
- Authoritative-source and reconciliation rules.
- Failure, replay, and recovery behavior for each path.
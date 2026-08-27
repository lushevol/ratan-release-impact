---
type: query
title: What Is the Canonical Korea TLM Recon API Response Schema?
created: 2026-08-24
updated: 2026-08-24
tags: [api-contract, schema, korea, tlm, accounting, ebbs]
related: [query-recon-records, korea-tlm-accounting-reconciliation, tlm]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Swift Generation & Settlement Accounting Tech design/Korea Accounting - TLM Recon.md"]
---
# What Is the Canonical Korea TLM Recon API Response Schema?

The formal response table specifies `totalRecords`, `accountingFeeds`, and `publishTimestamp`. The generic example uses `totalNumberOfRecords`, `accountingRecords`, and `publishTimestamp`; Korea and UAT examples use misspelled `totoalNumberOfRecords`, `accountingRecords`, and `publishTimeStamp`.

An approved, versioned schema is needed for TLM implementation. It must establish field names, casing, typo compatibility, timestamp representation, error schema, HTTP status behavior, and pagination behavior.
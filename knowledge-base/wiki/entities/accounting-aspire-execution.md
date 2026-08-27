---
type: entity
title: accounting_aspire_execution
created: 2026-08-24
updated: 2026-08-24
tags: [database-table, accounting, file-delivery, execution-tracking]
related: [aspire, fileit, accounting-file-delivery-acknowledgement, accounting-feed-file-generation-idempotency]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Settlement Accounting for Aspire Tech design.md"]
---
# accounting_aspire_execution

`accounting_aspire_execution` is the proposed execution-tracking table for Aspire-related accounting-file processing.

The job walkthrough uses the table to find the latest `asOfDate` by country. Proposed processing then inserts an execution record with country, `asOfDate`, and `SENT`, and updates the response after FileIT acknowledgement.

Source-supported fields and values include:

- Country, illustrated as `HK`
- `asOfDate`
- Execution ID
- `file_sent`, illustrated as `SENT`, `ACKED`, and `NACK`
- `response_code`, illustrated as `2000`
- `response_desc`, illustrated as `SUCCESS` and `Invalid Request`

No DDL, primary key, uniqueness constraint, foreign-key relationship, or retention policy is provided. The related task table is unnamed.
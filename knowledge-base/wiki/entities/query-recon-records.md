---
type: entity
title: queryReconRecords
created: 2026-08-24
updated: 2026-08-24
tags: [rest-api, accounting, reconciliation, korea, ebbs]
related: [tlm, fmaa, ratan-accounting-request-task-history, korea-tlm-accounting-reconciliation, fmaa-authenticated-accounting-retrieval]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Swift Generation & Settlement Accounting Tech design/Korea Accounting - TLM Recon.md"]
---
# queryReconRecords

`queryReconRecords` is the RATAN endpoint for retrieving Korea accounting records in EBBS JSON format for TLM reconciliation.

```text
GET /api/ratan/v1/accounting/queryReconRecords
```

Mandatory query parameters are `startReleaseTime`, `endReleaseTime`, and `fmidList`. Selection is based on [[ratan-accounting-request-task-history]] `created_at`, with an inclusive start boundary and exclusive end boundary. The maximum interval is 72 hours.

The API requires FMAA credentials and should be called with `Accept-Encoding: gzip`. Its canonical response fields, timestamp format, timezone, and multi-FMID behavior remain unresolved in [[what-is-the-canonical-korea-tlm-recon-api-response-schema]], [[what-is-the-authoritative-timezone-for-korea-accounting-recon-release-times]], and [[does-query-recon-records-support-multiple-fmids-or-only-10036645]].
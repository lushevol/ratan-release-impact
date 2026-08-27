---
type: query
title: What Is the Authoritative Timezone for Korea Accounting Recon Release Times?
created: 2026-08-24
updated: 2026-08-24
tags: [timezone, korea, accounting, reconciliation, api]
related: [query-recon-records, korea-tlm-accounting-reconciliation, ratan-accounting-request-task-history]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Swift Generation & Settlement Accounting Tech design/Korea Accounting - TLM Recon.md"]
---
# What Is the Authoritative Timezone for Korea Accounting Recon Release Times?

The parameter specification says request timestamps must be converted to GMT, but request examples have no timezone suffix and scenario timestamps appear to be local timestamps. Response publication timestamps also use a space-separated format without an offset.

Confirm the timezone and serialization rules for `startReleaseTime`, `endReleaseTime`, task-history `created_at`, and response publication timestamps. This is required to prevent Korea day-boundary omissions or duplicate reconciliation.
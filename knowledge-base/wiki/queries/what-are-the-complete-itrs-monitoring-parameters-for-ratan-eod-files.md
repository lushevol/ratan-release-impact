---
type: query
title: What Are the Complete ITRS Monitoring Parameters for RATAN EOD Files?
created: 2026-08-22
updated: 2026-08-22
tags: [itrs, monitoring, ratan, eod, aspire, operations]
related: [itrs, ratan, controlm, aspire, itrs-to-control-m-file-monitor-mapping, 26-auto-netting-page-md-files--77-ratan-51358-ratan-51358-ratan-infra-control-m-job-details-ratan--p7oaav]
sources: ["RATAN - 51358/RATAN/RATAN -Infra/Control-M Job Details RATAN.md"]
---
# What Are the Complete ITRS Monitoring Parameters for RATAN EOD Files?

The inventory maps four Aspire accounting output filenames to Control-M jobs, but it does not include the monitor configuration needed to operate or audit EOD monitoring.

## Information needed

For each of `RATAN_PAYMENT_TRANSACTION_HK`, `RATAN_PAYMENT_TRANSACTION_TH`, `RATAN_PAYMENT_TRANSACTION_TW`, and `RATAN_PAYMENT_TRANSACTION_JE`, obtain:

- ITRS monitor ID and monitored directory or endpoint.
- Expected file-arrival time, timezone, business calendar, and tolerance window.
- Completeness, size, duplicate-file, and content-validation conditions.
- Alert severity, routing, escalation owner, and acknowledgement requirements.
- Control-M dependency relationship and operational recovery runbook.

The available filename-to-job traceability is documented in [[itrs-to-control-m-file-monitor-mapping]].
---
type: concept
title: Cashflow Data Retention Lifecycle
tags: [cashflow, retention, archival, cold-storage, purge]
related: [cash-settlement-home-page, hot-warm-cashflow-retrieval, historical-cashflow-immutability]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Archival & Retrieval.md"]
---
# Cashflow Data Retention Lifecycle

The source proposes a tiered lifecycle for cashflows managed by the [[cash-settlement-home-page]]:

1. **Hot:** Recent records in the Production Database, with a proposed duration of six months.
2. **Warm:** Older operationally retrievable records in an Archival Database, proposed from six months to five years.
3. **Cold:** Records in offline storage after five years until the applicable country retention schedule expires.
4. **Purged:** Records removed after the applicable retention period; timing and controls are unspecified.

These durations are proposals rather than approved requirements. The source provides no completed country-by-country values, purge rules, service levels, archival implementation, or authoritative lifecycle timestamp.

## Governance Requirements

A complete lifecycle policy must define:

- Retention duration for each FMID or jurisdiction.
- The date used to calculate retention.
- Physical movement triggers and retry or reconciliation behavior.
- Country-specific cold-storage and purge schedules.
- Legal holds, audit access, and deletion evidence.
- Access, export, and authorization behavior for each tier.

The source lists both country-coded and location-labelled FMID records. Their authoritative mapping is not established, and FMID `400991880` appears in both the `SA` and Saudi Arabia entries.

## Key Distinction

Logical retrieval tier and physical storage tier should not be treated as equivalent until the six-month query boundary is reconciled with the proposed movement rule of 15 months after trade expiry. This distinction is central to the [[hot-warm-cashflow-retrieval]] design.

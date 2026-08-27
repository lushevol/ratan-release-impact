---
type: query
title: What Is the Approved Indonesia Business Timezone and Temporal Data Model?
created: 2026-08-24
updated: 2026-08-24
tags: [ratan-indonesia, timezone, business-date, settlement, postgresql, java]
related: [utc-runtime-and-database-timezone-standardization, java-localdatetime-and-postgresql-timestamp-semantics, cash-settlement-platform, ratan-indonesia, postgresql, ratan-indonesia-onshoring-2026, rdm-api-based-holiday-compensation, ratan-indonesia-dual-environment-uat, what-is-the-approved-indonesia-rdm-api-schedule-and-data-freshness-sla, what-are-the-indonesia-ratan-production-nfr-acceptance-criteria]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/UTC Time zone impact - Indonesia.md"]
---
# What Is the Approved Indonesia Business Timezone and Temporal Data Model?

## Question

Which timezone defines Indonesia business dates, settlement cutoffs, holiday processing, accounting dates, and reports, and which Java and PostgreSQL temporal types are approved for each category of data?

## Why this is open

The source recommends UTC defaults for JVM and PostgreSQL runtime behavior, but it does not distinguish operational timestamps from local business-date rules. It also does not specify PostgreSQL timestamp types, Java-to-database mappings, scheduler technology, or session-level timezone controls.

A UTC infrastructure baseline does not by itself establish the applicable local date boundary for Indonesia settlement and holiday logic.

## Decisions needed

- Confirm whether all operational event timestamps are stored and exchanged as UTC instants.
- Identify the authoritative Indonesia business timezone, including whether `Asia/Jakarta` applies to settlement cutoffs and date-only rules.
- Approve mappings among `Instant`, `OffsetDateTime`, `ZonedDateTime`, `LocalDateTime`, PostgreSQL `timestamp`, and `timestamptz`.
- Identify the scheduler used by Indonesia batch jobs and require explicit trigger timezone configuration where available.
- Define PostgreSQL timezone enforcement across server, database, role, pool, and session layers.
- Define retention, audit, reconciliation, and reporting timezone conventions.

## Validation scenarios

UAT should include regression cases at UTC midnight and at the approved Indonesia business-date boundary. Tests should cover scheduled jobs, `current_date`, cashflow processing, RDM holiday compensation, and reconciliation between Java and PostgreSQL calculations.

This query informs [[ratan-indonesia-onshoring-2026]], [[ratan-indonesia-dual-environment-uat]], and [[rdm-api-based-holiday-compensation]].
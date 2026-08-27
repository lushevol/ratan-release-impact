---
type: query
title: What Is the Authoritative Auto Netting Cutoff Time Semantics?
created: 2026-08-22
updated: 2026-08-22
tags: [query, cutoff-time, business-calendar, time-zone, auto-netting, RATAN]
related: [business-calendar-relative-netting-time, cashflow-auto-netting, auto-netting-rule-management]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Cashflow Auto Netting- 2024.md"]
---
# What Is the Authoritative Auto Netting Cutoff Time Semantics?

## Question

How should RATAN calculate and enforce the auto-netting cutoff when a cashflow arrives near, or after, the configured `VD`, `VD-1`, or `VD-2` time?

## Ambiguities

The requirement states that a cashflow received after the netting datetime is sent to Pending Netting, but it does not define:

- Whether event time or ingestion time is authoritative.
- Which time zone applies to the configured time and comparison.
- How non-business days and calendar holidays roll forward or backward.
- Whether `VD` means payment date, valuation date, or another date.
- Which calendar service is authoritative.
- How clock skew and delayed upstream delivery are handled.

## Required Resolution

Confirm the scheduling contract, calendar-service behavior, time-zone rules, and late-arrival processing with the RATAN implementation and approved settlement operations documentation.

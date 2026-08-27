---
type: query
title: What Is the Authoritative Cashflow Version Key for Failed Reprocessing?
created: 2026-08-23
updated: 2026-08-23
tags: [open-question, cashflow-versioning, event-lineage, correlation, failed-cashflow]
related: [failed-cashflow-accounting, cashflow-event-versioning, trade-event-id-lineage, cashflow-lifecycle-supersession-and-audit-history]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Failed Process/Failed Cashflow Accounting.md"]
---

# What Is the Authoritative Cashflow Version Key for Failed Reprocessing?

## Question

Which identifier distinguishes multiple cashflow versions and events when the same cashflow ID is reused across `New` and `Amendment` processing?

## Evidence

All examples use cashflow ID `C101`, including the original `New` event, the later `Amendment`, repeated failure, and final re-processing. The source includes `minorVersionDescription` as a column but does not define its permitted values or semantics.

## Why It Matters

Accounting corrections and Swift generation must apply to the correct cashflow version. Reusing the same ID without an authoritative event or version key creates a risk that an older failed or accounted state will be confused with the latest amendment.

## Current Position

Unresolved. The required correlation may use an event ID, minor version, business version, event timestamp, or another identifier not specified in this requirement.
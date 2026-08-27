---
type: query
title: Who Owns and Governs RatanOne Nostro Static Data?
created: 2026-08-24
updated: 2026-08-24
tags: [open-question, Nostro, RatanOne, governance, maker-checker, audit]
related: [ssi-stamping-reference-data, database-first-static-data-caching, static-reference-data-synchronization]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/The Cache Data Layer Design.md"]
---

# Who Owns and Governs RatanOne Nostro Static Data?

## Question

Which RatanOne team or service owns Nostro data, and what controls govern its manual initialization and dump-based updates?

## Evidence

Nostro data is described as RatanOne-owned, approximately 100,000 records in 2022, manually initialized, and updated through new-data dumps. The source does not identify authoritative tables, a maintenance workflow, approval roles, validation rules, audit requirements, or distribution and cache-refresh semantics.

## Required resolution

Define the authoritative owner, database schema, change process, maker-checker or segregation-of-duties controls, validation rules, audit trail, rollback process, data-quality checks, and synchronization contract for cached Nostro records.

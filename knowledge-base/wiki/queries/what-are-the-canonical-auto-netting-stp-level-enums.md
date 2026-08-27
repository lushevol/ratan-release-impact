---
type: query
title: What Are the Canonical Auto Netting STP Level Enums?
tags: [auto-netting, stp-level, configuration, data-governance]
related: [cashflow-auto-netting, auto-netting-rule-management, ratan]
created: 2026-08-22
updated: 2026-08-22
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Ratan One Processing Guide (DOI).md"]
---
# What Are the Canonical Auto Netting STP Level Enums?

The RATAN ONE Processing Guide gives inconsistent representations of auto-netting STP levels.

Its static-data section lists:

- `NSTP_MAKER_CHECKER`
- `NSTP_CHECKER_ONLY`

Its process section states that an auto-netting resultant may require `maker_checker`, `checker_only`, or `full_stp`.

## Why this matters

The configured STP level determines whether an auto-netting resultant remains subject to approval and therefore affects release readiness, control evidence, and operational queue management.

## Required resolution

Confirm:

1. The authoritative enum values accepted by RATAN configuration.
2. Whether `full_stp` is implemented and available in production.
3. Whether the uppercase and lowercase forms are display labels, legacy values, or distinct values.
4. The resultant lifecycle and exception behavior for each level.

Until resolved, configuration changes should be validated against the deployed rule-management interface and release-specific technical specification.
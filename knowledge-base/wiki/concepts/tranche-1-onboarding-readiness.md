---
type: concept
title: Tranche 1 Onboarding Readiness
created: 2026-08-22
updated: 2026-08-22
tags: [onboarding, readiness, cash-settlement, configuration, testing]
related: ["entity-branch-onboarding", "post-implementation-testing", "2025-tranche-1-hk-tw-th-onboarding"]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/New Entity onboarding checking list/2025 Tranch1 (HK, TW, TH) Onboarding.md"]
---

# Tranche 1 Onboarding Readiness

Tranche 1 cash-settlement readiness is primarily a multi-system configuration and static-data exercise. Required work includes routing lists, feed exclusions, Murex migration configuration, SWIFT generation, currency release times, SSI hierarchy, settlement accounting, GUI controls, Vostro and Nostro setup, business rules, and firewall access.

The checklist does not establish go-live completion. It marks firewall access as done but leaves NDS Auto Netting and Pending Fixing STP/NSTP blacklists as `TBD`. Validation applicability is tentative, and UAT and regression testing are marked not required without documented justification.

## Readiness evidence needed

A reliable readiness record should separately identify the owner, implementer, applicability, status, evidence, and approval for each workstream. It should also record the canonical entity and product identifiers and confirm the exact Tranche 1 scope.

## Testing consideration

Changes to routing, SWIFT, accounting, SSI selection, and static data can have operational consequences. The source's “No” entries for UAT and regression testing should be treated as an explicit decision requiring rationale, rather than as proof that testing is unnecessary.
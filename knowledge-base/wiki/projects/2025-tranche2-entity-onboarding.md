---
type: project
title: 2025 Tranche 2 Entity Onboarding
status: planned
owner: Dev Team
start_date: 2025-01-01
target_date: ""
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, entity-onboarding, tranche-2, readiness]
related: ["entity-branch-onboarding", "2025-tranche2-onboarding-readiness"]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/New Entity onboarding checking list/2025 Tranch2 Onboarding.md"]
---

# 2025 Tranche 2 Entity Onboarding

## Purpose

Coordinate the configuration and readiness work required to onboard the 2025 Tranche 2 Cash Settlement entities and branches across settlement, accounting, messaging, static-data, and downstream systems.

## Scope

The source names Mauritius, Dubai, DIFC, Jakarta, Manila, Philippines FCU, Tokyo, and Johanesburg as the go-live locations. A normalized mapping from each location to legal entity, branch, booking entity, FMID, BIC, and accounting identifiers is still required.

## Workstreams

1. **Routing and suppression:** Configure BCS versus strategic routing, RAZOR or RATAN handling, Cashflow Suppression, and related business rules.
2. **Messaging:** Configure entity-specific FMIDs, sender BICs, Field 53, Field 58, receiver BICs, and branch mappings.
3. **Accounting:** Configure bridge accounts, EBBS branch codes, transaction types, and branch-specific accounting exceptions.
4. **Static data:** Complete Nostro and Vostro setup, including branch-specific SSI for over-account clients.
5. **Application and access:** Update LMS, Cashflow Blotter, Dashboard, Vostro SI Input Screen, and firewall access.
6. **Testing and assurance:** Complete downstream analysis, UAT, and regression testing.

## Current Readiness

Firewall access is the only item explicitly marked `Done`. UAT and regression testing are marked `No`. The NDS Auto Netting and Pending Fixing STP/NSTP blacklists remain `TBD`, and several checklist rows have no clear completion status.

The project should not be treated as go-live ready without completion evidence for configuration, static data, downstream sign-off, UAT, and regression testing. Readiness is tracked in [[2025-tranche2-onboarding-readiness]].

## Ownership

- Dev Team: CRs, firewall access, downstream engagement, and regression testing.
- Data Ops: static data and business-rule setup.
- Settlement Ops: UAT.
- Yang Chen: routing whitelist, currency release time, and Nostro-related setup.
- Mingyang Zhong: LMS filter and SWIFT-generation changes.
- Chongxuan Li and Guiling Wang: settlement accounting and business-rule-related work.
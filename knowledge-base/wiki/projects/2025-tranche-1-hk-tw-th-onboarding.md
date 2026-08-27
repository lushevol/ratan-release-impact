---
type: project
title: 2025 Tranche 1 HK TW TH Cash Settlement Onboarding
status: planned
owner: "Dev Team and Data Ops"
start_date: 2025-01-01
target_date: ""
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, onboarding, 2025-tranche-1, configuration]
related: ["entity-branch-onboarding", "tranche-1-onboarding-readiness", "legacy-versus-strategic-cash-settlement-routing", "entity-specific-swift-generation", "cash-settlement-2025-roadmap"]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/New Entity onboarding checking list/2025 Tranch1 (HK, TW, TH) Onboarding.md"]
---

# 2025 Tranche 1 HK TW TH Cash Settlement Onboarding

## Objective

Configure the cash-settlement ecosystem for the 2025 Tranche 1 entities identified as Hong Kong, Taiwan, and Thailand. The work spans application configuration, static data, routing, messaging, accounting, settlement instructions, and operational controls.

## Scope

The checklist identifies:

- HK, TW, and TH as the CPT list.
- LMS blacklist updates for `TH` and `TW`, alongside legacy exclusions.
- RAZOR and RATAN routing configuration.
- Entity-specific SWIFT and branch configuration.
- Currency release times.
- SSI hierarchy and its entity/product exceptions.
- EBBS, bridge-account, Vostro, Nostro, GUI, and business-rule setup.
- Firewall access for users in the new location.

New York is named in the referenced readiness-page title but is not included in the checklist title. It must not be treated as in scope until confirmed.

## Delivery status

The source is a requirements checklist, not a completion record. Firewall access is marked done. NDS Auto Netting and Pending Fixing STP/NSTP blacklists remain `TBD`; UAT and regression testing are marked not required, but the rationale is not documented.

## Dependencies and risks

- Confirm the authoritative entity scope.
- Resolve `LOANIQ` versus `LOANID`.
- Confirm whether validation remains necessary after post-MO validation moved to [[entities/fmrp]].
- Define final blacklists for [[entities/nds-auto-netting]] and pending-fixing controls.
- Confirm SWIFT BIC, FMID, branch, accounting, and settlement-instruction data.
- Define the volume threshold determining whether [[entities/razor]] or [[entities/data-ops]] performs Nostro static setup.
- Reassess the absence of UAT and regression testing before go-live.

## Retrospective

No implementation or post-go-live evidence is included in the source. Add a retrospective after completion, including configuration evidence, testing outcomes, ownership decisions, and production issues.
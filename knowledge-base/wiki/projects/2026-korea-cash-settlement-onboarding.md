---
type: project
title: "2026 Korea Cash Settlement Onboarding"
status: planned
owner: "Dev Team"
start_date: 2026-08-22
target_date: 2026-12-31
created: 2026-08-22
updated: 2026-08-22
tags: [Korea, cash-settlement, RATAN, onboarding, migration]
related: ["korea", "configuration-driven-onboarding", "entity-branch-onboarding", "legacy-versus-strategic-cash-settlement-routing", "entity-specific-swift-generation", "settlement-accounting", "nostro-static-management"]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement/Korea Migration/New Entity onboarding checking list - Korea 2026.md"]
---
# 2026 Korea Cash Settlement Onboarding

## Purpose

Onboard the Korea-related booking entity or entities into RATAN for the 2026 cash-settlement migration using configuration, static data, controlled CR deployment, downstream engagement, and formal testing.

## Scope

The planned work covers:

- Entity and branch setup.
- Legacy versus strategic routing determination.
- Entity-specific SWIFT and Tag 20 configuration.
- Release-cutoff, currency, Nostro, Vostro, and accounting static data.
- NDS Auto Netting, Pending Fixing, suppression, NSTP, and netting rules.
- GUI dropdown and query updates.
- Firewall and downstream-system assessment.
- UAT, regression testing, and CPT.

## Current status

The source is an onboarding checklist and does not confirm that implementation, testing, or go-live has occurred. The project remains planned until the authoritative entity scope, routing model, static data, CRs, and test evidence are confirmed.

## Key dependencies

- [[entities/korea]]
- [[entities/ratan-settlement]]
- [[entities/murex]]
- [[entities/lms]]
- [[entities/ebbs]]
- [[entities/fmmis]]
- [[entities/loaniq]]
- [[entities/bcs]]
- [[entities/stella]]
- [[concepts/nostro-static-management]]
- [[concepts/entity-specific-swift-generation]]
- [[concepts/settlement-accounting]]
- [[concepts/pending-fixing]]
- [[entities/nds-auto-netting]]

## Readiness gates

1. Confirm the booking-entity and branch list.
2. Resolve whether Korea follows legacy or strategic routing.
3. Obtain FMID, sender BIC, Field 53/58 BICs, receiver BIC, branch, currency, cutoff, accounting, and SSI data.
4. Finalise LMS feeding and source-system/Tag 20 ownership.
5. Finalise NDS Auto Netting and Pending Fixing blacklists.
6. Complete Nostro and Vostro static data with maker/checker controls.
7. Deploy required CRs and firewall changes.
8. Obtain downstream confirmations from RATAN EOD, SSDR, CIS, FMMIS, LMS, and eBBS.
9. Complete UAT, regression testing, and CPT with recorded acceptance evidence.

## Risks

- Korea is not included in the listed strategic-flow whitelist.
- The New MO Validation Model may not be confirmed as live for the relevant flows.
- Required blacklists and entity-specific static data remain unresolved.
- “Configuration-only” onboarding still depends on technical deployment and controlled releases.
- Entity names and FMIDs in the LMS reference table may require data-quality correction.
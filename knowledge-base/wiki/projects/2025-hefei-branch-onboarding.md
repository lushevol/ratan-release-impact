---
type: project
title: 2025 Hefei Branch Onboarding
created: 2026-08-22
updated: 2026-08-22
tags: [hefei, onboarding, cash-settlement, 2025]
related: [hefei-branch, hefei-strategic-settlement-routing, settlement-accounting, swift-mt-mx-integration, cashflow-blotter, is-post-mo-validation-required-for-hefei, are-hefei-uat-and-regression-tests-required, what-is-the-hefei-razor-ratan-routing-rule]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/New Entity onboarding checking list/2025 Hefei Branch Onboarding.md"]
status: planned
owner: ""
start_date: ""
target_date: ""
---
# 2025 Hefei Branch Onboarding

## Objective

Onboard [[hefei-branch]] into the cash-settlement operating model through required validation, routing, SWIFT, accounting, GUI, and access configuration.

## Required configuration scope

- Confirm the post-MO validation treatment following its move to [[fmrp]].
- Include China in the strategic routing whitelist and configure the associated cashflow-suppression routing.
- Configure branch-specific SWIFT identifiers and message fields.
- Configure currency release time.
- Configure [[settlement-accounting]] mappings and the EBBS bridge account.
- Add the branch to [[cashflow-blotter]] and Dashboard dropdowns.
- Open firewall access for users in the new location.

## Named release owners

- Bypass Validation Rule: Xinmiao Huang
- Strategic routing and SWIFT changes: Mingyang Zhong
- Currency Release Time: Chen Yang
- Settlement Accounting: Chongxuan Li
- GUI dropdown configuration: Guiling Wang

## Scope handled separately or marked not required

LMS entity-list updates, Murex Cash Migration batch configuration, NDS Auto Netting, pending-fixing STP/NSTP controls, SSI-stamping changes, currency mapping, Vostro SI screen changes, rounding, and downstream engagement are marked as not required for Hefei or otherwise outside this configuration workstream.

Nostro and Vostro static setup are assigned to Data Ops rather than this workstream.

## Delivery risks

- The checklist does not establish deployment, approval, or test completion for most required items.
- MT604/605 receiver BICs and Field 20 requirements are unspecified.
- UAT and regression testing are marked “No” despite changes to routing, SWIFT, accounting, and GUI behavior.
- Branch naming is inconsistent across source records.
- The routing decision boundary between [[razor]] and [[ratan]] is incomplete.

## Open questions

- [[is-post-mo-validation-required-for-hefei]]
- [[are-hefei-uat-and-regression-tests-required]]
- [[what-is-the-authoritative-hefei-entity-name]]
- [[what-is-the-hefei-razor-ratan-routing-rule]]
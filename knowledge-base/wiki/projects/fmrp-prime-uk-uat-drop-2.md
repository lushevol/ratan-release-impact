---
type: project
title: FMRP Prime UK UAT Drop 2
status: planned
owner: ""
start_date: ""
target_date: ""
created: 2026-08-22
updated: 2026-08-22
tags: [fmrp, prime-uk, uat, cash-settlement, re-platforming]
related: [fmrp, murex, ratan, stella, razor, aspire, irs, ccs, loan-depo, fmrp-prime-uk-uat-drop-2-checklist, ssi-stamping, auto-netting, cashflow-suppression, swift-mt-mx-integration, cashflow-migration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/F2B Milestone Onboarding check list/F2B Milestone Checklist - Prime Day 2.md"]
---
# FMRP Prime UK UAT Drop 2

## Purpose

This project covers onboarding and UAT validation for IRS, CCS, and Loan Depo in the FMRP Prime UK re-platforming scope.

## Workstreams

- **SSI and Nostro controls:** Validate SSI hierarchy, CFI codes, settlement methods, agent counts, CDUPS stamping, Vostro handling, and Nostro selection.
- **Cashflow operations:** Validate Dashboard, Group Pending, Group Pending Validation, Settlement Queue routing, and rates derivatives team filtering.
- **Netting:** Validate IRS interest auto-netting, ND IRS behavior, and cross-product netting between STELLA and Murex cashflows.
- **Rules and suppression:** Demonstrate NSTP, SWIFT suppression, cashflow suppression, clearing-portfolio suppression, and Murex-to-STELLA rule parity.
- **Messaging and accounting:** Validate the required SWIFT MT/MX generation and accounting generation for EBBS and Aspire.
- **Migration:** Validate duplicate-payment prevention, cutover handling, near-value cashflows, and historic past-value events.
- **Product onboarding:** Validate Loan Depo pending-fixing configuration and GUI visibility.
- **Currency configuration:** Validate SGO mapping to SGD and automatic SGO Nostro and Vostro attachment.

## Dependencies and risks

Downstream connectivity is unavailable in the described UAT environment, so Dev team replay is required for SWIFT and accounting scenarios. Replay evidence must be distinguished from live delivery, acknowledgment, and downstream reconciliation evidence.

The `UK MXGBLANK` SSI selection issue is an unresolved configuration risk in the source checklist. Applicability fields left blank require scope confirmation. Murex-to-STELLA rule parity is a stated requirement but is not demonstrated by the checklist.

## Scope exclusions

The checklist marks BIC Netting, NDS Auto Netting, DVP, Vostro SSI screen settlement-means changes, and rounding as not applicable for Prime. Principal plus Interest Netting is generally excluded, with internal counterparties noted as an exception.

## Completion evidence required

Completion should include executed test cases, pass/fail results, defect references, generated-message validation, accounting and reconciliation evidence, replay logs, migration test-pack results, named sign-off owners, and a formal UAT or go-live decision.
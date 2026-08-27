---
type: entity
title: FMMIS
created: 2026-08-22
updated: 2026-08-22
tags: [FMMIS, STP, NSTP, controls, settlement, downstream-system, integration]
related: ["f2b", "fmrp", "straight-through-processing", "high-risk-nstp-rule", "entity-branch-onboarding", "ratan", "cashflow-auto-netting"]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/F2B Milestone Onboarding check list.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting.md"]
---
# FMMIS

## Role in STP/NSTP controls

The onboarding checklist identifies FMMIS as a reporting or control touch point for STP/NSTP calculation.

The checklist requires any new FMRP actions to be reflected in FMMIS so that STP/NSTP calculations remain complete. The named events are:

- Booking
- Withdrawal
- Amendment
- Early termination
- Fixing
- Refixing
- Clearing
- Novation
- Close out
- Portfolio reassignment
- Undo
- Maturity
- Expiry

## Settlement Day 2 integration

The Settlement Day 2 cashflow auto-netting source references FMMIS as a potential downstream consumer or query client for cashflow auto-netting data from [[ratan]].

That source records a need to confirm whether FMMIS can query the relevant data or should receive updates. It does not establish an implemented interface, data contract, ownership model, or initial-scope commitment.

## Information not defined by the sources

The onboarding checklist does not define the FMMIS interface, action schema, ownership, or test evidence. The Settlement Day 2 cashflow auto-netting source likewise does not establish an implemented interface, data contract, ownership model, or initial-scope commitment.
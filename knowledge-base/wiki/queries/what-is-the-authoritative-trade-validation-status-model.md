---
type: query
title: What Is the Authoritative Trade Validation Status Model?
created: 2026-08-24
updated: 2026-08-24
tags: [open-question, trade-validation, status-model, RATAN, Murex-2-11]
related: [trade-validation-cashflow-gating, cashflow-lifecycle-state-model, ratan, murex-211, stella]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade Validation & Cashflow Process/RATAN Settlement Control on Trade Validation.md"]
---
# What Is the Authoritative Trade Validation Status Model?

## Question

What are the canonical meanings, ownership, and transitions for the trade and settlement statuses shown in the requirement?

## Statuses requiring definition

The source uses or references:

- `CHCK`
- `VALD`
- `COMP`
- `INIT`
- `SNTR`
- `CNCL`
- `STP`
- `NSTP`
- `Pending Validation`

The document does not identify which system owns each status, which status qualifies as validated, or how trade status maps to cashflow-ingestion eligibility and settlement release.

## Information needed

A canonical status dictionary should specify the system of record, allowed transitions, effective timing, trade-to-cashflow matching key, and behavior for cancellations, amendments, reversals, rebooks, and manual pushes.
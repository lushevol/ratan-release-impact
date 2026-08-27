---
type: concept
title: Netting API Contract
created: 2026-08-23
updated: 2026-08-23
tags: [netting, API, GUI, validation, RATAN]
related: [ratan, razor, cashflow-netting, bilateral-netting-eligibility, netting-resultant-cashflow, what-is-the-authoritative-manual-netting-and-un-netting-eligibility-matrix, what-is-the-authoritative-razor-release-validation-for-netting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Netting Service - GUI & API intergration.md"]
---
# Netting API Contract

The RATAN netting API receives cashflow identifiers and displayed economic attributes from the GUI, but must re-query the current backend records for all selected component cashflows. GUI-provided attributes are therefore request context, not the authoritative basis for execution.

## Backend validation

The backend requirement permits components only when all are true:

- State is `Projected`, `Queued`, `Pending`, or `Validated`.
- Netting Id is blank.
- Payment currency is identical across components.
- Payment date is identical across components.
- Booking entity SCI FMID is identical across components.
- Counterparty SCI FMID is identical across components.

The stated check that a current or prior component version was not sent to [[razor]] remains TBC.

## Un-net contract

An un-net request identifies a resultant cashflow and Netting Id. RATAN re-queries the resultant and validates that its Netting Id is present and its state is `Queued`, `Pending`, or `Validated`. It then queries the associated components by Netting Id.

The source conflicts with its high-level GUI guide, which also lists `Hold` as eligible for un-netting. See [[what-is-the-authoritative-manual-netting-and-un-netting-eligibility-matrix]].

## Component lookup

The GUI can request underlying netting components using a Netting Id. The backend queries and returns the associated component cashflows for display.
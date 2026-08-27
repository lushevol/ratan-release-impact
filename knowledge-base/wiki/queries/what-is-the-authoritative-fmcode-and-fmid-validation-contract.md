---
type: query
title: What Is the Authoritative FMCODE and FMID Validation Contract?
created: 2026-08-24
updated: 2026-08-24
tags: [open-question, fmcode, fmid, validation, bpsi, legal-entity]
related: [bpsi, cashflow-precheck-validation, cashflow-lifecycle-stamping, lifecycle-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Cashflow Lifecycle Stamping Logic.md"]
---
# What Is the Authoritative FMCODE and FMID Validation Contract?

## Question

Are FMCODE and FMID distinct identifiers, aliases, or inconsistent terminology for the same legal-entity data?

## Evidence

The requirements identify booking-entity and counterparty FMCODEs as mandatory for Day 1 China. The validation list instead refers to entity and counterparty FMIDs, including a duplicated entity FMID check.

The source does not define:

- Which identifier is required for each party.
- The authoritative lookup system.
- Whether BPSI supplies FMCODE, FMID, or both.
- Validation error codes and messages.
- Behavior when an identifier is missing, stale, or unavailable.

## Current position

The terms must not be treated as interchangeable until the identifier and validation contract is confirmed.

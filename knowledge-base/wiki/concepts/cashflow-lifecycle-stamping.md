---
type: concept
title: Cashflow Lifecycle Stamping
created: 2026-08-24
updated: 2026-08-24
tags: [cashflow, lifecycle, stamping, enrichment, cash-settlement]
related: [lifecycle-service, data-persistence-node, bpsi, cashflow-precheck-validation, lien-stamping-and-re-stamping, pending-fixing-flag-processing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Cashflow Lifecycle Stamping Logic.md"]
---
# Cashflow Lifecycle Stamping

Cashflow lifecycle stamping is the enrichment of an incoming cashflow with party, client, event, beneficiary, and future processing attributes before lifecycle execution.

## Proposed ownership

The source proposes that stamping move from the Data Persistence Node into a separate API and reusable lifecycle action within [[entities/lifecycle-service]]. The intended benefit is to prevent expanding business-enrichment logic from remaining coupled to persistence.

The design names reinstate as a potential reuse path. It does not establish that the API or action has been implemented.

## Stamped attributes

The initial mandatory scope is booking entity FMCODE and counterparty FMCODE for Day 1 China. Additional attributes are listed as optional:

- Client Type.
- Reversal / Rebook.
- Client domicile country.
- Client BIC.
- `LIEN AMOUNT`.
- Pending Fixing Flag.

Legal-entity enrichment includes `FMCODE`, `FMTYPE`, `DOMICILECOUNTRY`, and `ADDRLINE` for `party1` and `party2`. The source also mentions event-reason and beneficiary `bic` enrichment.

## Architectural boundary

The proposed boundary separates:

- Persistence of `RatanStellaMessageEvent`.
- Construction of SCBML and lifecycle requests.
- Attribute enrichment and validation.
- Lifecycle execution.

The exact API contract, transaction boundary, authorization, idempotency, retries, and failure recovery remain unspecified.

## Caveat

The source uses both FMCODE and FMID terminology. Their relationship and authoritative validation source require confirmation; they should not be treated as interchangeable without an explicit contract.

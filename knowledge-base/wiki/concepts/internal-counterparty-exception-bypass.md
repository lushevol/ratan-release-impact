---
type: concept
title: Internal Counterparty Exception Bypass
tags: [cash-settlement, exception-handling, internal-counterparty, controls, STP]
related: [inter-entity-cashflow-stp, hard-blocker-exception, settlement-day-2]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Inter Entity STP.md"]
---
# Internal Counterparty Exception Bypass

Internal counterparty exception bypass is the proposed use of an internal-counterparty identifier to allow eligible inter-entity cashflows to bypass otherwise applicable exceptions during STP processing.

## Documented intent

The requirement calls for an internal-counterparty identifier that can be used to bypass exceptions in the context of [[inter-entity-cashflow-stp]]. The source does not establish that every SCB counterparty is internal or that every internal counterparty is automatically eligible.

## Undefined control boundaries

The requirement does not specify:

- the identifier field, format, source system, or owning team;
- the values that qualify as internal;
- whether eligibility also requires MX classification;
- the exception classes subject to bypass;
- controls that are categorically non-bypassable;
- behavior for missing, stale, ambiguous, or inconsistent identifiers;
- authorization, audit logging, monitoring, reconciliation, fallback, or rollback behavior.

In particular, the source does not authorize bypassing [[hard-blocker-exception]], compliance or sanctions controls, settlement-risk validations, accounting controls, or message-generation controls. These boundaries require explicit confirmation in [[which-exceptions-may-internal-counterparties-bypass]].
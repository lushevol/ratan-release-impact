---
type: entity
title: BPSI
created: 2026-08-24
updated: 2026-08-24
tags: [bpsi, cash-settlement, dependency, fmcode, integration, cashflow, enrichment, authentication, token, ratan, dqsl, sci]
related: [dqsl, cash-settlement-dependent-service-failure, cash-settlement-exception-handling, cashflow-lifecycle-stamping, cashflow-precheck-validation, lifecycle-service, sci, ratan-counterparty-data-integration, what-is-the-authoritative-ratan-dqsl-bpsi-sci-counterparty-api-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Exception Handling.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Cashflow Lifecycle Stamping Logic.md", "RATAN/RATAN -Interfaces/Ratan and BPSI-51437 & SCI-14768 (via DQSL 51129).md"]
---
# BPSI

BPSI is an integration dependency referenced in Cash Settlement and RATAN counterparty-information flows. Its documented responsibility differs by source context.

## Cash Settlement and cashflow stamping

The Cashflow Lifecycle Stamping Logic source describes BPSI as an integration used during Cash Settlement processing to retrieve booking-entity and counterparty FMCODE information for cashflow enrichment. It is accessed through [[dqsl]].

The original Day 1 China design integrated with BPSI to fetch booking-entity and counterparty FMCODEs. The cashflow stamping source explicitly identifies those FMCODEs as mandatory information for that phase.

That source documents BPSI as an integration dependency rather than as a fully defined validation authority. It does not specify:

- The BPSI API or message contract.
- Availability or timeout behavior.
- Caching requirements.
- Data ownership or authority.
- Retry and fallback behavior.
- The relationship between FMCODE and FMID.

## Cash Settlement exception and recovery behavior

According to the Exception Handling source, if BPSI is unavailable before FMCODE retrieval, the cashflow can become technically failed because Razor requires counterparty FMCODE. After BPSI recovers, OPS is notified to use `Reinstate`.

The same source records a separate post-FMCODE outcome involving two NSTP exceptions:

- `GSAM client Unknown`
- `CORP client Unknown`

That source does not resolve whether this post-FMCODE outcome should instead be classified as a technical failure.

## RATAN counterparty-information flow

The RATAN and BPSI interface source describes BPSI differently: BPSI is the authentication dependency in the documented RATAN counterparty-information flow. [[dqsl]] invokes the BPSI API to obtain a valid token required to access [[sci]].

In that RATAN integration, the source explicitly states that BPSI is used only for authentication and does not provide business data. BPSI must therefore not be treated as the source of counterparty information in this integration; [[sci]] is the stated business-data source.

This authentication-only statement is specific to the documented RATAN flow and is separate from the Cashflow Lifecycle Stamping Logic source's description of BPSI FMCODE retrieval.

## RATAN authentication unknowns

The RATAN and BPSI interface source does not define:

- Token type.
- Authentication grant.
- Scopes.
- Expiry.
- Renewal process.
- Authorization model.
- Error handling.

These details remain open in [[what-is-the-authoritative-ratan-dqsl-bpsi-sci-counterparty-api-contract]].
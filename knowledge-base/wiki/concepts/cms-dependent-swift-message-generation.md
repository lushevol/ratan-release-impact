---
type: concept
title: CMS-Dependent SWIFT Message Generation
created: 2026-08-24
updated: 2026-08-24
tags: [cms, swift, mt103, mt202, vostro-ssi, static-data]
related: [25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--11-static-data--10-vostr--1jab0vj, mt202-beneficiary-institution-field-58a-resolution, field-70-72-customization-and-reference-id, manual-swift-tag-70-and-72-flags, notice-to-receive-mt210-control, ratanone-swift-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/Vostro SSI/Murex Vostro Analysis.md"]
---
# CMS-Dependent SWIFT Message Generation

CMS Account Holder status, represented in the source as `CMS_FLAG`, conditionally changes selected MT103 and MT202 SWIFT fields. The documented behavior is static-data-driven and must remain distinct from manual Tag 70/72 customization described in [[field-70-72-customization-and-reference-id]] and [[manual-swift-tag-70-and-72-flags]].

## Receiver BIC differs by message type

For CMS messages, MT103 Header Block 2 uses the account-holder BIC (`SWIFT_ACHL`), whereas MT202 Header Block 2 uses the organisation's entity BIC.

For non-CMS messages, both types first branch on `FIN_COPY`, but their first-choice BIC differs:

- MT103 uses Counterparty BIC when `FIN_COPY` is blank.
- MT202 uses Correspondent BIC, described as the Nostro field-53 `Corr.Code`, when `FIN_COPY` is blank.
- When `FIN_COPY` is not blank, both use intermediary code when populated; otherwise, they use `SWIFT_ACHL`.

These rules must not be generalized across MT103 and MT202.

## Field 53 for China entities

For CMS MT103 and MT202, a China entity with a populated CMS Account Number renders field 53a with the CMS Account Number on line 1 and the entity BIC on line 2. Otherwise, the source specifies an entity SWIFT code for MT103 and an entity BIC for MT202.

The source does not prove that “entity SWIFT code” and “our entity BIC” are identical fields. Non-CMS field 53 does not rely on CMS Account Number.

## Field 72 construction

The default field-72 construction is `SNDREC1` through `SNDREC6`, rendered line by line.

For Jakarta, products `NDF`, `IRS`, `CS`, and `FXO` are exceptions:

- With `CMS_FLAG=Y`, the source refers to unspecified product-specific field-72 logic.
- With `CMS_FLAG<>Y`, MT103 applies unspecified special logic only for `IDR`, `IRO`, or `IRY`.
- With `CMS_FLAG<>Y`, MT202 states a hardcoded field-72 output for the same Jakarta, currency, and product branch.

The product-specific outcomes and the literal MT202 output are unresolved in [[what-are-the-jakarta-cms-field-72-special-rules]] and [[what-is-the-literal-mt202-field-72-output-for-non-cms-jakarta-cashflows]]. `IRO` is retained as written in the source and is not normalized.

## Other documented scope

For MT103, non-CMS field 26T is applicable and uses `:26T:TOF` for AED payments. Field 56 is applicable only in the non-CMS column. The source states that field 57 is not affected by CMS for MT103, while indicating that CMS affects MT210 without defining the MT210 rules. It also states that field 77b is CMS-affected only for Dubai.

Claims of CMS impact on MT210 and MTX92 lack field-level detail; see [[how-does-cms-affect-mt210-and-mtx92]] and [[notice-to-receive-mt210-control]].
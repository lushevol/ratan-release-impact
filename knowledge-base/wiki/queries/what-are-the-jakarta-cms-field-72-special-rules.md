---
type: query
title: What Are the Jakarta CMS Field 72 Special Rules?
created: 2026-08-24
updated: 2026-08-24
tags: [open-question, jakarta, cms, swift, mt103, mt202, field-72]
related: [25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--11-static-data--10-vostr--1jab0vj, cms-dependent-swift-message-generation, field-70-72-customization-and-reference-id]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/Vostro SSI/Murex Vostro Analysis.md"]
---
# What Are the Jakarta CMS Field 72 Special Rules?

The source states that Jakarta cashflows for `NDF`, `IRS`, `CS`, and `FXO` use product-specific field-72 logic when `CMS_FLAG=Y`, but it does not supply the resulting values.

For non-CMS MT103, the same unspecified exception additionally requires currency `IDR`, `IRO`, or `IRY`. The required output should be confirmed separately for each product, CMS state, message type, and relevant currency.

## Evidence needed

- Functional specifications or implementation code defining each product-specific field-72 output.
- Test cases covering MT103 and MT202 CMS and non-CMS Jakarta branches.
- Confirmation whether `IRO` is an internal currency identifier, a legacy value, or a documentation error.
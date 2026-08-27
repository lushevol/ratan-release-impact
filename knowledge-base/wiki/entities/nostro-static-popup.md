---
type: entity
title: Nostro Static Popup
tags: [RATAN, static-data, Nostro, SSI, user-interface]
related: [ratan, nostro-type-static-data-model, portfolio-based-rfi-nostro-stamping]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/RFI Nostro stamping based on Portfolio.md"]
---

# Nostro Static Popup

The Nostro Static Popup is the RATAN static-data interface where users create and maintain Nostro records.

The requirement adds:

- A `Nostro Type` dropdown with `RFI` and `DEFAULT` values.
- A multi-value `Portfolio` field.
- A disabled `Primary` flag when `Nostro Type = RFI`.
- List-view visibility for Nostro Type and Portfolio.
- Duplicate validation using booking entity, currency, settlement means, settlement account, and Nostro Type.

Nostro Type must also be visible when users select an SSI in the adhoc SSI/split popup and in cashflow details.

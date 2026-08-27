---
type: concept
title: Korea Settlement Localization
tags: [korea, cash-settlement, localization, rounding, korean-language-support]
related: [korea, korea-settlement-accounting, korea-swift-mx-message-generation, korean-character-reporting, cash-settlement]
created: 2026-08-22
updated: 2026-08-22
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Korea Migration Functional Analysis.md"]
---
# Korea Settlement Localization

## Definition

Korea settlement localization is the set of Korea-specific data, message, accounting, and operational requirements that may need to be supported during the RATAN cashflow migration.

The source identifies these items as analysis topics, not confirmed requirements or implemented capabilities.

## Potential scope

- Korean-character support in SSI, SCI, and cashflow data.
- MT/MX customization for Korea.
- Accounting behavior specific to Korea.
- Rounding or processing that must “Keep without decimal.”
- Manual handling of OUR payments, TPP, and decimal differences by OSCAR.
- Ensis integration through Solace.

Each item requires functional and technical confirmation before being treated as part of the approved migration design.

## Risks and open boundaries

The checklist does not identify which currencies, products, fields, or message types are subject to no-decimal processing. It also does not define TPP, OSCAR, Ensis, or the control model for manual payment entry.

This concept is related to [[concepts/korean-character-reporting]], but the potential scope here is broader than reporting and includes settlement instructions, source data, cashflows, messages, and operational exceptions.
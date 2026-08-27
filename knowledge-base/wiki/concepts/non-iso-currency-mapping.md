---
type: concept
title: Non-ISO-to-ISO Currency Mapping
created: 2026-08-22
updated: 2026-08-22
tags: [currency-configuration, iso-currency, swift, accounting, settlement-instructions]
related: [fmrp-prime-uk-uat-drop-2, sgo, swift-mt-mx-integration, iso-20022-mx, ssi-stamping, nostro-configuration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/F2B Milestone Onboarding check list/F2B Milestone Checklist - Prime Day 2.md"]
---
# Non-ISO-to-ISO Currency Mapping

Non-ISO-to-ISO currency mapping converts an internal or non-standard currency identifier into the ISO currency representation required by settlement messages and accounting feeds. The checklist also includes precious-currency mapping.

The named acceptance scenario requires SGO to generate SWIFT and accounting as SGD, without SWIFT or accounting failure, with automatic SGO Nostro and Vostro attachment.

The source defines the expected mapping and outcomes but does not provide execution evidence or field-level message and accounting validation.
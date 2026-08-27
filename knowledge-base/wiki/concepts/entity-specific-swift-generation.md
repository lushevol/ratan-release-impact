---
type: concept
title: Entity-Specific SWIFT Generation
created: 2026-08-22
updated: 2026-08-22
tags: [swift, cash-settlement, onboarding, branch-configuration]
related: ["swift-mt-mx-integration", "settlement-message-routing", "settlement-accounting", "2025-tranche-1-hk-tw-th-onboarding"]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/New Entity onboarding checking list/2025 Tranch1 (HK, TW, TH) Onboarding.md"]
---

# Entity-Specific SWIFT Generation

New-entity onboarding requires SWIFT configuration at both entity and branch level. The checklist identifies the following fields and mappings:

- Booking Entity FMID.
- Booking Entity SWIFT BIC and sender BIC.
- Field 53 SWIFT BIC for LCY and Over Account.
- Field 58 SWIFT BIC for Flip MT202.
- Receiver BIC for MT604/605.
- Branch-code mapping.
- Other branch-specific SWIFT requirements.

These changes are linked to the referenced “2025 Tranche 1 Go Live Readiness (Hongkong, Bangkok, Taipei, New York)” page. The source does not provide the final values or evidence that the configuration was deployed.

Entity-specific SWIFT setup must be coordinated with [[concepts/settlement-accounting]], [[concepts/nostro-vostro-settlement-controls]], and the selected [[concepts/settlement-message-routing]] workflow.
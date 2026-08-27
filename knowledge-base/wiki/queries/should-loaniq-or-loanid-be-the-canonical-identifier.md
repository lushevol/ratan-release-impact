---
type: query
title: Should LOANIQ or LOANID Be the Canonical Identifier?
created: 2026-08-22
updated: 2026-08-22
tags: [query, identifiers, cash-settlement, onboarding, ssi]
related: ["2025-tranche-1-hk-tw-th-onboarding", "ssi-selection-hierarchy", "legacy-versus-strategic-cash-settlement-routing"]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/New Entity onboarding checking list/2025 Tranch1 (HK, TW, TH) Onboarding.md"]
---

# Should LOANIQ or LOANID Be the Canonical Identifier?

The checklist uses `LOANIQ` in the bypass-validation and legacy-routing lists but uses `LOANID` in the SSI stamping hierarchy exception. The source does not define whether these are aliases, separate products, or a transcription error.

## Evidence required

Resolve the identifier against the authoritative product, entity, and SSI configuration sources before implementing either whitelist or hierarchy logic.
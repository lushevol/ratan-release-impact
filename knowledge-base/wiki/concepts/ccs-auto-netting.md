---
type: concept
title: CCS Auto Netting
created: 2026-08-22
updated: 2026-08-22
tags: [ccs, auto-netting, principal, coupon, nd-ccs, korea]
related: [korea, auto-netting, nd-irs-nd-ccs-netting, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/F2B Milestone Onboarding check list/F2B Milestone check list - Korea Cashflow Migration.md"]
---

# CCS Auto Netting

## Korea requirement

The checklist marks CCS auto netting as required and says to follow the current behavior. The described use cases include:

- Principal and coupon netting.
- NDCCS netting between two legs.
- Assessment of whether resultant cashflows require STP/NSTP handling.

The source does not define a new Korea-specific CCS algorithm. Existing rules should be validated for Korea without assuming that every CCS product or netting population is in scope.
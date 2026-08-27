---
type: query
title: Does HAU Require SWIFT Message Customization?
created: 2026-08-22
updated: 2026-08-22
tags: [hau, swift, message-customization, uat]
related: [hau, hau-currency-onboarding, swift-entity-configuration, hong-kong-physical-gold-settlement]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/HKCS initiative/Onboarding for HAU currency.md"]
---
# Does HAU Require SWIFT Message Customization?

UAT1 recorded HAU PM-currency and SWIFT UDF setup and generated a SWIFT message. The checklist nevertheless leaves HAU-specific SWIFT customization as an open question.

Message generation alone does not confirm payload-field correctness, routing, gold-unit treatment, schema validation, downstream acceptance, or production readiness. Resolution should define expected message content and retain validation evidence.
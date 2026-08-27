---
type: query
title: Why Does HAU Accounting Processing Have a Service Story If Accounting Publication Is Not Required?
created: 2026-08-22
updated: 2026-08-22
tags: [hau, accounting, accounting-suppression, delivery-scope]
related: [hau, hau-currency-onboarding, ebbs-settlement-accounting, hong-kong-physical-gold-settlement]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/HKCS initiative/Onboarding for HAU currency.md"]
---
# Why Does HAU Accounting Processing Have a Service Story If Accounting Publication Is Not Required?

The checklist says HAU does not need to publish accounting entries, while Azure DevOps Story `14900306` covers accounting processing for HAU and an accounting-service feature branch is listed.

This may represent implementation of intentional suppression, validation-only behavior, an exception flow, or inconsistent scope. The expected accounting outcome and test evidence need confirmation before the requirement can be treated as settled.
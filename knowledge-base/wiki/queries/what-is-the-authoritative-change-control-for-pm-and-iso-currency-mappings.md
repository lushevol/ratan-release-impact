---
type: query
title: What Is the Authoritative Change Control for PM and ISO Currency Mappings?
created: 2026-08-23
updated: 2026-08-23
tags: [configuration-governance, precious-metals, iso-code, ratan, static-data]
related: [precious-metal-currency-classification, booking-currency-to-iso-code-mapping, new-currency-onboarding-static-data-readiness, ratan, murex-2-11]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Static Data/New Currency Onboarding Checklist.md"]
---
# What Is the Authoritative Change Control for PM and ISO Currency Mappings?

RATAN's PM currency list and booking-currency-to-ISO-code mapping are described as hardcoded, while their reference information is maintained in separate Confluence documents.

The unresolved questions are:

- Whether RATAN code/configuration or the respective Confluence document is authoritative at runtime;
- which team owns, approves, and deploys changes;
- how currency-list and mapping changes are tested before release;
- how drift between the implementation and documented reference data is detected and remediated;
- what happens when a new currency has no deployed PM classification or ISO mapping.

Evidence currently comes from [[25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--11-static-data--33-new-c--15q2nmq]] only.
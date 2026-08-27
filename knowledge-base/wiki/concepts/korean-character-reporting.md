---
type: concept
title: Korean Character Reporting
created: 2026-08-22
updated: 2026-08-22
tags: [korea, reporting, ssdr, localization, data-quality]
related: [korea, cashflow-blotter, korea-ssi-onboarding]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/F2B Milestone Onboarding check list/F2B Milestone check list - Korea Cashflow Migration.md"]
---

# Korean Character Reporting

## Requirement

The checklist records no general dependency on Korean characters but explicitly marks a dependency for the SSDR report.

The source asks whether Korean characters must also be supported in SSI, SCI, and cashflow data. It does not resolve that question.

## Implementation boundary

SSDR character support should be treated as confirmed for analysis and validation. Support in SSI, SCI, cashflow records, dashboards, or other reports requires separate confirmation, including field encoding, storage, search, display, and export behavior.
---
type: comparison
title: RATAN versus Razor SWIFT Generation Scope
created: 2026-08-23
updated: 2026-08-23
tags: [ratan, razor, swift, migration, scope]
related: [ratan-swift-message-generation, fmrp-to-ratan-migration-scope, settlement-first-migration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/FMRP Swift Generation.md"]
---
# RATAN versus Razor SWIFT Generation Scope

The FMRP requirement describes a transitional division of SWIFT-generation ownership between [[ratan]] and [[razor]].

| Dimension | RATAN | Razor |
| --- | --- | --- |
| MT scope | China, Malaysia, India, and partial Singapore | LOANIQ, Egypt, Nepal, and Saudi Arabia |
| MX scope | Singapore only | Not specified |
| UI query key | Cashflow ID in RATAN | Tag 20 through FMSRE |
| Primary downstream route | FMSGW; also FMSRE/ENISIS paths are specified | FMSRE query path is specified |
| Role in migration | Intended strategic generation capability for defined FMRP scope | Legacy generation retained for excluded country/product scope |

This is a functional-scope boundary, not evidence that all routing was deployed or that the named markets were fully migrated. In particular, Malaysia is included in RATAN MT scope but explicitly excluded from ISO MX scope.
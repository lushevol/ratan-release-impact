---
type: query
title: What Is the Approved Korea Migration Functional Scope?
tags: [korea, migration, functional-scope, open-question]
related: [korea, ratan-settlement, tds3, tlm, lms, korea-settlement-localization, korea-swift-mx-message-generation, korea-settlement-accounting]
created: 2026-08-22
updated: 2026-08-22
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Korea Migration Functional Analysis.md"]
---
# What Is the Approved Korea Migration Functional Scope?

## Question

Which items in the Korea Migration Functional Analysis are approved go-live requirements, and which are exploratory questions or future considerations?

## Evidence

The checklist spans Murex message and transport requirements, fixing and netting, SWIFT generation, SSI and Nostro statics, settlement accounting, business rules, firewall access, TDS3, TLM, LMS, MT/MX behavior, Ensis-Solace integration, localization, and manual payment handling.

It explicitly marks several per-entity values as mandatory, but provides no populated configuration, approval record, test evidence, owner, or completion status. TDS3, TLM, LMS, firewall access, and Korea customizations remain insufficiently specified.

## Resolution needed

The migration team should classify every checklist row as:

1. approved requirement;
2. dependency or prerequisite;
3. unresolved design question;
4. operational workaround; or
5. out of scope.

The resulting scope should identify in-scope legal/system entities, required interfaces, acceptance criteria, owners, and go-live evidence. Related Korea onboarding material in sources/26-auto-netting-page-md-files--216-cash-settlement-home-page-cash-settlement-home-page-functional-requirement-04--lpgtrq should be reconciled without assuming that its scope or status applies unchanged.
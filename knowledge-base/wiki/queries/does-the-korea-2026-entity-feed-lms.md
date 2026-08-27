---
type: query
title: "Does the Korea 2026 Entity Feed LMS?"
created: 2026-08-22
updated: 2026-08-22
tags: [Korea, LMS, Tag-20, source-system, cash-settlement]
related: ["2026-korea-cash-settlement-onboarding", "lms", "tag-20-logic", "settlement-message-routing"]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement/Korea Migration/New Entity onboarding checking list - Korea 2026.md"]
---
# Does the Korea 2026 Entity Feed LMS?

## Question

Does the new Korea 2026 entity need to feed LMS, and which source system and Tag 20 convention should be used?

## Evidence

The checklist explicitly requires confirmation with Settlement and LMS teams. It records existing examples where entities do not feed LMS and states that other entities do feed LMS. It also documents different source-system and Tag 20 patterns:

- SABRE EQ through STELLA and the BCS stack: `EQ + Branch Code + Cashflow ID`.
- LOANIQ flow: `LQ + Branch Code + Cashflow ID`.
- BLADE/S2BX/CFETS through FMRP: `DV`.
- FMRP GUI queries through RATAN use cashflow ID.

## Required resolution

Record the authoritative LMS feeding decision, source-system mapping, Tag 20 construction, FMID, and entity FM code for the Korea scope. The source table contains uncertain or incomplete values that should not be copied into production configuration without validation.
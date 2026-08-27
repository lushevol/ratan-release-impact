---
type: query
title: What Is the Resolution Status of SSI ID 43262410?
created: 2026-08-23
updated: 2026-08-23
tags: [ssi, static-data, mt202, amh, production-incident, data-quality]
related: [ssi-plus, amh, ssi-data-quality-for-swift-generation, static-data-readiness]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/FMRP Swift Generation/Production Issue - Swift Message.md"]
---
# What Is the Resolution Status of SSI ID 43262410?

## Question

Was SSI ID `43262410` corrected in ES, and did regenerated MT202 output for cashflow `N00000014342` pass AMH validation?

## Evidence

The incident dated 2025-01-23 is marked Open. AMH rejected MT202 field `57D` with `T31`, reporting a missing or incorrect line, subfield, component separator, or delimiter. The source associates the issue with SSI data for `Has_Cash_Custodian_Account` and directs SSI+ to correct data in ES.

## Information needed

- the corrected ES record and change approval;
- whether `Has_Cash_Custodian_Account` was incorrectly populated, incorrectly serialized, or both;
- a regenerated MT202 payload demonstrating valid field `57D`;
- AMH acceptance evidence and closure approval.
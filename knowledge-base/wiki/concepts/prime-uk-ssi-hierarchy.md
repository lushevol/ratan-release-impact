---
type: concept
title: Prime UK SSI Hierarchy
created: 2026-08-22
updated: 2026-08-22
tags: [ssi, settlement-instructions, prime-uk, configuration, fmrp]
related: [fmrp-prime-uk-uat-drop-2, ssi-stamping, ssi-selection-hierarchy, nostro-configuration, irs, ccs, loan-depo]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/F2B Milestone Onboarding check list/F2B Milestone Checklist - Prime Day 2.md"]
---
# Prime UK SSI Hierarchy

The Prime UK checklist requires the UK SSI model to be followed automatically. Its stated precedence gives priority to **Country Specific + Global Product** SSI over **Global Entity + Product Specific SSI**.

The hierarchy must be tested for IRS, CCS, and Loan Depo, including CFI-code selection, FEDWIRE versus CASH settlement method, single-agent and two-agent support, and automatic Nostro attachment.

The checklist identifies `UK MXGBLANK` being selected instead of the Global IRS SSI as a potential configuration issue. It does not establish whether the issue is resolved. SSI evidence should record the selected instruction, product, country, entity, CFI code, settlement method, agent count, and Nostro.
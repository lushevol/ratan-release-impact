---
type: concept
title: SSI Stamping Hierarchy
created: 2026-08-22
updated: 2026-08-22
tags: [ssi, settlement-instructions, configuration, hierarchy]
related: [manual-entity-settlement-onboarding, ssi-dual-blind-remediation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/00 Manual Entities Onboarding Checklist.md"]
---
# SSI Stamping Hierarchy

SSI stamping hierarchy determines which settlement instruction is selected when country-specific and entity/product-specific SSI definitions overlap.

The checklist describes a UK model that gives priority to “Country Specific + Global Product” SSI over “Global Entity + Product Specific” SSI. It separately identifies `CN/MY/IN/SG/LOANID` as using old logic and all other entities as using new logic.

The source explicitly asks whether newly onboarded manual entities should use the UK/new model. It therefore records a policy decision point rather than an approved default.

Vostro static setup is also described as driving Nostro assignment, with over-account clients created as branch-specific SSI. See [[should-manual-entities-use-the-uk-ssi-stamping-hierarchy]].
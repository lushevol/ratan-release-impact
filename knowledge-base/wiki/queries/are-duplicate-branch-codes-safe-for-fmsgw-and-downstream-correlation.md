---
type: query
title: Are Duplicate Branch Codes Safe for FMSGW and Downstream Correlation?
created: 2026-08-23
updated: 2026-08-23
tags: [branch-code, fmsgw, swift, correlation, solace]
related: [ratan-swift-reference-and-correspondent-derivation, fmsgw, cashflow-identifier]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/02 Swift Message Analysing for manual entities.md"]
---
# Are Duplicate Branch Codes Safe for FMSGW and Downstream Correlation?

The source identifies duplicate branch codes, including `2`, `28`, `60`, and widespread use of `73` across China entities.

RATAN embeds branch code in SWIFT Tags `:20:` and `:21:` and passes it as a mandatory FMSGW JMS-header value when publishing through Solace. Confirm whether duplicates are safe for FMSGW and all downstream systems, and define any required uniqueness, correlation, or migration controls.
---
type: query
title: What Is the Authoritative FMRP Entity Eligibility Configuration?
created: 2026-08-24
updated: 2026-08-24
tags: [fmrp, murex-211, entity-eligibility, static-data, governance]
related: [fmrp-h2-entity-dbf, fmrp-payment-eligibility-and-suppression, fmrp]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/Settlement - Murex 2.11 DOI Document - H2 2024.md"]
---
# What Is the Authoritative FMRP Entity Eligibility Configuration?

The DOI describes `FMRP_H2_ENTITY_DBF` as the table storing Ratan-eligible entity labels, but does not identify which rows are active, pending, retired, or aliases.

Questions to resolve:

- Does every row in the source table represent currently enabled Ratan eligibility?
- What business meaning, if any, does `M_EBBS = NA` have?
- Are `SRI LANKA` and `FCBUSLANKA`, which share FMID `10036647`, aliases or separate operational identities?
- How should duplicate or apparently source-specific labels such as `HHANGZHOU`, `NNCHANG`, `XXIAN`, and `SHYANG` be governed?
- What effective-date and approval evidence accompanies changes to the table?
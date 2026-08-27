---
type: entity
title: FMRP_PURGE
created: 2026-08-24
updated: 2026-08-24
tags: [murex-211, fmrp, batch-job, data-retention, purge]
related: [scb-fmrp-dbf, fmrp-ent-dbf, fmrp-retry-and-purge-policy]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/Settlement - Murex 2.11 DOI Document - H2 2024.md"]
---
# FMRP_PURGE

`FMRP_PURGE` is the Murex batch job named in the DOI to implement purge of [[scb-fmrp-dbf]] records.

The source specifies that data in `SCB_FMRP_DBF` remains available for one month after the related cashflow has been released in Ratan, measured by value date. It does not specify job scheduling, retry behavior, or evidence controls for completed purges.
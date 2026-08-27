---
type: query
title: Is MATH or MACH the Canonical SCB_FMRP_DBF Status Code?
created: 2026-08-24
updated: 2026-08-24
tags: [murex-211, scb-fmrp-dbf, status-code, data-quality]
related: [scb-fmrp-dbf, murex-ratan-bidirectional-cashflow-integration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Murex2.11 Technical Design.md"]
---
# Is MATH or MACH the Canonical SCB_FMRP_DBF Status Code?

The documented `SCB_FMRP_DBF` schema lists `INIT/SENT/MATH/CANC` as Murex status values. A struck-through `FACR` queue condition instead filters for `M_STATUS='MACH'`.

The source defines neither `MATH` nor `MACH`, and it does not establish whether one is a typographical error, a retired code, or a historical implementation change.

## Evidence needed

- Current database data dictionary or deployed DDL.
- Workflow status-code reference.
- Confirmation of whether the retired `FACR` configuration ever used a valid production status.
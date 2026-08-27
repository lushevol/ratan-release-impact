---
type: stakeholder
title: MO
created: 2026-08-24
updated: 2026-08-24
tags: [middle-office, trade-amendments, settlement]
related: [non-economic-cashflow-amendment-handling, ratan, stella]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade & Cashflow Events Control/Non Economic amendment(FMRP) Cashflows.md"]
---
# MO

MO is the Middle Office user group that initiates non-economic trade amendments in [[stella]].

The documented use cases include correction of a MIFID-report timestamp, CI allocation amendments, Tranche ID updates, and LCH clearing-detail updates following timing-related STP failure. These amendments are intended to have no trade PV impact but cause Stella to create new trade and cashflow versions.
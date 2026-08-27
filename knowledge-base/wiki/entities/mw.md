---
type: entity
title: MW
created: 2026-08-22
updated: 2026-08-22
tags: [mw, allocation, trade-booking, fmrp]
related: [vpa, stella, allocation-cashflow-state-handling, fmrp-market-event-settlement-impact]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/03-FMRP Requirement.md"]
---
# MW

MW is the originating component for the allocation flow described in the FMRP requirement. The documented path is `MW → VPA → Stella`.

The source also associates MW with prime booking and early-risk trade processing. Early-risk trades may be booked as placeholder trades and cashflows in `SUSPENDED` status before a subsequent event, although the exact transition and RATAN responsibility are unresolved.
---
type: query
title: What Is the Authoritative IRS Netting and Amendment State Machine?
created: 2026-08-23
updated: 2026-08-23
tags: [IRS, state-machine, netting, amendments, cashflow-status]
related: [irs-fixed-floating-leg-netting, irs-refixing-unnetting-and-renetting, pending-another-leg-status, netting-resultant-cashflow]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/IRS Fix Leg & Floating leg payment handling.md"]
---
# What Is the Authoritative IRS Netting and Amendment State Machine?

The source uses `PROJECTED`, `QUEUED`, `WAITING`, `READY`, `RELEASED`, `SETTLED`, `NETTED`, `CANCELLED`, and `DEAD`, but does not define a complete or consistently named lifecycle. It also varies between `CANCELED` and `CANCELLED`.

## Questions to Resolve

- What are the canonical cashflow statuses, sub-statuses, and permitted transitions?
- Which transitions apply to components, intra-trade resultants, and cross-trade resultants?
- What is the authoritative lineage between withdrawal, cancelled component, dead resultant, and replacement resultant?
- Does “settle as Gross” prohibit downstream cross-trade or cross-product netting?
- What exact release or settlement milestone changes re-fixing from automatic processing to manual NSTP remediation?

Resolution should produce an authoritative state machine and amendment-control specification.
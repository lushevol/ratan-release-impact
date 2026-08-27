---
type: concept
title: Non-Economic Cashflow Amendment Handling
created: 2026-08-24
updated: 2026-08-24
tags: [cashflows, amendments, ratan, stella, settlement]
related: [six-attribute-cashflow-equivalence, cashflow-lineage-and-operational-visibility, fmrp-payment-eligibility-and-suppression, released-settled-amendment-control, cashflow-netting-and-auto-un-netting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade & Cashflow Events Control/Non Economic amendment(FMRP) Cashflows.md"]
---
# Non-Economic Cashflow Amendment Handling

A non-economic amendment occurs when [[stella]] withdraws cashflows from a prior trade version and creates replacement cashflows without changing the defined settlement-economic attributes.

[[ratan]] evaluates withdrawn and newly generated cashflows individually using [[six-attribute-cashflow-equivalence]]. Equivalent replacements are operationally suppressed: the original cashflows remain available to [[settlement-ops]], while replacement records are retained for lineage and synchronization.

A single trade amendment can have mixed results. For example, an unchanged leg remains represented by its original cashflow, whereas a leg with a changed amount becomes a new cashflow and must repeat Suppression, Netting, NSTP, and exception controls.

“Ignore” means suppression from operational visibility and downstream publication, not deletion or exemption from all lifecycle maintenance.
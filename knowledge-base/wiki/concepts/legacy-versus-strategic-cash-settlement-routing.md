---
type: concept
title: Legacy versus Strategic Cash Settlement Routing
created: 2026-08-22
updated: 2026-08-22
tags: [cash-settlement, routing, razor, ratan, cashflow-suppression]
related: ["settlement-message-routing", "cashflow-suppression", "2025-tranche-1-hk-tw-th-onboarding"]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/New Entity onboarding checking list/2025 Tranch1 (HK, TW, TH) Onboarding.md"]
---

# Legacy versus Strategic Cash Settlement Routing

The onboarding checklist uses entity lists to distinguish legacy and strategic cash-settlement processing. The named legacy list is `EG/NP/SAUDI/LOANIQ`; the strategic list is `CN/SG/MY/IN/UK/DE`; and `HK/TW/TH` are identified as the CPT list.

The workflow whitelist, covered through a [[concepts/cashflow-suppression]] rule, determines whether an in-scope cashflow is sent to [[entities/razor]] or handled in [[entities/ratan]]. RATAN generates SWIFT and accounting for the flows it handles.

This classification is source-specific. It must not be generalized to all products or entities. The source also mentions “BCS vs Strategic Routing” without defining BCS.

## Operational implications

Routing configuration must preserve the exact entity lists, distinguish migration-only logic from general settlement processing, and provide evidence that each new entity is assigned to the intended workflow.
---
type: query
title: What Is the Final Indonesia Routing and Blacklist Scope?
created: 2026-08-22
updated: 2026-08-22
tags: [Indonesia, Jakarta, routing, blacklist, whitelist, scope, cash-settlement]
related: [indonesia-entity-onboarding-checklist, indonesia-jakarta, cashflow-suppression, settlement-suppression, auto-netting, pending-fixing-stp-nstp-control, lms, nds-auto-netting, ratan, razor]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/New Entity onboarding checking list/2026 Indonesia Instance.md"]
---

# What Is the Final Indonesia Routing and Blacklist Scope?

## Question

Which routing path and system-specific entity lists should be configured for the Indonesia/Jakarta entity?

## Evidence

The checklist identifies separate control populations:

- Legacy flow: `EG`, `NP`, `SAUDI`, `LOANIQ`.
- Strategic flow: `CN`, `SG`, `MY`, `IN`, `UK`, `DE`.
- CPT list: `HK`, `TW`, `TH`.
- LMS blacklist: `EG`, `NP`, `SAUDI`, `KL`, `TH`, `TW`.
- NDS Auto Netting blacklist: `TBD`.
- Pending Fixing STP/NSTP blacklist: `TBD`.
- SSI old-logic whitelist: `CN`, `MY`, `IN`, `SG`, `LOANID`.

The source states that entity whitelists control BCS versus Strategic Routing and determine whether transactions are sent to [[razor]] or handled in [[ratan]], where RATAN generates SWIFT and accounting outputs. It does not explicitly assign Indonesia/Jakarta to a final route.

## Why this remains open

The lists serve different subsystems and cannot be copied between LMS, NDS Auto Netting, Pending Fixing, routing, and SSI controls. The source also does not clarify whether `IN` in the Strategic flow represents the new Indonesia/Jakarta entity or another established entity convention.

## Required resolution

Confirm:

1. The official entity and branch identifier represented by `IN`.
2. Whether Indonesia/Jakarta routes through RAZOR, RATAN, BCS, Strategic Routing, or another path.
3. The final LMS blacklist.
4. The final NDS Auto Netting blacklist.
5. The final Pending Fixing STP/NSTP blacklist.
6. Whether the H2 Adaptor whitelist includes the entity for Murex cash migration.
7. Whether the SSI old-logic exception applies to this entity.

Until confirmed, system-specific lists should remain independently managed and `TBD` values should not be replaced by inference.

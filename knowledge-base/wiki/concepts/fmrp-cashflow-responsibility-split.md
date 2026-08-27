---
type: concept
title: FMRP Cashflow Responsibility Split
created: 2026-08-24
updated: 2026-08-24
tags: [FMRP, architecture, responsibility, pre-trade, post-trade, cashflow]
related: [fmrp, fmrp-stella, stella, ratan, cashflow-lifecycle-state-model, nostrо-centralization]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Ratan & Stella cashflow integration.md"]
---
# FMRP Cashflow Responsibility Split

The FMRP proposal separates cashflow generation from post-trade lifecycle and settlement processing.

## Pre-trade responsibility

[[entities/fmrp-stella]] generates cashflows from trade business events and assigns business versions. Newly generated cashflows start in `Projected`.

## Post-trade responsibility

[[entities/ratan]] materializes cashflows and owns operational processing, including:

- Lifecycle status movement.
- NSTP review and FMO intervention.
- Netting and resultant cashflow generation.
- Auto un-netting.
- Payment-date maintenance.
- Swift release and settlement processing.

This separation is intended to remove post-trade functionality from Stella and support China entity onboarding during Murex decommissioning. It remains a proposed design rather than a confirmed architectural decision.
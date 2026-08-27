---
type: entity
title: Tradehub
created: 2026-08-22
updated: 2026-08-22
tags: [Tradehub, trade-mapping, SWIFT, field-mapping, trading-integration, fmrp, ltfx, rtns]
related: [f2b, murex, fmrp, swift-mt-mx-integration, tag-20-logic, ratan, fmrp-to-ratan-migration-scope]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/04-Onboarding(Entity Product) Check List/F2B Milestone Onboarding check list.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/03-FMRP Requirement.md"]
---
# TradeHub

## Role and integrations

The FMRP Requirement source identifies TradeHub as an integration target for FMRP Global Rates capabilities. It describes a new Global Rates S2BX and TradeHub Integration (LTFX) interface covering FX Spot, Forward, Swap, and NDF products.

The same source also names TradeHub in the RTNS Integration feature. RTNS work is described as outside Q2 scope and therefore should not automatically be treated as a Tranche 1 settlement commitment.

Separately, the onboarding checklist identifies an existing Strategy-to-field-26C mapping in TradeHub.

## Settlement relevance

For HK/TW LTFX, the FMRP Requirement source states that RATAN requires UAT support for NDF, while FX cashflows are replicated to [[razor|Razor]]. It characterizes the LTFX feature as primarily concerning DealHub-to-TradeHub transit and identifies no special settlement behavior.

## Onboarding implications

According to the onboarding checklist, new strategies, typologies, allocations, products, or branches may require verification of the existing Strategy-to-field-26C mapping.

The onboarding checklist does not state whether that mapping is authoritative for FMRP or whether additional mapping is required for STELLA-originated flows.
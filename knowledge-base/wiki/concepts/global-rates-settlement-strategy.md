---
type: concept
title: Global Rates Settlement Strategy
created: 2026-08-22
updated: 2026-08-22
tags: [global-rates, settlement-strategy, rat an, fmrp, migration]
related: [ratan, stella, fmrp, settlement-method-stamping, strategy-golden-source, cashflow-migration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/03-FMRP Requirement/Global Rates - Settlement Strategy Process & Dependency.md"]
---
# Global Rates Settlement Strategy

Global Rates Settlement Strategy is the cross-system operating model required to migrate G10 and EM desk trades, primarily in DE, HK, IN, SG, and TW, onto [[entities/ratan]].

It combines upstream booking and strategy decisions with settlement execution, static data, clearing, event sourcing, and downstream integration. The central design question is not only how RATAN settles cashflows, but how Blade and [[entities/stella]] produce authoritative trade and cashflow attributes before RATAN processing.

The first rollout excludes RFR package trade models. China production precedents for clearing and product mapping may reduce the need for new RATAN functionality, but they do not resolve ownership or interface questions for the Global Rates scope.
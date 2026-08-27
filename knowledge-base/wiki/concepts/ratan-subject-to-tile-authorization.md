---
type: concept
title: RATAN Subject-to-Tile Authorization
created: 2026-08-22
updated: 2026-08-22
tags: [ratan, ratan-one, authorization, application-tiles, access-subjects]
related: [ratan, ratan-one-access-control, ratan-cashflow-blotter, auto-netting-rule-management, netting-eligibility-rules, what-is-the-canonical-ratan-nostro-and-bic-netting-subject-mapping]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Ratan One Processing Guide (DOI)/How to apply for RATAN ONE access.md"]
---
# RATAN Subject-to-Tile Authorization

RATAN ONE request subjects are technical access identifiers associated with user-interface tiles. The documented subjects cover trade and cashflow blotters, grouping, validation and settlement exceptions, business-rule functions, and static-data functions.

Examples include:

- `RATAN_CASHFLOW_BLOTTER` for the FX & Equity Cashflow Blotter, providing access-request context for [[ratan-cashflow-blotter]].
- `RATAN_AUTO_NETTING_RULE` for the Auto Netting Rules tile, providing access-control context for [[auto-netting-rule-management]].
- `RATAN_NETTING_RULE` for Netting Static.
- `RATAN_ENTITLEMENT_RULE` for Data Entitlement Rules.

A subject-to-tile mapping does not specify the actions available inside a tile. It must not be interpreted as evidence that a subject grants edit, approval, configuration, or administrative authority.

## Ambiguous static-data mapping

The guide maps `RATAN_NOSTRO_BLOTTER` to both `Static - Nostro Static` and `Static - BIC Netting Static`. It is unclear whether this represents a deliberately shared entitlement or an incorrect/missing identifier. This ambiguity is tracked in [[what-is-the-canonical-ratan-nostro-and-bic-netting-subject-mapping]].

The document also marks `RATAN_MO_EXCEPTION` as unused.
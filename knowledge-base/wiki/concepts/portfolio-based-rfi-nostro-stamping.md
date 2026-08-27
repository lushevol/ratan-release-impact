---
type: concept
title: Portfolio-Based RFI Nostro Stamping
tags: [RFI, Nostro, portfolio, cashflow, SSI-stamping, RATAN]
related: [ratan, rfi-nostro-account, nostro-type-static-data-model, ssi-stamping-behavior-differences, rfi-swift-account-propagation]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/RFI Nostro stamping based on Portfolio.md"]
---

# Portfolio-Based RFI Nostro Stamping

Portfolio-based RFI Nostro stamping selects a dedicated RFI Nostro for qualifying cashflows using booking entity, currency, and portfolio rather than product.

## Selection flow

For a cashflow identified as belonging to an RFI portfolio, RATAN:

1. Queries Nostro static data by booking entity, currency, and portfolio.
2. Stamps the single matching RFI Nostro when exactly one record is found.
3. Raises the specified missing-Nostro exception when multiple records are found and permits manual RFI selection.
4. Falls back to the existing process when no RFI record is found.

The source lists these RFI portfolios:

- `IR_SWP_KOR_NYRF_STL`
- `IR_SWP_KOR_RFI_STL`
- `IR_SWP_KOR_RFI`
- `IR_SWP_KOR_NYRF`

Matching semantics for multi-value Portfolio fields, normalization rules, and the behavior for missing or invalid portfolios remain undefined.

## Stamping precedence

Existing Vostro stamping remains unchanged. For RFI portfolios, however, the Vostro result must not overwrite the RFI Nostro stamp. The implementation order or explicit precedence mechanism is not specified.

If the Vostro settlement means or settlement account differs from the selected Nostro instruction, RATAN raises an SI-mismatch exception and requires the user to amend the Vostro SSI.

## Scope

The rule applies to cashflow SSI stamping and is product-agnostic. It does not deliver RFI trade stamping, which remains BAU and is deferred to a separate strategic trade-stamping solution.

A future common selection mechanism may support additional attributes such as strategy, typology, or another FMRP attribute, but that extension is not a confirmed scope commitment.

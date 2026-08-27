---
type: query
title: What Is the Authoritative Counterparty BIC Display Mapping?
created: 2026-08-23
updated: 2026-08-23
tags: [counterparty, swift-bic, sci, cashflow-details, ui-requirement, integration]
related: [cash-settlement-home-page, sci, counterparty-bic-display-mapping, cashflow-detail-field-projection]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/KTLO Requirement/8870075-Update counterparty BIC display in  i  icon.md"]
---
# What Is the Authoritative Counterparty BIC Display Mapping?

The requirement proposes sourcing `SWIFT BIC` from SCI `addrLine` where `mediumUsage = 'MAIN'`, but the complete selection, exception, and fallback contract is not defined.

## Questions to resolve

- Is `SCBLGB2LXXX` compared with the existing BIC type value, the selected `addrLine`, or the final displayed `SWIFT BIC`?
- When the comparison equals `SCBLGB2LXXX`, should the UI retain the current BIC type value, display nothing, or apply another mapping?
- Which record is selected if SCI returns multiple items with `mediumUsage = 'MAIN'`?
- What is displayed if there is no `MAIN` item or the selected `addrLine` is empty?
- Is `addrLine` guaranteed to contain a valid BIC in the relevant SCI context?
- Does SCI already expose `addrLine` and `mediumUsage` at the UI-facing integration boundary?
- Is this a front-end-only change, as suggested by the requirement, or are SCI or backend changes required?
- Does the rule apply to all counterparties or a defined subset?

## Evidence

The source explicitly identifies the affected display location and proposes the `addrLine`/`mediumUsage = 'MAIN'` mapping. It does not define the above exception and integration details.

See [[counterparty-bic-display-mapping]] and [[sci]].
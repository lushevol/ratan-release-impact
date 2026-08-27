---
type: concept
title: Counterparty BIC Display Mapping
created: 2026-08-23
updated: 2026-08-23
tags: [counterparty, swift-bic, cashflow-details, field-mapping, ui]
related: [cash-settlement-home-page, sci, cashflow-detail-field-projection, what-is-the-authoritative-counterparty-bic-display-mapping]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/KTLO Requirement/8870075-Update counterparty BIC display in  i  icon.md"]
---
# Counterparty BIC Display Mapping

Counterparty BIC display mapping is the rule that determines the value shown as `SWIFT BIC` in the `Cashflow Details-Counterparty` view of the [[cash-settlement-home-page]].

## Proposed mapping

The requirement proposes replacing the current SCI-derived BIC type value with `addrLine` from an SCI item selected by:

```text
mediumUsage = 'MAIN'
```

The intended projection is:

```text
SCI selected item.addrLine → Cashflow Details-Counterparty.SWIFT BIC
```

## Exception under clarification

The requirement qualifies the proposed mapping with:

```text
SWIFT BIC != SCBLGB2LXXX
```

It does not define the value being compared, the fallback behavior if the condition is false, or the handling of missing, blank, or multiple `MAIN` records. The authoritative rule is tracked by [[what-is-the-authoritative-counterparty-bic-display-mapping]].

This mapping extends [[cashflow-detail-field-projection]] but does not establish a change to cashflow processing, accounting, payment generation, or settlement status.
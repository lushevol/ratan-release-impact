---
type: concept
title: Structured-Product Package Trade Model
created: 2026-08-23
updated: 2026-08-23
tags: [structured-products, package-trades, trade-model, SCBML, cashflows]
related: [blade, stella, cdu, package-identifier-lineage, trade-cashflow-reference-linkage, cashflow-reference-consistency-validation, trade-confirmation-driven-cashflow-stp]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Deprecated docs/Structure products.md"]
---
# Structured-Product Package Trade Model

## Definition

A structured-product package trade model represents several related trades as one booking or contract while preserving each component as an individual trade message and maintaining its associated cashflows.

In the deprecated [[sources/25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--15-deprecated-docs--18-st--tn9c1x|Structure Products]] requirement, [[entities/blade|Blade]] books the package as one contract but emits one `SCBML` document per individual trade. [[entities/stella|Stella]] then enriches each message with its own package ID.

## Relationship structure

The intended hierarchy is:

```text
Structured-product package
├── Individual trade
│   └── Trade SCBML
└── Cashflows associated with each trade
    └── Cashflow SCBML
```

A package may contain different trade and cashflow types. The source example includes an `NDF`, `FX Swap` near-leg and far-leg cashflows, broker-fee cashflows, USD, JPY, and GBP amounts, and both Pay and Receive directions.

Package membership must therefore be represented explicitly. It cannot safely be inferred from trade type, cashflow type, currency, payment direction, or amount.

## Confirmation implication

The source proposes that [[entities/cdu|CDU]] consolidate individual trade `SCBML` documents sharing a package ID into one package-level confirmation. This is marked `TBC` and is not an established requirement. Any implementation would need to preserve component trades, component cashflows, and their individual statuses alongside the consolidated confirmation.

## Reconciliation implications

The model requires stable linkage between package, trade, and cashflow records. It is relevant to [[concepts/trade-cashflow-reference-linkage]] and [[concepts/cashflow-reference-consistency-validation]]. A reconciliation process should distinguish:

- Package-level booking identity.
- Trade-level identity and message.
- Cashflow-level identity and message.
- Confirmation-level identity and status.

Because the source table is structurally inconsistent, the example should be used to illustrate relationships rather than as a normative schema.
---
type: concept
title: Configurable Cashflow ID Prefixes
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, cashflow-id, configuration, netting, splitting, indonesia]
related: [story-13292989, how-does-the-12-character-indonesia-cashflow-id-format-handle-sequence-overflow, what-is-the-resultant-and-split-cashflow-id-prefix-contract-for-indonesia, cashflow-split-and-unsplit-control, ratan-indonesia, ratan-gdc]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Netting Spliting ID prefix.md"]
---
# Configurable Cashflow ID Prefixes

Configurable cashflow-ID prefixes separate an identifier namespace policy from split and netting lifecycle logic. The cited implementation note proposes that [[ratan-indonesia]] use:

- `SID` for split cashflows.
- `NID` for netting-resultant cashflows.

The [[ratan-gdc]] baseline uses `S` and `N`, respectively.

## Identified generation paths

The note identifies split-ID generation through:

```java
Utils.getCashFlowId(Constant.SPLIT_CASHFLOW_PREFIX, 11, String.valueOf(cashflowIdSeq));
```

It identifies resultant netting-ID generation through:

```java
Utils.getCashFlowId("N", 11, String.valueOf(cashflowIdSeq));
```

Only the netting example is explicitly a literal hard-coded prefix. `Constant.SPLIT_CASHFLOW_PREFIX` is named as a constant, but the source does not establish whether it is already externally configurable.

## Scope boundary

Prefix configuration should not be conflated with split or netting eligibility. The note records `getAmountSplitRule(entityFmId, nostrolAgent, currency)` for splitting and a `checkIrsRule` orchestration call for netting, but gives no evidence that these rule-resolution paths construct identifiers or distribute prefix settings.

Lifecycle regression coverage must extend beyond initial creation to [[cashflow-split-and-unsplit-control]] operations, including split withdrawal, unnetting, and unsplitting. Identifier behavior during reversal operations remains unspecified.

## Fixed-width risk

The proposed Indonesia format retains a total length of 12 characters. Three-character prefixes therefore leave nine numeric positions, rather than the eleven positions available after a one-character prefix. Before adoption, validate sequence overflow behavior, database and message field lengths, downstream ID parsing, reconciliation usage, migration handling, and uniqueness across environments.

The `SID` and `NID` values remain a proposal in the available source, not an approved contract. See [[what-is-the-resultant-and-split-cashflow-id-prefix-contract-for-indonesia]] and [[how-does-the-12-character-indonesia-cashflow-id-format-handle-sequence-overflow]].
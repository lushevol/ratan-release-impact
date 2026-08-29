---
type: concept
title: Netting Type Derivation
created: 2026-08-22
updated: 2026-08-22
tags: [netting-type, ccila, bic, netting-rules, rule-conditions]
related: [netting-static-blotter, cashflow-auto-netting, ccil-settlement-method-stamping, queries/what-are-the-ratan-netting-rule-match-and-precedence-semantics]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Day2 Auto Netting TestCase.md"]
---
# Netting Type Derivation

## Definition

Netting Type Derivation is the conditional population of the `Netting Type` field from rule conditions in the [[netting-static-blotter]].

## Documented conditions

The source records the following behavior:

```text
Initial Netting Type value: blank

Settlement method == "CCIL"
Counterparty SCI FMID <> 400021949
Result: "CCIL netting"

Counterparty_SCI_BIC_Net_Flag == "Y"
Result: "BIC netting"
```

The CCIL condition excludes counterparty SCI FMID `400021949`. The BIC condition uses the exact field identifier `Counterparty_SCI_BIC_Net_Flag`.

## Unresolved precedence

The test cases do not state what happens when both the CCIL and BIC conditions match. They also do not establish whether:

- The conditions are mutually exclusive.
- CCIL takes precedence over BIC.
- BIC takes precedence over CCIL.
- The field can be manually overridden.
- The field remains blank when no condition matches.

This precedence question remains connected to what are the ratan netting rule match and precedence semantics.

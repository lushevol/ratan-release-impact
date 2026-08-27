---
type: concept
title: Direction-Dependent PreMatchKey
created: 2026-08-22
updated: 2026-08-22
tags: [prematch-key, cashflow-matching, auto-netting, inter-entity-netting]
related: [inter-entity-netting, auto-netting-rule-check, netting-type-derivation, cross-rule-netting-isolation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Inter Entity Netting/Inter Entity Netting Design.md"]
---
# Direction-Dependent PreMatchKey

A direction-dependent `PreMatchKey` is a composite matching key whose entity ordering changes according to the cashflow direction.

## Key Formats

For a `Pay` cashflow, the design specifies:

```text
EntityFMID-CounterPartyFMID-Amount
```

For a `Receive` cashflow, it specifies:

```text
CounterPartyFMID-EntityFMID-Amount
```

This reversal allows reciprocal cashflows to produce the same key. For example:

```text
Pay:     400906330-7-100
Receive: 400906330-7-100
```

The amount component makes the matching amount-sensitive. A receive cashflow for `600` does not match a reciprocal payment for `200`.

## Sample Outcomes

- Cashflows 1 and 4 match on `400906330-7-100`.
- Cashflows 2 and 5 match on `7-400906330-200`.
- Cashflow 3 does not match because its key contains `600`.
- Cashflow 6 shares the key `7-400906330-200` with cashflow 5 but is marked as not matched.
- Cashflow 7 does not match because it uses the different entity pair `10075222-400906330`.

## Boundaries of the Documented Key

`Currency` and `VD` are present in the sample records but are not included in the displayed `PreMatchKey` formulas. The design therefore does not establish whether they are separate eligibility filters or omitted matching dimensions. It also does not specify the exact field represented by `Amount`, including whether it is the USD-normalized value populated during Cashflow Enrichment.

The duplicate-key example implies one-to-one consumption or allocation, but no deterministic selection rule is documented.
---
type: concept
title: Swap Agent MTM/Coupon Netting Separation
created: 2026-08-22
updated: 2026-08-22
tags: [swap-agent, mtm, coupon, auto-netting, segregation, SWAP_AGENT, interim-MTM, clearing, bilateral-settlement-risk]
related: [swap-agent, cashflow-auto-netting, netting-resultant-cashflow-lifecycle, cross-rule-netting-isolation, cash-settlement-home-page, clearing-resultant-swift-suppression, netting-validation-and-preview, netting-resultant-cashflow, pending-auto-netting-state]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Day2 Auto Netting TestCase.md"]
---
# Swap Agent MTM/Coupon Netting Separation

## Definition

Swap Agent auto-netting applies separation rules between specified cashflow categories.

The Day2 Auto Netting Test Case source states that a cashflow of type `MTM` must not be netted with a cashflow of type `Coupon`, even when other grouping attributes match.

Separately, the Hard Block UAT testing source documents a prohibition on netting `SWAP_AGENT` Coupon cashflows with `SWAP_AGENT` Interim MTM cashflows. According to that source, combining those flows could allow clearing-eligible cashflows to settle bilaterally.

These source-specific findings should not be interpreted as establishing that every `SWAP_AGENT` payment type is mutually incompatible.

## Day2 Auto Netting Test Case Evidence

The Day2 Auto Netting Test Case source states that:

- Eligible Swap Agent cashflows with matching attributes are netted.
- `MTM` cashflows are not netted with `Coupon` cashflows.
- Cashflows with different booking entity, counterparty, currency, or value date are not netted.

The tested product and payment attributes include:

```text
Product_Strategy = "SWAP_AGENT"
Payment_Type = "Coupon"
```

### Resultants

The Day2 source expects separate resultants for each cashflow category:

```text
SAL or SWAP AGENT MTM Netting
SAL or SWAP AGENT Coupon Netting
```

That source further states that MTM and Coupon netting resultants are suppressed while the original cashflows remain unaffected. The exact lifecycle status and technical meaning of “suppressed” are not defined; see [[netting-resultant-cashflow-lifecycle]].

## Hard Block UAT Evidence

In the 2025-10-31 new-solution UAT test documented by the Hard Block UAT testing source, two otherwise matching cashflows were selected:

- C1: `SWAP_AGENT` / `Coupon`
- C2: `SWAP_AGENT` / `Interim MTM`

The netting request was rejected before a resultant cashflow was created. The application displayed:

> “SWAP AGENT Coupon or Interim MTM can't net with the other payment type cashflow to avoid clearing eligible cashflows settling Bilaterally”.

This behavior was observed by both the UK Settlement Team and Clearing Ops Team using separate cashflow identifiers.

### Scope of the UAT Finding

The Hard Block UAT evidence supports the specific prohibition of `SWAP_AGENT` Coupon plus `SWAP_AGENT` Interim MTM. It does not establish that all `SWAP_AGENT` payment types are mutually incompatible.

The same source also records a separate rejected test involving:

- `SWAP_AGENT` / `Coupon`
- `RECALC` / `Coupon`

That result supports rejection of the tested strategy combination only and should not be generalized to all different product strategies. In that scenario, the error message referred to payment-type incompatibility even though both tested flows were Coupon flows.

## Relationship to Hard Blocking

The Hard Block UAT testing source distinguishes netting-validation separation from post-netting NSTP hard blocking:

1. `SWAP_AGENT` Coupon plus `SWAP_AGENT` Interim MTM was rejected during netting validation, before a resultant was created.
2. In another test, same-payment-type Coupon netting was allowed to generate resultant `N1`.
3. Resultant `N1` subsequently received the `Hard block Swap Agent` NSTP exception and could not be submitted by the maker.

Therefore, according to the UAT source, payment-type separation during netting validation and NSTP hard blocking after netting are distinct controls.

See [[netting-validation-and-preview]], [[netting-resultant-cashflow]], and [[clearing-resultant-swift-suppression]].

## Scope Boundary

The documented separation behavior is specific to Swap Agent flows in the cited sources. It should not automatically be generalized to all bilateral netting flows or to other product strategies.
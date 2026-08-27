---
type: concept
title: Stella SUSPENDED-MATURED Hard Block
tags: [stella, cashflow-status, hard-block, fx, duplicate-payment-control]
related: [stella, tds3, razor, ratan, fx-cashflow-status-write-back, cashflow-status-lifecycle, cashflow-suppression]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/FX Cashflow Status Write Back - Razor to Stella.md"]
---
# Stella SUSPENDED-MATURED Hard Block

`SUSPENDED-MATURED` is the specified Stella status used to distinguish Razor-managed FX cashflows from cashflows processed by Stella. Under the requirement, a matched eligible Razor event causes RATAN to set this state so that Stella can apply hard-block logic.

This status must not be conflated with [[cashflow-suppression]], SWIFT suppression, external network acknowledgement, or proof that settlement is final.

## Asserted behavior

The source states that:

- Stella hard block is based on T1 or T1-and-live cashflows.
- If a user cancels or updates a trade whose cashflow is `SUSPENDED-MATURED`, hard block is automatically lifted until the new cashflow reaches `SUSPENDED-MATURED`.
- For a trade with two cashflows, one `SUSPENDED-MATURED` cashflow is sufficient to hard-block the trade.
- TDS3-generated FX cashflows default to `Suspended`; fee-related cashflows are an exception and are `Projected`.
- Fee-related release or settlement status is not required for hard block.

These are source-specific design assertions and are not established for non-FX products, fee cashflows, or other settlement systems.

## Terminology requiring confirmation

The source uses `SUSPENDED-MATURED`, `SUSPEND-MATURED`, and `SUSPENDED`. The canonical Stella enumeration, valid transitions, and distinction between `SUSPENDED` and `SUSPENDED-MATURED` require confirmation before implementation or control testing.
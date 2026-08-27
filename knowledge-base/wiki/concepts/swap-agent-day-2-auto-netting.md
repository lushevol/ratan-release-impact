---
type: concept
title: SWAP_AGENT Settlement Day 2 Auto-Netting
created: 2026-08-22
updated: 2026-08-22
tags: [swap-agent, settlement-day-2, auto-netting, coupon, interim-mtm]
related: [swap-agent, sal-mtm-and-coupon-auto-netting, swap-agent-mtm-coupon-netting-separation, pending-auto-netting-state, netting-job-retry, netting-resultant-cashflow, clearing-resultant-swift-suppression]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Swap Agent Day2.md"]
---
# SWAP_AGENT Settlement Day 2 Auto-Netting

This concept captures the Settlement Day 2 requirement for separate auto-netting of `SWAP_AGENT` interim MTM and coupon cashflows.

## Eligibility

The two populations are selected independently:

```text
Product_Strategy = "SWAP_AGENT"
&& Payment_Type = "Interim MTM"
&& (Cashflow__Netting_Id == null || Cashflow__Netting_Id == "")
```

```text
Product_Strategy = "SWAP_AGENT"
&& Payment_Type = "Coupon"
&& (Cashflow__Netting_Id == null || Cashflow__Netting_Id == "")
```

Grouping requires the same booking entity, counterparty, currency, value date, and payment type. `Interim MTM` cannot net with `Coupon`. `Initial Notional` and `Final Notional` are excluded because they do not satisfy either payment-type predicate.

## Resultants

The resultant payment type identifies the source population:

- `Interim MTM` produces `SAL MTM Netting`.
- `Coupon` produces `SAL Coupon Netting`.

The suppression rule applies to resultants with either payment type when `Cashflow__Netting_Id` is populated:

```text
Payment_Type in ("SAL MTM Netting", "SAL Coupon Netting")
&& (Cashflow__Netting_Id != null && Cashflow__Netting_Id != "")
```

Expected successful processing leaves source cashflows in `Netted` state and creates a resultant in `SWIFT_SUPPRESSED` state. The resultant is not sent to LMS. The source separately expects accounting entries to be generated and sent, but does not identify the accounting destination.

## Operations

The start time is configurable. A failed scheduled job should be retried by another job 30 minutes later. The source does not establish whether this interval is configurable, how failures are scoped, or how duplicate resultants are prevented.

Before processing, eligible cashflows are expected to be `WAITING` with sub-state `Pending Auto Netting`.

This is a functional requirement rather than deployment or test evidence. See [[cash-settlement-home-page-settlement-day-2-swap-agent-requirement]].
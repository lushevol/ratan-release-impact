---
type: query
title: Does Ratan Auto Un-Netting Place Affected Cashflows in NSTP, Queued, or Both?
created: 2026-08-23
updated: 2026-08-23
tags: [ratan, netting, un-netting, nstp, cashflow-status]
related: [automatic-un-netting-on-trade-market-events, ratan, what-is-the-authoritative-netting-state-name-and-un-netting-resultant-identity]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/Auto Un-Net - Trade market event.md"]
---
# Does Ratan Auto Un-Netting Place Affected Cashflows in NSTP, Queued, or Both?

## Question

Does Ratan auto un-netting place affected cashflows in `NSTP`, `Queued`, or a combination of an operational status and separate hold/review control?

## Evidence

The narrative states that un-netted cashflows “will be hold as NSTP” pending user review and action.

The detailed Amendment example instead assigns `Queued` to all released components:

- `C101`: `Netted` to `Queued`
- `C102`: `Netted` to `Queued`
- `C103`: `Projected` to `Queued`

The prior resultant `C104` becomes `Dead`.

## Why this matters

The distinction determines whether released cashflows are eligible for downstream processing, whether a user must act before further processing, and how operational monitoring should identify an auto-un-net exception.

## Needed clarification

Confirm whether `NSTP` is:

1. a cashflow status replacing `Queued`;
2. a hold flag or exception queue applied alongside `Queued`;
3. a transient state omitted from the final table; or
4. outdated narrative terminology.

Related: [[automatic-un-netting-on-trade-market-events]] and [[what-is-the-authoritative-netting-state-name-and-un-netting-resultant-identity]].
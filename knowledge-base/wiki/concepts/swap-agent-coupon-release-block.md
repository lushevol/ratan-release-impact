---
type: concept
title: Swap Agent Coupon and Interim MTM Release Block
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, ratan, murex, swap-agent, coupon, interim-mtm, release-control]
related: [hard-blocker-exception, ratan, murex, settlement-day-2, hard-blocker-go-live-checklist]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Hard Blocker/Hard Blocker go live checklist.md"]
---
# Swap Agent Coupon and Interim MTM Release Block

This release restriction applies when a cashflow has the Murex product strategy value `SWAP_AGENT` and the payment type is `Coupon` or `Interim MTM`. The restriction is implemented as part of the documented `HARD_BLOCKER` NSTP rule and prevents release from Ratan.

## Rule condition

```text
Instrument_Common__Murex_Product_Strategy == "SWAP_AGENT" && Cashflow__Payment_Type in ("Coupon", "Interim MTM")
```

The complete configured expression also matches cashflows where:

```text
Cashflow__Is_Hard_Blocker == true
```

Therefore, the Swap Agent condition is one branch of the rule rather than the complete definition of all hard-blocked cashflows.

## User-facing behavior

The expected message for the Swap Agent scenario is:

```text
This is a Swap Agent Coupon or Interim MTM cashflow, can't be release from Ratan.
```

The message must be shown when a maker attempts **Submit** or a checker attempts **Approve**. In bulk submission, matching cashflows must be marked with a validation error and excluded from back-end posting.

[[murex]] supplies the product-strategy input described by the rule; the source does not state that Murex itself enforces the release block. [[ratan]] is the system from which release is blocked.
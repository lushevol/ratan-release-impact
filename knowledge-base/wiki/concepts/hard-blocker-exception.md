---
type: concept
title: Hard Blocker Exception
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, nstp, hard-blocker, exception-management, ratan]
related: [settlement-day-2, ratan, cashflow-suppression-rule, hard-blocker-go-live-checklist, maker-checker-control]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Hard Blocker/Hard Blocker go live checklist.md"]
---
# Hard Blocker Exception

A hard blocker is an NSTP exception category that prevents a cashflow from being released through normal settlement workflows. In the documented configuration, the exception category is `HARD_BLOCKER`, the operation level is `MAKER_CHECKER`, and bulk eligibility is disabled.

## Required behavior

For a single cashflow:

- The hard-blocker exception appears first in the exception list.
- It uses an error color equivalent to the high-risk exception color.
- Maker **Submit** is blocked.
- Checker **Approve** is blocked.
- The cashflow cannot be released from Ratan.

For bulk processing:

- Hard-blocked cashflows receive a validation error.
- They are displayed with strikethrough formatting.
- They are not posted to the back end.

The source does not define whether valid cashflows in the same bulk selection continue processing.

## Rule scope

The documented rule matches either:

```text
Instrument_Common__Murex_Product_Strategy == "SWAP_AGENT"
```

with `Cashflow__Payment_Type` equal to `Coupon` or `Interim MTM`, or:

```text
Cashflow__Is_Hard_Blocker == true
```

The latter condition can classify cashflows outside the Swap Agent-specific scenario as hard blockers.

## Message-scope limitation

The documented UI message is:

```text
This is a Swap Agent Coupon or Interim MTM cashflow, can't be release from Ratan.
```

This message accurately describes the first rule branch but may not describe every cashflow matched by the broader `Cashflow__Is_Hard_Blocker` condition. The correct message for non-Swap Agent hard blockers remains unresolved.

This concept is distinct from [[manual-cancellation-queue]], [[high-value-payment-queue]], and other manual validation queues.
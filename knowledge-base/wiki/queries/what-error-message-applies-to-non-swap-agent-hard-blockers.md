---
type: query
title: What Error Message Applies to Non-Swap Agent Hard Blockers?
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, hard-blocker, user-interface, error-message, ratan]
related: [hard-blocker-go-live-checklist, hard-blocker-exception, swap-agent-coupon-release-block]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Hard Blocker/Hard Blocker go live checklist.md"]
---
# What Error Message Applies to Non-Swap Agent Hard Blockers?

The configured rule matches all cashflows where `Cashflow__Is_Hard_Blocker == true`, including cashflows that may not be `SWAP_AGENT` Coupon or Interim MTM transactions. However, the documented UI message only describes the Swap Agent scenario:

```text
This is a Swap Agent Coupon or Interim MTM cashflow, can't be release from Ratan.
```

The source does not clarify whether this message is intended for every hard blocker or whether a separate generic message is required.
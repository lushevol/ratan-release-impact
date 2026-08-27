---
type: concept
title: Notice to Receive MT210 Control
created: 2026-08-23
updated: 2026-08-23
tags: [mt210, swift, nostro, static-data, notice-to-receive, ratan]
related: [mt210-message-generation, nostro-stamping, portfolio-based-nostro-stamping, which-nostro-is-selected-for-non-rfi-receive-cashflows-with-kro-main]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/RFI Nostro stamping based on Portfolio/RFI Nostro stamping based on Portfolio - UAT.md"]
---
# Notice to Receive MT210 Control

`Notice to Receive` is a nostro-static-data control evidenced in RATAN KRW/KRO UAT receive-cashflow scenarios.

When the selected nostro static data had `Notice to Receive = N`, test 6 reported that tag `:25:` was not generated. When the setting was enabled, test 6.1 reported expected MT210 generation with tag `:25:`. Test 4 provides an outbound MT210 example containing:

```text
:25:03910010005
```

This is configuration-specific UAT evidence. It does not establish whether the flag controls only tag `:25:`, the full MT210 lifecycle, or all receive flows across products and currencies.

The control depends on the nostro selected for the cashflow and therefore intersects with [[portfolio-based-nostro-stamping]] and [[nostro-stamping]]. The conflicting wording about the selected nostro in tests 6 and 6.1 is tracked in [[which-nostro-is-selected-for-non-rfi-receive-cashflows-with-kro-main]].
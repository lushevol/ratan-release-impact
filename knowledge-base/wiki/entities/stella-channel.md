---
type: entity
title: StellaChannel
created: 2026-08-24
updated: 2026-08-24
tags: [java, enum, stella, strategic-cashflow]
related: [sabre-booking-api, stella, strategic-cashflow]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Strategic Cashflow Stella Ambassandor.md"]
---
# StellaChannel

`StellaChannel` is the Java enum defining Stella integration channels in `sabre-booking-api`.

The source documents `RATANCASH_V2("ratancash-v2")` as the channel added for strategic cashflow integration. It should be treated as distinct from merely setting `stellaMessageType: STRATEGIC_CASHFLOW` on a message.
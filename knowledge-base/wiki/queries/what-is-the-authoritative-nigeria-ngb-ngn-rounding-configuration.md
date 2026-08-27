---
type: query
title: What Is the Authoritative Nigeria NGB-NGN Rounding Configuration?
created: 2026-08-23
updated: 2026-08-23
tags: [nigeria, currency-mapping, rounding, ratan, open-question]
related: [ratan, scb-nigeria-lag-gbs, manual-entity-go-live-readiness]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/04 Go live checklist for Manual Entities-Overall/Tranche2.md"]
---
# What Is the Authoritative Nigeria NGB-NGN Rounding Configuration?

The checklist requires a `NGB` to `NGN` mapping in Ratan, but records incompatible rounding instructions:

- a 2026-04-02 note changes NGN precision from `2` to `0`;
- a 2026-08-14 note says NGN precision should be `2`; and
- the active row is `NGB`, precision `2`, with `ROUNDING_OFF`.

It is unresolved whether Ratan requires separate `NGB` and `NGN` rounding entries, which currency is operational after mapping, and which precision is deployed. Obtain an approved configuration decision and deployment evidence before Nigeria go-live.
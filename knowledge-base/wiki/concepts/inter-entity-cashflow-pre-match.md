---
type: concept
title: Inter-Entity Cashflow Pre-Match
created: 2026-08-22
updated: 2026-08-22
tags: [cashflow, pre-match, inter-entity, fmid, netting]
related: [inter-entity-auto-netting, counterparty-mapping-static, netting-resultant-cashflow]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Inter Entity Netting.md"]
---
# Inter-Entity Cashflow Pre-Match

Inter-entity cashflow pre-match is the bilateral validation required before eligible internal cashflows may enter [[inter-entity-auto-netting]].

For cashflows C1 and C2, the requirement specifies:

- identical currency, value date, and amount;
- opposite payment directions;
- C1 booking-entity FMID equal to C2 counterparty mapped value; and
- C2 booking-entity FMID equal to C1 counterparty mapped value.

A counterparty's mapped value defaults to its FMID. Where raw FMIDs differ across internal structures, [[counterparty-mapping-static]] supplies a canonical mapped FMID.

## Grouping

For pay flows, the group uses booking entity plus counterparty. For receive flows, it uses counterparty plus booking entity, so reciprocal sides produce the same grouping identity when the pair is valid.

The source contains an unresolved sample inconsistency: an expected group key references `400906330` where the row's counterparty FMID is `400927052`. Do not infer an undocumented normalization rule from that example.
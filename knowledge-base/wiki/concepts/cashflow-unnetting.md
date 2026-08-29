---
type: concept
title: Cashflow Unnetting
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, netting, unnetting, reversal]
related: [netting-service, cashflow-netting, resultant-cashflow-generation, cashflow-reinstatement-and-replay]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Netting Service Design.md"]
---

# Cashflow Unnetting

Cashflow unnetting reverses a netting operation. The documented DoD requires component cashflows to return to `Pending` and the resultant cashflow to become `Dead`.

The request model represents unnetting with the `UNNET` action. The process examples include `DEAD`, `WAITING`, and `CANCELLED` records, but they do not provide a complete before-and-after transition or explain whether the original netting identifier remains reusable.

Unnetting semantics are therefore only partially specified. The design does not define atomicity, authorization, repeated-unnet behavior, treatment of downstream processing, or status write-back details. These issues may intersect with cashflow reinstatement and replay, but this source does not prescribe a replay procedure.
---
type: query
title: What Is the Authoritative Netting State Machine?
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, netting, state-machine, open-question]
related: [netting-service, cashflow-netting, cashflow-unnetting, cashflow-splitting, cash-settlement-exception-handling]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Netting Service Design.md"]
---

# What Is the Authoritative Netting State Machine?

The source provides intended transitions but not a complete authoritative state machine.

The DoD states that component cashflows can move from `Pending`, `Validated`, `Queued`, or `Projected` to `Netted`, and that unnetting returns components to `Pending` while marking the resultant `Dead`. Examples additionally use `WAITING`, `WAITING PAL`, `CANCELLED`, and `SPLIT`.

The following points require confirmation:

- Whether a newly generated resultant is always `QUEUED` or may be `WAITING`.
- What causes a resultant to become `DEAD`.
- Whether `SPLIT` is terminal.
- How `WAITING PAL` and `CANCELLED` participate in withdrawal.
- Whether split outputs can be re-netted.
- Whether transitions differ between IRS aggregation and bilateral netting.
- Whether state changes are atomic across all components and resultants.

This query should be resolved against the canonical cashflow lifecycle and any implementation or API specifications.
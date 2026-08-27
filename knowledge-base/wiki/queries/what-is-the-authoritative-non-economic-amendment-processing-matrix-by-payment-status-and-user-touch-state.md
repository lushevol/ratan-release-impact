---
type: query
title: What Is the Authoritative Non-Economic Amendment Processing Matrix by Payment Status and User-Touch State?
created: 2026-08-24
updated: 2026-08-24
tags: [cashflow, non-economic-amendment, workflow, payment-status]
related: [non-economic-cashflow-amendment, cashflow-lifecycle-state-machine-restructuring, what-is-the-authoritative-cashflow-lifecycle-state-transition-and-persistence-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Ratan processing on cashflow events/Group Management Service - Non-Eco Amendment Technical Design.md"]
---
# What Is the Authoritative Non-Economic Amendment Processing Matrix by Payment Status and User-Touch State?

The source says non-economic amendments are currently ignored directly, but proposes that this occurs only for payments touched by users or already settled. It explicitly requires replacements in `PROJECTED` and `QUEUED` status to proceed to workflow.

A complete policy is missing. It should define how user touch and settlement are determined, whether `PROJECTED` and `QUEUED` are exhaustive workflow-eligible states, and the treatment of netted, held, failed, and exception states.
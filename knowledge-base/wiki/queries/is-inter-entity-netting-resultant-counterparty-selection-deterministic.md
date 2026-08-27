---
type: query
title: Is Inter-Entity Netting Resultant Counterparty Selection Deterministic?
tags: [inter-entity-netting, netting-resultant, counterparty, auditability]
related: [inter-entity-netting, net-resultant-cashflow, ratan]
created: 2026-08-22
updated: 2026-08-22
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Ratan One Processing Guide (DOI).md"]
---
# Is Inter-Entity Netting Resultant Counterparty Selection Deterministic?

The guide states that an Inter Entity Netting resultant's counterparty FMID and BIC code “will randomly derive from one component cashflow.”

This wording is unsuitable for an auditable settlement process unless it describes a deterministic implementation that has been imprecisely documented.

## Why this matters

Counterparty identity on a resultant can affect SSI selection, SWIFT generation, reconciliation, reporting, exception handling, and investigation of asymmetric release or un-net outcomes.

## Required resolution

Confirm:

1. The actual selection algorithm and whether it is deterministic.
2. The ordering or tie-breaker used when choosing a component.
3. Whether FMID and BIC are selected as a consistent pair.
4. The audit evidence available for the selected resultant attributes.
5. Whether the selected component affects downstream payment instructions or is display-only.

The answer should replace “randomly” with an implementation-accurate and control-approved description.
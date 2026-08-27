---
type: query
title: What Is the Final stpFlag and lastUser Contract Between RATAN and FMSGW?
created: 2026-08-23
updated: 2026-08-23
tags: [open-question, stp, nstp, ratan, fmsgw, swift-header]
related: [ratan, fmsgw, bcs, fmrp, loaniq, stp-nstp-and-last-user-message-contract, ratan-high-value-payment-control]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/High Value Payment Control - RATAN.md"]
---
# What Is the Final stpFlag and lastUser Contract Between RATAN and FMSGW?

The documented FMRP/LOANIQ proposal defines `stpFlag` as `Y` for STP and `N` for NSTP, and defines `lastUser` as a user bank ID that is blank for STP. However, the same source records both definitions as pending confirmation.

Resolution is needed for:

- The exact actions that produce NSTP for each cashflow flow.
- Whether BCS manual touch and FMRP/LOANIQ exception closure are equivalent conditions.
- Whether `lastUser` carries a bank ID, a PSID, or another identifier.
- The field values and identity source for maker/checker versus single-level actions.
- Whether the proposed FMRP/LOANIQ field semantics apply unchanged to BCS.
- The final handling of auto-distributed or auto-split child cashflows.

Until confirmed, the documented field values are a proposed interface design rather than an approved cross-flow contract.
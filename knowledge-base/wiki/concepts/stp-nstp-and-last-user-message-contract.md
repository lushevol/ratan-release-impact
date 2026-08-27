---
type: concept
title: STP/NSTP and Last-User Message Contract
created: 2026-08-23
updated: 2026-08-23
tags: [stp, nstp, swift-header, user-attribution, ratan, fmsgw]
related: [ratan, fmsgw, bcs, fmrp, loaniq, ratan-high-value-payment-control, fmsgw-inbound-message-routing]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/High Value Payment Control - RATAN.md"]
---
# STP/NSTP and Last-User Message Contract

This proposed interface contract enriches RATAN settlement messages sent to [[fmsgw]] with processing classification and user attribution.

## Proposed fields

For FMRP/LOANIQ cashflows, the source proposes these Swift-header fields:

| Field | Proposed rule |
| --- | --- |
| `stpFlag` | `Y` for STP and `N` for NSTP |
| NSTP condition | Exception closed by a user |
| STP condition | All other flows |
| Failed or reinstated actions | Not considered |
| Comments | Not considered |
| `lastUser` | User bank ID; blank where `stpFlag` is `Y` |

For maker/checker actions, RATAN should send the last checker PSID. For a single-level action, such as affirmation, RATAN should send the last maker PSID.

For automatic distribution or splitting, a child cashflow must derive its STP/NSTP information from its parent.

## Provisional status

The source lists the definitions of `stpFlag` and `lastUser` as pending confirmation. It does not establish whether user bank ID and PSID are the same identifier, nor does it finalize which user actions trigger NSTP.

There is a further flow-specific tension: BCS describes NSTP as a cashflow having a user manual touch, whereas FMRP/LOANIQ proposes NSTP as an exception closed by a user. These must not be treated as one confirmed canonical rule. See [[what-is-the-final-stpflag-and-lastuser-contract-between-ratan-and-fmsgw]].
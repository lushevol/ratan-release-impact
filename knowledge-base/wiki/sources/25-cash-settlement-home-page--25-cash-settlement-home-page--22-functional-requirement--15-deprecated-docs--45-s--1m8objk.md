---
type: source
title: "Stella Business Event Action & Cashflow Impact"
created: 2026-08-23
updated: 2026-08-23
tags: [deprecated, functional-requirement, stella, cashflow, trade-events, ratan]
related: [stella, ratan, stella-business-event-cashflow-mapping, cashflow-withdrawal-and-new, cashflow-partial-update, trade-economic-versus-non-economic-update, what-is-the-authoritative-stella-business-event-to-cashflow-mapping]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Deprecated docs/Stella Business event action & cashflow impact.md"]
authors: []
year: 2023
url: ""
venue: "Deprecated functional requirement"
---
# Stella Business Event Action & Cashflow Impact

> **Status: deprecated historical reference.** This document is not a complete or current implementation contract. It contains blank mappings and does not define event correlation, versioning, precedence, or CDU confirmation behavior.

This source records a historical Stella action-to-cashflow crosswalk. It identifies a Ratan settlement-state condition: a cashflow amendment can be processed as `Withdrawal/New` when the preceding cashflow event is settled in Ratan.

## Regional Applicability

| Business Event | Applicable for Egypt | Applicable for CN & Onward |
| --- | --- | --- |
| Trade | Y | Y |
| Amendment | Y | Y |
| Withdrawal | Y | Y |
| Termination | N | Y |
| Partial Termination | N | Y |
| Novation | N | Y |
| Expiry | N | Y |
| Allocation | N | Y |
| Close Out | N | Y |

The historical matrix limits Egypt to Trade, Amendment, and Withdrawal. CN & Onward additionally includes Termination, Partial Termination, Novation, Expiry, Allocation, and Close Out. The source does not fully specify the cashflow behavior for many of those additional events.

## Stella Action-to-Cashflow Mapping

| Business Event | Action | Pre Trade Status | Target Trade Status | CDU Confirmation | Cashflow Events | Sample Cashflows |
| --- | --- | --- | --- | --- | --- | --- |
| Trade | Book | TOBESENT/SENT | TOBESENT |  | New |  |
|  | Update(Economic) | TOBESENT/SENT | TOBESENT |  | 1. New → Amendment 2. New ( Cashflow Partial update) |  |
|  | Update(Non-Economic) | TOBESENT/SENT |  |  |  |  |
|  | Cancel | TOBESENT/SENT | TOBESENT |  | 1. New → Withdrawal 2. New → Amendment → Withdrawal |  |
| Amendment | Book (Economic) | AFFIRMED/CONFIRMED | TOBESENT |  | 1. New → Amendment 2. New ( Cashflow Partial update) |  |
|  | Book (Non-Economic) | AFFIRMED/CONFIRMED | TOBESENT |  | New |  |
|  | Update (Economic) | TOBESENT/SENT | TOBESENT |  | 1. New → Amendment → Amendment 2. New → Amendment 3. New |  |
|  | Update (Non-Economic) |  |  |  |  |  |
|  | Cancel | TOBESENT/SENT | TOBESENT |  | 1. New →Amendment ->Withdrawal 2. New → Withdrawal |  |
| Withdrawal | Book | AFFIRMED/CONFIRMED | TOBESENT |  | 1. New→ Withdrawal 2. New → Amendment → Withdrawal |  |
|  | Undo (Revive) | TOBESENT/SENT | TOBESENT |  | 1. New→ Withdrawal → Amendment 2. New → Amendment → Withdrawal → Amendment | Trade ID: 3860748027 |
| Termination | Book |  | TOBESENT |  | Withdrawal/New |  |
|  | Undo | TOBESENT/SENT | TOBESENT |  | Withdrawal/New |  |
| Partial Termination | Book |  |  |  | Amendment/New/Withdrawal |  |
|  | Undo |  |  |  |  |  |
| Close Out | Book |  |  |  |  |  |
|  | Update |  |  |  |  |  |
|  | Cancel |  |  |  |  |  |
| Expiry | Book |  |  |  |  |  |
| Novation | Book |  |  |  |  |  |
| Allocation | Book |  |  |  |  |  |

## Historical Observations

- Economic updates are associated with Amendment chains or a `Cashflow Partial update`; the source does not state which condition selects either outcome.
- Withdrawal and cancellation can follow either a direct `New → Withdrawal` path or an amendment history.
- A withdrawal Undo/Revive may result in a further Amendment rather than restoring the original cashflow unchanged.
- The sample withdrawal-revive scenario cites Trade ID `3860748027`; its supporting screenshots are not represented as structured event evidence in the document.
- Every `CDU Confirmation` entry is blank. This source establishes no confirmation-status mapping.

## Related Pages

The historical mapping concerns [[stella]], [[ratan]], and [[stella-business-event-cashflow-mapping]]. Its unresolved replacement semantics are tracked in [[what-is-the-authoritative-stella-business-event-to-cashflow-mapping]] and [[what-is-the-authoritative-withdrawal-new-sequencing-and-nstp-rule]].
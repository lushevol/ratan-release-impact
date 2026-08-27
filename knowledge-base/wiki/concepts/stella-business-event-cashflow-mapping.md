---
type: concept
title: Stella Business Event Cashflow Mapping
created: 2026-08-23
updated: 2026-08-23
tags: [stella, trade-events, cashflow-lifecycle, deprecated, settlement]
related: [stella, ratan, cashflow-partial-update, cashflow-withdrawal-and-new, cashflow-amendment-supersession, trade-economic-versus-non-economic-update, cn-settlement, what-is-the-authoritative-stella-business-event-to-cashflow-mapping]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Deprecated docs/Stella Business event action & cashflow impact.md"]
---
# Stella Business Event Cashflow Mapping

Stella business-event cashflow mapping describes the historical relationship between a Stella trade lifecycle action and the cashflow event sequence that follows it.

## Historical Behavior

The deprecated source associates:

- economic Trade and Amendment actions with either Amendment processing or [[cashflow-partial-update]];
- cancellation and Withdrawal actions with Withdrawal sequences that may include prior Amendments;
- Withdrawal Undo/Revive with a subsequent Amendment;
- Termination Book and Undo with `Withdrawal/New`; and
- Partial Termination Book with `Amendment/New/Withdrawal`.

The mapping depends on lifecycle history rather than solely on the current action. For example, cancellation may follow either `New → Withdrawal` or `New → Amendment → Withdrawal`.

## Settled-Cashflow Branch

For Stella, the source identifies a RATAN-specific branch: if the prior cashflow event is settled in [[ratan]], an Amendment can become [[cashflow-withdrawal-and-new]]. The source does not establish precedence between settlement status, economic-change classification, business-event type, product, or cashflow type.

## Scope and Limitations

The mapping is historical and incomplete:

- Egypt is listed as supporting Trade, Amendment, and Withdrawal only.
- CN & Onward is listed as additionally supporting Termination, Partial Termination, Novation, Expiry, Allocation, and Close Out.
- Cashflow mappings for several CN & Onward events are blank.
- CDU Confirmation values are blank throughout.
- No correlation key, version model, event ordering rule, or duplicate-event behavior is supplied.

Do not treat this page as a current contract. The authoritative mapping remains under investigation in [[what-is-the-authoritative-stella-business-event-to-cashflow-mapping]].